#!/usr/bin/env python3
"""Download the MailerMine OpenAPI spec and regenerate ``generated/``.

Never hand-edit files under ``generated/``. Fix issues via this script's
generator configuration, then regenerate.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import shutil
import subprocess
import sys
import tempfile
import time
import urllib.request
from pathlib import Path
from typing import Any

OPENAPI_URL = "https://www.mailermine.com/openapi.json"
GENERATOR_VERSION = "7.23.0"
GENERATOR_NAME = "python"
GENERATOR_SHA256 = "cb087e40001e31eb08ef6140dd5de10938dbeb89016a1fe0481eaa25cd569026"
GENERATOR_URL = (
    "https://repo.maven.apache.org/maven2/org/openapitools/openapi-generator-cli/"
    f"{GENERATOR_VERSION}/openapi-generator-cli-{GENERATOR_VERSION}.jar"
)

# Library choice: urllib3 (see GENERATION_REPORT.md for evaluation).
# Note: httpx in OpenAPI Generator 7.23.0 is async-only; supportHttpxSync is not
# available in this release. urllib3 provides production sync DX for the v1 wrapper.
LIBRARY = "urllib3"
PACKAGE_NAME = "mailermine_generated"
PROJECT_NAME = "mailermine-generated"

REPO_ROOT = Path(__file__).resolve().parent.parent
SPEC_PATH = REPO_ROOT / "openapi.json"
NORMALIZED_SPEC_PATH = REPO_ROOT / "openapi.normalized.json"
GENERATED_PATH = REPO_ROOT / "generated"
CACHE_DIR = REPO_ROOT / ".cache" / "openapi-generator"
GENERATOR_JAR = CACHE_DIR / f"openapi-generator-cli-{GENERATOR_VERSION}.jar"
REPORT_PATH = REPO_ROOT / "GENERATION_REPORT.md"

# Allow `python scripts/generate.py` without installing the package.
sys.path.insert(0, str(Path(__file__).resolve().parent))
from openapi_normalize import normalize_openapi_document  # noqa: E402

REQUIRED_RESOURCES = (
    "Projects",
    "Api Keys",
    "Emails",
    "Domains",
    "Templates",
    "Contacts",
    "Lists",
    "Segments",
    "Tags",
    "Audiences",
    "Campaigns",
    "Analytics",
    "Events",
    "Messages",
    "Webhooks",
    "Suppressions",
    "Imports",
    "Exports",
)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--skip-download",
        action="store_true",
        help="Reuse existing openapi.json instead of downloading.",
    )
    parser.add_argument(
        "--skip-report",
        action="store_true",
        help="Skip writing GENERATION_REPORT.md (tests may still inspect output).",
    )
    args = parser.parse_args()

    started = time.perf_counter()
    warnings: list[str] = []

    print_step(1, "Downloading the latest OpenAPI specification")
    if args.skip_download and SPEC_PATH.is_file():
        print(f"  Reusing {SPEC_PATH}")
    else:
        download_specification(SPEC_PATH)

    print_step(2, "Validating the OpenAPI specification")
    specification = load_json(SPEC_PATH)
    validate_specification(specification)
    api_version = str(specification.get("info", {}).get("version", "unknown"))
    spec_version = str(specification.get("openapi") or specification.get("swagger") or "unknown")
    path_count = len(specification.get("paths") or {})
    schema_count = len((specification.get("components") or {}).get("schemas") or {})
    print(
        f"  Validated {specification.get('info', {}).get('title', 'OpenAPI')} "
        f"{api_version} (OpenAPI {spec_version}, {path_count} paths, "
        f"{schema_count} schemas)."
    )

    print_step(3, "Normalizing OpenAPI schemas for Python generation")
    normalized = normalize_openapi_document(specification)
    NORMALIZED_SPEC_PATH.write_text(
        json.dumps(normalized, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )
    print(f"  Wrote {NORMALIZED_SPEC_PATH.relative_to(REPO_ROOT)}")

    print_step(4, "Ensuring OpenAPI Generator JAR")
    assert_java_available()
    ensure_generator_jar()

    print_step(5, f"Clearing {GENERATED_PATH.relative_to(REPO_ROOT)}")
    if GENERATED_PATH.exists():
        shutil.rmtree(GENERATED_PATH)
    GENERATED_PATH.mkdir(parents=True)

    print_step(
        6,
        f"Generating {GENERATOR_NAME}/{LIBRARY} client (OpenAPI Generator {GENERATOR_VERSION})",
    )
    generation_output = run_generator(api_version)
    warnings.extend(extract_warnings(generation_output))

    print_step(7, "Normalizing generated package layout")
    package_root = normalize_generated_layout()
    print(f"  Package root: {package_root.relative_to(REPO_ROOT)}")

    print_step(8, "Smoke-importing generated package")
    smoke_import(package_root)

    elapsed = time.perf_counter() - started
    inventory = build_inventory(specification, package_root)

    if not args.skip_report:
        print_step(9, f"Writing {REPORT_PATH.name}")
        write_report(
            api_version=api_version,
            spec_version=spec_version,
            path_count=path_count,
            schema_count=schema_count,
            elapsed=elapsed,
            warnings=unique(warnings),
            inventory=inventory,
            generation_output=generation_output,
        )
    else:
        print_step(9, "Skipping GENERATION_REPORT.md")

    print("")
    print("  Generation complete.")
    print(f"  Spec version:     {api_version} (OpenAPI {spec_version})")
    print(f"  Generator:        {GENERATOR_VERSION} / {GENERATOR_NAME}")
    print(f"  Library:          {LIBRARY}")
    print(f"  API classes:      {len(inventory['api_classes'])}")
    print(f"  Models:           {len(inventory['models'])}")
    print(f"  Endpoints:        {inventory['endpoint_count']}")
    print(f"  Missing resources:{len(inventory['missing_resources'])}")
    print(f"  Elapsed:          {elapsed:.2f}s")
    return 0 if not inventory["missing_resources"] else 1


def print_step(number: int, message: str) -> None:
    print(f"\n[{number}] {message}")


def download_specification(dest: Path) -> None:
    request = urllib.request.Request(
        OPENAPI_URL,
        headers={
            "Accept": "application/json",
            "Cache-Control": "no-cache",
            "Pragma": "no-cache",
            "User-Agent": "mailermine-python OpenAPI generator",
        },
    )
    with urllib.request.urlopen(request, timeout=60) as response:
        payload = response.read()
    dest.write_bytes(payload)
    print(f"  Wrote {dest} ({len(payload)} bytes)")


def load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def validate_specification(specification: dict[str, Any]) -> None:
    if not isinstance(specification.get("paths"), dict) or not specification["paths"]:
        raise SystemExit("OpenAPI specification has no paths.")
    if not (specification.get("openapi") or specification.get("swagger")):
        raise SystemExit("OpenAPI specification is missing openapi/swagger version.")
    components = specification.get("components")
    if not isinstance(components, dict) or not isinstance(components.get("schemas"), dict):
        raise SystemExit("OpenAPI specification has no component schemas.")


def assert_java_available() -> None:
    try:
        subprocess.run(
            ["java", "-version"],
            check=True,
            capture_output=True,
            text=True,
        )
    except (OSError, subprocess.CalledProcessError) as exc:
        raise SystemExit("Java is required to run OpenAPI Generator. Install a JDK 17+.") from exc


def ensure_generator_jar() -> None:
    CACHE_DIR.mkdir(parents=True, exist_ok=True)
    if GENERATOR_JAR.is_file():
        digest = sha256_file(GENERATOR_JAR)
        if digest == GENERATOR_SHA256:
            print(f"  Using cached {GENERATOR_JAR.name}")
            return
        print("  Cached JAR hash mismatch; re-downloading.")
        GENERATOR_JAR.unlink()

    print(f"  Downloading {GENERATOR_URL}")
    with urllib.request.urlopen(GENERATOR_URL, timeout=120) as response:
        data = response.read()
    digest = hashlib.sha256(data).hexdigest()
    if digest != GENERATOR_SHA256:
        raise SystemExit(
            f"OpenAPI Generator JAR SHA-256 mismatch: expected {GENERATOR_SHA256}, got {digest}"
        )
    GENERATOR_JAR.write_bytes(data)
    print(f"  Verified SHA-256 {digest}")


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def run_generator(api_version: str) -> str:
    # Generate into a temp dir, then move the Python package into generated/.
    with tempfile.TemporaryDirectory(prefix="mailermine-openapi-") as tmp:
        out = Path(tmp) / "out"
        out.mkdir()
        additional = ",".join(
            [
                f"packageName={PACKAGE_NAME}",
                f"projectName={PROJECT_NAME}",
                f"packageVersion={api_version}",
                f"library={LIBRARY}",
                "generateSourceCodeOnly=false",
                "hideGenerationTimestamp=true",
                "disallowAdditionalPropertiesIfNotPresent=false",
            ]
        )
        cmd = [
            "java",
            "-jar",
            str(GENERATOR_JAR),
            "generate",
            "--input-spec",
            str(NORMALIZED_SPEC_PATH),
            "--generator-name",
            GENERATOR_NAME,
            "--output",
            str(out),
            "--additional-properties",
            additional,
            "--skip-validate-spec",
        ]
        result = subprocess.run(cmd, capture_output=True, text=True, check=False)
        output = (result.stdout or "") + (result.stderr or "")
        if result.returncode != 0:
            print(output)
            raise SystemExit(f"OpenAPI Generator failed with exit code {result.returncode}")

        # Move generator output into generated/
        for child in out.iterdir():
            target = GENERATED_PATH / child.name
            if target.exists():
                if target.is_dir():
                    shutil.rmtree(target)
                else:
                    target.unlink()
            shutil.move(str(child), str(target))

        # Keep a marker so humans know not to edit.
        (GENERATED_PATH / "DO_NOT_EDIT").write_text(
            "Generated by scripts/generate.py. Do not edit by hand.\n"
            f"Generator: OpenAPI Generator {GENERATOR_VERSION} / {GENERATOR_NAME}\n"
            f"Library: {LIBRARY}\n"
            f"Spec: {OPENAPI_URL}\n"
            f"Normalized input: {NORMALIZED_SPEC_PATH.name}\n",
            encoding="utf-8",
        )
        return output


def normalize_generated_layout() -> Path:
    """Return the importable package directory under generated/."""
    package_dir = GENERATED_PATH / PACKAGE_NAME
    if package_dir.is_dir() and (package_dir / "__init__.py").is_file():
        return package_dir

    # Some generator layouts nest the package one level deeper.
    candidates = list(GENERATED_PATH.rglob(PACKAGE_NAME))
    for candidate in candidates:
        if candidate.is_dir() and (candidate / "__init__.py").is_file():
            if candidate.parent != GENERATED_PATH:
                # Flatten: move package to generated/<package>
                target = GENERATED_PATH / PACKAGE_NAME
                if target.exists():
                    shutil.rmtree(target)
                shutil.move(str(candidate), str(target))
                return target
            return candidate

    raise SystemExit(f"Could not locate generated package {PACKAGE_NAME!r} under {GENERATED_PATH}")


def smoke_import(package_root: Path) -> None:
    env_pythonpath = str(package_root.parent)
    code = (
        f"import sys; sys.path.insert(0, {env_pythonpath!r}); "
        f"import {PACKAGE_NAME} as pkg; "
        f"from {PACKAGE_NAME} import ApiClient, Configuration; "
        f"print('ok', pkg.__name__, ApiClient.__name__, Configuration.__name__)"
    )
    result = subprocess.run(
        [sys.executable, "-c", code],
        capture_output=True,
        text=True,
        check=False,
        cwd=str(REPO_ROOT),
    )
    if result.returncode != 0:
        print(result.stdout)
        print(result.stderr)
        raise SystemExit("Smoke import of generated package failed.")
    print(f"  {result.stdout.strip()}")


def build_inventory(
    specification: dict[str, Any],
    package_root: Path,
) -> dict[str, Any]:
    api_dir = package_root / "api"
    models_dir = package_root / "models"
    api_modules = sorted(p.stem for p in api_dir.glob("*_api.py") if p.name != "__init__.py")
    api_classes = [snake_to_pascal(name) for name in api_modules]
    models = sorted(
        p.stem
        for p in models_dir.glob("*.py")
        if p.name not in {"__init__.py"} and not p.name.startswith("...")
    )

    tag_names = {
        str(tag.get("name"))
        for tag in specification.get("tags") or []
        if isinstance(tag, dict) and tag.get("name")
    }
    operation_tags: set[str] = set()
    endpoint_rows: list[dict[str, str]] = []

    for path, item in (specification.get("paths") or {}).items():
        if not isinstance(item, dict):
            continue
        for method, operation in item.items():
            if method.startswith("x-") or not isinstance(operation, dict):
                continue
            if method.lower() not in {
                "get",
                "post",
                "put",
                "patch",
                "delete",
                "head",
                "options",
                "trace",
            }:
                continue
            tags = [str(t) for t in (operation.get("tags") or [])]
            operation_tags.update(tags)
            request_model = resolve_request_model(operation)
            response_model = resolve_response_model(operation)
            endpoint_rows.append(
                {
                    "api_class": guess_api_class(tags, api_classes),
                    "endpoint": str(path),
                    "http_method": method.upper(),
                    "operation_id": str(operation.get("operationId") or ""),
                    "request_model": request_model,
                    "response_model": response_model,
                    "tags": ", ".join(tags),
                }
            )

    present_resources, missing_resources = match_resources(api_classes, operation_tags)
    schema_names = sorted((specification.get("components") or {}).get("schemas") or {})

    return {
        "api_classes": api_classes,
        "models": models,
        "schema_names": schema_names,
        "endpoint_rows": endpoint_rows,
        "endpoint_count": len(endpoint_rows),
        "tag_names": sorted(tag_names),
        "operation_tags": sorted(operation_tags),
        "present_resources": present_resources,
        "missing_resources": missing_resources,
        "package_root": str(package_root.relative_to(REPO_ROOT)),
    }


def snake_to_pascal(name: str) -> str:
    """Convert ``api_keys_api`` → ``APIKeysApi`` when possible via known map."""
    known = {
        "api_keys_api": "APIKeysApi",
        "analytics_api": "AnalyticsApi",
        "audiences_api": "AudiencesApi",
        "campaign_analytics_api": "CampaignAnalyticsApi",
        "campaign_events_api": "CampaignEventsApi",
        "campaign_lifecycle_api": "CampaignLifecycleApi",
        "campaigns_api": "CampaignsApi",
        "contacts_api": "ContactsApi",
        "domains_api": "DomainsApi",
        "emails_api": "EmailsApi",
        "events_api": "EventsApi",
        "exports_api": "ExportsApi",
        "imports_api": "ImportsApi",
        "lists_api": "ListsApi",
        "marketing_api": "MarketingApi",
        "messages_api": "MessagesApi",
        "projects_api": "ProjectsApi",
        "segments_api": "SegmentsApi",
        "suppressions_api": "SuppressionsApi",
        "tags_api": "TagsApi",
        "templates_api": "TemplatesApi",
        "webhooks_api": "WebhooksApi",
    }
    if name in known:
        return known[name]
    return "".join(part.capitalize() for part in name.split("_"))


def guess_api_class(tags: list[str], api_classes: list[str]) -> str:
    if not tags:
        return "(untagged)"
    for tag in tags:
        expected = tag_to_api_class(tag)
        for candidate in api_classes:
            if candidate.lower() == expected.lower():
                return candidate
            # API Keys → APIKeysApi (generator capitalizes API)
            if candidate.lower().replace("api", "", 1) == expected.lower().replace("api", "", 1):
                return candidate
    # Prefer first matching class that contains the first tag token
    first = tags[0]
    needle = "".join(ch for ch in first if ch.isalnum()).lower()
    for candidate in api_classes:
        compact = candidate.lower().replace("api", "")
        if needle and needle.replace(" ", "") in compact:
            return candidate
    return tag_to_api_class(tags[0])


def tag_to_api_class(tag: str) -> str:
    parts = "".join(ch if ch.isalnum() else " " for ch in tag).split()
    return "".join(p[:1].upper() + p[1:] for p in parts) + "Api"


def match_resources(
    api_classes: list[str],
    operation_tags: set[str],
) -> tuple[list[str], list[str]]:
    present: list[str] = []
    missing: list[str] = []
    lower_tags = {t.lower() for t in operation_tags}
    lower_classes = {c.lower() for c in api_classes}

    aliases = {
        "Api Keys": ("api keys", "apikeysapi", "api_keys"),
        "Projects": ("projects", "projectsapi"),
        "Emails": ("emails", "emailsapi"),
        "Domains": ("domains", "domainsapi"),
        "Templates": ("templates", "templatesapi"),
        "Contacts": ("contacts", "contactsapi"),
        "Lists": ("lists", "listsapi"),
        "Segments": ("segments", "segmentsapi"),
        "Tags": ("tags", "tagsapi"),
        "Audiences": ("audiences", "audiencesapi"),
        "Campaigns": (
            "campaigns",
            "campaignsapi",
            "campaign lifecycle",
            "campaign analytics",
            "campaign events",
        ),
        "Analytics": ("analytics", "analyticsapi"),
        "Events": ("events", "eventsapi"),
        "Messages": ("messages", "messagesapi"),
        "Webhooks": ("webhooks", "webhooksapi"),
        "Suppressions": ("suppressions", "suppressionsapi"),
        "Imports": ("imports", "importsapi"),
        "Exports": ("exports", "exportsapi"),
    }

    for resource in REQUIRED_RESOURCES:
        keys = aliases.get(resource, (resource.lower(),))
        found = False
        for key in keys:
            if key in lower_tags:
                found = True
                break
            if key.endswith("api") and key in lower_classes:
                found = True
                break
            # class form ProjectsApi
            class_key = key if key.endswith("api") else key.replace(" ", "") + "api"
            if class_key in lower_classes:
                found = True
                break
        if found:
            present.append(resource)
        else:
            missing.append(resource)
    return present, missing


def resolve_request_model(operation: dict[str, Any]) -> str:
    request_body = operation.get("requestBody")
    if not isinstance(request_body, dict):
        return "—"
    content = request_body.get("content")
    if not isinstance(content, dict):
        return "—"
    for media in content.values():
        if not isinstance(media, dict):
            continue
        schema = media.get("schema")
        name = schema_ref_name(schema)
        if name:
            return name
    return "(inline)"


def resolve_response_model(operation: dict[str, Any]) -> str:
    responses = operation.get("responses")
    if not isinstance(responses, dict):
        return "—"
    for status in ("200", "201", "202", "204"):
        response = responses.get(status)
        if not isinstance(response, dict):
            continue
        if status == "204":
            return "—"
        content = response.get("content")
        if not isinstance(content, dict):
            return "—"
        for media in content.values():
            if not isinstance(media, dict):
                continue
            name = schema_ref_name(media.get("schema"))
            if name:
                return name
            return "(inline)"
    # fallback first response with content
    for response in responses.values():
        if not isinstance(response, dict):
            continue
        content = response.get("content")
        if not isinstance(content, dict):
            continue
        for media in content.values():
            if not isinstance(media, dict):
                continue
            name = schema_ref_name(media.get("schema"))
            if name:
                return name
    return "—"


def schema_ref_name(schema: Any) -> str | None:
    if not isinstance(schema, dict):
        return None
    ref = schema.get("$ref")
    if isinstance(ref, str) and ref.startswith("#/components/schemas/"):
        return ref.rsplit("/", 1)[-1]
    for key in ("allOf", "oneOf", "anyOf"):
        items = schema.get(key)
        if isinstance(items, list):
            for item in items:
                name = schema_ref_name(item)
                if name:
                    return name
    return None


def extract_warnings(output: str) -> list[str]:
    warnings: list[str] = []
    for line in output.splitlines():
        stripped = line.strip()
        if not stripped:
            continue
        # OpenAPI Generator logs use levels like "WARN" / "WARNING".
        if " WARN " in stripped or " WARNING " in stripped or "[warn]" in stripped.lower():
            warnings.append(stripped)
    return warnings


def unique(values: list[str]) -> list[str]:
    seen: set[str] = set()
    result: list[str] = []
    for value in values:
        if value not in seen:
            seen.add(value)
            result.append(value)
    return result


def write_report(
    *,
    api_version: str,
    spec_version: str,
    path_count: int,
    schema_count: int,
    elapsed: float,
    warnings: list[str],
    inventory: dict[str, Any],
    generation_output: str,
) -> None:
    # Model file names are snake_case; schemas are often PascalCase — compare via normalization
    model_set = {m.replace("_", "").lower() for m in inventory["models"]}
    schema_missing_in_models: list[str] = []
    for schema in inventory["schema_names"]:
        key = "".join(ch for ch in schema if ch.isalnum()).lower()
        if key not in model_set:
            schema_missing_in_models.append(schema)

    duplicate_models = find_duplicates(inventory["models"])

    lines: list[str] = []
    lines.append("# MailerMine Python SDK — Generation Report")
    lines.append("")
    lines.append("**Phase:** 2 — Generated OpenAPI client only  ")
    lines.append(f"**Generated at:** script runtime (elapsed {elapsed:.2f}s)  ")
    lines.append(f"**Source of truth:** {OPENAPI_URL}")
    lines.append("")
    lines.append("---")
    lines.append("")
    lines.append("## Generator")
    lines.append("")
    lines.append("| Item | Value |")
    lines.append("| --- | --- |")
    lines.append(f"| OpenAPI Generator | `{GENERATOR_VERSION}` |")
    lines.append(f"| Generator name | `{GENERATOR_NAME}` |")
    lines.append(f"| JAR SHA-256 | `{GENERATOR_SHA256}` |")
    lines.append(f"| Spec OpenAPI version | `{spec_version}` |")
    lines.append(f"| Spec `info.version` | `{api_version}` |")
    lines.append(f"| Paths in spec | {path_count} |")
    lines.append(f"| Schemas in spec | {schema_count} |")
    lines.append(f"| Package name | `{PACKAGE_NAME}` |")
    lines.append(f"| Output | `{inventory['package_root']}` |")
    lines.append("")
    lines.append("## Library selection")
    lines.append("")
    lines.append("Evaluated options supported by the stable `python` generator in **7.23.0**:")
    lines.append("")
    lines.append("| Library | Sync | Async | Notes |")
    lines.append("| --- | --- | --- | --- |")
    lines.append(
        "| `urllib3` | Yes | No | Default; production-proven; ideal for sync-first public APIs. |"
    )
    lines.append(
        "| `requests` | Yes (legacy) | No | Not offered by modern `python` generator "
        "(legacy generators only). |"
    )
    lines.append(
        "| `httpx` | **No in 7.23.0** | Yes | Async-only on this release. "
        "`supportHttpxSync` appears in upstream docs/PRs but is **not** exposed by "
        "`config-help` for 7.23.0 (verified). |"
    )
    lines.append("| `asyncio` (aiohttp) | No | Yes | Async-only; weaker sync DX for v1 wrapper. |")
    lines.append("")
    lines.append("**Selected: `urllib3`.**")
    lines.append("")
    lines.append(
        "Rationale: the official SDK public surface is sync-first (parity with Laravel and "
        "Node). On OpenAPI Generator 7.23.0, `httpx` cannot provide sync methods, so choosing "
        "it would force every wrapper call through `asyncio.run` — poor DX and awkward "
        "nesting. `urllib3` keeps dependencies small (`urllib3`, `pydantic`, "
        "`python-dateutil`, typing helpers) and matches the architecture plan. "
        "When a stable generator release ships dual sync/async `httpx` "
        "(`supportHttpxSync`), revisit regeneration to unlock `AsyncMailerMine` without a "
        "second client."
    )
    lines.append("")
    lines.append("## Generator options")
    lines.append("")
    lines.append("```text")
    lines.append(f"packageName={PACKAGE_NAME}")
    lines.append(f"projectName={PROJECT_NAME}")
    lines.append(f"packageVersion={api_version}")
    lines.append(f"library={LIBRARY}")
    lines.append("generateSourceCodeOnly=false")
    lines.append("hideGenerationTimestamp=true")
    lines.append("disallowAdditionalPropertiesIfNotPresent=false")
    lines.append("```")
    lines.append("")
    lines.append("## Resource coverage")
    lines.append("")
    lines.append("| Resource | Status |")
    lines.append("| --- | --- |")
    for resource in REQUIRED_RESOURCES:
        status = "present" if resource in inventory["present_resources"] else "**MISSING**"
        lines.append(f"| {resource} | {status} |")
    lines.append("")
    if inventory["missing_resources"]:
        lines.append("### Missing resources")
        lines.append("")
        for resource in inventory["missing_resources"]:
            lines.append(f"- {resource}")
        lines.append("")
    else:
        lines.append("All required MailerMine resources are present in the generated client.")
        lines.append("")

    lines.append("## Generated API classes")
    lines.append("")
    for name in inventory["api_classes"]:
        lines.append(f"- `{name}`")
    lines.append("")
    lines.append(f"**Total API classes:** {len(inventory['api_classes'])}")
    lines.append("")
    lines.append("## Generated models")
    lines.append("")
    lines.append(f"**Total model modules:** {len(inventory['models'])}")
    lines.append(f"**OpenAPI component schemas:** {len(inventory['schema_names'])}")
    lines.append("")
    if duplicate_models:
        lines.append("### Duplicate model modules")
        lines.append("")
        for name in duplicate_models:
            lines.append(f"- `{name}`")
        lines.append("")
    else:
        lines.append("No duplicate model module filenames detected.")
        lines.append("")
    if schema_missing_in_models:
        lines.append("### Schemas without an obvious generated model module")
        lines.append("")
        lines.append(
            "These schema names did not match a snake_case model module after "
            "normalization (may be inlined, renamed, or composed):"
        )
        lines.append("")
        for name in schema_missing_in_models[:50]:
            lines.append(f"- `{name}`")
        if len(schema_missing_in_models) > 50:
            lines.append(f"- … and {len(schema_missing_in_models) - 50} more")
        lines.append("")
    else:
        lines.append("Every component schema maps to a generated model module (name-normalized).")
        lines.append("")

    lines.append("## Endpoint inventory")
    lines.append("")
    lines.append(f"**Total endpoints:** {inventory['endpoint_count']}")
    lines.append("")
    lines.append("| API class | Endpoint | HTTP method | Request model | Response model |")
    lines.append("| --- | --- | --- | --- | --- |")
    for row in sorted(
        inventory["endpoint_rows"],
        key=lambda r: (r["api_class"], r["endpoint"], r["http_method"]),
    ):
        lines.append(
            f"| `{row['api_class']}` | `{row['endpoint']}` | `{row['http_method']}` | "
            f"`{row['request_model']}` | `{row['response_model']}` |"
        )
    lines.append("")

    lines.append("## Warnings")
    lines.append("")
    if warnings:
        for warning in warnings:
            lines.append(f"- `{warning}`")
    else:
        lines.append("No generator warnings captured.")
    lines.append("")

    # Capture a short excerpt of generator output for debugging
    interesting = [
        line
        for line in generation_output.splitlines()
        if any(token in line.lower() for token in ("error", "warn", "skip", "fail", "exception"))
    ]
    lines.append("## Problems")
    lines.append("")
    problems: list[str] = []
    if inventory["missing_resources"]:
        problems.append("Missing required resources: " + ", ".join(inventory["missing_resources"]))
    if duplicate_models:
        problems.append("Duplicate model modules detected.")
    if interesting and not warnings:
        problems.append("Generator output contained error/warn/skip lines; review excerpt below.")
    if not problems:
        lines.append("No blocking problems detected for Phase 2.")
    else:
        for problem in problems:
            lines.append(f"- {problem}")
    lines.append("")
    if interesting:
        lines.append("### Generator output excerpt")
        lines.append("")
        lines.append("```text")
        lines.extend(interesting[:80])
        lines.append("```")
        lines.append("")

    lines.append("## Recommendations")
    lines.append("")
    lines.append(
        "1. Keep regenerating via `python scripts/generate.py` only — never edit "
        "`generated/` by hand."
    )
    lines.append(
        "2. Phase 3 should wrap `mailermine_generated` behind `mailermine.config` / "
        "exception mapping; do not re-export generated models."
    )
    lines.append(
        "3. Call the generated sync urllib3 API methods from the v1 handwritten wrapper. "
        "Revisit `library=httpx` when OpenAPI Generator ships dual sync/async support "
        "in a stable release; that enables a future `AsyncMailerMine` without a second client."
    )
    lines.append(
        "4. Default runtime `host` must override the OpenAPI `servers` localhost URL "
        "to `https://mailermine.com/api/v1`."
    )
    lines.append(
        "5. Pin OpenAPI Generator `7.23.0` (same major line as `@mailermine/node`) "
        "until a coordinated upgrade."
    )
    lines.append("")
    lines.append("## OpenAPI tags observed")
    lines.append("")
    for tag in inventory["operation_tags"]:
        lines.append(f"- {tag}")
    lines.append("")

    REPORT_PATH.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"  Wrote {REPORT_PATH}")


def find_duplicates(names: list[str]) -> list[str]:
    seen: set[str] = set()
    dupes: list[str] = []
    for name in names:
        if name in seen:
            dupes.append(name)
        seen.add(name)
    return dupes


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except KeyboardInterrupt:
        raise SystemExit(130) from None
