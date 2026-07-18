"""Response, Collection, and Pagination value objects."""

from __future__ import annotations

from collections.abc import Iterator, Mapping, Sequence
from typing import Generic, TypeVar, overload

from mailermine.types import JsonValue

T = TypeVar("T")


class Pagination:
    """Pagination metadata for a list response page.

    Parameters
    ----------
    current_page:
        Current page number (1-based).
    per_page:
        Page size.
    total:
        Total number of matching items.
    last_page:
        Last available page number.
    """

    __slots__ = ("current_page", "last_page", "per_page", "total")

    def __init__(
        self,
        *,
        current_page: int,
        per_page: int,
        total: int,
        last_page: int,
    ) -> None:
        self.current_page = current_page
        self.per_page = per_page
        self.total = total
        self.last_page = last_page

    @property
    def has_next_page(self) -> bool:
        """Whether another page is available after the current page."""
        return self.current_page < self.last_page

    @property
    def has_previous_page(self) -> bool:
        """Whether a previous page is available before the current page."""
        return self.current_page > 1

    def to_dict(self) -> dict[str, int | bool]:
        """Serialize pagination metadata to a plain dictionary."""
        return {
            "current_page": self.current_page,
            "per_page": self.per_page,
            "total": self.total,
            "last_page": self.last_page,
            "has_next_page": self.has_next_page,
            "has_previous_page": self.has_previous_page,
        }


class Response(Generic[T]):
    """Successful single-object API response envelope.

    Parameters
    ----------
    data:
        Primary payload.
    message:
        Human-readable API message.
    success:
        API success flag.
    meta:
        Optional metadata dictionary.
    """

    __slots__ = ("data", "message", "meta", "success")

    def __init__(
        self,
        data: T,
        message: str = "",
        success: bool = True,
        meta: Mapping[str, JsonValue] | None = None,
    ) -> None:
        self.data = data
        self.message = message
        self.success = success
        self.meta: dict[str, JsonValue] = dict(meta or {})

    def to_dict(self) -> dict[str, JsonValue]:
        """Serialize the response envelope to a plain dictionary."""
        return {
            "success": self.success,
            "message": self.message,
            "data": _as_json_value(self.data),
            "meta": self.meta,
        }


class Collection(Response[list[T]], Generic[T]):
    """Successful list response with pagination metadata.

    Parameters
    ----------
    items:
        Items on the current page.
    pagination:
        Pagination metadata for the page.
    message:
        Human-readable API message.
    success:
        API success flag.
    meta:
        Optional raw metadata dictionary.
    """

    __slots__ = ("items", "pagination")

    def __init__(
        self,
        items: Sequence[T],
        pagination: Pagination,
        message: str = "",
        success: bool = True,
        meta: Mapping[str, JsonValue] | None = None,
    ) -> None:
        materialised = list(items)
        super().__init__(materialised, message=message, success=success, meta=meta)
        self.items = materialised
        self.pagination = pagination

    def __len__(self) -> int:
        return len(self.items)

    def __iter__(self) -> Iterator[T]:
        return iter(self.items)

    @overload
    def __getitem__(self, index: int) -> T: ...

    @overload
    def __getitem__(self, index: slice) -> list[T]: ...

    def __getitem__(self, index: int | slice) -> T | list[T]:
        return self.items[index]

    def first(self) -> T | None:
        """Return the first item, or ``None`` when empty."""
        return self.items[0] if self.items else None

    def is_empty(self) -> bool:
        """Return whether the collection has no items."""
        return not self.items

    def to_dict(self) -> dict[str, JsonValue]:
        """Serialize the collection envelope to a plain dictionary."""
        return {
            "success": self.success,
            "message": self.message,
            "data": [_as_json_value(item) for item in self.items],
            "meta": self.meta or self.pagination.to_dict(),
            "items": [_as_json_value(item) for item in self.items],
            "pagination": self.pagination.to_dict(),
        }


def _as_json_value(value: object) -> JsonValue:
    if value is None or isinstance(value, (str, int, float, bool)):
        return value
    if isinstance(value, Mapping):
        return {str(key): _as_json_value(item) for key, item in value.items()}
    if isinstance(value, Sequence) and not isinstance(value, (str, bytes, bytearray)):
        return [_as_json_value(item) for item in value]
    if hasattr(value, "to_dict") and callable(value.to_dict):
        return _as_json_value(value.to_dict())
    return str(value)


__all__ = ["Collection", "Pagination", "Response"]
