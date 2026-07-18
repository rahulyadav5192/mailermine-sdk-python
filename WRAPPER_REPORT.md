# MailerMine Python SDK — Wrapper Report

**Phase:** 3 — Handwritten wrapper over generated OpenAPI client  
**Package:** `mailermine`  
**Transport:** `mailermine_generated` (OpenAPI Generator `python` / `urllib3`)  
**Parity targets:** `@mailermine/node`, `mailermine/mailermine` (Laravel)

Generated code under `generated/` was **not modified**. Customers never import it.

---

## Wrapper architecture

```text
Application
    │
    ▼
mailermine.MailerMine          # public client, lazy resources
    │
    ├── mailermine.config.Configuration
    ├── mailermine.exceptions.*   # public errors only
    ├── mailermine.support.*      # Response / Collection / Pagination
    └── mailermine.resources.*    # 18 handwritten resources
            │
            ▼
mailermine._internal.apis.GeneratedApis   # private
            │
            ▼
mailermine_generated (ApiClient + *Api classes)
```

### Hard boundaries

| Layer | Public? | Notes |
| --- | --- | --- |
| `mailermine/` | Yes | Handwritten Stripe/Resend-style API |
| `mailermine/_internal/` | No | Generated client wiring only |
| `generated/mailermine_generated/` | No | Immutable OpenAPI output |

Every resource call goes through `BaseResource.execute()`, which maps generated exceptions into the public hierarchy before they can leak.

---

## Public resources (18)

| Accessor | Class | Generated API class(es) |
| --- | --- | --- |
| `emails` | `Emails` | `EmailsApi` + `MessagesApi` |
| `projects` | `Projects` | `ProjectsApi` |
| `api_keys` | `ApiKeys` | `APIKeysApi` |
| `domains` | `Domains` | `DomainsApi` |
| `templates` | `Templates` | `TemplatesApi` |
| `contacts` | `Contacts` | `ContactsApi` |
| `lists` | `Lists` | `ListsApi` |
| `segments` | `Segments` | `SegmentsApi` |
| `tags` | `Tags` | `TagsApi` |
| `audiences` | `Audiences` | `AudiencesApi` (+ lists/segments/contacts) |
| `campaigns` | `Campaigns` | `CampaignsApi` + Lifecycle + Analytics + Events |
| `analytics` | `Analytics` | `AnalyticsApi` (+ campaigns/events fallbacks) |
| `events` | `Events` | `EventsApi` + `MessagesApi` |
| `messages` | `Messages` | `MessagesApi` |
| `webhooks` | `Webhooks` | `WebhooksApi` |
| `suppressions` | `Suppressions` | `SuppressionsApi` |
| `imports` | `Imports` | `ImportsApi` |
| `exports` | `Exports` | `ExportsApi` |

`MarketingApi` remains generated-only (parity with Node/Laravel — not a public resource).

---

## Public methods

### `emails`
- `send()`, `list()`, `get()`, `events()`

### `projects`
- `create()`, `list()`, `get()`, `update()`, `delete()`

### `api_keys`
- `create()`, `list()`, `get()`, `update()`, `delete()`, `rotate()`, `reveal()`

### `domains`
- `create()`, `list()`, `get()`, `verify()`, `delete()`, `dns_records()`, `status()`

### `templates`
- `create()`, `list()`, `get()`, `update()`, `preview()`, `duplicate()`, `test()`, `delete()`

### `contacts`
- `create()`, `list()`, `get()`, `update()`, `delete()`, `upsert()`, `search()`, `identify()`, `subscribe()`, `unsubscribe()`

### `lists`
- `create()`, `list()`, `get()`, `update()`, `delete()`, `add_contact()`, `remove_contact()`

### `segments`
- `create()`, `list()`, `get()`, `update()`, `delete()`, `preview()`

### `tags`
- `create()`, `list()`, `get()`, `update()`, `delete()`, `assign()`, `remove()`

### `audiences`
- `create()`, `list()`, `get()`, `update()`, `delete()`, `contacts()`, `add_contacts()`, `remove_contacts()`

### `campaigns`
- Core: `create()`, `list()`, `get()`, `update()`, `delete()`, `duplicate()`, `archive()`, `restore()`
- Content: `set_subject()`, `set_sender()`, `set_reply_to()`, `set_preheader()`, `set_template()`
- Audience: `add_segment()`, `add_audience()`, `remove_segment()`, `remove_audience()`, `recipient_count()`, `preview_recipients()`
- Lifecycle: `validate()`, `mark_ready()`, `send()`, `schedule()`, `reschedule()`, `unschedule()`, `send_now()`, `pause()`, `resume()`, `cancel()`, `cancel_schedule()`
- Insights: `preview()`, `render()`, `status()`, `progress()`, `analytics()`, `opens()`, `clicks()`, `bounces()`, `complaints()`, `unsubscribes()`, `deliveries()`, `delivery()`, `links()`, `events()`, `activity()`, `timeline()`, `recipients()`

### `analytics`
- `overview()`, `deliveries()`, `opens()`, `clicks()`, `bounces()`, `complaints()`, `unsubscribes()`, `usage()`, `activity()`, `messages()`, `engagement()`, `campaigns()`, `domains()`, `projects()`, `providers()`

### `events`
- `list()`, `get()`, `timeline()`, `history()`, `message()`

### `messages`
- `list()`, `get()`, `search()`, `filter()`, `events()`, `timeline()`

### `webhooks`
- `create()`, `list()`, `get()`, `update()`, `delete()`, `test()`, `rotate_secret()`, `enable()`, `disable()`, `deliveries()`, `delivery()`, `logs()`, `failures()`, `replay()`, `retry()`, `verify()` (static)

### `suppressions`
- `list()`, `get()`, `add()`, `remove()`, `restore()`, `check()`

### `imports`
- `list()`, `create()`, `status()`, `configure()`, `start()`, `cancel()` (raises `ApiError` 405 — unsupported)

### `exports`
- `create()`, `status()`, `download()`

---

## Exception mapping

```text
MailerMineError
└── ApiError
    ├── AuthenticationError   # 401
    ├── PlanError             # 403 (+ upgrade URL guidance)
    ├── NotFoundError         # 404
    ├── ValidationError       # 422 (+ field errors)
    └── RateLimitError        # 429 (+ retry_after)
```

| Source | Public type |
| --- | --- |
| Generated `ApiException` 401 | `AuthenticationError` |
| Generated `ApiException` 403 | `PlanError` |
| Generated `ApiException` 404 | `NotFoundError` |
| Generated `ApiException` 422 / client `ApiValueError` | `ValidationError` |
| Generated `ApiException` 429 | `RateLimitError` |
| Other HTTP / transport | `ApiError` (`status=0` for pure transport) |

Messages are sanitized to strip generated class / package names. `BaseResource.execute()` is the single choke point.

---

## Response architecture

`Response[T]`:

| Attribute | Meaning |
| --- | --- |
| `success` | API success flag |
| `data` | Primary payload (plain dict / list / scalar — never a generated model) |
| `message` | Human-readable API message |
| `meta` | Optional metadata map |
| `to_dict()` | JSON-serializable envelope |

Requests accept `dict` / kwargs / primitives. Wrappers convert via `to_generated_request()` before calling generated APIs. Responses are normalized with `to_plain()` / `to_response()`.

Public payloads stay **snake_case** (Pythonic). Use `from_` as a kwargs alias for the reserved `from` field when sending email.

---

## Collection architecture

`Collection[T]` extends `Response[list[T]]`:

| Feature | Behavior |
| --- | --- |
| `items` | Page items |
| `pagination` | `Pagination` instance |
| `len(collection)` | Page size |
| iteration | `for item in collection` |
| index access | `collection[0]` |
| `first()` / `is_empty()` | Convenience helpers |
| `to_dict()` | Full envelope including pagination |

`Pagination`:

- `current_page`, `per_page`, `total`, `last_page`
- `has_next_page`, `has_previous_page`

---

## Configuration

```python
Configuration.create(
    api_key="relay_live_xxx",          # or MAILERMINE_API_KEY
    base_url="https://mailermine.com/api/v1",  # or MAILERMINE_BASE_URL
    timeout=30.0,                      # seconds; or MAILERMINE_TIMEOUT
    user_agent="mailermine-python/0.1.0",
)
```

| Option | Default | Env var |
| --- | --- | --- |
| `api_key` | required | `MAILERMINE_API_KEY` |
| `base_url` | `https://mailermine.com/api/v1` | `MAILERMINE_BASE_URL` |
| `timeout` | `30.0` seconds | `MAILERMINE_TIMEOUT` |
| `user_agent` | `mailermine-python/{VERSION}` | — |

Client construction mirrors Node:

```python
from mailermine import MailerMine

client = MailerMine(api_key="relay_live_xxx")
client.emails.send(...)
client.projects.list()
client.contacts.create(...)
```

One shared generated `ApiClient` backs all lazy-loaded resources.

---

## Future async strategy

v1 is **sync-only** (urllib3 generated client).

Architecture already isolates transport behind:

1. `create_generated_apis(configuration)`
2. Resource classes that only depend on injected API objects
3. `BaseResource.execute()` for error mapping

A future `AsyncMailerMine` can:

1. Regenerate (or dual-generate) with `library=httpx` once stable dual sync/async lands in OpenAPI Generator
2. Add `mailermine/_internal/async_apis.py`
3. Mirror resources as `AsyncEmails`, etc., reusing the same Response/exception/config types

No public API changes are required for sync callers.

---

## Verification

```bash
ruff check mailermine tests
mypy mailermine
pytest
```

Results for this phase:

| Gate | Result |
| --- | --- |
| Ruff | Pass |
| Mypy (strict on `mailermine/`) | Pass |
| Pytest | **38 passed** |

Smoke coverage includes:

- All 18 resource accessors on `MailerMine`
- `Response` / `Collection` / `Pagination`
- Exception status mapping (401/403/404/422/429)
- Webhook signature verification
- Public `__all__` does not export generated symbols
- `emails.send` kwargs → generated request conversion (mocked)

---

## Explicit non-goals (still deferred)

- Async client
- Live integration tests against production
- Marketing/custom-fields public resource
- PyPI GA release polish (examples expansion, full README rewrite)
