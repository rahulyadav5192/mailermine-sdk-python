"""Internal factory that builds generated OpenAPI API clients.

This module is private. Application code must never import it.
"""

from __future__ import annotations

from dataclasses import dataclass

from mailermine_generated import (
    AnalyticsApi,
    ApiClient,
    APIKeysApi,
    AudiencesApi,
    CampaignAnalyticsApi,
    CampaignEventsApi,
    CampaignLifecycleApi,
    CampaignsApi,
    ContactsApi,
    DomainsApi,
    EmailsApi,
    EventsApi,
    ExportsApi,
    ImportsApi,
    ListsApi,
    MessagesApi,
    ProjectsApi,
    SegmentsApi,
    SuppressionsApi,
    TagsApi,
    TemplatesApi,
    WebhooksApi,
)
from mailermine_generated import (
    Configuration as GeneratedConfiguration,
)

from mailermine._internal.transport import ResilientApiClient
from mailermine.config import Configuration


@dataclass(frozen=True, slots=True)
class GeneratedApis:
    """Bundle of generated API clients sharing one ``ApiClient``."""

    api_client: ApiClient
    emails: EmailsApi
    messages: MessagesApi
    projects: ProjectsApi
    api_keys: APIKeysApi
    domains: DomainsApi
    templates: TemplatesApi
    contacts: ContactsApi
    lists: ListsApi
    segments: SegmentsApi
    tags: TagsApi
    audiences: AudiencesApi
    campaigns: CampaignsApi
    campaign_lifecycle: CampaignLifecycleApi
    campaign_analytics: CampaignAnalyticsApi
    campaign_events: CampaignEventsApi
    analytics: AnalyticsApi
    events: EventsApi
    webhooks: WebhooksApi
    suppressions: SuppressionsApi
    imports: ImportsApi
    exports: ExportsApi


def create_generated_apis(configuration: Configuration) -> GeneratedApis:
    """Create the generated transport layer from public configuration.

    Parameters
    ----------
    configuration:
        Validated SDK configuration.

    Returns
    -------
    GeneratedApis
        Shared generated client bundle.
    """
    generated = GeneratedConfiguration(host=configuration.base_url)
    generated.access_token = configuration.api_key

    api_client = ResilientApiClient(
        configuration=generated,
        max_retries=configuration.max_retries,
        max_retry_delay=configuration.max_retry_delay,
    )
    api_client.user_agent = configuration.user_agent

    return GeneratedApis(
        api_client=api_client,
        emails=EmailsApi(api_client),
        messages=MessagesApi(api_client),
        projects=ProjectsApi(api_client),
        api_keys=APIKeysApi(api_client),
        domains=DomainsApi(api_client),
        templates=TemplatesApi(api_client),
        contacts=ContactsApi(api_client),
        lists=ListsApi(api_client),
        segments=SegmentsApi(api_client),
        tags=TagsApi(api_client),
        audiences=AudiencesApi(api_client),
        campaigns=CampaignsApi(api_client),
        campaign_lifecycle=CampaignLifecycleApi(api_client),
        campaign_analytics=CampaignAnalyticsApi(api_client),
        campaign_events=CampaignEventsApi(api_client),
        analytics=AnalyticsApi(api_client),
        events=EventsApi(api_client),
        webhooks=WebhooksApi(api_client),
        suppressions=SuppressionsApi(api_client),
        imports=ImportsApi(api_client),
        exports=ExportsApi(api_client),
    )
