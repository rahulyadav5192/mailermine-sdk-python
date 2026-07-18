"""Contact resource."""

from __future__ import annotations

from collections.abc import Mapping
from typing import Any

from mailermine_generated import ContactsApi

from mailermine.exceptions import NotFoundError, ValidationError
from mailermine.resources.base import BaseResource
from mailermine.support import Collection, Response
from mailermine.support.serialization import (
    deleted_response,
    to_collection,
    to_generated_request,
    to_response,
)
from mailermine.types import JsonObject


class Contacts(BaseResource):
    """Contact operations."""

    def __init__(self, contacts_api: ContactsApi, *, timeout: float) -> None:
        super().__init__(timeout=timeout)
        self._api = contacts_api

    def create(
        self,
        payload: Mapping[str, Any] | None = None,
        /,
        **kwargs: Any,
    ) -> Response[object]:
        """Create a contact with optional lists, tags, metadata, and fields.

        Parameters
        ----------
        payload:
            Contact fields as a mapping (``email``, ``first_name``, …).
        **kwargs:
            Alternative keyword fields merged into the request body.

        Returns
        -------
        Response[object]
            Created contact payload.

        Raises
        ------
        ValidationError
            When required fields are missing or invalid.
        ApiError
            On API or transport failures.

        Examples
        --------
        >>> client.contacts.create(email="john@example.com", subscribed=True)
        """
        body = to_generated_request(_merge(payload, kwargs))
        return self.execute(
            lambda: to_response(
                self._api.create_contact(
                    create_contact_request=body,  # type: ignore[arg-type]
                    _request_timeout=self._timeout,
                )
            )
        )

    def upsert(
        self,
        payload: Mapping[str, Any] | None = None,
        /,
        **kwargs: Any,
    ) -> Response[object]:
        """Create a contact or update the existing contact with the same email.

        Parameters
        ----------
        payload:
            Contact fields as a mapping. Must include ``email``.
        **kwargs:
            Alternative keyword fields merged into the request body.

        Returns
        -------
        Response[object]
            Created or updated contact payload.

        Raises
        ------
        ValidationError
            When ``email`` is missing.
        ApiError
            On API or transport failures.

        Examples
        --------
        >>> client.contacts.upsert(email="john@example.com", first_name="John")
        """
        body = _merge(payload, kwargs)
        email = str(body.get("email", "")).strip()
        if not email:
            raise ValidationError("The email field is required for upsert().")
        existing = self._find_by_email(email)
        if existing is not None:
            return self.update(_identifier(existing), body)
        return self.create(body)

    def list(self, **options: Any) -> Collection[object]:
        """List contacts with filters and pagination.

        Parameters
        ----------
        **options:
            Optional filters such as ``search``, ``status``, ``subscribed``,
            ``list``, ``tag``, ``segment``, ``sort``, ``direction``, ``page``,
            ``per_page``.

        Returns
        -------
        Collection[object]
            Paginated contact list.

        Raises
        ------
        ApiError
            On API or transport failures.

        Examples
        --------
        >>> client.contacts.list(subscribed=True, page=1)
        """
        return self.execute(
            lambda: to_collection(
                self._api.list_contacts(
                    **_query(options),
                    _request_timeout=self._timeout,
                )
            )
        )

    def get(self, contact_id: str) -> Response[object]:
        """Retrieve a contact by UUID.

        Parameters
        ----------
        contact_id:
            Contact UUID.

        Returns
        -------
        Response[object]
            Contact payload.

        Raises
        ------
        NotFoundError
            When the contact does not exist.
        ApiError
            On API or transport failures.

        Examples
        --------
        >>> client.contacts.get("con_123")
        """
        return self.execute(
            lambda: to_response(
                self._api.get_contact(
                    contact=contact_id,  # type: ignore[arg-type]
                    _request_timeout=self._timeout,
                )
            )
        )

    def update(
        self,
        contact_id: str,
        payload: Mapping[str, Any] | None = None,
        /,
        **kwargs: Any,
    ) -> Response[object]:
        """Partially update a contact.

        Parameters
        ----------
        contact_id:
            Contact UUID.
        payload:
            Fields to update as a mapping.
        **kwargs:
            Alternative keyword fields merged into the request body.

        Returns
        -------
        Response[object]
            Updated contact payload.

        Raises
        ------
        NotFoundError
            When the contact does not exist.
        ValidationError
            When the update payload is invalid.
        ApiError
            On API or transport failures.

        Examples
        --------
        >>> client.contacts.update("con_123", first_name="Jane")
        """
        body = to_generated_request(_merge(payload, kwargs))
        return self.execute(
            lambda: to_response(
                self._api.update_contact(
                    contact=contact_id,  # type: ignore[arg-type]
                    update_contact_request=body,  # type: ignore[arg-type]
                    _request_timeout=self._timeout,
                )
            )
        )

    def delete(self, contact_id: str) -> Response[JsonObject]:
        """Soft-delete a contact.

        Parameters
        ----------
        contact_id:
            Contact UUID.

        Returns
        -------
        Response[JsonObject]
            Delete acknowledgement (``{"deleted": True}``).

        Raises
        ------
        NotFoundError
            When the contact does not exist.
        ApiError
            On API or transport failures.

        Examples
        --------
        >>> client.contacts.delete("con_123")
        """

        def operation() -> Response[JsonObject]:
            envelope = to_response(
                self._api.delete_contact(
                    contact=contact_id,  # type: ignore[arg-type]
                    _request_timeout=self._timeout,
                )
            )
            return deleted_response(envelope.message, envelope.success)

        return self.execute(operation)

    def search(self, query: str, **options: Any) -> Collection[object]:
        """Search contacts by free-text query across email and name fields.

        Parameters
        ----------
        query:
            Free-text search string.
        **options:
            Additional list filters merged with the search query.

        Returns
        -------
        Collection[object]
            Matching contacts.

        Raises
        ------
        ApiError
            On API or transport failures.

        Examples
        --------
        >>> client.contacts.search("john", per_page=50)
        """
        return self.list(search=query, **options)

    def identify(self, email: str) -> Response[object]:
        """Identify an existing contact by exact email match.

        Parameters
        ----------
        email:
            Contact email address.

        Returns
        -------
        Response[object]
            The matching contact payload.

        Raises
        ------
        NotFoundError
            When no contact matches the email.
        ApiError
            On API or transport failures.

        Examples
        --------
        >>> client.contacts.identify("john@example.com")
        """
        contact = self._find_by_email(email)
        if contact is None:
            raise NotFoundError(f"No contact found for email [{email}].", status=404)
        return Response(contact, message="Contact identified.")

    def subscribe(self, contact_id: str) -> Response[object]:
        """Mark a contact as subscribed.

        Parameters
        ----------
        contact_id:
            Contact UUID.

        Returns
        -------
        Response[object]
            Updated contact payload.

        Raises
        ------
        NotFoundError
            When the contact does not exist.
        ApiError
            On API or transport failures.

        Examples
        --------
        >>> client.contacts.subscribe("con_123")
        """
        return self.update(contact_id, {"subscribed": True, "status": "active"})

    def unsubscribe(self, contact_id: str) -> Response[object]:
        """Mark a contact as unsubscribed.

        Parameters
        ----------
        contact_id:
            Contact UUID.

        Returns
        -------
        Response[object]
            Updated contact payload.

        Raises
        ------
        NotFoundError
            When the contact does not exist.
        ApiError
            On API or transport failures.

        Examples
        --------
        >>> client.contacts.unsubscribe("con_123")
        """
        return self.update(contact_id, {"subscribed": False, "status": "unsubscribed"})

    def _find_by_email(self, email: str) -> object | None:
        matches = self.list(search=email, per_page=25)
        target = email.lower()
        for contact in matches:
            if isinstance(contact, Mapping):
                value = contact.get("email")
                if isinstance(value, str) and value.lower() == target:
                    return contact
        return None


def _identifier(contact: object) -> str:
    if isinstance(contact, Mapping):
        for key in ("id", "uuid"):
            value = contact.get(key)
            if value is not None:
                return str(value)
    raise ValidationError("Contact payload does not contain an id.")


def _merge(payload: Mapping[str, Any] | None, kwargs: Mapping[str, Any]) -> dict[str, Any]:
    merged: dict[str, Any] = dict(payload or {})
    merged.update({key: value for key, value in kwargs.items() if value is not None})
    return merged


def _query(options: Mapping[str, Any]) -> dict[str, Any]:
    return {key: value for key, value in options.items() if value is not None}
