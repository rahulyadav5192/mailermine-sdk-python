"""Resource package — public API resource wrappers."""

from __future__ import annotations

from mailermine.resources.analytics import Analytics
from mailermine.resources.api_keys import ApiKeys
from mailermine.resources.audiences import Audiences
from mailermine.resources.campaigns import Campaigns
from mailermine.resources.contacts import Contacts
from mailermine.resources.domains import Domains
from mailermine.resources.emails import Emails
from mailermine.resources.events import Events
from mailermine.resources.exports import Exports
from mailermine.resources.imports import Imports
from mailermine.resources.lists import Lists
from mailermine.resources.messages import Messages
from mailermine.resources.projects import Projects
from mailermine.resources.segments import Segments
from mailermine.resources.suppressions import Suppressions
from mailermine.resources.tags import Tags
from mailermine.resources.templates import Templates
from mailermine.resources.webhooks import Webhooks

__all__ = [
    "Analytics",
    "ApiKeys",
    "Audiences",
    "Campaigns",
    "Contacts",
    "Domains",
    "Emails",
    "Events",
    "Exports",
    "Imports",
    "Lists",
    "Messages",
    "Projects",
    "Segments",
    "Suppressions",
    "Tags",
    "Templates",
    "Webhooks",
]
