"""Phase 2 verification: generated OpenAPI client imports and resource coverage.

These tests exercise ``mailermine_generated`` only. They do not depend on the
handwritten ``mailermine`` wrapper (not built yet).
"""

from __future__ import annotations

import importlib
import pkgutil
from typing import Final

import pytest

REQUIRED_API_CLASS_NAMES: Final[tuple[str, ...]] = (
    "ProjectsApi",
    "APIKeysApi",
    "EmailsApi",
    "DomainsApi",
    "TemplatesApi",
    "ContactsApi",
    "ListsApi",
    "SegmentsApi",
    "TagsApi",
    "AudiencesApi",
    "CampaignsApi",
    "AnalyticsApi",
    "EventsApi",
    "MessagesApi",
    "WebhooksApi",
    "SuppressionsApi",
    "ImportsApi",
    "ExportsApi",
)

# Campaign sub-resources must also be generated (parity with OpenAPI tags).
REQUIRED_CAMPAIGN_RELATED: Final[tuple[str, ...]] = (
    "CampaignLifecycleApi",
    "CampaignAnalyticsApi",
    "CampaignEventsApi",
)


def test_import_core_symbols() -> None:
    from mailermine_generated import ApiClient, ApiException, Configuration

    assert ApiClient is not None
    assert Configuration is not None
    assert issubclass(ApiException, Exception)


def test_configuration_and_client_construct() -> None:
    from mailermine_generated import ApiClient, Configuration

    config = Configuration(host="https://mailermine.com/api/v1")
    config.access_token = "test_token"
    client = ApiClient(configuration=config)
    assert client.configuration.host == "https://mailermine.com/api/v1"


@pytest.mark.parametrize("class_name", REQUIRED_API_CLASS_NAMES + REQUIRED_CAMPAIGN_RELATED)
def test_required_api_classes_exist(class_name: str) -> None:
    module = importlib.import_module("mailermine_generated")
    assert hasattr(module, class_name), f"Missing generated API class: {class_name}"
    api_cls = getattr(module, class_name)
    assert isinstance(api_cls, type)


def test_all_api_modules_import() -> None:
    import mailermine_generated.api as api_pkg

    failures: list[str] = []
    for module_info in pkgutil.iter_modules(api_pkg.__path__):
        name = f"mailermine_generated.api.{module_info.name}"
        try:
            importlib.import_module(name)
        except Exception as exc:
            failures.append(f"{name}: {exc}")
    assert failures == [], "API module import failures:\n" + "\n".join(failures)


def test_all_model_modules_import() -> None:
    import mailermine_generated.models as models_pkg

    failures: list[str] = []
    for module_info in pkgutil.iter_modules(models_pkg.__path__):
        name = f"mailermine_generated.models.{module_info.name}"
        try:
            importlib.import_module(name)
        except Exception as exc:
            failures.append(f"{name}: {exc}")
    assert failures == [], "Model module import failures:\n" + "\n".join(failures)


def test_package_all_lists_api_classes() -> None:
    import mailermine_generated as pkg

    exported = set(pkg.__all__)
    missing = [name for name in REQUIRED_API_CLASS_NAMES if name not in exported]
    assert missing == [], f"Required API classes missing from __all__: {missing}"


def test_emails_api_exposes_sync_send() -> None:
    """urllib3 library emits synchronous API methods (no async def)."""
    import inspect

    from mailermine_generated import EmailsApi

    assert hasattr(EmailsApi, "send_email")
    assert not inspect.iscoroutinefunction(EmailsApi.send_email)


def test_exceptions_module_exports() -> None:
    from mailermine_generated import exceptions

    for name in (
        "OpenApiException",
        "ApiTypeError",
        "ApiValueError",
        "ApiKeyError",
        "ApiAttributeError",
        "ApiException",
        "BadRequestException",
        "NotFoundException",
        "UnauthorizedException",
        "ForbiddenException",
        "ServiceException",
    ):
        assert hasattr(exceptions, name), f"Missing exception: {name}"
