# Changelog

All notable changes to the MailerMine Python SDK are documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.2.0] — 2026-11-27

### Added

- `emails.send(..., tracking={"opens": ..., "clicks": ...})` turns open/click
  tracking on or off for one email. Omitted keys use the project default.
- Project `settings["tracking"]` (`opens`, `clicks`) sets a project's tracking
  defaults on `projects.create()` / `update()`.
- `WebhookEventPayload`, `WebhookClick` and `WebhookOpen` types. `email.clicked`
  webhooks now include `click` (`url`, `link_id`, `is_unique`, `clicked_at`)
  and `email.opened` includes `open` (`is_unique`, `opened_at`).

### Fixed

- `metadata`, `headers` and `variables` on `emails.send()`, and `settings` on
  `projects.create()` / `update()`, were silently sent as `null`. The generated
  request models used an `anyOf` wrapper that pydantic's request validation
  turned into `None`; request bodies now use plain dict fields
  (`scripts/openapi_normalize.py`).

### Changed

- Regenerated the client from the latest API spec (openapi-generator 7.23.0).

## [1.1.0] — 2026-11-17

### Added

- Automatic retries with backoff for 429/502/503/504 and transport errors,
  honouring `Retry-After` (`max_retries`, default 2; `max_retry_delay`,
  default 30s; `MAILERMINE_MAX_RETRIES`). POSTs are only replayed when they
  carry an `Idempotency-Key`.
- `emails.send(..., idempotency_key=...)`; sends get a random key by default
  so SDK retries never deliver twice.
- `client.rate_limit` / `ApiError.rate_limit` (`RateLimitInfo`) and
  `ApiError.is_retryable`.
- `MissingScopeError` (subclass of `PlanError`) with `missing_scopes`.
- `Scopes` / `ScopePresets`, including `webhooks.*`, `suppressions.*` and
  `events.read`.
- `Webhooks.verify_headers()`.
- `held` message status: messages held for MailerMine trust & safety review
  (the send call still succeeds). Older SDK versions reject this value in
  strict response models, so upgrade before relying on it. Blocked sends are
  `ValidationError`s with an `errors.content`, `errors.sending_limit`,
  `errors.recipients` or `errors.sending` entry.

### Fixed

- `Webhooks.verify()` could never validate a real MailerMine delivery: the
  server signs `{timestamp}.{body}`. It now accepts the timestamp and rejects
  stale deliveries (5 minute default); without a timestamp it keeps the old
  body-only check.

### Changed

- Regenerated the OpenAPI client from the current API spec.

## [1.0.0] — 2026-07-18

First stable public release of the official MailerMine Python SDK. Full public-surface
parity with `@mailermine/node` and `mailermine/mailermine` (Laravel).

### Features

- `MailerMine` client with lazy-loaded resources and shared generated transport
- Immutable `Configuration` with environment variable support
- Sync-only HTTP client (urllib3) with architecture ready for a future async client
- Typed public surface (`py.typed`) for IDE autocomplete

### Resources

Eighteen resources with Node/Laravel method parity:

- Projects, API Keys, Emails, Domains, Templates
- Contacts, Lists, Segments, Tags, Audiences
- Campaigns, Analytics, Events, Messages
- Webhooks, Suppressions, Imports, Exports

### Exceptions

Public hierarchy (generated exceptions never leak):

- `MailerMineError`
- `ApiError`
- `AuthenticationError`
- `ValidationError`
- `NotFoundError`
- `PlanError`
- `RateLimitError`

### Responses

- `Response` — `success`, `data`, `message`, `meta`
- `Collection` — iterable items, index access, `len()`
- `Pagination` — `current_page`, `per_page`, `total`, `last_page`

### Packaging

- PyPI name: `mailermine`
- Python `>=3.10`
- Install via `pip`, `poetry`, or `uv`
- MIT license
- Wheel includes `mailermine` + internal `mailermine_generated` transport

[1.0.0]: https://github.com/rahulyadav5192/mailermine-sdk-python/releases/tag/v1.0.0
