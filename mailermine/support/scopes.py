"""API key scopes.

A ``.write`` scope also grants the matching ``.read`` scope; ``admin`` grants
everything; a key created without scopes has full access.

Examples
--------
>>> client.api_keys.create(project_id, name="Mailer", scopes=list(ScopePresets.SENDING_ONLY))
"""

from __future__ import annotations


class Scopes:
    """API key scope names."""

    EMAILS_SEND = "emails.send"
    EMAILS_READ = "emails.read"
    TEMPLATES_READ = "templates.read"
    TEMPLATES_WRITE = "templates.write"
    DOMAINS_READ = "domains.read"
    DOMAINS_WRITE = "domains.write"
    CONTACTS_READ = "contacts.read"
    CONTACTS_WRITE = "contacts.write"
    CAMPAIGNS_READ = "campaigns.read"
    CAMPAIGNS_WRITE = "campaigns.write"
    ANALYTICS_READ = "analytics.read"
    BILLING_READ = "billing.read"
    PROJECTS_READ = "projects.read"
    PROJECTS_WRITE = "projects.write"
    API_KEYS_READ = "api_keys.read"
    API_KEYS_WRITE = "api_keys.write"
    WEBHOOKS_READ = "webhooks.read"
    WEBHOOKS_WRITE = "webhooks.write"
    SUPPRESSIONS_READ = "suppressions.read"
    SUPPRESSIONS_WRITE = "suppressions.write"
    EVENTS_READ = "events.read"
    ADMIN = "admin"

    @classmethod
    def all(cls) -> list[str]:
        """Every scope name."""
        return [v for k, v in vars(cls).items() if k.isupper() and isinstance(v, str)]


class ScopePresets:
    """Ready-made scope bundles."""

    SENDING_ONLY: tuple[str, ...] = (Scopes.EMAILS_SEND,)
    SENDING_AND_LOGS: tuple[str, ...] = (
        Scopes.EMAILS_SEND,
        Scopes.EMAILS_READ,
        Scopes.EVENTS_READ,
        Scopes.ANALYTICS_READ,
    )
    MARKETING: tuple[str, ...] = (
        Scopes.CONTACTS_READ,
        Scopes.CONTACTS_WRITE,
        Scopes.CAMPAIGNS_READ,
        Scopes.CAMPAIGNS_WRITE,
        Scopes.TEMPLATES_READ,
        Scopes.ANALYTICS_READ,
    )
