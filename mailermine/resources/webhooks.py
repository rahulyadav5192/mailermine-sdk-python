"""Webhook endpoints, deliveries, replay, and signature verification."""

from __future__ import annotations

import hashlib
import hmac
import re
import time
from collections.abc import Mapping
from typing import Any

from mailermine_generated import WebhooksApi

from mailermine.resources.base import BaseResource
from mailermine.support import Collection, Response
from mailermine.support.serialization import (
    deleted_response,
    to_collection,
    to_generated_request,
    to_response,
)
from mailermine.types import JsonObject

_HEX_64 = re.compile(r"^[a-f0-9]{64}$", re.IGNORECASE)


class Webhooks(BaseResource):
    """Webhook endpoints, deliveries, replay, and signature verification."""

    def __init__(self, webhooks_api: WebhooksApi, *, timeout: float) -> None:
        super().__init__(timeout=timeout)
        self._api = webhooks_api

    def create(
        self,
        payload: Mapping[str, Any] | None = None,
        /,
        **kwargs: Any,
    ) -> Response[object]:
        """Create a webhook. Its signing secret is returned only once.

        Parameters
        ----------
        payload:
            Webhook fields as a mapping (``url``, ``events``, …).
        **kwargs:
            Alternative keyword fields merged into the request body.

        Returns
        -------
        Response[object]
            Created webhook payload including the one-time signing secret.

        Raises
        ------
        ValidationError
            When required fields are missing or invalid.
        ApiError
            On API or transport failures.

        Examples
        --------
        >>> client.webhooks.create(url="https://example.com/hook", events=["*"])
        """
        body = to_generated_request(_merge(payload, kwargs))
        return self.execute(
            lambda: to_response(
                self._api.create_webhook(
                    create_webhook_request=body,  # type: ignore[arg-type]
                    _request_timeout=self._timeout,
                )
            )
        )

    def list(self, **options: Any) -> Collection[object]:
        """List webhook endpoints.

        Parameters
        ----------
        **options:
            Optional filters such as ``search``, ``status``, ``sort``,
            ``direction``, ``page``, ``per_page``.

        Returns
        -------
        Collection[object]
            Paginated webhook list.

        Raises
        ------
        ApiError
            On API or transport failures.

        Examples
        --------
        >>> client.webhooks.list(status="active")
        """
        return self.execute(
            lambda: to_collection(
                self._api.list_webhooks(
                    **_query(options),
                    _request_timeout=self._timeout,
                )
            )
        )

    def get(self, webhook_id: str) -> Response[object]:
        """Retrieve a webhook by UUID.

        Parameters
        ----------
        webhook_id:
            Webhook UUID.

        Returns
        -------
        Response[object]
            Webhook payload.

        Raises
        ------
        NotFoundError
            When the webhook does not exist.
        ApiError
            On API or transport failures.

        Examples
        --------
        >>> client.webhooks.get("whk_123")
        """
        return self.execute(
            lambda: to_response(
                self._api.get_webhook(
                    webhook=webhook_id,  # type: ignore[arg-type]
                    _request_timeout=self._timeout,
                )
            )
        )

    def update(
        self,
        webhook_id: str,
        payload: Mapping[str, Any] | None = None,
        /,
        **kwargs: Any,
    ) -> Response[object]:
        """Update a webhook endpoint.

        Parameters
        ----------
        webhook_id:
            Webhook UUID.
        payload:
            Fields to update as a mapping.
        **kwargs:
            Alternative keyword fields merged into the request body.

        Returns
        -------
        Response[object]
            Updated webhook payload.

        Raises
        ------
        NotFoundError
            When the webhook does not exist.
        ValidationError
            When the update payload is invalid.
        ApiError
            On API or transport failures.

        Examples
        --------
        >>> client.webhooks.update("whk_123", url="https://example.com/new")
        """
        merged = _merge(payload, kwargs)
        body = to_generated_request(merged) if merged else None
        return self.execute(
            lambda: to_response(
                self._api.update_webhook(
                    webhook=webhook_id,  # type: ignore[arg-type]
                    update_webhook_request=body,  # type: ignore[arg-type]
                    _request_timeout=self._timeout,
                )
            )
        )

    def delete(self, webhook_id: str) -> Response[JsonObject]:
        """Delete a webhook endpoint.

        Parameters
        ----------
        webhook_id:
            Webhook UUID.

        Returns
        -------
        Response[JsonObject]
            Delete acknowledgement (``{"deleted": True}``).

        Raises
        ------
        NotFoundError
            When the webhook does not exist.
        ApiError
            On API or transport failures.

        Examples
        --------
        >>> client.webhooks.delete("whk_123")
        """

        def operation() -> Response[JsonObject]:
            envelope = to_response(
                self._api.delete_webhook(
                    webhook=webhook_id,  # type: ignore[arg-type]
                    _request_timeout=self._timeout,
                )
            )
            return deleted_response(envelope.message, envelope.success)

        return self.execute(operation)

    def test(
        self,
        webhook_id: str,
        payload: Mapping[str, Any] | None = None,
        /,
        **kwargs: Any,
    ) -> Response[object]:
        """Queue a test webhook delivery.

        Parameters
        ----------
        webhook_id:
            Webhook UUID.
        payload:
            Optional test fields as a mapping (``event_type``, …).
        **kwargs:
            Alternative keyword fields merged into the request body.

        Returns
        -------
        Response[object]
            Test delivery payload.

        Raises
        ------
        NotFoundError
            When the webhook does not exist.
        ApiError
            On API or transport failures.

        Examples
        --------
        >>> client.webhooks.test("whk_123", event_type="email.delivered")
        """
        merged = _merge(payload, kwargs)
        body = to_generated_request(merged) if merged else None
        return self.execute(
            lambda: to_response(
                self._api.test_webhook(
                    webhook=webhook_id,  # type: ignore[arg-type]
                    test_webhook_request=body,  # type: ignore[arg-type]
                    _request_timeout=self._timeout,
                )
            )
        )

    def rotate_secret(self, webhook_id: str) -> Response[object]:
        """Rotate the signing secret. The new secret is returned only once.

        Parameters
        ----------
        webhook_id:
            Webhook UUID.

        Returns
        -------
        Response[object]
            Webhook payload including the new one-time signing secret.

        Raises
        ------
        NotFoundError
            When the webhook does not exist.
        ApiError
            On API or transport failures.

        Examples
        --------
        >>> client.webhooks.rotate_secret("whk_123")
        """
        return self.execute(
            lambda: to_response(
                self._api.rotate_webhook_secret(
                    webhook=webhook_id,  # type: ignore[arg-type]
                    _request_timeout=self._timeout,
                )
            )
        )

    def enable(self, webhook_id: str) -> Response[object]:
        """Enable a webhook endpoint.

        Parameters
        ----------
        webhook_id:
            Webhook UUID.

        Returns
        -------
        Response[object]
            Updated webhook payload.

        Raises
        ------
        NotFoundError
            When the webhook does not exist.
        ApiError
            On API or transport failures.

        Examples
        --------
        >>> client.webhooks.enable("whk_123")
        """
        return self.execute(
            lambda: to_response(
                self._api.enable_webhook(
                    webhook=webhook_id,  # type: ignore[arg-type]
                    _request_timeout=self._timeout,
                )
            )
        )

    def disable(self, webhook_id: str) -> Response[object]:
        """Disable a webhook endpoint.

        Parameters
        ----------
        webhook_id:
            Webhook UUID.

        Returns
        -------
        Response[object]
            Updated webhook payload.

        Raises
        ------
        NotFoundError
            When the webhook does not exist.
        ApiError
            On API or transport failures.

        Examples
        --------
        >>> client.webhooks.disable("whk_123")
        """
        return self.execute(
            lambda: to_response(
                self._api.disable_webhook(
                    webhook=webhook_id,  # type: ignore[arg-type]
                    _request_timeout=self._timeout,
                )
            )
        )

    def deliveries(self, webhook_id: str, **options: Any) -> Collection[object]:
        """List deliveries for a webhook.

        Parameters
        ----------
        webhook_id:
            Webhook UUID.
        **options:
            Optional filters such as ``status``, ``event_type``, ``search``,
            ``http_status``, ``from``, ``to``, ``per_page``.

        Returns
        -------
        Collection[object]
            Paginated delivery list.

        Raises
        ------
        NotFoundError
            When the webhook does not exist.
        ApiError
            On API or transport failures.

        Examples
        --------
        >>> client.webhooks.deliveries("whk_123", status="failed")
        """
        return self.execute(
            lambda: to_collection(
                self._api.list_webhook_deliveries(
                    webhook=webhook_id,  # type: ignore[arg-type]
                    **_delivery_query(options),
                    _request_timeout=self._timeout,
                )
            )
        )

    def delivery(self, delivery_id: str) -> Response[object]:
        """Retrieve one webhook delivery.

        Parameters
        ----------
        delivery_id:
            Webhook delivery UUID.

        Returns
        -------
        Response[object]
            Delivery payload.

        Raises
        ------
        NotFoundError
            When the delivery does not exist.
        ApiError
            On API or transport failures.

        Examples
        --------
        >>> client.webhooks.delivery("dlv_123")
        """
        return self.execute(
            lambda: to_response(
                self._api.get_webhook_delivery(
                    webhook_delivery=delivery_id,  # type: ignore[arg-type]
                    _request_timeout=self._timeout,
                )
            )
        )

    def logs(self, webhook_id: str, **options: Any) -> Collection[object]:
        """List delivery logs for a webhook.

        Alias of :meth:`deliveries`.

        Parameters
        ----------
        webhook_id:
            Webhook UUID.
        **options:
            Optional delivery filters.

        Returns
        -------
        Collection[object]
            Paginated delivery list.

        Raises
        ------
        NotFoundError
            When the webhook does not exist.
        ApiError
            On API or transport failures.

        Examples
        --------
        >>> client.webhooks.logs("whk_123")
        """
        return self.deliveries(webhook_id, **options)

    def failures(self, webhook_id: str, **options: Any) -> Collection[object]:
        """List failed deliveries for a webhook.

        Parameters
        ----------
        webhook_id:
            Webhook UUID.
        **options:
            Optional delivery filters (``status`` is forced to ``failed``).

        Returns
        -------
        Collection[object]
            Paginated failed-delivery list.

        Raises
        ------
        NotFoundError
            When the webhook does not exist.
        ApiError
            On API or transport failures.

        Examples
        --------
        >>> client.webhooks.failures("whk_123")
        """
        options.pop("status", None)
        return self.deliveries(webhook_id, status="failed", **options)

    def replay(
        self,
        webhook_id: str,
        payload: Mapping[str, Any] | None = None,
        /,
        **kwargs: Any,
    ) -> Response[object]:
        """Replay webhook deliveries in bulk.

        Parameters
        ----------
        webhook_id:
            Webhook UUID.
        payload:
            Optional replay filters as a mapping (``from``, ``to``, …).
        **kwargs:
            Alternative keyword fields merged into the request body.

        Returns
        -------
        Response[object]
            Replay result payload.

        Raises
        ------
        NotFoundError
            When the webhook does not exist.
        ApiError
            On API or transport failures.

        Examples
        --------
        >>> client.webhooks.replay("whk_123")
        """
        merged = _merge(payload, kwargs)
        body = to_generated_request(_normalize_dates(merged)) if merged else None
        return self.execute(
            lambda: to_response(
                self._api.replay_webhook_deliveries(
                    webhook=webhook_id,  # type: ignore[arg-type]
                    replay_webhook_request=body,  # type: ignore[arg-type]
                    _request_timeout=self._timeout,
                )
            )
        )

    def retry(self, delivery_id: str) -> Response[object]:
        """Retry one webhook delivery.

        Parameters
        ----------
        delivery_id:
            Webhook delivery UUID.

        Returns
        -------
        Response[object]
            Retried delivery payload.

        Raises
        ------
        NotFoundError
            When the delivery does not exist.
        ApiError
            On API or transport failures.

        Examples
        --------
        >>> client.webhooks.retry("dlv_123")
        """
        return self.execute(
            lambda: to_response(
                self._api.replay_webhook_delivery(
                    webhook_delivery=delivery_id,  # type: ignore[arg-type]
                    _request_timeout=self._timeout,
                )
            )
        )

    #: Default maximum age, in seconds, of a signed webhook timestamp.
    DEFAULT_TOLERANCE_SECONDS = 300

    @staticmethod
    def verify(
        payload: str | bytes,
        signature: str,
        secret: str,
        timestamp: str | int | None = None,
        tolerance: int = 300,
    ) -> bool:
        """Verify a MailerMine webhook signature locally.

        MailerMine signs ``{timestamp}.{raw_body}`` with HMAC-SHA256 and sends the
        timestamp in ``X-MailerMine-Timestamp`` and the signature in
        ``X-MailerMine-Signature`` (``sha256=<hex>``). Pass the timestamp so the
        signature matches and stale deliveries are rejected (replay protection).
        Without a timestamp only a body-only signature is checked (legacy).
        Prefer :meth:`verify_headers`.

        Parameters
        ----------
        payload:
            Raw request body exactly as received.
        signature:
            ``X-MailerMine-Signature`` value (optionally ``sha256=``-prefixed).
        secret:
            Webhook signing secret.
        timestamp:
            ``X-MailerMine-Timestamp`` value.
        tolerance:
            Maximum age of the timestamp in seconds (0 disables the check).

        Returns
        -------
        bool
            ``True`` when the signature is valid (and fresh), otherwise ``False``.

        Examples
        --------
        >>> Webhooks.verify(
        ...     raw_body,
        ...     request.headers["X-MailerMine-Signature"],
        ...     secret,
        ...     request.headers["X-MailerMine-Timestamp"],
        ... )
        """
        if not secret or not signature:
            return False
        normalized = signature.strip()
        normalized = normalized[7:] if normalized.lower().startswith("sha256=") else normalized
        if not _HEX_64.match(normalized):
            return False

        message = payload.encode("utf-8") if isinstance(payload, str) else payload
        if timestamp is not None and timestamp != "":
            try:
                seconds = int(str(timestamp).strip())
            except ValueError:
                return False
            if tolerance > 0 and abs(time.time() - seconds) > tolerance:
                return False
            message = f"{seconds}.".encode() + message

        expected = hmac.new(secret.encode("utf-8"), message, hashlib.sha256).hexdigest()
        return hmac.compare_digest(expected, normalized.lower())

    @staticmethod
    def verify_headers(
        payload: str | bytes,
        headers: Mapping[str, Any],
        secret: str,
        tolerance: int = 300,
    ) -> bool:
        """Verify a webhook from its request headers.

        Reads ``X-MailerMine-Signature`` and ``X-MailerMine-Timestamp`` (falling
        back to the legacy ``X-Relay-*`` headers), case-insensitively.

        Examples
        --------
        >>> Webhooks.verify_headers(request.get_data(), request.headers, secret)
        """
        lowered = {str(key).lower().replace("_", "-"): value for key, value in headers.items()}

        def read(*names: str) -> str | None:
            for name in names:
                value = lowered.get(name)
                if isinstance(value, (list, tuple)):
                    value = value[0] if value else None
                if value:
                    return str(value)
            return None

        signature = read("x-mailermine-signature", "x-relay-signature")
        timestamp = read("x-mailermine-timestamp", "x-relay-timestamp")
        if signature is None or timestamp is None:
            return False
        return Webhooks.verify(payload, signature, secret, timestamp, tolerance)


def _normalize_dates(options: Mapping[str, Any]) -> dict[str, Any]:
    result: dict[str, Any] = {}
    for key, value in options.items():
        result[key] = _iso(value) if key in ("from", "from_", "to") else value
    return result


def _delivery_query(options: Mapping[str, Any]) -> dict[str, Any]:
    aliases = {"from": "var_from", "from_": "var_from"}
    result: dict[str, Any] = {}
    for key, value in options.items():
        if value is None:
            continue
        target = aliases.get(key, key)
        result[target] = _iso(value) if target in ("var_from", "to") else value
    return result


def _iso(value: Any) -> Any:
    if value is None:
        return None
    if hasattr(value, "isoformat") and callable(value.isoformat):
        return value.isoformat()
    return value


def _merge(payload: Mapping[str, Any] | None, kwargs: Mapping[str, Any]) -> dict[str, Any]:
    merged: dict[str, Any] = dict(payload or {})
    merged.update({key: value for key, value in kwargs.items() if value is not None})
    return merged


def _query(options: Mapping[str, Any]) -> dict[str, Any]:
    return {key: value for key, value in options.items() if value is not None}
