"""JSON-compatible value aliases used across the public SDK surface."""

from __future__ import annotations

from collections.abc import Mapping, Sequence

JsonPrimitive = str | int | float | bool | None
JsonValue = JsonPrimitive | Mapping[str, "JsonValue"] | Sequence["JsonValue"]
JsonObject = dict[str, JsonValue]
