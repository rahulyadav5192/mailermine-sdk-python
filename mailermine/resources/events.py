"""Event querying and message timeline resource."""

from __future__ import annotations

from collections.abc import Mapping
from typing import Any, cast

from mailermine_generated import EventsApi, MessagesApi

from mailermine.resources.base import BaseResource
from mailermine.support import Collection, Response
from mailermine.support.serialization import to_collection, to_response


class Events(BaseResource):
    """Global event querying and message timeline helpers."""

    def __init__(
        self,
        events_api: EventsApi,
        messages_api: MessagesApi,
        *,
        timeout: float,
    ) -> None:
        super().__init__(timeout=timeout)
        self._events = events_api
        self._messages = messages_api

    def list(self, **options: Any) -> Collection[object]:
        """List message events with filters.

        Parameters
        ----------
        **options:
            Optional filters such as ``event_type``, ``source``, ``campaign``,
            ``message``, ``search``, ``from``, ``to``, ``per_page``.

        Returns
        -------
        Collection[object]
            Paginated event list.

        Raises
        ------
        ApiError
            On API or transport failures.

        Examples
        --------
        >>> client.events.list(event_type="email.opened")
        """
        return self.execute(
            lambda: to_collection(
                self._events.list_events(
                    **_event_query(options),
                    _request_timeout=self._timeout,
                )
            )
        )

    def get(self, event_id: str) -> Response[object]:
        """Retrieve a single event by UUID.

        Parameters
        ----------
        event_id:
            Event UUID.

        Returns
        -------
        Response[object]
            Event payload.

        Raises
        ------
        NotFoundError
            When the event does not exist.
        ApiError
            On API or transport failures.

        Examples
        --------
        >>> client.events.get("evt_123")
        """
        return self.execute(
            lambda: to_response(
                self._events.get_event(
                    email_event=event_id,  # type: ignore[arg-type]
                    _request_timeout=self._timeout,
                )
            )
        )

    def timeline(self, message_id: str) -> Collection[object]:
        """Retrieve the event timeline for a message.

        Parameters
        ----------
        message_id:
            Message UUID.

        Returns
        -------
        Collection[object]
            Message event timeline.

        Raises
        ------
        NotFoundError
            When the message does not exist.
        ApiError
            On API or transport failures.

        Examples
        --------
        >>> client.events.timeline("msg_123")
        """
        return self.execute(
            lambda: to_collection(
                self._messages.message_events(
                    message=cast(Any, message_id),  # UUID string; validated by the API client
                    _request_timeout=self._timeout,
                )
            )
        )

    def history(self, message_id: str) -> Collection[object]:
        """Retrieve the event history for a message.

        Alias of :meth:`timeline`.

        Parameters
        ----------
        message_id:
            Message UUID.

        Returns
        -------
        Collection[object]
            Message event history.

        Raises
        ------
        NotFoundError
            When the message does not exist.
        ApiError
            On API or transport failures.

        Examples
        --------
        >>> client.events.history("msg_123")
        """
        return self.timeline(message_id)

    def message(self, message_id: str) -> Response[object]:
        """Retrieve delivery-log detail for a message.

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
        >>> client.events.message("msg_123")
        """
        return self.execute(
            lambda: to_response(
                self._messages.get_message(
                    message=cast(Any, message_id),  # UUID string; validated by the API client
                    _request_timeout=self._timeout,
                )
            )
        )


def _event_query(options: Mapping[str, Any]) -> dict[str, Any]:
    aliases = {
        "from": "var_from",
        "from_": "var_from",
        "campaign_id": "campaign",
        "message_id": "message",
        "type": "event_type",
    }
    result: dict[str, Any] = {}
    for key, value in options.items():
        if value is None:
            continue
        target = aliases.get(key, key)
        result[target] = value
    return result
