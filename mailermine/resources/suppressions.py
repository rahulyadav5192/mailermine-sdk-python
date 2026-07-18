"""Account suppression-list resource."""

from __future__ import annotations

import re
from collections.abc import Mapping
from typing import Any, cast

from mailermine_generated import SuppressionsApi

from mailermine.exceptions import ValidationError
from mailermine.resources.base import BaseResource
from mailermine.support import Collection, Response
from mailermine.support.serialization import (
    deleted_response,
    to_collection,
    to_generated_request,
    to_response,
)
from mailermine.types import JsonObject, JsonValue

_EMAIL = re.compile(r"^[^\s@]+@[^\s@]+\.[^\s@]+$")


class Suppressions(BaseResource):
    """Account suppression-list operations."""

    def __init__(self, suppressions_api: SuppressionsApi, *, timeout: float) -> None:
        super().__init__(timeout=timeout)
        self._api = suppressions_api

    def list(self, **options: Any) -> Collection[object]:
        """List suppressions with filters.

        Parameters
        ----------
        **options:
            Optional filters such as ``search``, ``reason``, ``per_page``.

        Returns
        -------
        Collection[object]
            Paginated suppression list.

        Raises
        ------
        ApiError
            On API or transport failures.

        Examples
        --------
        >>> client.suppressions.list(reason="bounce")
        """
        return self.execute(
            lambda: to_collection(
                self._api.list_suppressions(
                    **_query(options),
                    _request_timeout=self._timeout,
                )
            )
        )

    def get(self, suppression_id: str) -> Response[object]:
        """Retrieve a suppression by UUID.

        Parameters
        ----------
        suppression_id:
            Suppression UUID.

        Returns
        -------
        Response[object]
            Suppression payload.

        Raises
        ------
        NotFoundError
            When the suppression does not exist.
        ApiError
            On API or transport failures.

        Examples
        --------
        >>> client.suppressions.get("sup_123")
        """
        return self.execute(
            lambda: to_response(
                self._api.get_suppression(
                    suppression=suppression_id,  # type: ignore[arg-type]
                    _request_timeout=self._timeout,
                )
            )
        )

    def add(
        self,
        payload: Mapping[str, Any] | None = None,
        /,
        **kwargs: Any,
    ) -> Response[object]:
        """Add an email address to the suppression list.

        Parameters
        ----------
        payload:
            Suppression fields as a mapping (``email``, ``reason``, …).
        **kwargs:
            Alternative keyword fields merged into the request body.

        Returns
        -------
        Response[object]
            Created suppression payload.

        Raises
        ------
        ValidationError
            When required fields are missing or invalid.
        ApiError
            On API or transport failures.

        Examples
        --------
        >>> client.suppressions.add(email="user@example.com", reason="manual")
        """
        body = to_generated_request(_merge(payload, kwargs))
        return self.execute(
            lambda: to_response(
                self._api.create_suppression(
                    create_suppression_request=body,  # type: ignore[arg-type]
                    _request_timeout=self._timeout,
                )
            )
        )

    def remove(self, suppression_id: str) -> Response[JsonObject]:
        """Remove a suppression by UUID.

        Parameters
        ----------
        suppression_id:
            Suppression UUID.

        Returns
        -------
        Response[JsonObject]
            Delete acknowledgement (``{"deleted": True}``).

        Raises
        ------
        NotFoundError
            When the suppression does not exist.
        ApiError
            On API or transport failures.

        Examples
        --------
        >>> client.suppressions.remove("sup_123")
        """

        def operation() -> Response[JsonObject]:
            envelope = to_response(
                self._api.delete_suppression(
                    suppression=suppression_id,  # type: ignore[arg-type]
                    _request_timeout=self._timeout,
                )
            )
            return deleted_response(envelope.message, envelope.success)

        return self.execute(operation)

    def restore(self, suppression_id: str) -> Response[object]:
        """Restore a removed or soft-deleted suppression.

        Parameters
        ----------
        suppression_id:
            Suppression UUID.

        Returns
        -------
        Response[object]
            Restored suppression payload.

        Raises
        ------
        NotFoundError
            When the suppression does not exist.
        ApiError
            On API or transport failures.

        Examples
        --------
        >>> client.suppressions.restore("sup_123")
        """
        return self.execute(
            lambda: to_response(
                self._api.restore_suppression(
                    suppression=suppression_id,  # type: ignore[arg-type]
                    _request_timeout=self._timeout,
                )
            )
        )

    def check(self, email: str) -> Response[JsonObject]:
        """Check whether an exact email address is suppressed.

        Parameters
        ----------
        email:
            Email address to check.

        Returns
        -------
        Response[JsonObject]
            Result payload with ``email``, ``suppressed``, and ``suppression``.

        Raises
        ------
        ValidationError
            When a valid email address is not provided.
        ApiError
            On API or transport failures.

        Examples
        --------
        >>> client.suppressions.check("user@example.com")
        """
        normalized = email.strip().lower()
        if not _EMAIL.match(normalized):
            raise ValidationError("A valid email address is required.")

        matches = self.list(search=normalized, per_page=100)
        suppression: object | None = None
        for item in matches:
            if isinstance(item, Mapping):
                value = item.get("email")
                if isinstance(value, str) and value.lower() == normalized:
                    suppression = item
                    break

        result: JsonObject = {
            "email": normalized,
            "suppressed": suppression is not None,
            "suppression": cast("JsonValue", suppression),
        }
        return Response(result, message="OK")


def _merge(payload: Mapping[str, Any] | None, kwargs: Mapping[str, Any]) -> dict[str, Any]:
    merged: dict[str, Any] = dict(payload or {})
    merged.update({key: value for key, value in kwargs.items() if value is not None})
    return merged


def _query(options: Mapping[str, Any]) -> dict[str, Any]:
    return {key: value for key, value in options.items() if value is not None}
