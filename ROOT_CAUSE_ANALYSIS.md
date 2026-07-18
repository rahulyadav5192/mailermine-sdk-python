# MailerMine Python SDK — Root Cause Analysis

**Phase:** Production QA root-cause fix (OpenAPI → Python generation)  
**Date:** 2026-07-19  
**Result:** Production QA **193 passed / 0 failed / 20 skipped** (was ~75 passed / 46 failed)

---

## Executive verdict

The failures were **not** backend bugs, wrapper bugs, or test bugs.

They came from **incorrect OpenAPI schemas** (PHP associative arrays published as JSON Schema `type: array` with empty `items: {}`), which OpenAPI Generator **correctly** turned into `List[Any]`. Pydantic then rejected live JSON **objects** (and PHP’s empty-array encoding `[]` for empty maps).

Node and Laravel pass because they do **not** strictly validate response shapes the same way.

**Fix location:** generation pipeline only — `scripts/openapi_normalize.py` + `scripts/generate.py`, then regenerate. No hand-edits to models. No QA or backend changes.

---

## Generator audit

| Item | Value |
| --- | --- |
| Generator | OpenAPI Generator **7.23.0** |
| Generator name | `python` |
| Library | `urllib3` |
| JAR SHA-256 | `cb087e40001e31eb08ef6140dd5de10938dbeb89016a1fe0481eaa25cd569026` |
| Spec source | `https://www.mailermine.com/openapi.json` (pinned as `openapi.json`) |
| Normalized input | `openapi.normalized.json` (written by `scripts/generate.py`) |
| Package | `generated/mailermine_generated` |
| Templates | Upstream defaults (no custom Mustache templates) |
| Options | `packageName=mailermine_generated`, `library=urllib3`, `disallowAdditionalPropertiesIfNotPresent=false`, `hideGenerationTimestamp=true` |

**Why `object` became `List[Any]`:**  
For `type: array` + `items: {}`, the Python generator emits `List[Any]`. That is correct relative to the published schema — the schema was wrong relative to the live API and PHPDoc (`@var array<string, mixed>`, `@var array{...}`).

---

## OpenAPI → Generated → Expected (representative)

| Field | OpenAPI (raw) | Generated (before) | Expected / after |
| --- | --- | --- | --- |
| `ProjectResource.settings` | `array` + `items: {}` | `List[Any]` | free-form object (`Dict` / anyOf object&#124;empty-array) |
| `TemplateResource.branding` | `array&#124;null` + empty items | `Optional[List[Any]]` | optional free-form object |
| `TemplateResource.metadata` | `array&#124;null` + empty items | `Optional[List[Any]]` | optional free-form object |
| `TemplateResource.project` | `array&#124;null` + empty items | `Optional[List[Any]]` | optional free-form object |
| `TemplateResource.usage` | `array&#124;null` + empty items | `Optional[List[Any]]` | optional free-form object |
| `TemplateResource.tags` | `array` + empty items (`list<string>`) | `List[Any]` | `List[str]` |
| `TemplateResource.variables` | required `array[TemplateVariable]` | `List[...]` (rejected `null`) | `Optional[List[...]]` |
| `ContactResource.metadata` | `array` + empty items | `List[Any]` | free-form object (+ PHP `[]`) |
| `ContactResource.custom_fields` | `array` + empty items | `List[Any]` | free-form object (+ PHP `[]`) |
| `ContactResource.tags` | `array` + empty items (`list<array{…}>`) | `List[Any]` | `List[Dict[str, Any]]` |
| `ContactResource.lists` | `array` + empty items | `List[Any]` | `List[Dict[str, Any]]` |
| `CampaignResource.project` | `array&#124;null` + empty items | `Optional[List[Any]]` | optional free-form object |
| `CampaignResource.*_count` | required `integer` | `int` (rejected `null`) | `Optional[int]` |
| `SegmentResource.rules` | `array` + empty items | `List[Any]` | free-form object |
| `TimelineEvent.payload` | `array` + empty items | `List[Any]` | nullable free-form object |
| `TimelineEvent.metadata` | `array` + empty items | `List[Any]` | nullable free-form object |
| `TimelineEvent.tags` / `id` | required non-null | non-optional | nullable (delivery-log shapes) |
| `ExportJob.filters` | `array` + empty items | `List[Any]` | free-form object |
| `ImportJob.metadata` / `counters` | `array` + empty items | `List[Any]` | free-form object |
| `ImportJob` / `ImportProgress.summary` | `string&#124;null` | `Optional[str]` | `string &#124; object &#124; null` |
| `Suppression.metadata` | `object` + `additionalProperties: {}` | strict empty map | `additionalProperties: true` (+ PHP `[]`) |
| `DomainResource.dns_records` | required `array[DNSRecord]` | `List[DNSRecord]` (rejected `null`) | `Optional[List[DNSRecord]]` |
| `Message.headers` / `metadata` | `array` + empty items | `List[Any]` | free-form object (+ PHP `[]`) |
| `ConfigureContactImportRequest.field_mappings` | `array[string]` | `List[str]` | `Dict[str, str]` (live + Laravel/Node) |
| `UpdateSegmentRequest.rules` | **required** | required | optional (partial updates) |
| `POST /contacts/import` content-type | `application/json` + binary | JSON body → `bytes` not serializable | `multipart/form-data` |
| `GET …/recipients` | no `per_page` | `@validate_call` rejects kwargs | `per_page` query param added |

**Empty-items arrays in raw OpenAPI:** **47**  
**After normalization:** **0**

---

## Classification of root causes

### 1. OpenAPI schema bugs (primary)

PHP `array<string, mixed>` / shaped `array{…}` documented as JSON Schema arrays with empty `items`. Live JSON is objects (or `[]` for empty maps).

Also:

- Required fields that the API returns as `null` (`dns_records`, template `variables`, campaign counts, timeline fields).
- `Import* .summary` typed as string but returned as objects.
- `field_mappings` typed as `string[]` but accepted/sent as maps by Laravel/Node/QA.
- Import upload declared as `application/json` instead of multipart.

### 2. Generator behaviour (correct relative to bad schemas)

OpenAPI Generator 7.23.0 `python` + Pydantic v2 faithfully implements the schemas. Not a generator bug for `List[Any]`.

**Caveat discovered:** `anyOf` wrappers work on **response** `from_dict` paths, but **request** `@validate_call` / `model_validate` can leave anyOf `actual_instance=None` (seen on `field_mappings`). Request bodies that must be objects are normalized as plain `type: object`, not `anyOf`.

### 3. SDK wrapper (secondary, fixed)

| Issue | Fix |
| --- | --- |
| Pydantic deserialize failures mapped to public `ValidationError` | Map to `ApiError` (HTTP 422 only → `ValidationError`) |
| Missing `ApiError.message` (Node `Error.message` parity) | `@property message` on `ApiError` |
| `imports.create` used JSON request model | After multipart regen, pass `file=(filename, bytes)` |
| Campaign `recipients(..., per_page=)` | Spec normalized to include `per_page` |

### 4. Not responsible

- MailerMine backend behaviour for these fields (Laravel/Node already green).
- QA project assertions (unchanged).
- Hand-edited generated models (none).

---

## Fix applied

### Pipeline

1. Download/pin `openapi.json`.
2. **`scripts/openapi_normalize.py`** rewrites schemas for Python safety.
3. Write `openapi.normalized.json`.
4. Generate with OpenAPI Generator 7.23.0 → `generated/`.
5. Rebuild wheel; no manual model edits.

### Normalization rules (summary)

- Empty-items arrays + `@var array<string, mixed>|array{…}` / known map names → free-form object **anyOf** `{object, empty-array[, null]}` (PHP `[]` for empty maps).
- `@var list<string>` / known string lists → `array` of `string`.
- `@var list<array…>` / `tags` objects / `lists` / `timeline` → `array` of objects.
- Free-form `object` + `additionalProperties: {}` → `additionalProperties: true` + PHP empty-array anyOf.
- Known nullability fixes (`dns_records`, `variables`, campaign counts, `TimelineEvent` fields).
- `ImportJob` / `ImportJobDetail` / `ImportProgress.summary` → string&#124;object&#124;null.
- `ConfigureContactImportRequest.field_mappings` → `object` map of strings.
- `UpdateSegmentRequest.required` drops `rules`.
- Import upload → `multipart/form-data`.
- Campaign recipients → add `per_page` query parameter.

### Exception / wrapper files

- `mailermine/exceptions/__init__.py` — `.message`; Pydantic → `ApiError`; `ApiValueError` → `ValidationError`.
- `mailermine/resources/imports.py` — multipart `file=` API.

---

## Files changed

| Path | Role |
| --- | --- |
| `scripts/openapi_normalize.py` | **New** — OpenAPI normalization |
| `scripts/generate.py` | Normalize step; generate from normalized spec |
| `openapi.normalized.json` | Generated normalized spec (committed artifact of generate) |
| `generated/**` | Fully regenerated (~200 model modules) |
| `mailermine/exceptions/__init__.py` | Error mapping + `.message` |
| `mailermine/resources/imports.py` | Multipart create |
| `tests/test_wrapper.py` | Coverage for mapping / `.message` |
| `GENERATION_REPORT.md` | Regenerated inventory |
| `ROOT_CAUSE_ANALYSIS.md` | This document |

**Not modified:** MailerMine backend, QA project (`mailermine-python-test` sources), handwritten resource method surface beyond imports/exceptions.

**Regenerated models:** **200** model modules under `generated/mailermine_generated/models/` (was ~197 before anyOf helpers; no hand edits).

---

## Before vs after (production QA)

| Metric | Before | After |
| --- | --- | --- |
| Passed | ~75 | **193** |
| Failed | ~46 | **0** |
| Skipped | ~92 | **20** (plan gates / opt-in sends) |
| Dominant failure | `List[Any]` vs JSON object / Pydantic as `ValidationError` | — |
| `imports.create(bytes)` | `Object of type bytes is not JSON serializable` | multipart upload |
| Deserialization failure type | public `ValidationError` | `ApiError` |
| `err.message` | missing | present |

Skipped items are plan quotas (multi-domain, webhooks, attachments) or `MAILERMINE_SEND_CAMPAIGN` opt-in — **Plan limitation**, not SDK defects.

---

## Remaining failures

**None** in the latest production QA run (`193 / 0 / 20`).

---

## Comparison with Node SDK

| Area | Node | Python (after fix) |
| --- | --- | --- |
| Same raw OpenAPI mistypes | Generated `Array<any>` exists | Normalized before generate |
| Runtime validation | Loose (fetch JSON) | Strict Pydantic — must match reality |
| Import upload | FormData + strip Content-Type | `multipart/form-data` + `file` param |
| `field_mappings` | `JsonObject &#124; string[]` in handwritten types | `Dict[str, str]` via normalized schema |
| Errors | `Error.message` | `ApiError.message` property |
| HTTP 422 | `ValidationError` | `ValidationError` |
| Deserialize failure | typically `ApiError` | `ApiError` (was wrongly `ValidationError`) |

---

## How to regenerate

```bash
python scripts/generate.py          # download + normalize + generate
# or
python scripts/generate.py --skip-download
python -m build --wheel
```

Never edit `generated/` by hand. Extend `scripts/openapi_normalize.py` when new schema mismatches appear.

---

## Evidence standard

Every conclusion above was verified against:

1. Published `openapi.json` property types and PHPDoc `@var` lines.
2. Generated Pydantic field annotations before/after regeneration.
3. Live production QA in `mailermine-python-test` against wheel installs.
4. Node/Laravel SDK behaviour for multipart imports, `field_mappings`, and error shapes.
