"""Retries, idempotency, rate limits, scope errors and webhook verification."""

from __future__ import annotations

import hashlib
import hmac
import json
import time
from typing import Any

import pytest
import urllib3
from mailermine import (
    ApiError,
    MailerMine,
    MissingScopeError,
    PlanError,
    RateLimitError,
    ScopePresets,
    Scopes,
    Webhooks,
)
from mailermine_generated import rest

EMAIL = {"from": "hi@example.com", "to": "user@example.com", "subject": "Hi", "html": "<p>Hi</p>"}


def _response(
    status: int, body: Any = None, headers: dict[str, str] | None = None
) -> rest.RESTResponse:
    raw = urllib3.HTTPResponse(
        body=json.dumps(body if body is not None else {}).encode(),
        status=status,
        headers={"Content-Type": "application/json", **(headers or {})},
        preload_content=True,
    )
    response = rest.RESTResponse(raw)
    response.read()
    return response


def _sent(headers: dict[str, str] | None = None) -> rest.RESTResponse:
    return _response(202, {"success": True, "data": {"id": "msg_1", "status": "queued"}}, headers)


def _client(queue: list[Any], *, max_retries: int = 2, max_retry_delay: float = 0.0):
    from mailermine.config import Configuration

    client = MailerMine(
        configuration=Configuration(
            api_key="test-key",
            base_url="https://api.example.test/api/v1",
            max_retries=max_retries,
            max_retry_delay=max_retry_delay,
        )
    )
    api_client = client._apis.api_client
    api_client._sleep = lambda _seconds: None
    history: list[dict[str, Any]] = []

    def fake_request(method, url, headers=None, body=None, post_params=None, _request_timeout=None):
        history.append({"method": method, "url": url, "headers": dict(headers or {}), "body": body})
        item = queue.pop(0)
        if isinstance(item, BaseException):
            raise item
        return item

    api_client.rest_client.request = fake_request  # type: ignore[method-assign]

    # These tests cover the transport, not model parsing: pass successful JSON
    # through as-is; errors still go through the generated deserializer.
    original = api_client.response_deserialize

    def passthrough(response_data, response_types_map=None):
        if 200 <= response_data.status < 300:
            from mailermine_generated.api_response import ApiResponse

            return ApiResponse(
                status_code=response_data.status,
                data=json.loads(response_data.data or b"{}"),
                headers=response_data.getheaders(),
                raw_data=response_data.data,
            )
        return original(response_data, response_types_map)

    api_client.response_deserialize = passthrough  # type: ignore[method-assign]
    return client, history


def test_send_adds_idempotency_key_and_reuses_it_on_retry() -> None:
    client, history = _client([_response(503, {"message": "down"}), _sent()])

    client.emails.send(EMAIL)

    assert len(history) == 2
    key = history[0]["headers"]["Idempotency-Key"]
    assert len(key) == 36
    assert history[1]["headers"]["Idempotency-Key"] == key


def test_caller_supplied_idempotency_key_is_sent() -> None:
    client, history = _client([_sent()])

    client.emails.send(EMAIL, idempotency_key="order-42")

    assert history[0]["headers"]["Idempotency-Key"] == "order-42"


def test_invalid_idempotency_key_is_rejected() -> None:
    client, _ = _client([])

    with pytest.raises(ValueError):
        client.emails.send(EMAIL, idempotency_key="")


def test_rate_limited_requests_retry_then_raise() -> None:
    limited = lambda: _response(  # noqa: E731
        429, {"message": "slow down"}, {"X-RateLimit-Limit": "10", "X-RateLimit-Remaining": "0"}
    )
    client, history = _client([limited(), limited(), limited()])

    with pytest.raises(RateLimitError) as caught:
        client.emails.send(EMAIL)

    assert len(history) == 3
    assert caught.value.rate_limit is not None
    assert caught.value.rate_limit.remaining == 0
    assert caught.value.is_retryable


def test_long_retry_after_is_not_waited_for() -> None:
    client, history = _client(
        [_response(429, {"message": "slow down"}, {"Retry-After": "120"})], max_retry_delay=5
    )

    with pytest.raises(RateLimitError) as caught:
        client.domains.list()

    assert len(history) == 1
    assert caught.value.retry_after == 120


def test_server_errors_on_non_idempotent_posts_are_not_retried() -> None:
    client, history = _client([_response(503, {"message": "down"})])

    with pytest.raises(ApiError):
        client.contacts.create(email="a@example.com")

    assert len(history) == 1


def test_transport_errors_on_get_are_retried() -> None:
    client, history = _client(
        [urllib3.exceptions.ProtocolError("reset"), _response(200, {"success": True, "data": []})]
    )

    client.domains.list()

    assert len(history) == 2


def test_retries_can_be_disabled() -> None:
    client, history = _client([_response(429, {"message": "slow"})], max_retries=0)

    with pytest.raises(RateLimitError):
        client.domains.list()

    assert len(history) == 1


def test_client_exposes_latest_rate_limit() -> None:
    reset = int(time.time()) + 30
    client, _ = _client(
        [
            _sent(
                {
                    "X-RateLimit-Limit": "600",
                    "X-RateLimit-Remaining": "42",
                    "X-RateLimit-Reset": str(reset),
                }
            )
        ]
    )

    client.emails.send(EMAIL)

    assert client.rate_limit is not None
    assert client.rate_limit.limit == 600
    assert client.rate_limit.remaining == 42
    assert client.rate_limit.seconds_until_reset > 0


def test_missing_scope_maps_to_missing_scope_error() -> None:
    client, _ = _client(
        [
            _response(
                403,
                {
                    "success": False,
                    "message": "This API key is missing the required scope: domains.read.",
                    "errors": {"scope": ["domains.read"]},
                },
            )
        ]
    )

    with pytest.raises(MissingScopeError) as caught:
        client.domains.list()

    assert isinstance(caught.value, PlanError)
    assert caught.value.missing_scopes == ["domains.read"]
    assert "billing" not in str(caught.value)


def test_plan_restrictions_stay_plan_errors() -> None:
    client, _ = _client([_response(403, {"success": False, "message": "Not on Free."})])

    with pytest.raises(PlanError) as caught:
        client.domains.list()

    assert not isinstance(caught.value, MissingScopeError)


def test_scope_constants() -> None:
    assert Scopes.WEBHOOKS_WRITE == "webhooks.write"
    assert "events.read" in Scopes.all()
    assert ScopePresets.SENDING_ONLY == ("emails.send",)


SECRET = "whsec_test"
PAYLOAD = '{"type":"email.delivered","data":{"id":"msg_1"}}'


def _sign(timestamp: int, payload: str = PAYLOAD) -> str:
    digest = hmac.new(SECRET.encode(), f"{timestamp}.{payload}".encode(), hashlib.sha256)
    return "sha256=" + digest.hexdigest()


def test_webhook_verify_matches_server_signing() -> None:
    timestamp = int(time.time())
    signature = _sign(timestamp)

    assert Webhooks.verify(PAYLOAD, signature, SECRET, timestamp)
    assert Webhooks.verify(PAYLOAD.encode(), signature, SECRET, str(timestamp))
    assert Webhooks.verify_headers(
        PAYLOAD,
        {"X-MailerMine-Signature": signature, "X-MailerMine-Timestamp": str(timestamp)},
        SECRET,
    )
    assert Webhooks.verify_headers(
        PAYLOAD, {"x-relay-signature": signature, "x-relay-timestamp": str(timestamp)}, SECRET
    )


def test_webhook_verify_rejects_bad_or_stale_deliveries() -> None:
    timestamp = int(time.time())
    signature = _sign(timestamp)

    assert not Webhooks.verify(PAYLOAD + " ", signature, SECRET, timestamp)
    assert not Webhooks.verify(PAYLOAD, signature, "other", timestamp)
    assert not Webhooks.verify(PAYLOAD, signature, SECRET, timestamp + 1)
    assert not Webhooks.verify_headers(PAYLOAD, {}, SECRET)

    old = timestamp - 3600
    assert not Webhooks.verify(PAYLOAD, _sign(old), SECRET, old)
    assert Webhooks.verify(PAYLOAD, _sign(old), SECRET, old, tolerance=0)
