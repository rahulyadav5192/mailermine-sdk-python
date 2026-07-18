"""Workspace project resource."""

from __future__ import annotations

from collections.abc import Mapping
from typing import Any

from mailermine_generated import ProjectsApi

from mailermine.resources.base import BaseResource
from mailermine.support import Collection, Response
from mailermine.support.serialization import (
    deleted_response,
    to_collection,
    to_generated_request,
    to_response,
)
from mailermine.types import JsonObject


class Projects(BaseResource):
    """Workspace project operations."""

    def __init__(self, projects_api: ProjectsApi, *, timeout: float) -> None:
        super().__init__(timeout=timeout)
        self._api = projects_api

    def create(
        self,
        payload: Mapping[str, Any] | None = None,
        /,
        **kwargs: Any,
    ) -> Response[object]:
        """Create a project for the authenticated workspace owner.

        Parameters
        ----------
        payload:
            Project fields as a mapping (``name``, …).
        **kwargs:
            Alternative keyword fields merged into the request body.

        Returns
        -------
        Response[object]
            Created project payload.

        Raises
        ------
        ValidationError
            When required fields are missing or invalid.
        ApiError
            On API or transport failures.

        Examples
        --------
        >>> client.projects.create(name="Marketing")
        """
        body = to_generated_request(_merge(payload, kwargs))
        return self.execute(
            lambda: to_response(
                self._api.create_project(
                    create_project_request=body,  # type: ignore[arg-type]
                    _request_timeout=self._timeout,
                )
            )
        )

    def list(self, **options: Any) -> Collection[object]:
        """List projects owned by the authenticated workspace owner.

        Parameters
        ----------
        **options:
            Optional filters such as ``search``, ``status``, ``sort``,
            ``direction``, ``page``, ``per_page``.

        Returns
        -------
        Collection[object]
            Paginated project list.

        Raises
        ------
        ApiError
            On API or transport failures.

        Examples
        --------
        >>> client.projects.list(page=1, per_page=25)
        """
        return self.execute(
            lambda: to_collection(
                self._api.list_projects(
                    **_query(options),
                    _request_timeout=self._timeout,
                )
            )
        )

    def get(self, project_id: str) -> Response[object]:
        """Retrieve a project by UUID.

        Parameters
        ----------
        project_id:
            Project UUID.

        Returns
        -------
        Response[object]
            Project payload.

        Raises
        ------
        NotFoundError
            When the project does not exist.
        ApiError
            On API or transport failures.

        Examples
        --------
        >>> client.projects.get("prj_123")
        """
        return self.execute(
            lambda: to_response(
                self._api.get_project(
                    project=project_id,  # type: ignore[arg-type]
                    _request_timeout=self._timeout,
                )
            )
        )

    def update(
        self,
        project_id: str,
        payload: Mapping[str, Any] | None = None,
        /,
        **kwargs: Any,
    ) -> Response[object]:
        """Partially update a project.

        Parameters
        ----------
        project_id:
            Project UUID.
        payload:
            Fields to update as a mapping.
        **kwargs:
            Alternative keyword fields merged into the request body.

        Returns
        -------
        Response[object]
            Updated project payload.

        Raises
        ------
        NotFoundError
            When the project does not exist.
        ValidationError
            When the update payload is invalid.
        ApiError
            On API or transport failures.

        Examples
        --------
        >>> client.projects.update("prj_123", name="Renamed")
        """
        body = to_generated_request(_merge(payload, kwargs))
        return self.execute(
            lambda: to_response(
                self._api.update_project(
                    project=project_id,  # type: ignore[arg-type]
                    update_project_request=body,  # type: ignore[arg-type]
                    _request_timeout=self._timeout,
                )
            )
        )

    def delete(self, project_id: str) -> Response[JsonObject]:
        """Soft-delete a project.

        Parameters
        ----------
        project_id:
            Project UUID.

        Returns
        -------
        Response[JsonObject]
            Delete acknowledgement (``{"deleted": True}``).

        Raises
        ------
        NotFoundError
            When the project does not exist.
        ApiError
            On API or transport failures.

        Examples
        --------
        >>> client.projects.delete("prj_123")
        """

        def operation() -> Response[JsonObject]:
            envelope = to_response(
                self._api.delete_project(
                    project=project_id,  # type: ignore[arg-type]
                    _request_timeout=self._timeout,
                )
            )
            return deleted_response(envelope.message, envelope.success)

        return self.execute(operation)


def _merge(payload: Mapping[str, Any] | None, kwargs: Mapping[str, Any]) -> dict[str, Any]:
    merged: dict[str, Any] = dict(payload or {})
    merged.update({key: value for key, value in kwargs.items() if value is not None})
    return merged


def _query(options: Mapping[str, Any]) -> dict[str, Any]:
    return {key: value for key, value in options.items() if value is not None}
