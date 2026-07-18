"""Contact import job resource."""

from __future__ import annotations

from collections.abc import Mapping
from typing import Any

from mailermine_generated import ImportsApi

from mailermine.exceptions import ApiError
from mailermine.resources.base import BaseResource
from mailermine.support import Collection, Response
from mailermine.support.serialization import to_collection, to_generated_request, to_response


class Imports(BaseResource):
    """Contact import job operations."""

    def __init__(self, imports_api: ImportsApi, *, timeout: float) -> None:
        super().__init__(timeout=timeout)
        self._api = imports_api

    def list(self) -> Collection[object]:
        """List recent contact import jobs.

        Returns
        -------
        Collection[object]
            Recent import jobs.

        Raises
        ------
        ApiError
            On API or transport failures.

        Examples
        --------
        >>> client.imports.list()
        """
        return self.execute(
            lambda: to_collection(
                self._api.list_contact_imports(
                    _request_timeout=self._timeout,
                )
            )
        )

    def create(
        self,
        file: bytes | str,
        filename: str | None = None,
    ) -> Response[object]:
        """Upload a contact import file (CSV, TSV, XLSX, or XLS).

        Parameters
        ----------
        file:
            File contents as bytes, or a path/string accepted by the transport.
        filename:
            Optional filename recorded with the upload (defaults to ``contacts.csv``
            when ``file`` is bytes).

        Returns
        -------
        Response[object]
            Created import job payload.

        Raises
        ------
        ValidationError
            When the file is missing or invalid.
        ApiError
            On API or transport failures.

        Examples
        --------
        >>> with open("contacts.csv", "rb") as handle:
        ...     client.imports.create(handle.read(), filename="contacts.csv")
        """
        # Multipart upload: pass (filename, bytes) so urllib3 attaches a filename
        # (Node SDK FormData.append('file', blob, filename) parity).
        file_value: bytes | str | tuple[str, bytes]
        if isinstance(file, (bytes, bytearray)):
            file_value = (filename or "contacts.csv", bytes(file))
        else:
            file_value = file
        return self.execute(
            lambda: to_response(
                self._api.import_contacts(
                    file=file_value,
                    _request_timeout=self._timeout,
                )
            )
        )

    def status(self, import_id: str) -> Response[object]:
        """Retrieve import job status and progress.

        Parameters
        ----------
        import_id:
            Import job UUID.

        Returns
        -------
        Response[object]
            Import job payload.

        Raises
        ------
        NotFoundError
            When the import job does not exist.
        ApiError
            On API or transport failures.

        Examples
        --------
        >>> client.imports.status("imp_123")
        """
        return self.execute(
            lambda: to_response(
                self._api.get_contact_import(
                    contact_import=import_id,  # type: ignore[arg-type]
                    _request_timeout=self._timeout,
                )
            )
        )

    def configure(
        self,
        import_id: str,
        payload: Mapping[str, Any] | None = None,
        /,
        **kwargs: Any,
    ) -> Response[object]:
        """Configure field mappings and import options.

        Parameters
        ----------
        import_id:
            Import job UUID.
        payload:
            Configuration fields as a mapping (``mappings``, ``options``, …).
        **kwargs:
            Alternative keyword fields merged into the request body.

        Returns
        -------
        Response[object]
            Updated import job payload.

        Raises
        ------
        NotFoundError
            When the import job does not exist.
        ValidationError
            When the configuration payload is invalid.
        ApiError
            On API or transport failures.

        Examples
        --------
        >>> client.imports.configure("imp_123", mappings={"email": "Email"})
        """
        body = to_generated_request(_merge(payload, kwargs))
        return self.execute(
            lambda: to_response(
                self._api.configure_contact_import(
                    contact_import=import_id,  # type: ignore[arg-type]
                    configure_contact_import_request=body,  # type: ignore[arg-type]
                    _request_timeout=self._timeout,
                )
            )
        )

    def start(self, import_id: str) -> Response[object]:
        """Start processing a configured import.

        Parameters
        ----------
        import_id:
            Import job UUID.

        Returns
        -------
        Response[object]
            Updated import job payload.

        Raises
        ------
        NotFoundError
            When the import job does not exist.
        ApiError
            On API or transport failures.

        Examples
        --------
        >>> client.imports.start("imp_123")
        """
        return self.execute(
            lambda: to_response(
                self._api.start_contact_import(
                    contact_import=import_id,  # type: ignore[arg-type]
                    _request_timeout=self._timeout,
                )
            )
        )

    def cancel(self, import_id: str) -> Response[object]:
        """Import cancellation is not supported by the MailerMine API.

        Parameters
        ----------
        import_id:
            Import job UUID.

        Returns
        -------
        Response[object]
            Never returns; always raises.

        Raises
        ------
        ApiError
            Always, with HTTP status ``405``. Poll :meth:`status` instead.

        Examples
        --------
        >>> client.imports.cancel("imp_123")  # raises ApiError(status=405)
        """
        raise ApiError("Contact import cancellation is not supported.", status=405)


def _merge(payload: Mapping[str, Any] | None, kwargs: Mapping[str, Any]) -> dict[str, Any]:
    merged: dict[str, Any] = dict(payload or {})
    merged.update({key: value for key, value in kwargs.items() if value is not None})
    return merged
