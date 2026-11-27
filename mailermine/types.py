"""JSON-compatible value aliases used across the public SDK surface."""

from __future__ import annotations

from collections.abc import Mapping, Sequence
from typing import Any, TypedDict

JsonPrimitive = str | int | float | bool | None
JsonValue = JsonPrimitive | Mapping[str, "JsonValue"] | Sequence["JsonValue"]
JsonObject = dict[str, JsonValue]


class WebhookClick(TypedDict):
    """``click`` block on ``email.clicked`` webhook payloads."""

    url: str | None
    link_id: str | None
    is_unique: bool | None
    clicked_at: str | None


class WebhookOpen(TypedDict):
    """``open`` block on ``email.opened`` webhook payloads."""

    is_unique: bool | None
    opened_at: str | None


class WebhookEventPayload(TypedDict, total=False):
    """Body of a MailerMine webhook delivery (verify the signature first).

    ``click`` is present on ``email.clicked`` and ``open`` on ``email.opened``.
    """

    id: str
    type: str
    created_at: str
    project: dict[str, str]
    email: dict[str, Any]
    click: WebhookClick
    open: WebhookOpen
