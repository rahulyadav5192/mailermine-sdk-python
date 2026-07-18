# Changelog

All notable changes to the MailerMine Python SDK are documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

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
