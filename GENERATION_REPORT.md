# MailerMine Python SDK — Generation Report

**Phase:** 2 — Generated OpenAPI client only  
**Generated at:** script runtime (elapsed 6.67s)  
**Source of truth:** https://www.mailermine.com/openapi.json

---

## Generator

| Item | Value |
| --- | --- |
| OpenAPI Generator | `7.23.0` |
| Generator name | `python` |
| JAR SHA-256 | `cb087e40001e31eb08ef6140dd5de10938dbeb89016a1fe0481eaa25cd569026` |
| Spec OpenAPI version | `3.1.0` |
| Spec `info.version` | `1.0.0` |
| Paths in spec | 97 |
| Schemas in spec | 154 |
| Package name | `mailermine_generated` |
| Output | `generated/mailermine_generated` |

## Library selection

Evaluated options supported by the stable `python` generator in **7.23.0**:

| Library | Sync | Async | Notes |
| --- | --- | --- | --- |
| `urllib3` | Yes | No | Default; production-proven; ideal for sync-first public APIs. |
| `requests` | Yes (legacy) | No | Not offered by modern `python` generator (legacy generators only). |
| `httpx` | **No in 7.23.0** | Yes | Async-only on this release. `supportHttpxSync` appears in upstream docs/PRs but is **not** exposed by `config-help` for 7.23.0 (verified). |
| `asyncio` (aiohttp) | No | Yes | Async-only; weaker sync DX for v1 wrapper. |

**Selected: `urllib3`.**

Rationale: the official SDK public surface is sync-first (parity with Laravel and Node). On OpenAPI Generator 7.23.0, `httpx` cannot provide sync methods, so choosing it would force every wrapper call through `asyncio.run` — poor DX and awkward nesting. `urllib3` keeps dependencies small (`urllib3`, `pydantic`, `python-dateutil`, typing helpers) and matches the architecture plan. When a stable generator release ships dual sync/async `httpx` (`supportHttpxSync`), revisit regeneration to unlock `AsyncMailerMine` without a second client.

## Generator options

```text
packageName=mailermine_generated
projectName=mailermine-generated
packageVersion=1.0.0
library=urllib3
generateSourceCodeOnly=false
hideGenerationTimestamp=true
disallowAdditionalPropertiesIfNotPresent=false
```

## Resource coverage

| Resource | Status |
| --- | --- |
| Projects | present |
| Api Keys | present |
| Emails | present |
| Domains | present |
| Templates | present |
| Contacts | present |
| Lists | present |
| Segments | present |
| Tags | present |
| Audiences | present |
| Campaigns | present |
| Analytics | present |
| Events | present |
| Messages | present |
| Webhooks | present |
| Suppressions | present |
| Imports | present |
| Exports | present |

All required MailerMine resources are present in the generated client.

## Generated API classes

- `AnalyticsApi`
- `APIKeysApi`
- `AudiencesApi`
- `CampaignAnalyticsApi`
- `CampaignEventsApi`
- `CampaignLifecycleApi`
- `CampaignsApi`
- `ContactsApi`
- `DomainsApi`
- `EmailsApi`
- `EventsApi`
- `ExportsApi`
- `ImportsApi`
- `ListsApi`
- `MarketingApi`
- `MessagesApi`
- `ProjectsApi`
- `SegmentsApi`
- `SuppressionsApi`
- `TagsApi`
- `TemplatesApi`
- `WebhooksApi`

**Total API classes:** 22

## Generated models

**Total model modules:** 200
**OpenAPI component schemas:** 154

No duplicate model module filenames detected.

Every component schema maps to a generated model module (name-normalized).

## Endpoint inventory

**Total endpoints:** 133

| API class | Endpoint | HTTP method | Request model | Response model |
| --- | --- | --- | --- | --- |
| `APIKeysApi` | `/projects/{project}/api-keys` | `GET` | `—` | `ApiKeyListResponse` |
| `APIKeysApi` | `/projects/{project}/api-keys` | `POST` | `CreateApiKeyRequest` | `ApiKeyResponse` |
| `APIKeysApi` | `/projects/{project}/api-keys/{apiKey}` | `DELETE` | `—` | `DeleteResponse` |
| `APIKeysApi` | `/projects/{project}/api-keys/{apiKey}` | `GET` | `—` | `ApiKeyResponse` |
| `APIKeysApi` | `/projects/{project}/api-keys/{apiKey}` | `PATCH` | `UpdateApiKeyRequest` | `ApiKeyResponse` |
| `APIKeysApi` | `/projects/{project}/api-keys/{apiKey}/reveal` | `POST` | `—` | `(inline)` |
| `APIKeysApi` | `/projects/{project}/api-keys/{apiKey}/rotate` | `POST` | `—` | `ApiKeyResponse` |
| `AnalyticsApi` | `/analytics/campaigns` | `GET` | `—` | `AnalyticsCampaignsResponse` |
| `AnalyticsApi` | `/analytics/domains` | `GET` | `—` | `AnalyticsDomainsResponse` |
| `AnalyticsApi` | `/analytics/engagement` | `GET` | `—` | `AnalyticsEngagementResponse` |
| `AnalyticsApi` | `/analytics/messages` | `GET` | `—` | `AnalyticsMessagesResponse` |
| `AnalyticsApi` | `/analytics/overview` | `GET` | `—` | `AnalyticsOverviewResponse` |
| `AnalyticsApi` | `/analytics/projects` | `GET` | `—` | `AnalyticsProjectsResponse` |
| `AnalyticsApi` | `/analytics/providers` | `GET` | `—` | `AnalyticsProvidersResponse` |
| `AudiencesApi` | `/audiences` | `GET` | `—` | `AudienceCollection` |
| `AudiencesApi` | `/audiences/{source}/{audience}` | `GET` | `—` | `AudienceResponse` |
| `AudiencesApi` | `/audiences/{source}/{audience}/contacts` | `DELETE` | `—` | `(inline)` |
| `AudiencesApi` | `/audiences/{source}/{audience}/contacts` | `POST` | `ListContactsMembershipRequest` | `(inline)` |
| `CampaignAnalyticsApi` | `/campaigns/{campaign}/analytics` | `GET` | `—` | `CampaignAnalyticsResponse` |
| `CampaignAnalyticsApi` | `/campaigns/{campaign}/links` | `GET` | `—` | `CampaignLinksResponse` |
| `CampaignEventsApi` | `/campaigns/{campaign}/activities` | `GET` | `—` | `CampaignActivityCollection` |
| `CampaignEventsApi` | `/campaigns/{campaign}/events` | `GET` | `—` | `CampaignEventsResponse` |
| `CampaignEventsApi` | `/campaigns/{campaign}/recipients` | `GET` | `—` | `CampaignRecipientCollection` |
| `CampaignEventsApi` | `/campaigns/{campaign}/timeline` | `GET` | `—` | `CampaignTimelineResponse` |
| `CampaignLifecycleApi` | `/campaigns/{campaignUuid}/restore` | `POST` | `—` | `CampaignResponse` |
| `CampaignLifecycleApi` | `/campaigns/{campaign}/archive` | `POST` | `—` | `CampaignResponse` |
| `CampaignLifecycleApi` | `/campaigns/{campaign}/cancel` | `POST` | `—` | `CampaignResponse` |
| `CampaignLifecycleApi` | `/campaigns/{campaign}/duplicate` | `POST` | `DuplicateCampaignRequest` | `CampaignResponse` |
| `CampaignLifecycleApi` | `/campaigns/{campaign}/mark-ready` | `POST` | `—` | `CampaignResponse` |
| `CampaignLifecycleApi` | `/campaigns/{campaign}/pause` | `POST` | `—` | `CampaignResponse` |
| `CampaignLifecycleApi` | `/campaigns/{campaign}/progress` | `GET` | `—` | `CampaignStatisticsResponse` |
| `CampaignLifecycleApi` | `/campaigns/{campaign}/resume` | `POST` | `—` | `CampaignResponse` |
| `CampaignLifecycleApi` | `/campaigns/{campaign}/schedule` | `POST` | `ScheduleCampaignRequest` | `CampaignResponse` |
| `CampaignLifecycleApi` | `/campaigns/{campaign}/send` | `POST` | `—` | `CampaignResponse` |
| `CampaignsApi` | `/campaigns` | `GET` | `—` | `CampaignCollection` |
| `CampaignsApi` | `/campaigns` | `POST` | `CreateCampaignRequest` | `CampaignResponse` |
| `CampaignsApi` | `/campaigns/{campaign}` | `DELETE` | `—` | `DeleteResponse` |
| `CampaignsApi` | `/campaigns/{campaign}` | `GET` | `—` | `CampaignResponse` |
| `CampaignsApi` | `/campaigns/{campaign}` | `PATCH` | `UpdateCampaignRequest` | `CampaignResponse` |
| `CampaignsApi` | `/campaigns/{campaign}/preview` | `GET` | `—` | `CampaignPreviewResponse` |
| `CampaignsApi` | `/campaigns/{campaign}/recipient-preview` | `GET` | `—` | `CampaignRecipientPreviewResponse` |
| `CampaignsApi` | `/campaigns/{campaign}/validate` | `GET` | `—` | `CampaignValidationResponse` |
| `ContactsApi` | `/contacts` | `GET` | `—` | `ContactCollection` |
| `ContactsApi` | `/contacts` | `POST` | `CreateContactRequest` | `ContactResponse` |
| `ContactsApi` | `/contacts/bulk-delete` | `POST` | `BulkContactIdsRequest` | `(inline)` |
| `ContactsApi` | `/contacts/bulk-update` | `POST` | `BulkUpdateContactsRequest` | `(inline)` |
| `ContactsApi` | `/contacts/restore` | `POST` | `BulkContactIdsRequest` | `(inline)` |
| `ContactsApi` | `/contacts/{contact}` | `DELETE` | `—` | `DeleteResponse` |
| `ContactsApi` | `/contacts/{contact}` | `GET` | `—` | `ContactResponse` |
| `ContactsApi` | `/contacts/{contact}` | `PATCH` | `UpdateContactRequest` | `ContactResponse` |
| `ContactsApi` | `/contacts/{contact}/restore` | `POST` | `—` | `ContactResponse` |
| `DomainsApi` | `/domains` | `GET` | `—` | `DomainListResponse` |
| `DomainsApi` | `/domains` | `POST` | `CreateDomainRequest` | `DomainResponse` |
| `DomainsApi` | `/domains/{domain}` | `DELETE` | `—` | `DeleteResponse` |
| `DomainsApi` | `/domains/{domain}` | `GET` | `—` | `DomainResponse` |
| `DomainsApi` | `/domains/{domain}/verify` | `POST` | `—` | `DomainResponse` |
| `EmailsApi` | `/emails` | `POST` | `SendEmailRequest` | `SendEmailResponse` |
| `EventsApi` | `/events` | `GET` | `—` | `EventListResponse` |
| `EventsApi` | `/events/{emailEvent}` | `GET` | `—` | `EventResponse` |
| `ExportsApi` | `/contacts/export` | `POST` | `ExportContactsRequest` | `ExportJobResponse` |
| `ExportsApi` | `/contacts/exports/{contactExport}` | `GET` | `—` | `ExportJobResponse` |
| `ExportsApi` | `/contacts/exports/{contactExport}/download` | `GET` | `—` | `(inline)` |
| `ImportsApi` | `/contacts/import` | `POST` | `(inline)` | `ImportJobResponse` |
| `ImportsApi` | `/contacts/imports` | `GET` | `—` | `ImportJobCollection` |
| `ImportsApi` | `/contacts/imports/{contactImport}` | `GET` | `—` | `ImportJobDetailResponse` |
| `ImportsApi` | `/contacts/imports/{contactImport}/config` | `POST` | `ConfigureContactImportRequest` | `ImportJobResponse` |
| `ImportsApi` | `/contacts/imports/{contactImport}/failures` | `GET` | `—` | `(inline)` |
| `ImportsApi` | `/contacts/imports/{contactImport}/start` | `POST` | `—` | `ImportJobResponse` |
| `ListsApi` | `/lists` | `GET` | `—` | `ListCollection` |
| `ListsApi` | `/lists` | `POST` | `CreateListRequest` | `ListResponse` |
| `ListsApi` | `/lists/{list}` | `DELETE` | `—` | `DeleteResponse` |
| `ListsApi` | `/lists/{list}` | `GET` | `—` | `ListResponse` |
| `ListsApi` | `/lists/{list}` | `PUT` | `UpdateListRequest` | `ListResponse` |
| `ListsApi` | `/lists/{list}/contacts` | `DELETE` | `—` | `(inline)` |
| `ListsApi` | `/lists/{list}/contacts` | `POST` | `ListContactsMembershipRequest` | `(inline)` |
| `ListsApi` | `/lists/{list}/contacts/bulk-add` | `POST` | `ListContactsMembershipRequest` | `(inline)` |
| `ListsApi` | `/lists/{list}/contacts/bulk-remove` | `POST` | `ListContactsMembershipRequest` | `(inline)` |
| `ListsApi` | `/lists/{list}/contacts/remove` | `POST` | `ListContactsMembershipRequest` | `(inline)` |
| `MarketingApi` | `/custom-fields` | `GET` | `—` | `CustomFieldCollection` |
| `MarketingApi` | `/custom-fields` | `POST` | `CreateCustomFieldRequest` | `CustomFieldResponse` |
| `MarketingApi` | `/custom-fields/{customField}` | `DELETE` | `—` | `DeleteResponse` |
| `MarketingApi` | `/custom-fields/{customField}` | `GET` | `—` | `CustomFieldResponse` |
| `MarketingApi` | `/custom-fields/{customField}` | `PATCH` | `UpdateCustomFieldRequest` | `CustomFieldResponse` |
| `MessagesApi` | `/delivery-logs` | `GET` | `—` | `MessageListResponse` |
| `MessagesApi` | `/delivery-logs/{message}` | `GET` | `—` | `MessageDetailResponse` |
| `MessagesApi` | `/messages/{message}/events` | `GET` | `—` | `MessageEventsResponse` |
| `ProjectsApi` | `/projects` | `GET` | `—` | `ProjectListResponse` |
| `ProjectsApi` | `/projects` | `POST` | `CreateProjectRequest` | `ProjectResponse` |
| `ProjectsApi` | `/projects/{project}` | `DELETE` | `—` | `DeleteResponse` |
| `ProjectsApi` | `/projects/{project}` | `GET` | `—` | `ProjectResponse` |
| `ProjectsApi` | `/projects/{project}` | `PATCH` | `UpdateProjectRequest` | `ProjectResponse` |
| `SegmentsApi` | `/segments` | `GET` | `—` | `SegmentCollection` |
| `SegmentsApi` | `/segments` | `POST` | `CreateSegmentRequest` | `SegmentResponse` |
| `SegmentsApi` | `/segments/preview` | `POST` | `PreviewSegmentRequest` | `SegmentPreviewResponse` |
| `SegmentsApi` | `/segments/{segment}` | `DELETE` | `—` | `DeleteResponse` |
| `SegmentsApi` | `/segments/{segment}` | `GET` | `—` | `SegmentResponse` |
| `SegmentsApi` | `/segments/{segment}` | `PUT` | `UpdateSegmentRequest` | `SegmentResponse` |
| `SegmentsApi` | `/segments/{segment}/count` | `GET` | `—` | `SegmentCountResponse` |
| `SegmentsApi` | `/segments/{segment}/preview` | `POST` | `—` | `SegmentPreviewResponse` |
| `SuppressionsApi` | `/suppressions` | `GET` | `—` | `SuppressionListResponse` |
| `SuppressionsApi` | `/suppressions` | `POST` | `CreateSuppressionRequest` | `SuppressionResponse` |
| `SuppressionsApi` | `/suppressions/{suppression}` | `DELETE` | `—` | `DeleteResponse` |
| `SuppressionsApi` | `/suppressions/{suppression}` | `GET` | `—` | `SuppressionResponse` |
| `SuppressionsApi` | `/suppressions/{suppression}/restore` | `POST` | `—` | `SuppressionResponse` |
| `TagsApi` | `/tags` | `GET` | `—` | `TagCollection` |
| `TagsApi` | `/tags` | `POST` | `CreateTagRequest` | `TagResponse` |
| `TagsApi` | `/tags/bulk-assign` | `POST` | `BulkTagContactsRequest` | `(inline)` |
| `TagsApi` | `/tags/bulk-remove` | `POST` | `BulkTagContactsRequest` | `(inline)` |
| `TagsApi` | `/tags/{tag}` | `DELETE` | `—` | `DeleteResponse` |
| `TagsApi` | `/tags/{tag}` | `GET` | `—` | `TagResponse` |
| `TagsApi` | `/tags/{tag}` | `PATCH` | `UpdateTagRequest` | `TagResponse` |
| `TemplatesApi` | `/templates` | `GET` | `—` | `TemplateListResponse` |
| `TemplatesApi` | `/templates` | `POST` | `CreateTemplateRequest` | `TemplateResponse` |
| `TemplatesApi` | `/templates/preview` | `POST` | `PreviewTemplateByIdRequest` | `TemplatePreviewResponse` |
| `TemplatesApi` | `/templates/{template}` | `DELETE` | `—` | `DeleteResponse` |
| `TemplatesApi` | `/templates/{template}` | `GET` | `—` | `TemplateResponse` |
| `TemplatesApi` | `/templates/{template}` | `PATCH` | `UpdateTemplateRequest` | `TemplateResponse` |
| `TemplatesApi` | `/templates/{template}/duplicate` | `POST` | `DuplicateTemplateRequest` | `TemplateResponse` |
| `TemplatesApi` | `/templates/{template}/preview` | `POST` | `PreviewTemplateRequest` | `TemplatePreviewResponse` |
| `TemplatesApi` | `/templates/{template}/test` | `POST` | `TestTemplateRequest` | `TemplateTestResponse` |
| `WebhooksApi` | `/webhook-deliveries/{webhookDelivery}` | `GET` | `—` | `WebhookDeliveryResponse` |
| `WebhooksApi` | `/webhook-deliveries/{webhookDelivery}/replay` | `POST` | `—` | `WebhookDeliveryResponse` |
| `WebhooksApi` | `/webhooks` | `GET` | `—` | `WebhookListResponse` |
| `WebhooksApi` | `/webhooks` | `POST` | `CreateWebhookRequest` | `WebhookSecretResponse` |
| `WebhooksApi` | `/webhooks/{webhook}` | `DELETE` | `—` | `DeleteResponse` |
| `WebhooksApi` | `/webhooks/{webhook}` | `GET` | `—` | `WebhookResponse` |
| `WebhooksApi` | `/webhooks/{webhook}` | `PATCH` | `UpdateWebhookRequest` | `WebhookResponse` |
| `WebhooksApi` | `/webhooks/{webhook}/deliveries` | `GET` | `—` | `WebhookDeliveryListResponse` |
| `WebhooksApi` | `/webhooks/{webhook}/disable` | `POST` | `—` | `WebhookResponse` |
| `WebhooksApi` | `/webhooks/{webhook}/enable` | `POST` | `—` | `WebhookResponse` |
| `WebhooksApi` | `/webhooks/{webhook}/replay` | `POST` | `ReplayWebhookRequest` | `WebhookReplayResponse` |
| `WebhooksApi` | `/webhooks/{webhook}/rotate-secret` | `POST` | `—` | `WebhookSecretResponse` |
| `WebhooksApi` | `/webhooks/{webhook}/test` | `POST` | `TestWebhookRequest` | `WebhookDeliveryResponse` |

## Warnings

- `[main] WARN  o.o.codegen.DefaultCodegen - OpenAPI 3.1 support is still in beta. To report an issue related to 3.1 spec, please kindly open an issue in the Github repo: https://github.com/openAPITools/openapi-generator.`
- `[main] WARN  o.o.codegen.utils.ModelUtils - Failed to get the schema name: null`
- `[main] WARN  o.o.c.l.AbstractPythonCodegen - From (reserved word) cannot be used as model name. Renamed to ModelFrom`
- `[main] WARN  o.o.c.l.AbstractPythonCodegen - Codegen property is null (e.g. map/dict of undefined type). Default to typing.Any.`

## Problems

No blocking problems detected for Phase 2.

### Generator output excerpt

```text
[main] WARN  o.o.codegen.DefaultCodegen - OpenAPI 3.1 support is still in beta. To report an issue related to 3.1 spec, please kindly open an issue in the Github repo: https://github.com/openAPITools/openapi-generator.
[main] WARN  o.o.codegen.DefaultCodegen - OpenAPI 3.1 support is still in beta. To report an issue related to 3.1 spec, please kindly open an issue in the Github repo: https://github.com/openAPITools/openapi-generator.
[main] WARN  o.o.codegen.utils.ModelUtils - Failed to get the schema name: null
[main] INFO  o.o.codegen.DefaultGenerator - Model importContacts_request not generated since it's marked as unused (due to form parameters) and `skipFormModel` (global property) set to true (default)
[main] WARN  o.o.c.l.AbstractPythonCodegen - From (reserved word) cannot be used as model name. Renamed to ModelFrom
[main] WARN  o.o.c.l.AbstractPythonCodegen - Codegen property is null (e.g. map/dict of undefined type). Default to typing.Any.
[main] INFO  o.o.codegen.TemplateManager - writing file /var/folders/rg/t9_l356n3dq14lywxk104h4m0000gn/T/mailermine-openapi-3ucbzm7o/out/mailermine_generated/exceptions.py
```

## Recommendations

1. Keep regenerating via `python scripts/generate.py` only — never edit `generated/` by hand.
2. Phase 3 should wrap `mailermine_generated` behind `mailermine.config` / exception mapping; do not re-export generated models.
3. Call the generated sync urllib3 API methods from the v1 handwritten wrapper. Revisit `library=httpx` when OpenAPI Generator ships dual sync/async support in a stable release; that enables a future `AsyncMailerMine` without a second client.
4. Default runtime `host` must override the OpenAPI `servers` localhost URL to `https://mailermine.com/api/v1`.
5. Pin OpenAPI Generator `7.23.0` (same major line as `@mailermine/node`) until a coordinated upgrade.

## OpenAPI tags observed

- API Keys
- Analytics
- Audiences
- Campaign Analytics
- Campaign Events
- Campaign Lifecycle
- Campaigns
- Contacts
- Domains
- Emails
- Events
- Exports
- Imports
- Lists
- Marketing
- Messages
- Projects
- Segments
- Suppressions
- Tags
- Templates
- Webhooks

