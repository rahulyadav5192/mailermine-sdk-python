"""Root MailerMine client."""

from __future__ import annotations

from collections.abc import Mapping

from mailermine._internal.apis import GeneratedApis, create_generated_apis
from mailermine.config import Configuration
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


class MailerMine:
    """Official MailerMine Python SDK client.

    Parameters
    ----------
    api_key:
        Bearer API key, or omit to use ``MAILERMINE_API_KEY``.
    base_url:
        Optional API base URL override.
    timeout:
        Optional request timeout in seconds.
    user_agent:
        Optional User-Agent override.
    configuration:
        Optional pre-built :class:`~mailermine.config.Configuration`.

    Examples
    --------
    >>> from mailermine import MailerMine
    >>> client = MailerMine(api_key="relay_live_xxx")
    >>> client.emails.send(
    ...     from_="hello@example.com",
    ...     to="user@example.com",
    ...     subject="Hi",
    ...     html="<p>Hi</p>",
    ... )
    """

    def __init__(
        self,
        api_key: str | Configuration | Mapping[str, object] | None = None,
        *,
        base_url: str | None = None,
        timeout: float | None = None,
        user_agent: str | None = None,
        configuration: Configuration | None = None,
    ) -> None:
        if configuration is not None:
            self._configuration = configuration
        elif isinstance(api_key, Configuration):
            self._configuration = api_key
        elif isinstance(api_key, Mapping):
            self._configuration = Configuration.from_mapping(api_key)
        elif isinstance(api_key, str) or api_key is None:
            self._configuration = Configuration.create(
                api_key=api_key,
                base_url=base_url,
                timeout=timeout,
                user_agent=user_agent,
            )
        else:
            raise TypeError(
                "MailerMine expects an api_key string, Configuration, mapping, or keyword options."
            )

        self._apis: GeneratedApis = create_generated_apis(self._configuration)

        self._emails: Emails | None = None
        self._projects: Projects | None = None
        self._api_keys: ApiKeys | None = None
        self._domains: Domains | None = None
        self._templates: Templates | None = None
        self._contacts: Contacts | None = None
        self._lists: Lists | None = None
        self._segments: Segments | None = None
        self._tags: Tags | None = None
        self._audiences: Audiences | None = None
        self._campaigns: Campaigns | None = None
        self._analytics: Analytics | None = None
        self._events: Events | None = None
        self._messages: Messages | None = None
        self._webhooks: Webhooks | None = None
        self._suppressions: Suppressions | None = None
        self._imports: Imports | None = None
        self._exports: Exports | None = None

    @property
    def configuration(self) -> Configuration:
        """Resolved SDK configuration."""
        return self._configuration

    @property
    def emails(self) -> Emails:
        """Transactional email operations."""
        if self._emails is None:
            self._emails = Emails(
                self._apis.emails,
                self._apis.messages,
                timeout=self._configuration.timeout,
            )
        return self._emails

    @property
    def projects(self) -> Projects:
        """Workspace project operations."""
        if self._projects is None:
            self._projects = Projects(
                self._apis.projects,
                timeout=self._configuration.timeout,
            )
        return self._projects

    @property
    def api_keys(self) -> ApiKeys:
        """Project API key operations."""
        if self._api_keys is None:
            self._api_keys = ApiKeys(
                self._apis.api_keys,
                timeout=self._configuration.timeout,
            )
        return self._api_keys

    @property
    def domains(self) -> Domains:
        """Sending domain operations."""
        if self._domains is None:
            self._domains = Domains(
                self._apis.domains,
                timeout=self._configuration.timeout,
            )
        return self._domains

    @property
    def templates(self) -> Templates:
        """Email template operations."""
        if self._templates is None:
            self._templates = Templates(
                self._apis.templates,
                timeout=self._configuration.timeout,
            )
        return self._templates

    @property
    def contacts(self) -> Contacts:
        """Contact operations."""
        if self._contacts is None:
            self._contacts = Contacts(
                self._apis.contacts,
                timeout=self._configuration.timeout,
            )
        return self._contacts

    @property
    def lists(self) -> Lists:
        """Static mailing list operations."""
        if self._lists is None:
            self._lists = Lists(
                self._apis.lists,
                timeout=self._configuration.timeout,
            )
        return self._lists

    @property
    def segments(self) -> Segments:
        """Dynamic segment operations."""
        if self._segments is None:
            self._segments = Segments(
                self._apis.segments,
                timeout=self._configuration.timeout,
            )
        return self._segments

    @property
    def tags(self) -> Tags:
        """Contact tag operations."""
        if self._tags is None:
            self._tags = Tags(
                self._apis.tags,
                timeout=self._configuration.timeout,
            )
        return self._tags

    @property
    def audiences(self) -> Audiences:
        """Unified audience catalog (lists and segments)."""
        if self._audiences is None:
            self._audiences = Audiences(
                self._apis.audiences,
                self.lists,
                self.segments,
                self.contacts,
                timeout=self._configuration.timeout,
            )
        return self._audiences

    @property
    def campaigns(self) -> Campaigns:
        """Marketing campaign operations."""
        if self._campaigns is None:
            self._campaigns = Campaigns(
                self._apis.campaigns,
                self._apis.campaign_lifecycle,
                self._apis.campaign_analytics,
                self._apis.campaign_events,
                timeout=self._configuration.timeout,
            )
        return self._campaigns

    @property
    def analytics(self) -> Analytics:
        """Account-wide delivery and engagement analytics."""
        if self._analytics is None:
            self._analytics = Analytics(
                self._apis.analytics,
                self.campaigns,
                self.events,
                timeout=self._configuration.timeout,
            )
        return self._analytics

    @property
    def events(self) -> Events:
        """Global message and delivery lifecycle events."""
        if self._events is None:
            self._events = Events(
                self._apis.events,
                self._apis.messages,
                timeout=self._configuration.timeout,
            )
        return self._events

    @property
    def messages(self) -> Messages:
        """Delivery logs and outbound message history."""
        if self._messages is None:
            self._messages = Messages(
                self._apis.messages,
                timeout=self._configuration.timeout,
            )
        return self._messages

    @property
    def webhooks(self) -> Webhooks:
        """Webhook endpoint and delivery operations."""
        if self._webhooks is None:
            self._webhooks = Webhooks(
                self._apis.webhooks,
                timeout=self._configuration.timeout,
            )
        return self._webhooks

    @property
    def suppressions(self) -> Suppressions:
        """Account suppression-list operations."""
        if self._suppressions is None:
            self._suppressions = Suppressions(
                self._apis.suppressions,
                timeout=self._configuration.timeout,
            )
        return self._suppressions

    @property
    def imports(self) -> Imports:
        """Contact import job operations."""
        if self._imports is None:
            self._imports = Imports(
                self._apis.imports,
                timeout=self._configuration.timeout,
            )
        return self._imports

    @property
    def exports(self) -> Exports:
        """Contact export job operations."""
        if self._exports is None:
            self._exports = Exports(
                self._apis.exports,
                timeout=self._configuration.timeout,
            )
        return self._exports
