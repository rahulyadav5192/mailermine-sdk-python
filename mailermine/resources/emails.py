"""Transactional email resource."""

from __future__ import annotations

from collections.abc import Mapping
from typing import Any, cast

from mailermine_generated import EmailsApi, MessagesApi

from mailermine.resources.base import BaseResource
from mailermine.support import Collection, Response
from mailermine.support.serialization import to_collection, to_generated_request, to_response


class Emails(BaseResource):
    """Transactional email operations."""

    def __init__(
        self,
        emails_api: EmailsApi,
        messages_api: MessagesApi,
        *,
        timeout: float,
    ) -> None:
        super().__init__(timeout=timeout)
        self._emails = emails_api
        self._messages = messages_api

    def send(
        self,
        payload: Mapping[str, Any] | None = None,
        /,
        *,
        idempotency_key: str | None = None,
        **kwargs: Any,
    ) -> Response[object]:
        """Queue a transactional email for delivery.

        Parameters
        ----------
        payload:
            Email fields as a mapping (``from``, ``to``, ``subject``, …).
        idempotency_key:
            Optional unique key (max 255 chars). Repeating a send with the same
            key and body returns the original response instead of sending
            again. A random key is used when omitted, so SDK retries are safe.
        **kwargs:
            Alternative keyword fields merged into the request body.

        Returns
        -------
        Response[object]
            Created message payload.

        Raises
        ------
        ValidationError
            When required fields are missing or invalid.
        ApiError
            On API or transport failures.

        Examples
        --------
        >>> client.emails.send(
        ...     from_="MailerMine <hello@example.com>",
        ...     to="user@example.com",
        ...     subject="Welcome",
        ...     html="<p>Hello</p>",
        ... )
        """
        body = _merge_payload(payload, kwargs)
        # Allow from_ as a Pythonic alias for the reserved word ``from``.
        if "from_" in body and "from" not in body:
            body["from"] = body.pop("from_")
        to_value = body.get("to")
        if isinstance(to_value, str):
            body["to"] = [to_value]
        if idempotency_key is not None and (
            not isinstance(idempotency_key, str)
            or not idempotency_key
            or len(idempotency_key) > 255
        ):
            raise ValueError(
                "idempotency_key must be a non-empty string of at most 255 characters."
            )
        request = to_generated_request(body)
        return self.execute(
            lambda: to_response(
                self._emails.send_email(
                    send_email_request=request,  # type: ignore[arg-type]
                    idempotency_key=idempotency_key,
                    _request_timeout=self._timeout,
                )
            )
        )

    def list(self, **options: Any) -> Collection[object]:
        """List recently sent and queued messages.

        Parameters
        ----------
        **options:
            Optional filters such as ``search``, ``status``, ``page``, ``per_page``.

        Returns
        -------
        Collection[object]
            Paginated message list.

        Raises
        ------
        ApiError
            On API or transport failures.

        Examples
        --------
        >>> client.emails.list(status="sent", page=1)
        """
        return self.execute(
            lambda: to_collection(
                self._messages.list_messages(
                    **_query(options),
                    _request_timeout=self._timeout,
                )
            )
        )

    def get(self, message_id: str) -> Response[object]:
        """Retrieve a single message by UUID.

        Parameters
        ----------
        message_id:
            Message UUID.

        Returns
        -------
        Response[object]
            Message payload.

        Raises
        ------
        NotFoundError
            When the message does not exist.
        ApiError
            On API or transport failures.

        Examples
        --------
        >>> client.emails.get("msg_123")
        """
        return self.execute(
            lambda: to_response(
                self._messages.get_message(
                    message=cast(Any, message_id),  # UUID string; validated by the API client
                    _request_timeout=self._timeout,
                )
            )
        )

    def events(self, message_id: str) -> Collection[object]:
        """Retrieve lifecycle events for a single message.

        Parameters
        ----------
        message_id:
            Message UUID.

        Returns
        -------
        Collection[object]
            Message events.

        Raises
        ------
        NotFoundError
            When the message does not exist.
        ApiError
            On API or transport failures.

        Examples
        --------
        >>> client.emails.events("msg_123")
        """
        return self.execute(
            lambda: to_collection(
                self._messages.message_events(
                    message=cast(Any, message_id),  # UUID string; validated by the API client
                    _request_timeout=self._timeout,
                )
            )
        )


def _merge_payload(
    payload: Mapping[str, Any] | None,
    kwargs: Mapping[str, Any],
) -> dict[str, Any]:
    merged: dict[str, Any] = dict(payload or {})
    merged.update({key: value for key, value in kwargs.items() if value is not None})
    return merged


def _query(options: Mapping[str, Any]) -> dict[str, Any]:
    return {key: value for key, value in options.items() if value is not None}
