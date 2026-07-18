# MailerMine Python SDK — Parity Report

**Phase:** 4 — Full public API parity with Laravel + Node  
**Package:** `mailermine`  
**Compared against:**
- `@mailermine/node` (`mailermine-node-sdk`)
- `mailermine/mailermine` (`mailermine-laravel-sdk`)

**Verdict: 18/18 resources · 173/173 public methods · 100% Node parity**

---

## Summary

| Metric | Result |
| --- | --- |
| Public resources | **18 / 18** |
| Missing resources | **0** |
| Public methods (Node baseline) | **173** |
| Public methods (Python) | **173** |
| Missing methods vs Node | **0** |
| Extra methods vs Node | **0** |
| Return wrappers | `Response` / `Collection` / `Pagination` |
| Exception mapping | Complete (generated never leaks) |
| Naming | snake_case (idiomatic Python) |
| Type hints + docstrings | Required on every public method (enforced by tests) |
| Autocomplete surface | Typed `MailerMine` resource properties |
| Smoke / parity tests | Pass (no live API) |

Python mirrors Node’s public surface exactly (snake_case). Laravel matches the same resource set; the only intentional Node/Laravel delta is `Webhooks.verify` (present in Node + Python, absent in Laravel).

---

## Resources (18/18)

| # | Python | Node | Laravel | Status |
| ---: | --- | --- | --- | --- |
| 1 | `emails` | `emails` | `emails()` | Present |
| 2 | `projects` | `projects` | `projects()` | Present |
| 3 | `api_keys` | `apiKeys` | `apiKeys()` | Present |
| 4 | `domains` | `domains` | `domains()` | Present |
| 5 | `templates` | `templates` | `templates()` | Present |
| 6 | `contacts` | `contacts` | `contacts()` | Present |
| 7 | `lists` | `lists` | `lists()` | Present |
| 8 | `segments` | `segments` | `segments()` | Present |
| 9 | `tags` | `tags` | `tags()` | Present |
| 10 | `audiences` | `audiences` | `audiences()` | Present |
| 11 | `campaigns` | `campaigns` | `campaigns()` | Present |
| 12 | `analytics` | `analytics` | `analytics()` | Present |
| 13 | `events` | `events` | `events()` | Present |
| 14 | `messages` | `messages` | `messages()` | Present |
| 15 | `webhooks` | `webhooks` | `webhooks()` | Present |
| 16 | `suppressions` | `suppressions` | `suppressions()` | Present |
| 17 | `imports` | `imports` | `imports()` | Present |
| 18 | `exports` | `exports` | `exports()` | Present |

**Missing resources:** none.

`MarketingApi` / custom-field definition endpoints remain generated-only — same as Node and Laravel (not a public SDK resource).

---

## Method parity (173/173)

Baseline = Node public methods → Python snake_case.

| Resource | Node | Python | Missing | Extra |
| --- | ---: | ---: | ---: | ---: |
| `emails` | 4 | 4 | 0 | 0 |
| `projects` | 5 | 5 | 0 | 0 |
| `api_keys` | 7 | 7 | 0 | 0 |
| `domains` | 7 | 7 | 0 | 0 |
| `templates` | 8 | 8 | 0 | 0 |
| `contacts` | 10 | 10 | 0 | 0 |
| `lists` | 7 | 7 | 0 | 0 |
| `segments` | 6 | 6 | 0 | 0 |
| `tags` | 7 | 7 | 0 | 0 |
| `audiences` | 8 | 8 | 0 | 0 |
| `campaigns` | 47 | 47 | 0 | 0 |
| `analytics` | 15 | 15 | 0 | 0 |
| `events` | 5 | 5 | 0 | 0 |
| `messages` | 6 | 6 | 0 | 0 |
| `webhooks` | 16 | 16 | 0 | 0 |
| `suppressions` | 6 | 6 | 0 | 0 |
| `imports` | 6 | 6 | 0 | 0 |
| `exports` | 3 | 3 | 0 | 0 |
| **Total** | **173** | **173** | **0** | **0** |

### Method inventory (Python)

**emails** — `send`, `list`, `get`, `events`

**projects** — `create`, `list`, `get`, `update`, `delete`

**api_keys** — `create`, `list`, `get`, `update`, `rotate`, `reveal`, `delete`

**domains** — `create`, `list`, `get`, `dns_records`, `status`, `verify`, `delete`

**templates** — `create`, `list`, `get`, `update`, `preview`, `duplicate`, `test`, `delete`

**contacts** — `create`, `upsert`, `list`, `get`, `identify`, `search`, `update`, `subscribe`, `unsubscribe`, `delete`

**lists** — `create`, `list`, `get`, `update`, `add_contact`, `remove_contact`, `delete`

**segments** — `create`, `list`, `get`, `update`, `preview`, `delete`

**tags** — `create`, `list`, `get`, `update`, `assign`, `remove`, `delete`

**audiences** — `create`, `list`, `get`, `update`, `delete`, `contacts`, `add_contacts`, `remove_contacts`

**campaigns** — `create`, `list`, `get`, `update`, `delete`, `duplicate`, `archive`, `restore`, `preview`, `render`, `validate`, `mark_ready`, `send`, `pause`, `resume`, `cancel`, `schedule`, `reschedule`, `unschedule`, `send_now`, `cancel_schedule`, `set_template`, `set_subject`, `set_sender`, `set_reply_to`, `set_preheader`, `recipient_count`, `preview_recipients`, `recipients`, `add_segment`, `add_audience`, `remove_segment`, `remove_audience`, `analytics`, `events`, `timeline`, `activity`, `opens`, `clicks`, `deliveries`, `delivery`, `bounces`, `complaints`, `unsubscribes`, `links`, `progress`, `status`

**analytics** — `overview`, `usage`, `messages`, `engagement`, `campaigns`, `domains`, `projects`, `providers`, `activity`, `opens`, `clicks`, `deliveries`, `bounces`, `complaints`, `unsubscribes`

**messages** — `list`, `search`, `filter`, `get`, `events`, `timeline`

**events** — `list`, `get`, `timeline`, `history`, `message`

**webhooks** — `create`, `list`, `get`, `update`, `delete`, `enable`, `disable`, `rotate_secret`, `test`, `verify`, `deliveries`, `delivery`, `logs`, `failures`, `replay`, `retry`

**suppressions** — `add`, `list`, `get`, `check`, `restore`, `remove`

**imports** — `create`, `list`, `status`, `configure`, `start`, `cancel`

**exports** — `create`, `status`, `download`

**Missing methods:** none.

---

## Naming conventions

| Concern | Node | Laravel | Python |
| --- | --- | --- | --- |
| Resource accessors | camelCase (`apiKeys`) | camelCase methods (`apiKeys()`) | snake_case (`api_keys`) |
| Method names | camelCase | camelCase | snake_case |
| Payload keys | camelCase in TS types → snake on wire | arrays / models | snake_case (`reply_to`, `scheduled_at`) |
| Reserved `from` | `from` | `from` | `from` in dicts; `from_` kwargs alias |

Functionality is identical; only Python idioms differ.

---

## Return types

| Pattern | Node | Laravel | Python |
| --- | --- | --- | --- |
| Single object | `Response<T>` | `Response` | `Response[object]` |
| List page | `Collection<T>` | `Collection` | `Collection[object]` |
| Pagination | `Pagination` | `Pagination` | `Pagination` |
| Delete ack | `Response<{deleted:true}>` | delete response | `Response[{"deleted": True}]` |
| Webhook verify | `boolean` | n/a | `bool` |
| Export download | `Response<string>` | string/body | `Response[str]` / plain payload |

Envelope fields:

- `Response`: `success`, `data`, `message`, `meta`
- `Collection`: `items`, `pagination`, iterable, `len()`, index access

Generated models are never returned.

---

## Exception mapping

| HTTP / condition | Node | Laravel | Python |
| --- | --- | --- | --- |
| Base | `ApiError` | `ApiException` | `MailerMineError` → `ApiError` |
| 401 | `AuthenticationError` | `AuthenticationException` | `AuthenticationError` |
| 403 | `PlanError` | `PlanException` | `PlanError` |
| 404 | `NotFoundError` | `NotFoundException` | `NotFoundError` |
| 422 | `ValidationError` | `ValidationException` | `ValidationError` |
| 429 | `RateLimitError` | `RateLimitException` | `RateLimitError` |
| Transport | `ApiError(status=0)` | `ApiException` | `ApiError(status=0)` |

All resource calls run through `BaseResource.execute()` → `map_generated_error()`. Generated exceptions never escape.

---

## Type hint & autocomplete coverage

| Area | Status |
| --- | --- |
| `MailerMine` resource properties | Annotated (`-> Emails`, `-> Campaigns`, …) |
| Public resource methods | Return annotations + Parameters/Returns/Raises/Examples docstrings |
| `py.typed` | Present |
| VS Code / Pyright surface | `client.projects`, `client.contacts`, `client.analytics`, method signatures |

Enforced by `tests/test_parity.py` (docstrings + return annotations + property return types).

---

## Laravel comparison notes

| Topic | Detail |
| --- | --- |
| Resources | Same 18 |
| Methods | Same set as Node, except Laravel has **no** `Webhooks::verify` helper |
| Python choice | Keep `Webhooks.verify` for Node parity (local HMAC verification) |
| Access style | Laravel uses `emails()` methods; Python/Node use attribute accessors |

---

## OpenAPI vs public SDK surface

OpenAPI includes additional generated APIs (e.g. `MarketingApi` custom fields, some bulk/restore operations). Official Laravel and Node SDKs **do not** expose those as first-class public resources/methods. Python follows the same public contract.

Transport coverage remains complete via `generated/`; wrappers only expose the shared official surface.

---

## Verification

```bash
pytest tests/test_parity.py tests/test_wrapper.py -q
ruff check mailermine tests
mypy mailermine
```

Parity suite asserts:

1. All 18 resources exist on `MailerMine`
2. Every Node method exists in snake_case on the matching Python class
3. No unexpected extra public methods
4. Totals are 18 resources / 173 methods
5. Docstrings + return annotations present
6. Client property annotations resolve to resource classes

---

## Goal checklist

| Goal | Status |
| --- | --- |
| 18/18 resources | ✅ |
| 100% public API parity with Node | ✅ |
| Laravel functional parity | ✅ (plus Node `webhooks.verify`) |
| Response / Collection / Pagination | ✅ |
| Exception mapping | ✅ |
| snake_case public API | ✅ |
| Generated models hidden | ✅ |
| Autocomplete-ready typed client | ✅ |
| Smoke tests (no live API) | ✅ |
