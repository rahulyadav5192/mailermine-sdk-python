"""Parity smoke tests — every resource and public method exists (no live API)."""

from __future__ import annotations

import inspect
import re

import pytest
from mailermine import MailerMine
from mailermine.resources import (
    Analytics,
    ApiKeys,
    Audiences,
    Campaigns,
    Contacts,
    Domains,
    Emails,
    Events,
    Exports,
    Imports,
    Lists,
    Messages,
    Projects,
    Segments,
    Suppressions,
    Tags,
    Templates,
    Webhooks,
)

# Authoritative Node SDK public surface (camelCase), converted to snake_case in tests.
NODE_PUBLIC_API: dict[str, tuple[str, ...]] = {
    "emails": ("send", "list", "get", "events"),
    "projects": ("create", "list", "get", "update", "delete"),
    "api_keys": ("create", "list", "get", "update", "delete", "rotate", "reveal"),
    "domains": ("create", "list", "get", "verify", "dnsRecords", "status", "delete"),
    "templates": (
        "create",
        "list",
        "get",
        "update",
        "preview",
        "duplicate",
        "test",
        "delete",
    ),
    "contacts": (
        "create",
        "upsert",
        "list",
        "get",
        "update",
        "delete",
        "search",
        "identify",
        "subscribe",
        "unsubscribe",
    ),
    "lists": ("create", "list", "get", "update", "delete", "addContact", "removeContact"),
    "segments": ("create", "list", "get", "update", "delete", "preview"),
    "tags": ("create", "list", "get", "update", "delete", "assign", "remove"),
    "audiences": (
        "create",
        "list",
        "get",
        "update",
        "delete",
        "contacts",
        "addContacts",
        "removeContacts",
    ),
    "campaigns": (
        "create",
        "list",
        "get",
        "update",
        "delete",
        "duplicate",
        "archive",
        "restore",
        "setSubject",
        "setSender",
        "setReplyTo",
        "setPreheader",
        "setTemplate",
        "recipientCount",
        "previewRecipients",
        "validate",
        "markReady",
        "send",
        "schedule",
        "reschedule",
        "unschedule",
        "sendNow",
        "cancelSchedule",
        "pause",
        "resume",
        "cancel",
        "preview",
        "render",
        "status",
        "progress",
        "analytics",
        "opens",
        "clicks",
        "bounces",
        "complaints",
        "unsubscribes",
        "deliveries",
        "delivery",
        "links",
        "events",
        "activity",
        "timeline",
        "recipients",
        "addSegment",
        "addAudience",
        "removeAudience",
        "removeSegment",
    ),
    "analytics": (
        "overview",
        "deliveries",
        "opens",
        "clicks",
        "bounces",
        "complaints",
        "unsubscribes",
        "usage",
        "activity",
        "messages",
        "engagement",
        "campaigns",
        "domains",
        "projects",
        "providers",
    ),
    "events": ("list", "get", "timeline", "history", "message"),
    "messages": ("list", "get", "search", "filter", "events", "timeline"),
    "webhooks": (
        "create",
        "list",
        "get",
        "update",
        "delete",
        "test",
        "rotateSecret",
        "enable",
        "disable",
        "deliveries",
        "delivery",
        "logs",
        "failures",
        "replay",
        "retry",
        "verify",
        "verifyHeaders",
    ),
    "suppressions": ("list", "get", "add", "remove", "restore", "check"),
    "imports": ("list", "create", "status", "configure", "start", "cancel"),
    "exports": ("create", "status", "download"),
}

RESOURCE_CLASSES: dict[str, type] = {
    "emails": Emails,
    "projects": Projects,
    "api_keys": ApiKeys,
    "domains": Domains,
    "templates": Templates,
    "contacts": Contacts,
    "lists": Lists,
    "segments": Segments,
    "tags": Tags,
    "audiences": Audiences,
    "campaigns": Campaigns,
    "analytics": Analytics,
    "events": Events,
    "messages": Messages,
    "webhooks": Webhooks,
    "suppressions": Suppressions,
    "imports": Imports,
    "exports": Exports,
}


def _camel_to_snake(name: str) -> str:
    return re.sub(r"(?<!^)(?=[A-Z])", "_", name).lower()


def _public_methods(cls: type) -> set[str]:
    names: set[str] = set()
    for name, obj in cls.__dict__.items():
        if name.startswith("_") or name == "execute":
            continue
        if inspect.isfunction(obj) or isinstance(obj, (staticmethod, classmethod)):
            names.add(name)
    return names


@pytest.mark.parametrize("resource_name", sorted(NODE_PUBLIC_API))
def test_resource_exists_on_client(resource_name: str) -> None:
    client = MailerMine(api_key="relay_parity_test")
    resource = getattr(client, resource_name)
    assert resource is not None
    assert isinstance(resource, RESOURCE_CLASSES[resource_name])


@pytest.mark.parametrize("resource_name", sorted(NODE_PUBLIC_API))
def test_resource_methods_match_node(resource_name: str) -> None:
    expected = {_camel_to_snake(name) for name in NODE_PUBLIC_API[resource_name]}
    actual = _public_methods(RESOURCE_CLASSES[resource_name])
    missing = sorted(expected - actual)
    unexpected = sorted(actual - expected)
    assert missing == [], f"{resource_name} missing methods: {missing}"
    assert unexpected == [], f"{resource_name} unexpected methods: {unexpected}"


def test_total_parity_counts() -> None:
    expected_total = sum(len(methods) for methods in NODE_PUBLIC_API.values())
    actual_total = sum(len(_public_methods(cls)) for cls in RESOURCE_CLASSES.values())
    assert len(NODE_PUBLIC_API) == 18
    assert len(RESOURCE_CLASSES) == 18
    assert expected_total == 174
    assert actual_total == expected_total


@pytest.mark.parametrize("resource_name", sorted(NODE_PUBLIC_API))
def test_public_methods_have_docstrings_and_annotations(resource_name: str) -> None:
    cls = RESOURCE_CLASSES[resource_name]
    for method_name in _public_methods(cls):
        method = getattr(cls, method_name)
        func = method.__func__ if isinstance(method, staticmethod) else method
        assert func.__doc__, f"{resource_name}.{method_name} missing docstring"
        hints = getattr(func, "__annotations__", {})
        assert "return" in hints, f"{resource_name}.{method_name} missing return annotation"


def test_client_property_annotations_for_autocomplete() -> None:
    # Properties may not all live in __annotations__; check annotated property return types.
    for resource_name, cls in RESOURCE_CLASSES.items():
        prop = MailerMine.__dict__[resource_name]
        assert isinstance(prop, property)
        assert prop.fget is not None
        return_hint = prop.fget.__annotations__.get("return")
        assert return_hint is cls or return_hint == cls.__name__
