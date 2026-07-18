"""Delivery-log and outbound message history resource."""

from __future__ import annotations

from collections.abc import Mapping
from typing import Any

from mailermine_generated import MessagesApi

from mailermine.resources.base import BaseResource
from mailermine.support import Collection, Response
from mailermine.support.serialization import to_collection, to_response


class Messages(BaseResource):
    """Delivery-log and outbound message history operations."""

    def __init__(self, messages_api: MessagesApi, *, timeout: float) -> None:
        super().__init__(timeout=timeout)
        self._messages = messages_api

    def list(self, **options: Any) -> Collection[object]:
        """List delivery logs with filters and pagination.

        Parameters
        ----------
        **options:
            Optional filters such as ``search``, ``status``, ``provider``,
            ``from``, ``to``, ``page``, ``per_page``.

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
        >>> client.messages.list(status="delivered", page=1)
        """
        return self.execute(
            lambda: to_collection(
                self._messages.list_messages(
                    **_message_query(options),
                    _request_timeout=self._timeout,
                )
            )
        )

    def get(self, message_id: str) -> Response[object]:
        """Retrieve a delivery log by message UUID.

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
        >>> client.messages.get("msg_123")
        """
        return self.execute(
            lambda: to_response(
                self._messages.get_message(
                    message=message_id,
                    _request_timeout=self._timeout,
                )
            )
        )

    def search(self, query: str, **options: Any) -> Collection[object]:
        """Search delivery logs.

        Parameters
        ----------
        query:
            Free-text search string.
        **options:
            Additional list filters merged with the search query.

        Returns
        -------
        Collection[object]
            Matching messages.

        Raises
        ------
        ApiError
            On API or transport failures.

        Examples
        --------
        >>> client.messages.search("user@example.com")
        """
        return self.list(search=query, **options)

    def filter(self, **options: Any) -> Collection[object]:
        """Filter delivery logs.

        Alias of :meth:`list`.

        Parameters
        ----------
        **options:
            Optional list filters.

        Returns
        -------
        Collection[object]
            Matching messages.

        Raises
        ------
        ApiError
            On API or transport failures.

        Examples
        --------
        >>> client.messages.filter(status="bounced")
        """
        return self.list(**options)

    def events(self, message_id: str) -> Collection[object]:
        """Retrieve lifecycle events for a message.

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
        >>> client.messages.events("msg_123")
        """
        return self.execute(
            lambda: to_collection(
                self._messages.message_events(
                    message=message_id,
                    _request_timeout=self._timeout,
                )
            )
        )

    def timeline(self, message_id: str) -> Collection[object]:
        """Retrieve the lifecycle timeline for a message.

        Alias of :meth:`events`.

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
        >>> client.messages.timeline("msg_123")
        """
        return self.events(message_id)


def _message_query(options: Mapping[str, Any]) -> dict[str, Any]:
    aliases = {"from": "var_from", "from_": "var_from"}
    result: dict[str, Any] = {}
    for key, value in options.items():
        if value is None:
            continue
        result[aliases.get(key, key)] = value
    return result
