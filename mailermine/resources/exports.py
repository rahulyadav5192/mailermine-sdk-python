"""Contact export job resource."""

from __future__ import annotations

from collections.abc import Mapping
from typing import Any

from mailermine_generated import ExportsApi

from mailermine.resources.base import BaseResource
from mailermine.support import Response
from mailermine.support.serialization import to_generated_request, to_response


class Exports(BaseResource):
    """Contact export job operations."""

    def __init__(self, exports_api: ExportsApi, *, timeout: float) -> None:
        super().__init__(timeout=timeout)
        self._api = exports_api

    def create(
        self,
        payload: Mapping[str, Any] | None = None,
        /,
        **kwargs: Any,
    ) -> Response[object]:
        """Queue an asynchronous CSV contact export.

        Parameters
        ----------
        payload:
            Optional export filters as a mapping (``segment``, ``list``, …).
        **kwargs:
            Alternative keyword fields merged into the request body.

        Returns
        -------
        Response[object]
            Created export job payload.

        Raises
        ------
        ValidationError
            When the export payload is invalid.
        ApiError
            On API or transport failures.

        Examples
        --------
        >>> client.exports.create(segment="seg_123")
        """
        merged = _merge(payload, kwargs)
        body = to_generated_request(merged) if merged else None
        return self.execute(
            lambda: to_response(
                self._api.export_contacts(
                    export_contacts_request=body,  # type: ignore[arg-type]
                    _request_timeout=self._timeout,
                )
            )
        )

    def status(self, export_id: str) -> Response[object]:
        """Retrieve export job status and download metadata.

        Parameters
        ----------
        export_id:
            Export job UUID.

        Returns
        -------
        Response[object]
            Export job payload.

        Raises
        ------
        NotFoundError
            When the export job does not exist.
        ApiError
            On API or transport failures.

        Examples
        --------
        >>> client.exports.status("exp_123")
        """
        return self.execute(
            lambda: to_response(
                self._api.get_contact_export(
                    contact_export=export_id,  # type: ignore[arg-type]
                    _request_timeout=self._timeout,
                )
            )
        )

    def download(self, export_id: str) -> Response[object]:
        """Download a completed export as CSV content.

        The CSV payload is available from ``response.data``.

        Parameters
        ----------
        export_id:
            Export job UUID.

        Returns
        -------
        Response[object]
            Response whose ``data`` is the raw CSV string.

        Raises
        ------
        NotFoundError
            When the export job does not exist.
        ApiError
            On API or transport failures.

        Examples
        --------
        >>> csv = client.exports.download("exp_123").data
        """

        def operation() -> Response[object]:
            csv = self._api.download_contact_export(
                contact_export=export_id,  # type: ignore[arg-type]
                _request_timeout=self._timeout,
            )
            return Response(csv, message="")

        return self.execute(operation)


def _merge(payload: Mapping[str, Any] | None, kwargs: Mapping[str, Any]) -> dict[str, Any]:
    merged: dict[str, Any] = dict(payload or {})
    merged.update({key: value for key, value in kwargs.items() if value is not None})
    return merged
