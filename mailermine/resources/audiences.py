"""Unified audience (lists and segments) resource."""

from __future__ import annotations

from collections.abc import Mapping, Sequence
from typing import TYPE_CHECKING, Any

from mailermine_generated import AudiencesApi

from mailermine.exceptions import ValidationError
from mailermine.resources.base import BaseResource
from mailermine.support import Collection, Response
from mailermine.support.serialization import to_collection, to_generated_request, to_response
from mailermine.types import JsonObject

if TYPE_CHECKING:
    from mailermine.resources.contacts import Contacts
    from mailermine.resources.lists import Lists
    from mailermine.resources.segments import Segments


class Audiences(BaseResource):
    """Unified audience catalog spanning lists and segments.

    Creation and mutation are delegated to :class:`Lists` or :class:`Segments`
    based on the audience source.
    """

    def __init__(
        self,
        audiences_api: AudiencesApi,
        lists_resource: Lists,
        segments_resource: Segments,
        contacts_resource: Contacts,
        *,
        timeout: float,
    ) -> None:
        super().__init__(timeout=timeout)
        self._api = audiences_api
        self._lists = lists_resource
        self._segments = segments_resource
        self._contacts = contacts_resource

    def create(
        self,
        payload: Mapping[str, Any] | None = None,
        /,
        **kwargs: Any,
    ) -> Response[object]:
        """Create a list- or segment-backed audience.

        Parameters
        ----------
        payload:
            Audience fields as a mapping. Use ``source`` to select ``"list"``
            (default) or ``"segment"``.
        **kwargs:
            Alternative keyword fields merged into the request body.

        Returns
        -------
        Response[object]
            Created list or segment payload.

        Raises
        ------
        ValidationError
            When ``source`` is invalid or required fields are missing.
        ApiError
            On API or transport failures.

        Examples
        --------
        >>> client.audiences.create(name="Newsletter", source="list")
        """
        body = _merge(payload, kwargs)
        source = body.pop("source", "list")
        _assert_source(source)
        if source == "segment":
            return self._segments.create(
                {
                    "name": body.get("name"),
                    "description": body.get("description"),
                    "rules": body.get("rules", {"logic": "and", "rules": []}),
                }
            )
        return self._lists.create(
            {
                "name": body.get("name"),
                "description": body.get("description"),
                "color": body.get("color"),
            }
        )

    def list(self, **options: Any) -> Collection[object]:
        """List audiences with pagination.

        Parameters
        ----------
        **options:
            Optional filters such as ``page`` and ``per_page``.

        Returns
        -------
        Collection[object]
            Paginated audience list.

        Raises
        ------
        ApiError
            On API or transport failures.

        Examples
        --------
        >>> client.audiences.list(page=1)
        """
        return self.execute(
            lambda: to_collection(
                self._api.list_audiences(
                    **_query(options),
                    _request_timeout=self._timeout,
                )
            )
        )

    def get(self, source: str, audience_id: str) -> Response[object]:
        """Retrieve an audience by source and UUID.

        Parameters
        ----------
        source:
            Audience backing type (``"list"`` or ``"segment"``).
        audience_id:
            List or segment UUID.

        Returns
        -------
        Response[object]
            Audience payload.

        Raises
        ------
        ValidationError
            When ``source`` is invalid.
        NotFoundError
            When the audience does not exist.
        ApiError
            On API or transport failures.

        Examples
        --------
        >>> client.audiences.get("list", "lst_123")
        """
        _assert_source(source)
        return self.execute(
            lambda: to_response(
                self._api.get_audience(
                    source=source,
                    audience=audience_id,  # type: ignore[arg-type]
                    _request_timeout=self._timeout,
                )
            )
        )

    def update(
        self,
        source: str,
        audience_id: str,
        payload: Mapping[str, Any] | None = None,
        /,
        **kwargs: Any,
    ) -> Response[object]:
        """Update a list- or segment-backed audience.

        Parameters
        ----------
        source:
            Audience backing type (``"list"`` or ``"segment"``).
        audience_id:
            List or segment UUID.
        payload:
            Fields to update as a mapping.
        **kwargs:
            Alternative keyword fields merged into the request body.

        Returns
        -------
        Response[object]
            Updated list or segment payload.

        Raises
        ------
        ValidationError
            When ``source`` is invalid.
        NotFoundError
            When the audience does not exist.
        ApiError
            On API or transport failures.

        Examples
        --------
        >>> client.audiences.update("list", "lst_123", name="Renamed")
        """
        _assert_source(source)
        body = _merge(payload, kwargs)
        if source == "segment":
            body.pop("color", None)
            return self._segments.update(audience_id, body)
        body.pop("rules", None)
        return self._lists.update(audience_id, body)

    def delete(self, source: str, audience_id: str) -> Response[JsonObject]:
        """Delete a list- or segment-backed audience.

        Parameters
        ----------
        source:
            Audience backing type (``"list"`` or ``"segment"``).
        audience_id:
            List or segment UUID.

        Returns
        -------
        Response[JsonObject]
            Delete acknowledgement (``{"deleted": True}``).

        Raises
        ------
        ValidationError
            When ``source`` is invalid.
        NotFoundError
            When the audience does not exist.
        ApiError
            On API or transport failures.

        Examples
        --------
        >>> client.audiences.delete("segment", "seg_123")
        """
        _assert_source(source)
        if source == "segment":
            return self._segments.delete(audience_id)
        return self._lists.delete(audience_id)

    def contacts(self, source: str, audience_id: str, **options: Any) -> Collection[object]:
        """List contacts belonging to an audience.

        Parameters
        ----------
        source:
            Audience backing type (``"list"`` or ``"segment"``).
        audience_id:
            List or segment UUID.
        **options:
            Additional contact list filters.

        Returns
        -------
        Collection[object]
            Paginated contact list scoped to the audience.

        Raises
        ------
        ValidationError
            When ``source`` is invalid.
        ApiError
            On API or transport failures.

        Examples
        --------
        >>> client.audiences.contacts("list", "lst_123", page=1)
        """
        _assert_source(source)
        scope = "segment" if source == "segment" else "list"
        return self._contacts.list(**{scope: audience_id, **options})

    def add_contacts(
        self,
        audience_id: str,
        contact_ids: str | Sequence[str],
    ) -> Response[object]:
        """Add contacts to a list-backed audience.

        Parameters
        ----------
        audience_id:
            List UUID of the audience.
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
            When the audience does not exist.
        ApiError
            On API or transport failures.

        Examples
        --------
        >>> client.audiences.add_contacts("lst_123", ["con_1", "con_2"])
        """
        ids = _normalize_ids(contact_ids)
        body = to_generated_request({"ids": ids})
        return self.execute(
            lambda: to_response(
                self._api.add_audience_members(
                    source="list",
                    audience=audience_id,  # type: ignore[arg-type]
                    list_contacts_membership_request=body,  # type: ignore[arg-type]
                    _request_timeout=self._timeout,
                )
            )
        )

    def remove_contacts(
        self,
        audience_id: str,
        contact_ids: str | Sequence[str],
    ) -> Response[object]:
        """Remove contacts from a list-backed audience.

        Parameters
        ----------
        audience_id:
            List UUID of the audience.
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
            When the audience does not exist.
        ApiError
            On API or transport failures.

        Examples
        --------
        >>> client.audiences.remove_contacts("lst_123", "con_1")
        """
        ids = _normalize_ids(contact_ids)
        return self.execute(
            lambda: to_response(
                self._api.remove_audience_members(
                    source="list",
                    audience=audience_id,  # type: ignore[arg-type]
                    ids=ids,  # type: ignore[arg-type]
                    _request_timeout=self._timeout,
                )
            )
        )


def _assert_source(source: str) -> None:
    if source not in ("list", "segment"):
        raise ValidationError('Audience source must be "list" or "segment".')


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
