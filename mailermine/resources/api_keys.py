"""Project API key resource."""

from __future__ import annotations

from collections.abc import Mapping
from typing import Any

from mailermine_generated import APIKeysApi

from mailermine.resources.base import BaseResource
from mailermine.support import Collection, Response
from mailermine.support.serialization import (
    deleted_response,
    to_collection,
    to_generated_request,
    to_response,
)
from mailermine.types import JsonObject


class ApiKeys(BaseResource):
    """Project API key operations."""

    def __init__(self, api_keys_api: APIKeysApi, *, timeout: float) -> None:
        super().__init__(timeout=timeout)
        self._api = api_keys_api

    def create(
        self,
        project_id: str,
        payload: Mapping[str, Any] | None = None,
        /,
        **kwargs: Any,
    ) -> Response[object]:
        """Create an API key. The plaintext secret is returned once.

        Parameters
        ----------
        project_id:
            Owning project UUID.
        payload:
            API key fields as a mapping (``name``, ``scopes``, …).
        **kwargs:
            Alternative keyword fields merged into the request body.

        Returns
        -------
        Response[object]
            Created API key payload including the one-time secret.

        Raises
        ------
        ValidationError
            When required fields are missing or invalid.
        ApiError
            On API or transport failures.

        Examples
        --------
        >>> client.api_keys.create("prj_123", name="CI", scopes=["emails.send"])
        """
        body = to_generated_request(_merge(payload, kwargs))
        return self.execute(
            lambda: to_response(
                self._api.create_api_key(
                    project=project_id,  # type: ignore[arg-type]
                    create_api_key_request=body,  # type: ignore[arg-type]
                    _request_timeout=self._timeout,
                )
            )
        )

    def list(self, project_id: str, **options: Any) -> Collection[object]:
        """List masked API keys for a project. Secrets are never returned.

        Parameters
        ----------
        project_id:
            Owning project UUID.
        **options:
            Optional filters such as ``search``, ``status``, ``sort``,
            ``direction``, ``page``, ``per_page``.

        Returns
        -------
        Collection[object]
            Paginated API key list.

        Raises
        ------
        NotFoundError
            When the project does not exist.
        ApiError
            On API or transport failures.

        Examples
        --------
        >>> client.api_keys.list("prj_123", status="active")
        """
        return self.execute(
            lambda: to_collection(
                self._api.list_api_keys(
                    project=project_id,  # type: ignore[arg-type]
                    **_query(options),
                    _request_timeout=self._timeout,
                )
            )
        )

    def get(self, project_id: str, api_key_id: str) -> Response[object]:
        """Retrieve API key metadata without the secret.

        Parameters
        ----------
        project_id:
            Owning project UUID.
        api_key_id:
            API key UUID.

        Returns
        -------
        Response[object]
            API key payload.

        Raises
        ------
        NotFoundError
            When the project or API key does not exist.
        ApiError
            On API or transport failures.

        Examples
        --------
        >>> client.api_keys.get("prj_123", "key_456")
        """
        return self.execute(
            lambda: to_response(
                self._api.get_api_key(
                    project=project_id,  # type: ignore[arg-type]
                    api_key=api_key_id,  # type: ignore[arg-type]
                    _request_timeout=self._timeout,
                )
            )
        )

    def update(
        self,
        project_id: str,
        api_key_id: str,
        payload: Mapping[str, Any] | None = None,
        /,
        **kwargs: Any,
    ) -> Response[object]:
        """Update API key name, expiry, status, or scopes.

        Parameters
        ----------
        project_id:
            Owning project UUID.
        api_key_id:
            API key UUID.
        payload:
            Fields to update as a mapping.
        **kwargs:
            Alternative keyword fields merged into the request body.

        Returns
        -------
        Response[object]
            Updated API key payload.

        Raises
        ------
        NotFoundError
            When the project or API key does not exist.
        ValidationError
            When the update payload is invalid.
        ApiError
            On API or transport failures.

        Examples
        --------
        >>> client.api_keys.update("prj_123", "key_456", name="Renamed")
        """
        body = to_generated_request(_merge(payload, kwargs))
        return self.execute(
            lambda: to_response(
                self._api.update_api_key(
                    project=project_id,  # type: ignore[arg-type]
                    api_key=api_key_id,  # type: ignore[arg-type]
                    update_api_key_request=body,  # type: ignore[arg-type]
                    _request_timeout=self._timeout,
                )
            )
        )

    def delete(self, project_id: str, api_key_id: str) -> Response[JsonObject]:
        """Soft-delete and revoke an API key.

        Parameters
        ----------
        project_id:
            Owning project UUID.
        api_key_id:
            API key UUID.

        Returns
        -------
        Response[JsonObject]
            Delete acknowledgement (``{"deleted": True}``).

        Raises
        ------
        NotFoundError
            When the project or API key does not exist.
        ApiError
            On API or transport failures.

        Examples
        --------
        >>> client.api_keys.delete("prj_123", "key_456")
        """

        def operation() -> Response[JsonObject]:
            envelope = to_response(
                self._api.delete_api_key(
                    project=project_id,  # type: ignore[arg-type]
                    api_key=api_key_id,  # type: ignore[arg-type]
                    _request_timeout=self._timeout,
                )
            )
            return deleted_response(envelope.message, envelope.success)

        return self.execute(operation)

    def rotate(self, project_id: str, api_key_id: str) -> Response[object]:
        """Rotate an API key and return its new one-time plaintext secret.

        Parameters
        ----------
        project_id:
            Owning project UUID.
        api_key_id:
            API key UUID.

        Returns
        -------
        Response[object]
            Rotated API key payload including the new one-time secret.

        Raises
        ------
        NotFoundError
            When the project or API key does not exist.
        ApiError
            On API or transport failures.

        Examples
        --------
        >>> client.api_keys.rotate("prj_123", "key_456")
        """
        return self.execute(
            lambda: to_response(
                self._api.rotate_api_key(
                    project=project_id,  # type: ignore[arg-type]
                    api_key=api_key_id,  # type: ignore[arg-type]
                    _request_timeout=self._timeout,
                )
            )
        )

    def reveal(self, project_id: str, api_key_id: str) -> Response[object]:
        """Attempt to reveal an API key.

        MailerMine normally rejects this operation because secrets are
        irreversibly hashed; the API error is mapped to the public SDK
        exception hierarchy.

        Parameters
        ----------
        project_id:
            Owning project UUID.
        api_key_id:
            API key UUID.

        Returns
        -------
        Response[object]
            API key payload when the API permits reveal.

        Raises
        ------
        PlanError
            When the account plan or scope does not permit the operation.
        ApiError
            On API or transport failures.

        Examples
        --------
        >>> client.api_keys.reveal("prj_123", "key_456")
        """
        return self.execute(
            lambda: to_response(
                self._api.reveal_api_key(
                    project=project_id,  # type: ignore[arg-type]
                    api_key=api_key_id,  # type: ignore[arg-type]
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
