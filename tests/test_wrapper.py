"""Phase 3 smoke tests for the handwritten MailerMine wrapper."""

from __future__ import annotations

import hashlib
import hmac
from typing import Any

import pytest
from mailermine import (
    ApiError,
    AuthenticationError,
    Collection,
    Configuration,
    MailerMine,
    MailerMineError,
    NotFoundError,
    PlanError,
    RateLimitError,
    Response,
    ValidationError,
)
from mailermine.exceptions import map_generated_error
from mailermine.support.serialization import to_collection, to_response
from mailermine_generated.exceptions import ApiException


def test_client_exposes_all_resources() -> None:
    client = MailerMine(api_key="relay_test_key")
    for name in (
        "emails",
        "projects",
        "api_keys",
        "domains",
        "templates",
        "contacts",
        "lists",
        "segments",
        "tags",
        "audiences",
        "campaigns",
        "analytics",
        "events",
        "messages",
        "webhooks",
        "suppressions",
        "imports",
        "exports",
    ):
        resource = getattr(client, name)
        assert resource is not None
        assert getattr(client, name) is resource  # lazy singleton


def test_configuration_defaults_and_env(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setenv("MAILERMINE_API_KEY", "env_key")
    monkeypatch.setenv("MAILERMINE_BASE_URL", "https://example.test/api/v1/")
    monkeypatch.setenv("MAILERMINE_TIMEOUT", "12.5")
    config = Configuration.create()
    assert config.api_key == "env_key"
    assert config.base_url == "https://example.test/api/v1"
    assert config.timeout == 12.5


def test_response_and_collection_wrappers() -> None:
    response = to_response(
        {
            "success": True,
            "message": "ok",
            "data": {"id": "abc", "email": "a@example.com"},
            "meta": {"request_id": "req_1"},
        }
    )
    assert isinstance(response, Response)
    assert response.success is True
    assert response.message == "ok"
    assert response.data == {"id": "abc", "email": "a@example.com"}
    assert response.meta["request_id"] == "req_1"

    collection = to_collection(
        {
            "success": True,
            "message": "listed",
            "data": [{"id": "1"}, {"id": "2"}],
            "meta": {
                "current_page": 1,
                "per_page": 25,
                "total": 2,
                "last_page": 1,
            },
        }
    )
    assert isinstance(collection, Collection)
    assert len(collection) == 2
    assert collection[0]["id"] == "1"
    assert collection.pagination.current_page == 1
    assert collection.pagination.has_next_page is False
    assert [item["id"] for item in collection] == ["1", "2"]


def test_api_error_message_property() -> None:
    err = ApiError("boom", status=500)
    assert err.message == "boom"
    assert AuthenticationError("nope", status=401).message == "nope"


def test_pydantic_validation_maps_to_api_error() -> None:
    from pydantic import BaseModel
    from pydantic import ValidationError as PydanticValidationError

    class Sample(BaseModel):
        settings: dict[str, object]

    try:
        Sample.model_validate({"settings": []})
    except PydanticValidationError as exc:
        mapped = map_generated_error(exc)
    assert isinstance(mapped, ApiError)
    assert not isinstance(mapped, ValidationError)
    assert mapped.status == 0
    assert mapped.message


def test_api_value_error_maps_to_validation_error() -> None:
    from mailermine_generated.exceptions import ApiValueError

    mapped = map_generated_error(ApiValueError("email is required"))
    assert isinstance(mapped, ValidationError)
    assert mapped.status == 422


def test_exception_mapping_status_codes() -> None:
    cases: list[tuple[int, type[MailerMineError]]] = [
        (401, AuthenticationError),
        (403, PlanError),
        (404, NotFoundError),
        (422, ValidationError),
        (429, RateLimitError),
        (500, ApiError),
    ]
    for status, expected in cases:
        mapped = map_generated_error(
            ApiException(status=status, reason="fail", body='{"message":"boom"}')
        )
        assert isinstance(mapped, expected)
        assert mapped.status == status
        assert "boom" in str(mapped)


def test_validation_error_field_errors() -> None:
    mapped = map_generated_error(
        ApiException(
            status=422,
            reason="invalid",
            body='{"message":"invalid","errors":{"email":["required"]}}',
        )
    )
    assert isinstance(mapped, ValidationError)
    assert mapped.errors["email"] == ["required"]


def test_rate_limit_retry_after() -> None:
    error = ApiException(
        status=429,
        reason="slow down",
        body='{"message":"rate limited"}',
    )
    error.headers = {"Retry-After": "30"}
    mapped = map_generated_error(error)
    assert isinstance(mapped, RateLimitError)
    assert mapped.retry_after == 30


def test_base_resource_execute_maps_errors() -> None:
    client = MailerMine(api_key="relay_test_key")

    def boom() -> None:
        raise ApiException(status=404, reason="missing", body='{"message":"gone"}')

    with pytest.raises(NotFoundError):
        client.projects.execute(boom)


def test_webhook_verify_timing_safe() -> None:
    secret = "whsec_test"
    payload = b'{"type":"email.delivered"}'
    digest = hmac.new(secret.encode("utf-8"), payload, hashlib.sha256).hexdigest()
    from mailermine import Webhooks

    assert Webhooks.verify(payload, digest, secret) is True
    assert Webhooks.verify(payload, f"sha256={digest}", secret) is True
    assert Webhooks.verify(payload, "deadbeef", secret) is False


def test_public_exports_hide_generated_package() -> None:
    import mailermine as sdk

    assert "mailermine_generated" not in sdk.__all__
    for name in sdk.__all__:
        assert "generated" not in name.lower()


def test_emails_send_accepts_kwargs_without_network(monkeypatch: pytest.MonkeyPatch) -> None:
    client = MailerMine(api_key="relay_test_key")
    captured: dict[str, Any] = {}

    def fake_send_email(**kwargs: Any) -> dict[str, Any]:
        captured.update(kwargs)
        return {
            "success": True,
            "message": "queued",
            "data": {"uuid": "msg_1"},
        }

    monkeypatch.setattr(client.emails._emails, "send_email", fake_send_email)
    result = client.emails.send(
        from_="hello@example.com",
        to="user@example.com",
        subject="Hi",
        html="<p>Hi</p>",
    )
    assert result.data["uuid"] == "msg_1"
    request = captured["send_email_request"]
    assert request["from"] == "hello@example.com"
    assert request["to"] == ["user@example.com"]
