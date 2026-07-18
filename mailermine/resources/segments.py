"""Dynamic segment resource."""

from __future__ import annotations

from collections.abc import Mapping, Sequence
from typing import Any

from mailermine_generated import SegmentsApi

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


class Segments(BaseResource):
    """Dynamic segment operations."""

    def __init__(self, segments_api: SegmentsApi, *, timeout: float) -> None:
        super().__init__(timeout=timeout)
        self._api = segments_api

    def create(
        self,
        payload: Mapping[str, Any] | None = None,
        /,
        **kwargs: Any,
    ) -> Response[object]:
        """Create a dynamic segment.

        Parameters
        ----------
        payload:
            Segment fields as a mapping (``name``, ``rules``, …).
        **kwargs:
            Alternative keyword fields merged into the request body.

        Returns
        -------
        Response[object]
            Created segment payload.

        Raises
        ------
        ValidationError
            When required fields are missing or invalid.
        ApiError
            On API or transport failures.

        Examples
        --------
        >>> client.segments.create(
        ...     name="Active",
        ...     rules={"logic": "and", "rules": []},
        ... )
        """
        body = to_generated_request(_merge(payload, kwargs))
        return self.execute(
            lambda: to_response(
                self._api.create_segment(
                    create_segment_request=body,  # type: ignore[arg-type]
                    _request_timeout=self._timeout,
                )
            )
        )

    def list(self, **options: Any) -> Collection[object]:
        """List segments with filters and pagination.

        Parameters
        ----------
        **options:
            Optional filters such as ``search``, ``sort``, ``direction``,
            ``page``, ``per_page``.

        Returns
        -------
        Collection[object]
            Paginated segment list.

        Raises
        ------
        ApiError
            On API or transport failures.

        Examples
        --------
        >>> client.segments.list(page=1)
        """
        return self.execute(
            lambda: to_collection(
                self._api.list_segments(
                    **_query(options),
                    _request_timeout=self._timeout,
                )
            )
        )

    def get(self, segment_id: str) -> Response[object]:
        """Retrieve a segment by UUID.

        Parameters
        ----------
        segment_id:
            Segment UUID.

        Returns
        -------
        Response[object]
            Segment payload.

        Raises
        ------
        NotFoundError
            When the segment does not exist.
        ApiError
            On API or transport failures.

        Examples
        --------
        >>> client.segments.get("seg_123")
        """
        return self.execute(
            lambda: to_response(
                self._api.get_segment(
                    segment=segment_id,  # type: ignore[arg-type]
                    _request_timeout=self._timeout,
                )
            )
        )

    def update(
        self,
        segment_id: str,
        payload: Mapping[str, Any] | None = None,
        /,
        **kwargs: Any,
    ) -> Response[object]:
        """Partially update a segment.

        Parameters
        ----------
        segment_id:
            Segment UUID.
        payload:
            Fields to update as a mapping.
        **kwargs:
            Alternative keyword fields merged into the request body.

        Returns
        -------
        Response[object]
            Updated segment payload.

        Raises
        ------
        NotFoundError
            When the segment does not exist.
        ValidationError
            When the update payload is invalid.
        ApiError
            On API or transport failures.

        Examples
        --------
        >>> client.segments.update("seg_123", name="Renamed")
        """
        body = to_generated_request(_merge(payload, kwargs))
        return self.execute(
            lambda: to_response(
                self._api.update_segment(
                    segment=segment_id,  # type: ignore[arg-type]
                    update_segment_request=body,  # type: ignore[arg-type]
                    _request_timeout=self._timeout,
                )
            )
        )

    def delete(self, segment_id: str) -> Response[JsonObject]:
        """Delete a segment.

        Parameters
        ----------
        segment_id:
            Segment UUID.

        Returns
        -------
        Response[JsonObject]
            Delete acknowledgement (``{"deleted": True}``).

        Raises
        ------
        NotFoundError
            When the segment does not exist.
        ApiError
            On API or transport failures.

        Examples
        --------
        >>> client.segments.delete("seg_123")
        """

        def operation() -> Response[JsonObject]:
            envelope = to_response(
                self._api.delete_segment(
                    segment=segment_id,  # type: ignore[arg-type]
                    _request_timeout=self._timeout,
                )
            )
            return deleted_response(envelope.message, envelope.success)

        return self.execute(operation)

    def preview(
        self,
        segment_id: str | None = None,
        rules: Mapping[str, Any] | Sequence[Any] | None = None,
    ) -> Response[object]:
        """Preview a saved segment or unsaved segment rules.

        Provide ``segment_id`` to preview a saved segment, or ``rules`` to
        preview an unsaved rule tree.

        Parameters
        ----------
        segment_id:
            Saved segment UUID to preview.
        rules:
            Unsaved rule tree to preview when ``segment_id`` is not supplied.

        Returns
        -------
        Response[object]
            Segment preview payload.

        Raises
        ------
        ValidationError
            When neither ``segment_id`` nor ``rules`` is provided.
        NotFoundError
            When the saved segment does not exist.
        ApiError
            On API or transport failures.

        Examples
        --------
        >>> client.segments.preview("seg_123")
        >>> client.segments.preview(rules={"logic": "and", "rules": []})
        """
        if segment_id:
            return self.execute(
                lambda: to_response(
                    self._api.preview_segment(
                        segment=segment_id,  # type: ignore[arg-type]
                        _request_timeout=self._timeout,
                    )
                )
            )

        if rules is None:
            raise ValidationError("Provide a segment id or rules when calling preview().")

        body = to_generated_request({"rules": rules})
        return self.execute(
            lambda: to_response(
                self._api.preview_segment_rules(
                    preview_segment_request=body,  # type: ignore[arg-type]
                    _request_timeout=self._timeout,
                )
            )
        )


def _merge(payload: Mapping[str, Any] | None, kwargs: Mapping[str, Any]) -> dict[str, Any]:
    merged: dict[str, Any] = dict(payload or {})
    merged.update({key: value for key, value in kwargs.items() if value is not None})
    return merged


def _query(options: Mapping[str, Any]) -> dict[str, Any]:
    return {key: value for key, value in options.items() if value is not None}
