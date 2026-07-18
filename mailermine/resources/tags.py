"""Contact tag resource."""

from __future__ import annotations

from collections.abc import Mapping, Sequence
from typing import Any

from mailermine_generated import TagsApi

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


class Tags(BaseResource):
    """Contact tag operations."""

    def __init__(self, tags_api: TagsApi, *, timeout: float) -> None:
        super().__init__(timeout=timeout)
        self._api = tags_api

    def create(
        self,
        payload: Mapping[str, Any] | None = None,
        /,
        **kwargs: Any,
    ) -> Response[object]:
        """Create a tag.

        Parameters
        ----------
        payload:
            Tag fields as a mapping (``name``, ``color``, …).
        **kwargs:
            Alternative keyword fields merged into the request body.

        Returns
        -------
        Response[object]
            Created tag payload.

        Raises
        ------
        ValidationError
            When required fields are missing or invalid.
        ApiError
            On API or transport failures.

        Examples
        --------
        >>> client.tags.create(name="VIP")
        """
        body = to_generated_request(_merge(payload, kwargs))
        return self.execute(
            lambda: to_response(
                self._api.create_tag(
                    create_tag_request=body,  # type: ignore[arg-type]
                    _request_timeout=self._timeout,
                )
            )
        )

    def list(self, **options: Any) -> Collection[object]:
        """List tags with filters and pagination.

        Parameters
        ----------
        **options:
            Optional filters such as ``search``, ``sort``, ``direction``,
            ``page``, ``per_page``.

        Returns
        -------
        Collection[object]
            Paginated tag list.

        Raises
        ------
        ApiError
            On API or transport failures.

        Examples
        --------
        >>> client.tags.list(page=1)
        """
        return self.execute(
            lambda: to_collection(
                self._api.list_tags(
                    **_query(options),
                    _request_timeout=self._timeout,
                )
            )
        )

    def get(self, tag_id: str) -> Response[object]:
        """Retrieve a tag by UUID.

        Parameters
        ----------
        tag_id:
            Tag UUID.

        Returns
        -------
        Response[object]
            Tag payload.

        Raises
        ------
        NotFoundError
            When the tag does not exist.
        ApiError
            On API or transport failures.

        Examples
        --------
        >>> client.tags.get("tag_123")
        """
        return self.execute(
            lambda: to_response(
                self._api.get_tag(
                    tag=tag_id,  # type: ignore[arg-type]
                    _request_timeout=self._timeout,
                )
            )
        )

    def update(
        self,
        tag_id: str,
        payload: Mapping[str, Any] | None = None,
        /,
        **kwargs: Any,
    ) -> Response[object]:
        """Partially update a tag.

        Parameters
        ----------
        tag_id:
            Tag UUID.
        payload:
            Fields to update as a mapping.
        **kwargs:
            Alternative keyword fields merged into the request body.

        Returns
        -------
        Response[object]
            Updated tag payload.

        Raises
        ------
        NotFoundError
            When the tag does not exist.
        ValidationError
            When the update payload is invalid.
        ApiError
            On API or transport failures.

        Examples
        --------
        >>> client.tags.update("tag_123", name="Renamed")
        """
        body = to_generated_request(_merge(payload, kwargs))
        return self.execute(
            lambda: to_response(
                self._api.update_tag(
                    tag=tag_id,  # type: ignore[arg-type]
                    update_tag_request=body,  # type: ignore[arg-type]
                    _request_timeout=self._timeout,
                )
            )
        )

    def delete(self, tag_id: str) -> Response[JsonObject]:
        """Delete a tag.

        Parameters
        ----------
        tag_id:
            Tag UUID.

        Returns
        -------
        Response[JsonObject]
            Delete acknowledgement (``{"deleted": True}``).

        Raises
        ------
        NotFoundError
            When the tag does not exist.
        ApiError
            On API or transport failures.

        Examples
        --------
        >>> client.tags.delete("tag_123")
        """

        def operation() -> Response[JsonObject]:
            envelope = to_response(
                self._api.delete_tag(
                    tag=tag_id,  # type: ignore[arg-type]
                    _request_timeout=self._timeout,
                )
            )
            return deleted_response(envelope.message, envelope.success)

        return self.execute(operation)

    def assign(
        self,
        contact_ids: str | Sequence[str],
        tag_ids: str | Sequence[str],
    ) -> Response[object]:
        """Assign one or more tags to one or more contacts.

        Parameters
        ----------
        contact_ids:
            A single contact UUID or a sequence of contact UUIDs.
        tag_ids:
            A single tag UUID or a sequence of tag UUIDs.

        Returns
        -------
        Response[object]
            Tag assignment result payload.

        Raises
        ------
        ValidationError
            When ``contact_ids`` or ``tag_ids`` is empty.
        ApiError
            On API or transport failures.

        Examples
        --------
        >>> client.tags.assign(["con_1"], ["tag_1", "tag_2"])
        """
        body = to_generated_request(
            {
                "contact_ids": _normalize_ids(contact_ids, "contact_ids"),
                "tag_ids": _normalize_ids(tag_ids, "tag_ids"),
            }
        )
        return self.execute(
            lambda: to_response(
                self._api.bulk_assign_tags(
                    bulk_tag_contacts_request=body,  # type: ignore[arg-type]
                    _request_timeout=self._timeout,
                )
            )
        )

    def remove(
        self,
        contact_ids: str | Sequence[str],
        tag_ids: str | Sequence[str],
    ) -> Response[object]:
        """Remove one or more tags from one or more contacts.

        Parameters
        ----------
        contact_ids:
            A single contact UUID or a sequence of contact UUIDs.
        tag_ids:
            A single tag UUID or a sequence of tag UUIDs.

        Returns
        -------
        Response[object]
            Tag assignment result payload.

        Raises
        ------
        ValidationError
            When ``contact_ids`` or ``tag_ids`` is empty.
        ApiError
            On API or transport failures.

        Examples
        --------
        >>> client.tags.remove("con_1", "tag_1")
        """
        body = to_generated_request(
            {
                "contact_ids": _normalize_ids(contact_ids, "contact_ids"),
                "tag_ids": _normalize_ids(tag_ids, "tag_ids"),
            }
        )
        return self.execute(
            lambda: to_response(
                self._api.bulk_remove_tags(
                    bulk_tag_contacts_request=body,  # type: ignore[arg-type]
                    _request_timeout=self._timeout,
                )
            )
        )


def _normalize_ids(value: str | Sequence[str], field: str) -> list[str]:
    ids = [value] if isinstance(value, str) else list(value)
    if not ids:
        raise ValidationError(f"The {field} field must contain at least one id.")
    return [str(item) for item in ids]


def _merge(payload: Mapping[str, Any] | None, kwargs: Mapping[str, Any]) -> dict[str, Any]:
    merged: dict[str, Any] = dict(payload or {})
    merged.update({key: value for key, value in kwargs.items() if value is not None})
    return merged


def _query(options: Mapping[str, Any]) -> dict[str, Any]:
    return {key: value for key, value in options.items() if value is not None}
