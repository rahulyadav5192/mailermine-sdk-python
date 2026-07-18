# MailerMine Python SDK — Architecture

**Package:** `mailermine`  
**Phase:** 1 — Architecture only (no resource implementations)  
**Source of truth:** https://www.mailermine.com/openapi.json  
**Parity targets:** `mailermine/mailermine` (Laravel/PHP) and `@mailermine/node`

This document is the authoritative design for the official MailerMine Python SDK. It locks every structural decision before any resource method is written.

---

## 1. Purpose and non-goals

### Purpose

Ship a production Python SDK that feels like Stripe, Resend, or OpenAI:

```python
from mailermine import MailerMine

client = MailerMine(api_key="relay_live_xxx")
client.emails.send(...)
client.projects.list()
client.contacts.create(...)
```

Developers interact only with the handwritten `mailermine/` surface. Generated OpenAPI code is an internal transport layer.

### Non-goals (Phase 1)

- Implementing any of the 18 resource APIs
- Running OpenAPI generation into `generated/`
- Publishing to PyPI
- Framework integrations (Django helpers, FastAPI deps) beyond a clean client API

---

## 2. Guiding principles

| Principle | Decision |
| --- | --- |
| Single source of truth | All paths, schemas, and operations come from OpenAPI. Never hardcode endpoints or request/response schemas in wrappers. |
| Generated code is immutable | Output lives only under `generated/`. Never edit by hand. Regenerate via `scripts/`. |
| Public surface is handwritten | Everything under `mailermine/` is owned, typed, and reviewed. |
| Generated types never leak | Callers never import generated models, APIs, or exceptions. |
| Cross-SDK parity | Same 18 resources, same capability surface, same error semantics as Laravel and Node. |
| Python-native DX | snake_case accessors, PEP 8, full type hints, modern packaging. |
| Fail closed on errors | Map every generated/transport failure into the public exception hierarchy. |

---

## 3. Repository layout

```text
mailermine-sdk-python/
├── mailermine/                 # Public handwritten SDK (shipped)
│   ├── __init__.py             # Public re-exports
│   ├── client.py               # MailerMine root client
│   ├── resources/              # One module per resource (18)
│   │   ├── base.py
│   │   ├── emails.py
│   │   ├── projects.py
│   │   ├── api_keys.py
│   │   ├── domains.py
│   │   ├── templates.py
│   │   ├── contacts.py
│   │   ├── lists.py
│   │   ├── segments.py
│   │   ├── tags.py
│   │   ├── audiences.py
│   │   ├── campaigns.py
│   │   ├── analytics.py
│   │   ├── events.py
│   │   ├── messages.py
│   │   ├── webhooks.py
│   │   ├── suppressions.py
│   │   ├── imports.py
│   │   └── exports.py
│   ├── exceptions/             # Public exception hierarchy
│   ├── support/                # Response, Collection, Pagination, Iterator, JSON
│   └── config/                 # Configuration / defaults
├── generated/                  # OpenAPI Generator output (do not hand-edit)
├── tests/                      # pytest suite
├── examples/                   # Runnable usage examples
├── scripts/                    # generate, release, parity helpers
├── pyproject.toml              # Package + tool configuration
├── ARCHITECTURE.md             # This document
├── README.md
└── LICENSE
```

### Ownership boundaries

| Path | Owner | Editable by hand? |
| --- | --- | --- |
| `mailermine/` | SDK team | Yes |
| `generated/` | OpenAPI Generator only | **No** |
| `scripts/` | SDK team | Yes (orchestration only) |
| `tests/`, `examples/` | SDK team | Yes |

Generated code may be **imported** from `mailermine/` (and `scripts/`), never re-exported from the public package API.

---

## 4. Public API design

### 4.1 Root client

Class name: `MailerMine` (matches Node; Laravel uses `Client` for PHP idioms).

```python
from mailermine import MailerMine

client = MailerMine(api_key="relay_live_xxx")
# or
client = MailerMine(api_key="...", base_url="https://mailermine.com/api/v1", timeout=30.0)
```

Constructor accepts:

1. Keyword options (`api_key`, `base_url`, `timeout`, `user_agent`, optional HTTP client)
2. A `Configuration` instance
3. A plain API key string shorthand (parity with Laravel/Node)

Resources are exposed as **attributes** (Node style), not methods (Laravel `emails()`), because that is the idiomatic Python SDK pattern:

| Laravel | Node | Python |
| --- | --- | --- |
| `$mm->emails()` | `mm.emails` | `client.emails` |
| `$mm->apiKeys()` | `mm.apiKeys` | `client.api_keys` |

### 4.2 The 18 resources (exact parity)

| # | Python accessor | Module | Responsibility |
| ---: | --- | --- | --- |
| 1 | `emails` | `emails.py` | Transactional send + message lookups |
| 2 | `projects` | `projects.py` | Workspace projects |
| 3 | `api_keys` | `api_keys.py` | Project API keys |
| 4 | `domains` | `domains.py` | Sending domains, DNS, verification |
| 5 | `templates` | `templates.py` | Reusable templates |
| 6 | `contacts` | `contacts.py` | Marketing contacts |
| 7 | `lists` | `lists.py` | Static contact lists |
| 8 | `segments` | `segments.py` | Dynamic segments |
| 9 | `tags` | `tags.py` | Contact tags |
| 10 | `audiences` | `audiences.py` | Unified list/segment catalog |
| 11 | `campaigns` | `campaigns.py` | Campaigns + lifecycle |
| 12 | `analytics` | `analytics.py` | Account / campaign analytics |
| 13 | `events` | `events.py` | Delivery & engagement events |
| 14 | `messages` | `messages.py` | Delivery logs / message history |
| 15 | `webhooks` | `webhooks.py` | Endpoints, deliveries, replay |
| 16 | `suppressions` | `suppressions.py` | Suppression list |
| 17 | `imports` | `imports.py` | Contact import jobs |
| 18 | `exports` | `exports.py` | Contact export jobs |

OpenAPI tags such as “Campaign Lifecycle”, “Campaign Analytics”, and “Marketing” are **not** separate public resources. They fold into `campaigns`, `analytics`, and related wrappers exactly as in Laravel and Node.

### 4.3 Public exports (`mailermine.__init__`)

Export only:

- `MailerMine`
- `Configuration` (+ option TypedDict / dataclass types)
- Exception types listed in §6
- `Response`, `Collection`, `Pagination` (+ iterator helpers)
- Version / default constants (`VERSION`, `DEFAULT_BASE_URL`, `DEFAULT_TIMEOUT`, `DEFAULT_USER_AGENT`)
- Resource classes (for typing / advanced use)

**Never** export anything from `generated/`.

---

## 5. Layered architecture

```text
┌─────────────────────────────────────────────────────────┐
│  Application code                                       │
│  from mailermine import MailerMine                      │
└───────────────────────────┬─────────────────────────────┘
                            │
┌───────────────────────────▼─────────────────────────────┐
│  mailermine.client.MailerMine                           │
│  lazy resource properties                               │
└───────────────────────────┬─────────────────────────────┘
                            │
┌───────────────────────────▼─────────────────────────────┐
│  mailermine.resources.*                                 │
│  BaseResource + typed methods                           │
│  input validation → call generated API                  │
│  map models → Response / Collection / dict/TypedDict    │
│  map errors → mailermine.exceptions                     │
└───────────────────────────┬─────────────────────────────┘
                            │
┌───────────────────────────▼─────────────────────────────┐
│  mailermine.config + internal generated wiring          │
│  auth header, base URL, timeout, user-agent             │
└───────────────────────────┬─────────────────────────────┘
                            │
┌───────────────────────────▼─────────────────────────────┐
│  generated/  (OpenAPI Generator — python)               │
│  API classes, models, urllib3 transport                 │
└─────────────────────────────────────────────────────────┘
```

### Responsibilities by layer

| Layer | Does | Does not |
| --- | --- | --- |
| `MailerMine` | Hold config; lazy-create resources | Know endpoints |
| `resources/*` | Friendly methods; shape inputs/outputs; catch errors | Duplicate OpenAPI paths |
| `support/*` | Normalize envelopes into Response/Collection | Talk to the network |
| `exceptions/*` | Public error types + mapper entrypoints | Expose generated exception types |
| `config/*` | Validate and freeze settings | Perform HTTP |
| `generated/` | HTTP + serialization per OpenAPI | Appear in public docs |

---

## 6. Exceptions

### Public hierarchy

```text
MailerMineError
└── ApiError
    ├── AuthenticationError   # HTTP 401
    ├── PlanError             # HTTP 403
    ├── NotFoundError         # HTTP 404
    ├── ValidationError       # HTTP 422 (+ client-side validation)
    └── RateLimitError        # HTTP 429
```

| Type | Role |
| --- | --- |
| `MailerMineError` | Root for `except MailerMineError` |
| `ApiError` | HTTP/transport failures; carries `status`, `body`, `headers`, `request_id` |
| `AuthenticationError` | Missing/invalid/revoked API key |
| `PlanError` | Plan or scope restriction; includes upgrade guidance parity with Laravel |
| `NotFoundError` | Missing resource |
| `ValidationError` | Field errors map (`errors: Mapping[str, Sequence[str]]`) |
| `RateLimitError` | Optional `retry_after: int \| None` (seconds) |

### Mapping rules (parity with Node/Laravel)

| Condition | Public exception |
| --- | --- |
| Generated API exception / HTTP 401 | `AuthenticationError` |
| HTTP 403 | `PlanError` |
| HTTP 404 | `NotFoundError` |
| HTTP 422 or client-side required-field failure | `ValidationError` |
| HTTP 429 | `RateLimitError` |
| Other HTTP / connection / timeout | `ApiError` (status `0` for pure transport) |

`BaseResource.execute()` (or equivalent) is the single choke point: every resource call runs through it so generated exceptions never propagate.

Messages must be sanitized — no generated class names, stack paths under `generated/`, or OpenAPI Generator identifiers in user-visible text.

---

## 7. Responses

Parity with Laravel/Node support objects:

| Type | Purpose |
| --- | --- |
| `Response[T]` | Single-object success envelope (`data`, `message`, `success`) |
| `Collection[T]` | List page: iterable items + `Pagination` |
| `Pagination` | `current_page`, `per_page`, `total`, `last_page`, `has_next_page`, `has_previous_page` |
| Iterator helpers | Page-walking helpers for “fetch all” without exposing raw HTTP |
| JSON | `to_dict()` / `json.dumps`-friendly via standard encoding; `JsonValue` type aliases |

### Envelope strategy

MailerMine API responses typically look like:

```json
{ "success": true, "message": "...", "data": { ... }, "meta": { ... } }
```

Wrappers:

1. Call the generated API method.
2. Convert generated models → plain `dict` / TypedDict / small dataclasses owned by `mailermine/`.
3. Wrap in `Response` or `Collection`.
4. Never return a generated model instance to the caller.

Python naming uses snake_case on these value objects (`current_page`, not `currentPage`), matching PEP 8 while preserving the same fields as Node/Laravel.

---

## 8. Configuration

Immutable, validated configuration (parity with siblings):

| Option | Default | Notes |
| --- | --- | --- |
| `api_key` | — (required) | Non-empty; trimmed |
| `base_url` | `https://mailermine.com/api/v1` | Absolute URL; trailing slashes stripped. **Do not** use the OpenAPI `servers` localhost URL in production defaults. |
| `timeout` | `30.0` seconds | Positive finite float (Python uses seconds; Node uses ms) |
| `user_agent` | `mailermine-python/{VERSION}` | Non-empty |
| HTTP client | Generated/default urllib3 | Injectable for tests |

OpenAPI `servers[0]` currently points at local development (`http://127.0.0.1:8000/api/v1`). Generation may rewrite that host; runtime config always prefers the SDK default unless the user overrides `base_url`.

---

## 9. Code generation strategy

### Tooling

| Item | Choice | Rationale |
| --- | --- | --- |
| Spec URL | `https://www.mailermine.com/openapi.json` | Canonical production spec |
| Local pin | `openapi.json` at repo root (downloaded by script, like Node) | Reproducible CI / offline regen |
| Generator | [OpenAPI Generator](https://openapi-generator.tech/) CLI | Same family as Laravel (`php`) and Node (`typescript-fetch`) |
| Generator version | Pin exact JAR version in `scripts/generate.py` (start from current Node pin lineage, e.g. 7.x) | Reproducible builds |
| Generator name | `python` | Official urllib3 + Pydantic client; mature, matches “generated transport” model |
| Output directory | `generated/` | Isolated; gitignored or committed (see §9.3) |

### Generation pipeline (`scripts/generate.py`)

1. Download latest OpenAPI JSON from the canonical URL.
2. Validate the document (paths present, OpenAPI 3.x).
3. Wipe `generated/` completely.
4. Run OpenAPI Generator with pinned JAR + fixed additional properties.
5. Optionally format only under `generated/` with Ruff (generated-only; never hand-tune).
6. Smoke-import generated package; fail the script on import errors.
7. Emit a short generation report (path count, generator version, timestamp).

Additional properties (illustrative; finalize when generation lands):

- `packageName=mailermine_generated` (internal name; not the public PyPI name)
- `projectName=mailermine-generated`
- `library=urllib3`
- Disable publishing the generated package as its own distribution

### Hard rules

- Never edit files under `generated/`.
- Never copy endpoint strings into `mailermine/resources/*`.
- Never redefine schemas already present in OpenAPI; map/adapt only.
- If the generator is wrong, fix via spec + regenerate, or adapt in the wrapper — not by patching generated sources.

### Commit policy for `generated/`

**Commit generated output** (same as Laravel/PHP and Node SDKs):

- Consumers and CI do not need Java/OpenAPI Generator to install or test.
- Diffs make API drift visible in PRs.
- Releases are reproducible without a network fetch of the generator.

Regeneration is a deliberate PR, not a silent install step.

---

## 10. Wrapper strategy

### Pattern

Each resource:

1. Subclasses `BaseResource`.
2. Receives only the generated API client(s) it needs (via an internal factory, mirroring Node `createInternalApis`).
3. Exposes snake_case methods aligned with Laravel/Node method names (`send`, `list`, `create`, `get`, `update`, `delete`, …).
4. Accepts plain dicts / TypedDicts / dataclasses as inputs — never generated model constructors in public signatures.
5. Uses `execute()` to invoke generated calls and map errors.
6. Returns `Response` / `Collection` / primitives.

### Internal (non-public) modules

Allowed under `mailermine/` for glue (not exported from `__init__.py`):

- `_generated_client.py` / `internal/` — wire `Configuration` → generated `Configuration` + API instances
- `_error_mapper.py` — generated exceptions → public exceptions
- `_serialization.py` — model → dict, camelCase/snake_case normalization if required

Prefer a private `mailermine/_internal/` package if the glue grows; keep resources free of generator imports where practical by injecting already-constructed API objects.

### Typing

- Public APIs are fully typed (`list[str]`, `Mapping[str, str]`, `TypedDict`, generics on `Response[T]` / `Collection[T]`).
- `Any` only at the generated boundary, immediately narrowed.
- Enable `mypy` strict (or near-strict) on `mailermine/`; generated code may use a looser override.

### Async

**v1 is sync-only**, matching Laravel and Node’s primary surface. An async client (`AsyncMailerMine`) is a future major/minor addition, not part of the initial architecture commitment.

---

## 11. Dependency choices

### Runtime

| Dependency | Role |
| --- | --- |
| `urllib3` | Transport used by the generated `python` client |
| `pydantic` (version required by the pinned generator) | Generated model validation/serialization |
| `python-dateutil` | Common OpenAPI Generator Python dependency for dates |
| `typing-extensions` | Backports if needed for 3.10 |

No hard dependency on `requests` or `httpx` in v1 unless generation options change. Test doubles inject at the generated/HTTP layer rather than requiring a second HTTP stack.

### Development / tooling

| Tool | Role |
| --- | --- |
| `hatchling` | PEP 517 build backend |
| `pytest` + `pytest-cov` | Tests |
| `respx` or urllib3/httpx mock helpers | HTTP mocking (choose based on final transport hooks) |
| `ruff` | Lint + format (PEP 8, isort, pyupgrade) |
| `mypy` | Static typing |
| `openapi-generator-cli` (via pinned JAR in script) | Codegen (dev/CI only) |

### Packaging name

| Field | Value |
| --- | --- |
| PyPI name | `mailermine` |
| Import package | `mailermine` |
| Python | `>=3.10` |
| License | MIT |

Supports install via:

```bash
pip install mailermine
poetry add mailermine
uv add mailermine
```

All three read `pyproject.toml`; no setup.py required.

---

## 12. Build and packaging configuration

`pyproject.toml` is the single config root:

- `[project]` — metadata, dependencies, requires-python
- `[build-system]` — `hatchling`
- `[tool.hatch.build.targets.wheel]` — include `mailermine/` **and** `generated/` (or `mailermine_generated` package path as emitted)
- `[tool.ruff]` / `[tool.mypy]` / `[tool.pytest.ini_options]` — quality gates

Wheel contents:

- Public package `mailermine`
- Generated package (internal)
- `py.typed` marker for PEP 561

Exclude from wheels: `tests/`, `examples/`, `scripts/`, `ARCHITECTURE.md`, local `openapi.json` (optional: ship spec only if needed for debugging — default **exclude**).

---

## 13. Versioning strategy

| Version | Meaning |
| --- | --- |
| SDK SemVer (`mailermine` package version) | Public Python API stability |
| OpenAPI `info.version` | Upstream API document version (tracked in generation reports, not necessarily equal to SDK version) |

Rules:

- **MAJOR** — breaking changes to `MailerMine`, resources, exceptions, or response shapes.
- **MINOR** — new endpoints/methods/resources, non-breaking additions.
- **PATCH** — bugfixes, dependency bumps, generation refresh without public API breaks.

Align major.minor with sibling SDKs when releasing a coordinated multi-language drop when practical; patch levels may diverge.

`mailermine.VERSION` is the single runtime constant used in `User-Agent`.

Keep a `CHANGELOG.md` (Keep a Changelog) starting when the first implementable release ships.

---

## 14. Testing strategy

### Layers

| Layer | What | Where |
| --- | --- | --- |
| Unit | Configuration validation, exception mapping, Response/Collection/Pagination, serialization | `tests/unit/` |
| Resource | Each resource method with mocked HTTP / injected generated client | `tests/resources/` |
| Contract / parity | Method presence vs Node/Laravel resource surface | `tests/parity/` |
| Smoke | Optional live API tests behind env flag | `tests/integration/` (skipped by default) |

### Rules

- No network in default CI.
- Assert that importing `mailermine` does not require callers to import `generated`.
- Assert public `__all__` never includes generated symbols.
- Prefer fixture JSON shaped like real API envelopes from OpenAPI examples.

### Quality commands (target)

```bash
ruff check .
ruff format --check .
mypy mailermine
pytest
```

Unified: `hatch run check` or `make check` once tooling is wired.

---

## 15. Release strategy

1. Regenerate from OpenAPI when the API changes; open a dedicated PR.
2. Implement/adjust wrappers; keep parity tests green.
3. Bump version in `pyproject.toml` + `mailermine` version constant + `CHANGELOG.md`.
4. Tag `vX.Y.Z`.
5. CI builds sdist + wheel; publish to PyPI with Trusted Publishing (OIDC) preferred over long-lived tokens.
6. GitHub Release notes from changelog excerpt.
7. Verify install: `pip install mailermine==X.Y.Z` and a minimal `MailerMine` import smoke test.

Pre-1.0 (`0.x`) may move faster; once `@mailermine/node` and Laravel are at `1.x`, Python should join `1.0.0` with matching resource coverage before declaring GA.

---

## 16. Project standards

| Standard | Choice |
| --- | --- |
| Style | PEP 8 via Ruff |
| Types | Full annotations; `py.typed` |
| Docstrings | Google style on public classes/methods |
| Line length | 100 (Ruff) |
| Imports | Absolute `mailermine.*`; no wildcard imports in public modules |
| Mutability | Prefer frozen config / read-only response objects |
| Secrets | Never log API keys; redact in error sanitization |
| Editor | `.editorconfig` (UTF-8, LF, trim) aligned with Node/Laravel |

---

## 17. Phased delivery (after this document)

| Phase | Scope |
| --- | --- |
| **1 (this)** | Architecture, layout, `pyproject.toml`, standards — **no resources** |
| **2** | OpenAPI generation into `generated/` + generation script |
| **3** | `Configuration`, exception mapper, Response/Collection/Pagination, `MailerMine` shell |
| **4** | Implement 18 resources behind the wrapper |
| **5** | Examples, README, parity tests, release tooling |
| **6** | PyPI GA aligned with sibling SDKs |

---

## 18. Decision log (why these choices)

1. **OpenAPI Generator `python` over hand-written HTTP** — Matches Laravel/Node “generate + wrap” model; prevents endpoint drift.
2. **Handwritten resources over exposing generated APIs** — Stripe/Resend DX; stable names when generator output churns.
3. **`MailerMine` attributes + snake_case** — Pythonic; same resource set as siblings.
4. **`MailerMineError` root above `ApiError`** — Python callers can catch one base type; still keeps `ApiError` parity with Node naming.
5. **Commit `generated/`** — Install/test without Java; reviewable API diffs.
6. **Production default base URL, not OpenAPI servers** — Spec’s localhost server must not ship as the SDK default.
7. **Sync-only v1** — Parity and simplicity; async later.
8. **hatchling + pyproject-only** — Modern, works with pip/poetry/uv without legacy setup.py.
9. **urllib3 via generator** — One HTTP stack; injectability for tests without forcing httpx on all users.
10. **No resource code in Phase 1** — Architecture freezes before implementation prevents thrash across 18 modules.

---

## 19. Explicit Phase 1 deliverables checklist

- [x] Folder structure under `mailermine/`, `generated/`, `tests/`, `examples/`, `scripts/`
- [x] `pyproject.toml` (package + build + tool configuration)
- [x] Architecture, dependency, generation, wrapper, versioning, testing, and release strategies documented herein
- [ ] Resource method implementations — **deferred**
- [ ] OpenAPI generation — **deferred**
- [ ] Public client runtime behavior — **deferred**
