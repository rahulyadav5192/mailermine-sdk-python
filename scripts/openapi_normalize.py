"""Normalize MailerMine OpenAPI schemas before Python code generation.

The published OpenAPI document incorrectly models many PHP associative arrays
(``array<string, mixed>``, ``array{...}``) as JSON Schema ``type: array`` with
empty ``items``. OpenAPI Generator then emits ``List[Any]``, and Pydantic rejects
the real JSON objects returned by the live API.

Additionally, PHP ``json_encode``s empty associative arrays as ``[]`` rather than
``{}``, so free-form object fields must also accept an empty JSON array.

Node/Laravel SDKs tolerate the same broken schemas because they do not strictly
validate response shapes. Python must correct the schemas at generation time.

This module never talks to the MailerMine backend and never hand-edits generated
Python models — it only rewrites the local OpenAPI document used as generator input.
"""

from __future__ import annotations

import copy
import re
from typing import Any

# Field names that are JSON objects in live API responses even when OpenAPI says array.
_OBJECT_FIELD_NAMES = frozenset(
    {
        "branding",
        "counters",
        "custom_fields",
        "filters",
        "headers",
        "metadata",
        "payload",
        "project",
        "rules",
        "settings",
        "usage",
        "dns_summary",
        "mail_from",
        "contact",
        "message",
        "template",
        "segment",
        "dmarc_recommendation",
    }
)

# Fields that are true string lists when items are empty in the spec.
_STRING_LIST_FIELD_NAMES = frozenset(
    {
        "bcc",
        "cc",
        "errors",
        "to_emails",
        "warnings",
    }
)

# Campaign counter fields that the API may return as null on create/duplicate.
_NULLABLE_INT_FIELD_NAMES = frozenset(
    {
        "completed_count",
        "estimated_recipients",
        "failed_count",
        "queued_count",
        "sending_count",
        "sent_count",
        "total_recipients",
    }
)

_VAR_ASSOC = re.compile(
    r"@var\s+array(?:<string\s*,\s*mixed>|\{)",
    re.IGNORECASE,
)
_VAR_LIST_STRING = re.compile(r"@var\s+list<\s*string\s*>", re.IGNORECASE)
_VAR_LIST_OBJECT = re.compile(r"@var\s+list<\s*(?:array|mixed)", re.IGNORECASE)
_VAR_NULLABLE = re.compile(r"\|null", re.IGNORECASE)


def normalize_openapi_document(document: dict[str, Any]) -> dict[str, Any]:
    """Return a deep-copied OpenAPI document with Python-safe schema fixes.

    Parameters
    ----------
    document:
        Parsed OpenAPI 3.x document.

    Returns
    -------
    dict[str, Any]
        Normalized document ready for OpenAPI Generator.
    """
    normalized = copy.deepcopy(document)
    components = normalized.setdefault("components", {})
    schemas = components.setdefault("schemas", {})
    for schema in schemas.values():
        if isinstance(schema, dict):
            _normalize_schema(schema)

    _apply_known_schema_fixes(schemas)
    _plain_free_form_objects_in_request_bodies(normalized)
    _fix_import_upload_multipart(normalized)
    _add_campaign_recipients_per_page(normalized)
    return normalized


def _request_body_schema_names(document: dict[str, Any]) -> set[str]:
    """Names of component schemas used as JSON request bodies."""
    names: set[str] = set()
    for path_item in (document.get("paths") or {}).values():
        if not isinstance(path_item, dict):
            continue
        for operation in path_item.values():
            if not isinstance(operation, dict):
                continue
            content = (operation.get("requestBody") or {}).get("content") or {}
            if not isinstance(content, dict):
                continue
            for media in content.values():
                ref = ((media or {}).get("schema") or {}).get("$ref")
                if isinstance(ref, str) and ref.startswith("#/components/schemas/"):
                    names.add(ref.rsplit("/", 1)[-1])
    return names


def _is_free_form_any_of(prop: dict[str, Any]) -> bool:
    """True for the ``_object_schema`` shape: object | empty array [| null]."""
    variants = prop.get("anyOf")
    if not isinstance(variants, list):
        return False
    kinds = {v.get("type") for v in variants if isinstance(v, dict)}
    has_free_object = any(
        isinstance(v, dict) and v.get("type") == "object" and v.get("additionalProperties") is True
        for v in variants
    )
    return has_free_object and kinds <= {"object", "array", "null"}


def _plain_free_form_objects_in_request_bodies(document: dict[str, Any]) -> None:
    """Use plain ``object`` maps (not anyOf wrappers) for request-body fields.

    The empty-array (``[]``) variant only matters for responses (PHP encodes
    empty maps as ``[]``). On requests, the generated ``@validate_call`` runs
    pydantic ``model_validate`` on the anyOf wrapper, which turns a plain dict
    into ``None``: ``metadata``, ``headers``, ``variables`` and project
    ``settings`` were silently dropped. A plain ``Dict[str, Any]`` keeps them.
    """
    schemas = (document.get("components") or {}).get("schemas") or {}
    for name in _request_body_schema_names(document):
        schema = schemas.get(name)
        props = schema.get("properties") if isinstance(schema, dict) else None
        if not isinstance(props, dict):
            continue
        for field_name, prop in list(props.items()):
            if not isinstance(prop, dict) or not _is_free_form_any_of(prop):
                continue
            nullable = any(isinstance(v, dict) and v.get("type") == "null" for v in prop["anyOf"])
            plain: dict[str, Any] = {
                "type": ["object", "null"] if nullable else "object",
                "additionalProperties": True,
            }
            if prop.get("description"):
                plain["description"] = prop["description"]
            props[field_name] = plain


def _normalize_schema(schema: dict[str, Any]) -> None:
    props = schema.get("properties")
    if isinstance(props, dict):
        for name, prop in list(props.items()):
            if isinstance(prop, dict):
                props[name] = _normalize_property(name, prop)

    if schema.get("additionalProperties") == {}:
        schema["additionalProperties"] = True

    for key in ("allOf", "oneOf", "anyOf"):
        items = schema.get(key)
        if isinstance(items, list):
            for item in items:
                if isinstance(item, dict):
                    _normalize_schema(item)

    if isinstance(schema.get("items"), dict):
        _normalize_schema(schema["items"])


def _normalize_property(name: str, prop: dict[str, Any]) -> dict[str, Any]:
    prop = copy.deepcopy(prop)
    description = str(prop.get("description") or "")
    types = prop.get("type")
    type_list = types if isinstance(types, list) else ([types] if types else [])
    nullable = (
        "null" in type_list or bool(prop.get("nullable")) or bool(_VAR_NULLABLE.search(description))
    )
    is_array = "array" in type_list or types == "array"
    is_object = "object" in type_list or types == "object"
    items = prop.get("items")
    empty_items = isinstance(items, dict) and items == {}
    has_structured_props = isinstance(prop.get("properties"), dict) and bool(prop.get("properties"))

    # Free-form object (no nested properties) — accept PHP empty-array encoding.
    if is_object and not has_structured_props and "anyOf" not in prop:
        if prop.get("additionalProperties") == {}:
            prop["additionalProperties"] = True
        return _object_schema(description=description, nullable=nullable)

    # Required arrays that the API returns as null on list endpoints.
    if name == "dns_records" and is_array:
        prop["type"] = ["array", "null"]
        prop["nullable"] = True
        if not isinstance(prop.get("items"), dict) or prop.get("items") == {}:
            prop["items"] = {"type": "object", "additionalProperties": True}
        return prop

    if is_array and empty_items:
        # Prefer explicit list annotations before map/object heuristics.
        if _VAR_LIST_STRING.search(description) or name in _STRING_LIST_FIELD_NAMES:
            return _string_array(description=description, nullable=nullable)
        if _VAR_LIST_OBJECT.search(description) or name == "sample_contacts":
            return _object_array(description=description, nullable=nullable)
        if name == "tags":
            # Contact tags are objects; Message/TimelineEvent tags are strings.
            if "array{" in description or "list<array" in description.lower():
                return _object_array(description=description, nullable=nullable)
            return _string_array(description=description, nullable=nullable)
        if name in {"timeline", "lists"}:
            return _object_array(description=description, nullable=nullable)
        if (
            _VAR_ASSOC.search(description)
            or _looks_like_assoc_object(description)
            or name in _OBJECT_FIELD_NAMES
        ):
            return _object_schema(description=description, nullable=nullable)
        # Unknown empty-items arrays: prefer free-form object maps (common PHP mistype).
        return _object_schema(description=description, nullable=nullable)

    # Nullable array unions already carrying structured items.
    if is_array and nullable and isinstance(items, dict) and items:
        prop["type"] = ["array", "null"]
        prop["nullable"] = True

    # Integer counters the API returns as null on some write responses.
    if name in _NULLABLE_INT_FIELD_NAMES and ("integer" in type_list or types == "integer"):
        prop["type"] = ["integer", "null"]
        prop["nullable"] = True
        return prop

    return prop


def _apply_known_schema_fixes(schemas: dict[str, Any]) -> None:
    """Apply field-specific fixes discovered against the live production API."""
    # Template list responses return variables: null while the field is required.
    template = schemas.get("TemplateResource")
    if isinstance(template, dict):
        props = template.get("properties")
        if isinstance(props, dict) and isinstance(props.get("variables"), dict):
            variables = copy.deepcopy(props["variables"])
            variables["type"] = ["array", "null"]
            variables["nullable"] = True
            props["variables"] = variables

    # ImportJob.summary is documented as string|null but the API returns an object.
    for schema_name in ("ImportJob", "ImportJobDetail", "ImportProgress"):
        job = schemas.get(schema_name)
        if not isinstance(job, dict):
            continue
        props = job.get("properties")
        if not isinstance(props, dict) or not isinstance(props.get("summary"), dict):
            continue
        description = str(props["summary"].get("description") or "")
        props["summary"] = {
            "description": description or "Import summary payload (string or structured object).",
            "nullable": True,
            "anyOf": [
                {"type": "string"},
                {"type": "object", "additionalProperties": True},
                {"type": "null"},
            ],
        }

    # Partial segment updates omit rules (Node/Laravel accept name-only patches).
    update_segment = schemas.get("UpdateSegmentRequest")
    if isinstance(update_segment, dict):
        required = update_segment.get("required")
        if isinstance(required, list) and "rules" in required:
            update_segment["required"] = [item for item in required if item != "rules"]

    # Timeline events omit id/metadata/tags/payload on some delivery-log shapes.
    timeline = schemas.get("TimelineEvent")
    if isinstance(timeline, dict):
        props = timeline.get("properties")
        if isinstance(props, dict):
            for field_name in ("id", "payload", "metadata", "tags", "message_id", "recipient"):
                field = props.get(field_name)
                if not isinstance(field, dict):
                    continue
                props[field_name] = _make_nullable(field)

    # Project ``settings`` documents an optional ``tracking`` object but stays an
    # open map (environment, timezone, default_sender, custom keys). Typed as a
    # model, ``@validate_call`` would drop the undeclared keys, so keep the same
    # free-form dict the SDK used before ``tracking`` was documented.
    for schema_name in ("CreateProjectRequest", "UpdateProjectRequest"):
        project_request = schemas.get(schema_name)
        if not isinstance(project_request, dict):
            continue
        props = project_request.get("properties")
        if isinstance(props, dict) and isinstance(props.get("settings"), dict):
            props["settings"] = _object_schema(
                description=str(props["settings"].get("description") or "Project settings."),
                nullable=False,
            )

    # ConfigureContactImportRequest.field_mappings is documented as string[] but the
    # live API (and Laravel/Node SDKs) accept a column→field object map.
    # Use a plain object schema (not anyOf): OpenAPI Generator anyOf wrappers fail
    # under pydantic ``model_validate`` used by ``@validate_call`` on requests.
    configure = schemas.get("ConfigureContactImportRequest")
    if isinstance(configure, dict):
        props = configure.get("properties")
        if isinstance(props, dict) and isinstance(props.get("field_mappings"), dict):
            description = str(props["field_mappings"].get("description") or "")
            props["field_mappings"] = {
                "type": "object",
                "additionalProperties": {"type": "string"},
                "description": description
                or "Map of CSV column names to MailerMine contact fields.",
                "minProperties": 1,
            }


def _make_nullable(prop: dict[str, Any]) -> dict[str, Any]:
    """Return a copy of ``prop`` that also accepts JSON null."""
    prop = copy.deepcopy(prop)
    prop["nullable"] = True
    if "anyOf" in prop:
        variants = prop["anyOf"]
        if isinstance(variants, list) and not any(
            isinstance(item, dict) and item.get("type") == "null" for item in variants
        ):
            variants.append({"type": "null"})
        return prop
    types = prop.get("type")
    if isinstance(types, list):
        if "null" not in types:
            prop["type"] = [*types, "null"]
    elif isinstance(types, str):
        prop["type"] = [types, "null"]
    else:
        prop["type"] = ["object", "null"]
        prop.setdefault("additionalProperties", True)
    return prop


def _looks_like_assoc_object(description: str) -> bool:
    lower = description.lower()
    # Avoid matching "list relationships" / "loaded relationships" list payloads.
    if "list<" in lower or "relationships" in lower:
        return False
    return any(
        token in lower
        for token in (
            "key-value",
            "keyed by",
            "metadata",
            "settings object",
            "summary",
            "counters",
            "configuration",
            "provider-specific payload",
        )
    )


def _object_schema(*, description: str, nullable: bool) -> dict[str, Any]:
    """Free-form object that also accepts PHP's empty-array encoding (``[]``)."""
    variants: list[dict[str, Any]] = [
        {"type": "object", "additionalProperties": True},
        {"type": "array", "maxItems": 0},
    ]
    if nullable:
        variants.append({"type": "null"})
    schema: dict[str, Any] = {"anyOf": variants}
    if description:
        schema["description"] = description
    if nullable:
        schema["nullable"] = True
    return schema


def _string_array(*, description: str, nullable: bool) -> dict[str, Any]:
    schema: dict[str, Any] = {
        "type": ["array", "null"] if nullable else "array",
        "items": {"type": "string"},
    }
    if description:
        schema["description"] = description
    if nullable:
        schema["nullable"] = True
    return schema


def _object_array(*, description: str, nullable: bool) -> dict[str, Any]:
    schema: dict[str, Any] = {
        "type": ["array", "null"] if nullable else "array",
        "items": {"type": "object", "additionalProperties": True},
    }
    if description:
        schema["description"] = description
    if nullable:
        schema["nullable"] = True
    return schema


def _fix_import_upload_multipart(document: dict[str, Any]) -> None:
    paths = document.get("paths")
    if not isinstance(paths, dict):
        return
    operation = (paths.get("/contacts/import") or {}).get("post")
    if not isinstance(operation, dict):
        return
    request_body = operation.get("requestBody")
    if not isinstance(request_body, dict):
        return
    content = request_body.get("content")
    if not isinstance(content, dict):
        return
    json_body = content.get("application/json")
    if not isinstance(json_body, dict):
        return
    # Replace JSON binary upload with multipart/form-data (Node SDK behaviour).
    content.clear()
    content["multipart/form-data"] = copy.deepcopy(json_body)


def _add_campaign_recipients_per_page(document: dict[str, Any]) -> None:
    """Expose ``per_page`` on campaign recipients (parity with other list endpoints)."""
    paths = document.get("paths")
    if not isinstance(paths, dict):
        return
    operation = (paths.get("/campaigns/{campaign}/recipients") or {}).get("get")
    if not isinstance(operation, dict):
        return
    parameters = operation.setdefault("parameters", [])
    if not isinstance(parameters, list):
        return
    if any(isinstance(p, dict) and p.get("name") == "per_page" for p in parameters):
        return
    parameters.append(
        {
            "name": "per_page",
            "in": "query",
            "required": False,
            "schema": {"type": "integer", "minimum": 1, "maximum": 100},
            "description": "Number of recipients per page.",
        }
    )
