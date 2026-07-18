"""Sending domain resource."""

from __future__ import annotations

from collections.abc import Mapping
from typing import Any

from mailermine_generated import DomainsApi

from mailermine.resources.base import BaseResource
from mailermine.support import Collection, Response
from mailermine.support.serialization import (
    deleted_response,
    to_collection,
    to_generated_request,
    to_response,
)
from mailermine.types import JsonObject

_STATUS_KEYS = (
    "status",
    "verified",
    "verification_status",
    "dns_status",
    "dkim_status",
    "spf_status",
    "tracking_status",
    "last_checked_at",
    "verification_error",
)


class Domains(BaseResource):
    """Sending domain operations."""

    def __init__(self, domains_api: DomainsApi, *, timeout: float) -> None:
        super().__init__(timeout=timeout)
        self._api = domains_api

    def create(
        self,
        payload: Mapping[str, Any] | None = None,
        /,
        **kwargs: Any,
    ) -> Response[object]:
        """Create a sending domain and return required DNS records.

        Parameters
        ----------
        payload:
            Domain fields as a mapping (``domain``, …).
        **kwargs:
            Alternative keyword fields merged into the request body.

        Returns
        -------
        Response[object]
            Created domain payload including DNS records.

        Raises
        ------
        ValidationError
            When required fields are missing or invalid.
        ApiError
            On API or transport failures.

        Examples
        --------
        >>> client.domains.create(domain="mail.example.com")
        """
        body = to_generated_request(_merge(payload, kwargs))
        return self.execute(
            lambda: to_response(
                self._api.create_domain(
                    create_domain_request=body,  # type: ignore[arg-type]
                    _request_timeout=self._timeout,
                )
            )
        )

    def list(self, **options: Any) -> Collection[object]:
        """List sending domains for the authenticated project.

        Parameters
        ----------
        **options:
            Optional filters such as ``search``, ``status``, ``sort``,
            ``direction``, ``page``, ``per_page``.

        Returns
        -------
        Collection[object]
            Paginated domain list.

        Raises
        ------
        ApiError
            On API or transport failures.

        Examples
        --------
        >>> client.domains.list(status="verified")
        """
        return self.execute(
            lambda: to_collection(
                self._api.list_domains(
                    **_query(options),
                    _request_timeout=self._timeout,
                )
            )
        )

    def get(self, domain_id: str) -> Response[object]:
        """Retrieve domain details, DNS records, and verification status.

        Parameters
        ----------
        domain_id:
            Domain UUID.

        Returns
        -------
        Response[object]
            Domain payload.

        Raises
        ------
        NotFoundError
            When the domain does not exist.
        ApiError
            On API or transport failures.

        Examples
        --------
        >>> client.domains.get("dom_123")
        """
        return self.execute(
            lambda: to_response(
                self._api.get_domain(
                    domain=domain_id,  # type: ignore[arg-type]
                    _request_timeout=self._timeout,
                )
            )
        )

    def verify(self, domain_id: str) -> Response[object]:
        """Check DNS and provider verification state.

        Parameters
        ----------
        domain_id:
            Domain UUID.

        Returns
        -------
        Response[object]
            Domain payload with refreshed verification state.

        Raises
        ------
        NotFoundError
            When the domain does not exist.
        ApiError
            On API or transport failures.

        Examples
        --------
        >>> client.domains.verify("dom_123")
        """
        return self.execute(
            lambda: to_response(
                self._api.verify_domain(
                    domain=domain_id,  # type: ignore[arg-type]
                    _request_timeout=self._timeout,
                )
            )
        )

    def dns_records(self, domain_id: str) -> Response[object]:
        """Return DNS records required for domain verification.

        Convenience helper over :meth:`get`.

        Parameters
        ----------
        domain_id:
            Domain UUID.

        Returns
        -------
        Response[object]
            List of DNS records from the domain payload.

        Raises
        ------
        NotFoundError
            When the domain does not exist.
        ApiError
            On API or transport failures.

        Examples
        --------
        >>> client.domains.dns_records("dom_123")
        """
        domain = self.get(domain_id)
        records = _get(domain.data, "dns_records") or []
        return Response(records, message=domain.message, success=domain.success)

    def status(self, domain_id: str) -> Response[JsonObject]:
        """Return a compact verification status view.

        Convenience helper over :meth:`get`.

        Parameters
        ----------
        domain_id:
            Domain UUID.

        Returns
        -------
        Response[JsonObject]
            Verification status summary.

        Raises
        ------
        NotFoundError
            When the domain does not exist.
        ApiError
            On API or transport failures.

        Examples
        --------
        >>> client.domains.status("dom_123")
        """
        domain = self.get(domain_id)
        summary = _pick(domain.data, _STATUS_KEYS)
        return Response(summary, message=domain.message, success=domain.success)

    def delete(self, domain_id: str) -> Response[JsonObject]:
        """Soft-delete a sending domain.

        Parameters
        ----------
        domain_id:
            Domain UUID.

        Returns
        -------
        Response[JsonObject]
            Delete acknowledgement (``{"deleted": True}``).

        Raises
        ------
        NotFoundError
            When the domain does not exist.
        ApiError
            On API or transport failures.

        Examples
        --------
        >>> client.domains.delete("dom_123")
        """

        def operation() -> Response[JsonObject]:
            envelope = to_response(
                self._api.delete_domain(
                    domain=domain_id,  # type: ignore[arg-type]
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


def _snake(value: str) -> str:
    chars: list[str] = []
    for index, char in enumerate(value):
        previous = value[index - 1] if index > 0 else ""
        if char.isupper() and (previous.islower() or previous.isdigit()):
            chars.append("_")
        chars.append(char.lower())
    return "".join(chars)


def _index(data: object) -> dict[str, Any]:
    if isinstance(data, Mapping):
        return {_snake(str(key)): value for key, value in data.items()}
    return {}


def _get(data: object, key: str) -> Any:
    return _index(data).get(_snake(key))


def _pick(data: object, keys: tuple[str, ...]) -> JsonObject:
    index = _index(data)
    return {key: index[_snake(key)] for key in keys if _snake(key) in index}
