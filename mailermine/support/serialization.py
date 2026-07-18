"""Serialize between plain Python values and generated OpenAPI payloads."""

from __future__ import annotations

from collections.abc import Mapping, Sequence
from typing import TypeVar, cast

from mailermine.support import Collection, Pagination, Response
from mailermine.types import JsonObject, JsonValue

T = TypeVar("T")

_NESTED_PASSTHROUGH_KEYS = frozenset({"metadata", "variables", "headers"})


def to_generated_request(value: Mapping[str, object] | None) -> dict[str, object]:
    """Convert a public request mapping into wire-format snake_case keys.

    Nested maps such as ``metadata``, ``variables``, and ``headers`` keep their
    developer-defined keys unchanged. Attachment objects are shallow-snake-cased.

    Parameters
    ----------
    value:
        Public request mapping (may use camelCase or snake_case keys).

    Returns
    -------
    dict[str, object]
        Payload suitable for the generated client.
    """
    if value is None:
        return {}
    result: dict[str, object] = {}
    for key, item in value.items():
        if item is None:
            continue
        snake_key = _to_snake_case(str(key))
        if (
            snake_key == "attachments"
            and isinstance(item, Sequence)
            and not isinstance(item, (str, bytes, bytearray))
        ):
            result[snake_key] = [
                _shallow_snake_case(attachment) if isinstance(attachment, Mapping) else attachment
                for attachment in item
            ]
        elif snake_key in _NESTED_PASSTHROUGH_KEYS and isinstance(item, Mapping):
            result[snake_key] = dict(item)
        else:
            result[snake_key] = item
    return result


def to_plain(value: object) -> object:
    """Convert generated models into plain JSON-compatible Python values.

    Parameters
    ----------
    value:
        Generated model, mapping, sequence, or primitive.

    Returns
    -------
    object
        Plain Python value with snake_case object keys.
    """
    if value is None or isinstance(value, (str, int, float, bool)):
        return value
    if hasattr(value, "to_dict") and callable(value.to_dict):
        return to_plain(value.to_dict())
    if isinstance(value, Mapping):
        return {str(key): to_plain(item) for key, item in value.items()}
    if isinstance(value, Sequence) and not isinstance(value, (str, bytes, bytearray)):
        return [to_plain(item) for item in value]
    return value


def to_response(value: object) -> Response[object]:
    """Wrap a generated response envelope in :class:`Response`.

    Parameters
    ----------
    value:
        Raw generated response (model or mapping).

    Returns
    -------
    Response[object]
        Public response envelope.
    """
    envelope = _as_mapping(to_plain(value))
    data = envelope.get("data", envelope)
    message = envelope.get("message", "")
    success = envelope.get("success", True)
    meta = envelope.get("meta")
    return Response(
        data,
        message=str(message) if message is not None else "",
        success=bool(success) if success is not None else True,
        meta=cast(Mapping[str, JsonValue], meta) if isinstance(meta, Mapping) else None,
    )


def to_collection(value: object) -> Collection[object]:
    """Wrap a generated list envelope in :class:`Collection`.

    Parameters
    ----------
    value:
        Raw generated list response.

    Returns
    -------
    Collection[object]
        Public collection with pagination.
    """
    envelope = _as_mapping(to_plain(value))
    raw_data = envelope.get("data", [])
    items: list[object]
    if isinstance(raw_data, Sequence) and not isinstance(raw_data, (str, bytes, bytearray)):
        items = list(raw_data)
    elif raw_data is None:
        items = []
    else:
        items = [raw_data]

    meta = _as_mapping(envelope.get("meta"))
    pagination = Pagination(
        current_page=_as_int(meta.get("current_page", meta.get("currentPage")), 1),
        per_page=_as_int(meta.get("per_page", meta.get("perPage")), len(items) or 1),
        total=_as_int(meta.get("total"), len(items)),
        last_page=_as_int(meta.get("last_page", meta.get("lastPage")), 1),
    )
    message = envelope.get("message", "")
    success = envelope.get("success", True)
    return Collection(
        items,
        pagination,
        message=str(message) if message is not None else "",
        success=bool(success) if success is not None else True,
        meta=cast(Mapping[str, JsonValue], meta) if meta else None,
    )


def deleted_response(message: str = "", success: bool = True) -> Response[JsonObject]:
    """Build the standard delete acknowledgement payload."""
    return Response({"deleted": True}, message=message, success=success)


def data_id(response: Response[object], *keys: str) -> str:
    """Extract an identifier from a response ``data`` payload."""
    payload = response.data
    if isinstance(payload, Mapping):
        for key in keys or ("id", "uuid"):
            value = payload.get(key)
            if value is not None:
                return str(value)
    raise ValueError("Response data does not contain an id.")


def _shallow_snake_case(value: Mapping[str, object]) -> dict[str, object]:
    return {_to_snake_case(str(key)): item for key, item in value.items() if item is not None}


def _to_snake_case(value: str) -> str:
    chars: list[str] = []
    for index, char in enumerate(value):
        if char in {" ", "-"}:
            chars.append("_")
            continue
        if (
            char.isupper()
            and index > 0
            and (value[index - 1].islower() or value[index - 1].isdigit())
        ):
            chars.append("_")
            chars.append(char.lower())
        else:
            chars.append(char.lower())
    return "".join(chars)


def _as_mapping(value: object) -> dict[str, object]:
    if isinstance(value, Mapping):
        return {str(key): item for key, item in value.items()}
    return {}


def _as_int(value: object, default: int) -> int:
    if isinstance(value, bool):
        return default
    if isinstance(value, int):
        return value
    if isinstance(value, float):
        return int(value)
    if isinstance(value, str):
        try:
            return int(value)
        except ValueError:
            return default
    return default
