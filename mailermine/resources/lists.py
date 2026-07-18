"""Static mailing list resource."""

from __future__ import annotations

from collections.abc import Mapping, Sequence
from typing import Any

from mailermine_generated import ListsApi

from mailermine.exceptions import ValidationError
from mailermine.resources.base import BaseResource
from mailermine.support import Collection, Response
from mailermine.support.serialization import (
    deleted_response,
    to_collection,
    to_generated_request,
    to_response,
)
from mailermine.types import JsonObject


class Lists(BaseResource):
    """Static mailing list operations."""

    def __init__(self, lists_api: ListsApi, *, timeout: float) -> None:
        super().__init__(timeout=timeout)
        self._api = lists_api

    def create(
        self,
        payload: Mapping[str, Any] | None = None,
        /,
        **kwargs: Any,
    ) -> Response[object]:
        """Create a static contact list.

        Parameters
        ----------
        payload:
            List fields as a mapping (``name``, ``description``, ``color``).
        **kwargs:
            Alternative keyword fields merged into the request body.

        Returns
        -------
        Response[object]
            Created list payload.

        Raises
        ------
        ValidationError
            When required fields are missing or invalid.
        ApiError
            On API or transport failures.

        Examples
        --------
        >>> client.lists.create(name="Newsletter")
        """
        body = to_generated_request(_merge(payload, kwargs))
        return self.execute(
            lambda: to_response(
                self._api.create_list(
                    create_list_request=body,  # type: ignore[arg-type]
                    _request_timeout=self._timeout,
                )
            )
        )

    def list(self, **options: Any) -> Collection[object]:
        """List contact lists with filters and pagination.

        Parameters
        ----------
        **options:
            Optional filters such as ``search``, ``sort``, ``direction``,
            ``page``, ``per_page``.

        Returns
        -------
        Collection[object]
            Paginated list collection.

        Raises
        ------
        ApiError
            On API or transport failures.

        Examples
        --------
        >>> client.lists.list(page=1)
        """
        return self.execute(
            lambda: to_collection(
                self._api.list_lists(
                    **_query(options),
                    _request_timeout=self._timeout,
                )
            )
        )

    def get(self, list_id: str) -> Response[object]:
        """Retrieve a list by UUID.

        Parameters
        ----------
        list_id:
            List UUID.

        Returns
        -------
        Response[object]
            List payload.

        Raises
        ------
        NotFoundError
            When the list does not exist.
        ApiError
            On API or transport failures.

        Examples
        --------
        >>> client.lists.get("lst_123")
        """
        return self.execute(
            lambda: to_response(
                self._api.get_list(
                    list=list_id,  # type: ignore[arg-type]
                    _request_timeout=self._timeout,
                )
            )
        )

    def update(
        self,
        list_id: str,
        payload: Mapping[str, Any] | None = None,
        /,
        **kwargs: Any,
    ) -> Response[object]:
        """Partially update a list.

        Parameters
        ----------
        list_id:
            List UUID.
        payload:
            Fields to update as a mapping.
        **kwargs:
            Alternative keyword fields merged into the request body.

        Returns
        -------
        Response[object]
            Updated list payload.

        Raises
        ------
        NotFoundError
            When the list does not exist.
        ValidationError
            When the update payload is invalid.
        ApiError
            On API or transport failures.

        Examples
        --------
        >>> client.lists.update("lst_123", name="Renamed")
        """
        body = to_generated_request(_merge(payload, kwargs))
        return self.execute(
            lambda: to_response(
                self._api.update_list(
                    list=list_id,  # type: ignore[arg-type]
                    update_list_request=body,  # type: ignore[arg-type]
                    _request_timeout=self._timeout,
                )
            )
        )

    def delete(self, list_id: str) -> Response[JsonObject]:
        """Delete a list.

        Parameters
        ----------
        list_id:
            List UUID.

        Returns
        -------
        Response[JsonObject]
            Delete acknowledgement (``{"deleted": True}``).

        Raises
        ------
        NotFoundError
            When the list does not exist.
        ApiError
            On API or transport failures.

        Examples
        --------
        >>> client.lists.delete("lst_123")
        """

        def operation() -> Response[JsonObject]:
            envelope = to_response(
                self._api.delete_list(
                    list=list_id,  # type: ignore[arg-type]
                    _request_timeout=self._timeout,
                )
            )
            return deleted_response(envelope.message, envelope.success)

        return self.execute(operation)

    def add_contact(
        self,
        list_id: str,
        contact_ids: str | Sequence[str],
    ) -> Response[object]:
        """Add one or more contacts to a list.

        Parameters
        ----------
        list_id:
            List UUID.
        contact_ids:
            A single contact UUID or a sequence of contact UUIDs.

        Returns
        -------
        Response[object]
            List membership result payload.

        Raises
        ------
        ValidationError
            When no contact id is provided.
        NotFoundError
            When the list does not exist.
        ApiError
            On API or transport failures.

        Examples
        --------
        >>> client.lists.add_contact("lst_123", ["con_1", "con_2"])
        """
        ids = _normalize_ids(contact_ids)
        body = to_generated_request({"ids": ids})
        return self.execute(
            lambda: to_response(
                self._api.add_contacts_to_list(
                    list=list_id,  # type: ignore[arg-type]
                    list_contacts_membership_request=body,  # type: ignore[arg-type]
                    _request_timeout=self._timeout,
                )
            )
        )

    def remove_contact(
        self,
        list_id: str,
        contact_ids: str | Sequence[str],
    ) -> Response[object]:
        """Remove one or more contacts from a list.

        Parameters
        ----------
        list_id:
            List UUID.
        contact_ids:
            A single contact UUID or a sequence of contact UUIDs.

        Returns
        -------
        Response[object]
            List membership result payload.

        Raises
        ------
        ValidationError
            When no contact id is provided.
        NotFoundError
            When the list does not exist.
        ApiError
            On API or transport failures.

        Examples
        --------
        >>> client.lists.remove_contact("lst_123", "con_1")
        """
        ids = _normalize_ids(contact_ids)
        return self.execute(
            lambda: to_response(
                self._api.remove_contacts_from_list(
                    list=list_id,  # type: ignore[arg-type]
                    ids=ids,  # type: ignore[arg-type]
                    _request_timeout=self._timeout,
                )
            )
        )


def _normalize_ids(contact_ids: str | Sequence[str]) -> list[str]:
    ids = [contact_ids] if isinstance(contact_ids, str) else list(contact_ids)
    if not ids:
        raise ValidationError("At least one contact id is required.")
    return [str(item) for item in ids]


def _merge(payload: Mapping[str, Any] | None, kwargs: Mapping[str, Any]) -> dict[str, Any]:
    merged: dict[str, Any] = dict(payload or {})
    merged.update({key: value for key, value in kwargs.items() if value is not None})
    return merged


def _query(options: Mapping[str, Any]) -> dict[str, Any]:
    return {key: value for key, value in options.items() if value is not None}
