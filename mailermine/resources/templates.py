"""Email template resource."""

from __future__ import annotations

from collections.abc import Mapping
from typing import Any

from mailermine_generated import TemplatesApi

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


class Templates(BaseResource):
    """Email template operations."""

    def __init__(self, templates_api: TemplatesApi, *, timeout: float) -> None:
        super().__init__(timeout=timeout)
        self._api = templates_api

    def create(
        self,
        payload: Mapping[str, Any] | None = None,
        /,
        **kwargs: Any,
    ) -> Response[object]:
        """Create a reusable email template.

        Parameters
        ----------
        payload:
            Template fields as a mapping (``name``, ``html``, …).
        **kwargs:
            Alternative keyword fields merged into the request body.

        Returns
        -------
        Response[object]
            Created template payload.

        Raises
        ------
        ValidationError
            When required fields are missing or invalid.
        ApiError
            On API or transport failures.

        Examples
        --------
        >>> client.templates.create(name="Welcome", html="<p>Hi</p>")
        """
        body = to_generated_request(_merge(payload, kwargs))
        return self.execute(
            lambda: to_response(
                self._api.create_template(
                    create_template_request=body,  # type: ignore[arg-type]
                    _request_timeout=self._timeout,
                )
            )
        )

    def list(self, **options: Any) -> Collection[object]:
        """List templates for the authenticated project.

        Parameters
        ----------
        **options:
            Optional filters such as ``search``, ``status``, ``editor_type``,
            ``sort``, ``direction``, ``page``, ``per_page``.

        Returns
        -------
        Collection[object]
            Paginated template list.

        Raises
        ------
        ApiError
            On API or transport failures.

        Examples
        --------
        >>> client.templates.list(status="published")
        """
        return self.execute(
            lambda: to_collection(
                self._api.list_templates(
                    **_query(options),
                    _request_timeout=self._timeout,
                )
            )
        )

    def get(self, template_id: str) -> Response[object]:
        """Retrieve full template content, variables, and branding.

        Parameters
        ----------
        template_id:
            Template UUID.

        Returns
        -------
        Response[object]
            Template payload.

        Raises
        ------
        NotFoundError
            When the template does not exist.
        ApiError
            On API or transport failures.

        Examples
        --------
        >>> client.templates.get("tpl_123")
        """
        return self.execute(
            lambda: to_response(
                self._api.get_template(
                    template=template_id,  # type: ignore[arg-type]
                    _request_timeout=self._timeout,
                )
            )
        )

    def update(
        self,
        template_id: str,
        payload: Mapping[str, Any] | None = None,
        /,
        **kwargs: Any,
    ) -> Response[object]:
        """Partially update template content, variables, status, or branding.

        Parameters
        ----------
        template_id:
            Template UUID.
        payload:
            Fields to update as a mapping.
        **kwargs:
            Alternative keyword fields merged into the request body.

        Returns
        -------
        Response[object]
            Updated template payload.

        Raises
        ------
        NotFoundError
            When the template does not exist.
        ValidationError
            When the update payload is invalid.
        ApiError
            On API or transport failures.

        Examples
        --------
        >>> client.templates.update("tpl_123", name="Renamed")
        """
        body = to_generated_request(_merge(payload, kwargs))
        return self.execute(
            lambda: to_response(
                self._api.update_template(
                    template=template_id,  # type: ignore[arg-type]
                    update_template_request=body,  # type: ignore[arg-type]
                    _request_timeout=self._timeout,
                )
            )
        )

    def preview(
        self,
        template_id: str,
        payload: Mapping[str, Any] | None = None,
        /,
        **kwargs: Any,
    ) -> Response[object]:
        """Render a template with runtime variables without saving or sending.

        Parameters
        ----------
        template_id:
            Template UUID.
        payload:
            Preview fields as a mapping (``variables``, …).
        **kwargs:
            Alternative keyword fields merged into the request body.

        Returns
        -------
        Response[object]
            Rendered preview payload.

        Raises
        ------
        NotFoundError
            When the template does not exist.
        ApiError
            On API or transport failures.

        Examples
        --------
        >>> client.templates.preview("tpl_123", variables={"name": "Sam"})
        """
        body = to_generated_request(_merge(payload, kwargs))
        return self.execute(
            lambda: to_response(
                self._api.preview_template(
                    template=template_id,  # type: ignore[arg-type]
                    preview_template_request=body,  # type: ignore[arg-type]
                    _request_timeout=self._timeout,
                )
            )
        )

    def duplicate(
        self,
        template_id: str,
        payload: Mapping[str, Any] | None = None,
        /,
        **kwargs: Any,
    ) -> Response[object]:
        """Duplicate a template into a new draft.

        Parameters
        ----------
        template_id:
            Template UUID.
        payload:
            Optional duplicate fields as a mapping (``name``, …).
        **kwargs:
            Alternative keyword fields merged into the request body.

        Returns
        -------
        Response[object]
            Duplicated template payload.

        Raises
        ------
        NotFoundError
            When the template does not exist.
        ApiError
            On API or transport failures.

        Examples
        --------
        >>> client.templates.duplicate("tpl_123", name="Copy")
        """
        body = to_generated_request(_merge(payload, kwargs))
        return self.execute(
            lambda: to_response(
                self._api.duplicate_template(
                    template=template_id,  # type: ignore[arg-type]
                    duplicate_template_request=body,  # type: ignore[arg-type]
                    _request_timeout=self._timeout,
                )
            )
        )

    def test(
        self,
        template_id: str,
        payload: Mapping[str, Any] | None = None,
        /,
        **kwargs: Any,
    ) -> Response[object]:
        """Send a test rendering of a template.

        Parameters
        ----------
        template_id:
            Template UUID.
        payload:
            Test fields as a mapping. Must include ``to`` (or ``email``).
        **kwargs:
            Alternative keyword fields merged into the request body.

        Returns
        -------
        Response[object]
            Test send result payload.

        Raises
        ------
        ValidationError
            When the ``to`` recipient is missing.
        NotFoundError
            When the template does not exist.
        ApiError
            On API or transport failures.

        Examples
        --------
        >>> client.templates.test("tpl_123", to="qa@example.com")
        """
        body = _merge(payload, kwargs)
        recipient = body.get("to") or body.pop("email", None)
        if not recipient:
            raise ValidationError("The to field is required.")
        body["to"] = recipient
        request = to_generated_request(body)
        return self.execute(
            lambda: to_response(
                self._api.test_template(
                    template=template_id,  # type: ignore[arg-type]
                    test_template_request=request,  # type: ignore[arg-type]
                    _request_timeout=self._timeout,
                )
            )
        )

    def delete(self, template_id: str) -> Response[JsonObject]:
        """Soft-delete a template.

        Parameters
        ----------
        template_id:
            Template UUID.

        Returns
        -------
        Response[JsonObject]
            Delete acknowledgement (``{"deleted": True}``).

        Raises
        ------
        NotFoundError
            When the template does not exist.
        ApiError
            On API or transport failures.

        Examples
        --------
        >>> client.templates.delete("tpl_123")
        """

        def operation() -> Response[JsonObject]:
            envelope = to_response(
                self._api.delete_template(
                    template=template_id,  # type: ignore[arg-type]
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
