"""Official MailerMine SDK for Python.

Install from PyPI with ``pip install mailermine``, then:

.. code-block:: python

    from mailermine import MailerMine

    client = MailerMine(api_key="relay_live_xxx")
    client.emails.send(
        from_="hello@example.com",
        to="user@example.com",
        subject="Welcome",
        html="<p>Hello</p>",
    )

Application code must never import ``mailermine_generated``.
"""

from __future__ import annotations

from mailermine.client import MailerMine
from mailermine.config import Configuration
from mailermine.constants import (
    DEFAULT_BASE_URL,
    DEFAULT_MAX_RETRIES,
    DEFAULT_MAX_RETRY_DELAY,
    DEFAULT_TIMEOUT,
    DEFAULT_USER_AGENT,
    VERSION,
)
from mailermine.exceptions import (
    ApiError,
    AuthenticationError,
    MailerMineError,
    MissingScopeError,
    NotFoundError,
    PlanError,
    RateLimitError,
    ValidationError,
)
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
from mailermine.support import Collection, Pagination, Response
from mailermine.support.rate_limit import RateLimitInfo
from mailermine.support.scopes import ScopePresets, Scopes
from mailermine.types import JsonObject, JsonPrimitive, JsonValue

__all__ = [
    "DEFAULT_BASE_URL",
    "DEFAULT_MAX_RETRIES",
    "DEFAULT_MAX_RETRY_DELAY",
    "DEFAULT_TIMEOUT",
    "DEFAULT_USER_AGENT",
    "VERSION",
    "Analytics",
    "ApiError",
    "ApiKeys",
    "Audiences",
    "AuthenticationError",
    "Campaigns",
    "Collection",
    "Configuration",
    "Contacts",
    "Domains",
    "Emails",
    "Events",
    "Exports",
    "Imports",
    "JsonObject",
    "JsonPrimitive",
    "JsonValue",
    "Lists",
    "MailerMine",
    "MailerMineError",
    "Messages",
    "MissingScopeError",
    "NotFoundError",
    "Pagination",
    "PlanError",
    "Projects",
    "RateLimitError",
    "RateLimitInfo",
    "Response",
    "ScopePresets",
    "Scopes",
    "Segments",
    "Suppressions",
    "Tags",
    "Templates",
    "ValidationError",
    "Webhooks",
]
