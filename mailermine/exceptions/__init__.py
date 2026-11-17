"""Public exception hierarchy for the MailerMine Python SDK."""

from __future__ import annotations

import json
import re
from collections.abc import Mapping, Sequence

from mailermine.constants import UPGRADE_URL
from mailermine.support.rate_limit import RateLimitInfo

__all__ = [
    "ApiError",
    "AuthenticationError",
    "MailerMineError",
    "MissingScopeError",
    "NotFoundError",
    "PlanError",
    "RateLimitError",
    "ValidationError",
    "map_generated_error",
]


class MailerMineError(Exception):
    """Base error for all MailerMine SDK failures.

    Catch this type to handle any SDK error in one place.

    Parameters
    ----------
    args:
        Standard exception arguments (typically a message string).

    Returns
    -------
    None
        Raised, never returned.

    Raises
    ------
    MailerMineError
        This class is the exception being raised.

    Examples
    --------
    >>> from mailermine import MailerMineError
    >>> try:
    ...     raise MailerMineError("boom")
    ... except MailerMineError as exc:
    ...     str(exc)
    'boom'
    """


class ApiError(MailerMineError):
    """HTTP or transport failure talking to the MailerMine API.

    Parameters
    ----------
    message:
        Developer-friendly error message.
    status:
        HTTP status code, or ``0`` for transport failures.
    body:
        Decoded response body when available.
    headers:
        Response headers when available.

    Returns
    -------
    None
        Raised, never returned.

    Raises
    ------
    ApiError
        This class is the exception being raised.

    Examples
    --------
    >>> from mailermine import ApiError
    >>> err = ApiError("failed", status=500)
    >>> err.status
    500
    """

    def __init__(
        self,
        message: str,
        status: int = 0,
        body: object | None = None,
        headers: Mapping[str, str] | None = None,
    ) -> None:
        super().__init__(message)
        self.status = status
        self.body = body
        self.headers: dict[str, str] = dict(headers or {})

    @property
    def message(self) -> str:
        """Human-readable error message (Node SDK ``Error.message`` parity).

        Returns
        -------
        str
            The exception message string.
        """
        return str(self)

    @property
    def request_id(self) -> str | None:
        """MailerMine request ID from the body or response headers, if present.

        Returns
        -------
        str | None
            Request ID when present.
        """
        if isinstance(self.body, Mapping):
            value = self.body.get("request_id")
            if isinstance(value, str) and value:
                return value
        for key in ("X-Request-Id", "x-request-id", "X-Request-ID"):
            value = self.headers.get(key)
            if value:
                return value
        return None

    @property
    def rate_limit(self) -> RateLimitInfo | None:
        """Rate-limit state from the error response headers, when present."""
        return RateLimitInfo.from_headers(self.headers)

    @property
    def is_retryable(self) -> bool:
        """Whether retrying the same request later may succeed (429 and 5xx)."""
        return self.status == 429 or self.status >= 500

    def is_client_error(self) -> bool:
        """Return whether this is an HTTP 4xx error.

        Returns
        -------
        bool
            ``True`` for client errors.
        """
        return 400 <= self.status < 500

    def is_server_error(self) -> bool:
        """Return whether this is an HTTP 5xx error.

        Returns
        -------
        bool
            ``True`` for server errors.
        """
        return self.status >= 500


class AuthenticationError(ApiError):
    """The API key is missing, invalid, expired, or revoked (HTTP 401).

    Parameters
    ----------
    message:
        Developer-friendly error message.
    status:
        HTTP status (typically 401).
    body:
        Decoded response body when available.
    headers:
        Response headers when available.

    Returns
    -------
    None
        Raised, never returned.

    Raises
    ------
    AuthenticationError
        This class is the exception being raised.

    Examples
    --------
    >>> from mailermine import AuthenticationError
    >>> isinstance(AuthenticationError("unauthorized", status=401), ApiError)
    True
    """


class PlanError(ApiError):
    """The account plan or API-key scope does not permit the operation (HTTP 403).

    Parameters
    ----------
    message:
        Developer-friendly error message (includes upgrade guidance when mapped).
    status:
        HTTP status (typically 403).
    body:
        Decoded response body when available.
    headers:
        Response headers when available.

    Returns
    -------
    None
        Raised, never returned.

    Raises
    ------
    PlanError
        This class is the exception being raised.

    Examples
    --------
    >>> from mailermine import PlanError
    >>> PlanError("upgrade required", status=403).upgrade_url.startswith("https://")
    True
    """

    @property
    def upgrade_url(self) -> str:
        """URL where the account plan can be upgraded.

        Returns
        -------
        str
            Billing upgrade URL.
        """
        return UPGRADE_URL


class MissingScopeError(PlanError):
    """The API key is valid but lacks a scope the endpoint requires (HTTP 403).

    Subclass of :class:`PlanError`, so existing ``except PlanError`` handlers
    still catch it. ``missing_scopes`` lists what the key would need.

    Examples
    --------
    >>> from mailermine import MissingScopeError
    >>> err = MissingScopeError("missing scope", missing_scopes=["domains.read"])
    >>> err.missing_scopes
    ['domains.read']
    """

    def __init__(
        self,
        message: str,
        status: int = 403,
        missing_scopes: list[str] | None = None,
        body: object | None = None,
        headers: Mapping[str, str] | None = None,
    ) -> None:
        super().__init__(message, status=status, body=body, headers=headers)
        self.missing_scopes: list[str] = list(missing_scopes or [])


class NotFoundError(ApiError):
    """The requested MailerMine object does not exist (HTTP 404).

    Parameters
    ----------
    message:
        Developer-friendly error message.
    status:
        HTTP status (typically 404).
    body:
        Decoded response body when available.
    headers:
        Response headers when available.

    Returns
    -------
    None
        Raised, never returned.

    Raises
    ------
    NotFoundError
        This class is the exception being raised.

    Examples
    --------
    >>> from mailermine import NotFoundError
    >>> NotFoundError("missing", status=404).status
    404
    """


class ValidationError(ApiError):
    """The MailerMine API rejected the request (HTTP 422).

    Also used for missing required request fields before the HTTP call
    (parity with the Node SDK ``RequiredError`` → ``ValidationError`` mapping).
    Never used for response deserialization failures — those raise :class:`ApiError`.

    Parameters
    ----------
    message:
        Summary message.
    status:
        HTTP status (typically 422).
    errors:
        Field-level validation messages.
    body:
        Raw response body.
    headers:
        Response headers.

    Returns
    -------
    None
        Raised, never returned.

    Raises
    ------
    ValidationError
        This class is the exception being raised.

    Examples
    --------
    >>> from mailermine import ValidationError
    >>> err = ValidationError("invalid", errors={"email": ["required"]})
    >>> err.errors["email"]
    ['required']
    """

    def __init__(
        self,
        message: str,
        status: int = 422,
        errors: Mapping[str, Sequence[str]] | None = None,
        body: object | None = None,
        headers: Mapping[str, str] | None = None,
    ) -> None:
        super().__init__(message, status=status, body=body, headers=headers)
        self.errors: dict[str, list[str]] = {
            str(field): [str(item) for item in messages]
            for field, messages in dict(errors or {}).items()
        }


class RateLimitError(ApiError):
    """The API rate limit was exceeded (HTTP 429).

    Parameters
    ----------
    message:
        Summary message.
    status:
        HTTP status (typically 429).
    retry_after:
        Seconds to wait before retrying, when provided by the API.
    body:
        Raw response body.
    headers:
        Response headers.

    Returns
    -------
    None
        Raised, never returned.

    Raises
    ------
    RateLimitError
        This class is the exception being raised.

    Examples
    --------
    >>> from mailermine import RateLimitError
    >>> RateLimitError("slow down", retry_after=30).retry_after
    30
    """

    def __init__(
        self,
        message: str,
        status: int = 429,
        retry_after: int | None = None,
        body: object | None = None,
        headers: Mapping[str, str] | None = None,
    ) -> None:
        super().__init__(message, status=status, body=body, headers=headers)
        self.retry_after = retry_after


_GENERATED_NOISE = re.compile(
    r"\b(?:ApiException|OpenApiException|UnauthorizedException|ForbiddenException|"
    r"NotFoundException|UnprocessableEntityException|BadRequestException|"
    r"ServiceException|ConflictException|mailermine_generated|"
    r"OpenAPI(?:\\Client)?|openapi-generator)\b",
    re.IGNORECASE,
)


def map_generated_error(error: BaseException) -> ApiError:
    """Map a generated/transport exception onto the public SDK hierarchy.

    Parameters
    ----------
    error:
        Exception raised by the generated client or transport layer.

    Returns
    -------
    ApiError
        A public SDK exception. Never returns generated exception types.
    """
    try:
        return _map_error(error)
    except Exception:
        return ApiError("MailerMine API request failed", status=0)


def _map_error(error: BaseException) -> ApiError:
    # Import locally so generated symbols never appear at module import time for consumers
    # who only catch public exceptions.
    from mailermine_generated.exceptions import (
        ApiException,
        ApiValueError,
        OpenApiException,
    )

    if isinstance(error, ApiError):
        return error

    if isinstance(error, ApiException):
        status = int(error.status or 0)
        headers = _normalize_headers(getattr(error, "headers", None))
        body = _decode_body(getattr(error, "body", None), getattr(error, "data", None))
        message = _resolve_message(body, error.reason or error.body or str(error))

        if status == 401:
            return AuthenticationError(
                message or "Authentication failed. Check your API key.",
                status=status,
                body=body,
                headers=headers,
            )
        missing_scopes = _extract_missing_scopes(body) if status == 403 else []
        if missing_scopes:
            return MissingScopeError(
                message or "This API key is missing a required scope.",
                status=status,
                missing_scopes=missing_scopes,
                body=body,
                headers=headers,
            )
        if status == 403:
            return PlanError(
                _plan_message(message),
                status=status,
                body=body,
                headers=headers,
            )
        if status == 404:
            return NotFoundError(
                message or "The requested resource was not found.",
                status=status,
                body=body,
                headers=headers,
            )
        if status == 422:
            return ValidationError(
                message or "The given data was invalid.",
                status=status,
                errors=_extract_errors(body),
                body=body,
                headers=headers,
            )
        if status == 429:
            return RateLimitError(
                message or "Too many requests. Please try again later.",
                status=status,
                retry_after=_extract_retry_after(headers),
                body=body,
                headers=headers,
            )
        return ApiError(
            message or f"API request failed with status {status}.",
            status=status,
            body=body,
            headers=headers,
        )

    # Pydantic ValidationError subclasses ValueError — check it before ValueError.
    # HTTP 200 + failed response parse is a deserialization/SDK issue, not HTTP 422.
    try:
        from pydantic import ValidationError as PydanticValidationError
    except ImportError:  # pragma: no cover
        PydanticValidationError = None  # type: ignore[assignment,misc]

    if PydanticValidationError is not None and isinstance(error, PydanticValidationError):
        text = _sanitize_text(str(error))
        deserialize_body: object | None = None
        errors_fn = getattr(error, "errors", None)
        if callable(errors_fn):
            try:
                deserialize_body = {"errors": errors_fn()}
            except Exception:
                deserialize_body = None
        return ApiError(
            text or "Failed to deserialize MailerMine API response.",
            status=0,
            body=deserialize_body,
        )

    # Client-side request construction (missing/invalid params) — Node RequiredError parity.
    if isinstance(error, ApiValueError):
        text = _sanitize_text(str(error))
        return ValidationError(
            text or "The given data was invalid.",
            status=422,
            errors={},
            body=None,
        )

    # Transport, serialization, and other generated failures.
    if isinstance(error, (OpenApiException, TypeError, ValueError)):
        text = _sanitize_text(str(error))
        return ApiError(
            text or "MailerMine API request failed.",
            status=0,
        )

    # urllib3 / connection failures
    text = _sanitize_text(str(error) or "Unable to connect to the MailerMine API.")
    return ApiError(text, status=0)


def _plan_message(message: str) -> str:
    base = message or "This action is not available on your current MailerMine plan."
    if UPGRADE_URL in base:
        return base
    guidance = (
        f"If your plan does not include this feature, upgrade at {UPGRADE_URL}. "
        "Otherwise, contact support@mailermine.com if you believe this is an error."
    )
    return f"{base.rstrip('.')}." + f" {guidance}"


def _resolve_message(body: object, fallback: object) -> str:
    if isinstance(body, Mapping):
        for key in ("message", "error"):
            value = body.get(key)
            if isinstance(value, str) and value.strip():
                return _sanitize_text(value)
    if isinstance(fallback, str) and fallback.strip():
        return _sanitize_text(fallback)
    return "MailerMine API request failed"


def _extract_missing_scopes(body: object) -> list[str]:
    if not isinstance(body, Mapping):
        return []
    errors = body.get("errors")
    if not isinstance(errors, Mapping):
        return []
    scope = errors.get("scope")
    values = [scope] if isinstance(scope, str) else scope if isinstance(scope, list) else []
    return [value for value in values if isinstance(value, str) and value]


def _extract_errors(body: object) -> dict[str, list[str]]:
    if not isinstance(body, Mapping):
        return {}
    raw = body.get("errors")
    if not isinstance(raw, Mapping):
        return {}
    result: dict[str, list[str]] = {}
    for field, messages in raw.items():
        if isinstance(messages, Sequence) and not isinstance(messages, (str, bytes)):
            result[str(field)] = [_sanitize_text(str(item)) for item in messages]
        else:
            result[str(field)] = [_sanitize_text(str(messages))]
    return result


def _extract_retry_after(headers: Mapping[str, str]) -> int | None:
    for key in ("Retry-After", "retry-after"):
        value = headers.get(key)
        if value is None:
            continue
        try:
            return int(value)
        except ValueError:
            return None
    return None


def _normalize_headers(headers: object) -> dict[str, str]:
    if headers is None:
        return {}
    if isinstance(headers, Mapping):
        result: dict[str, str] = {}
        for key, value in headers.items():
            if isinstance(value, Sequence) and not isinstance(value, (str, bytes)):
                result[str(key)] = str(value[0]) if value else ""
            else:
                result[str(key)] = str(value)
        return result
    return {}


def _decode_body(body: object, data: object) -> object | None:
    if data is not None:
        return _sanitize_value(data)
    if body is None:
        return None
    if isinstance(body, (bytes, bytearray)):
        try:
            body = body.decode("utf-8")
        except UnicodeDecodeError:
            return None
    if isinstance(body, str):
        stripped = body.strip()
        if not stripped:
            return None
        try:
            return _sanitize_value(json.loads(stripped))
        except json.JSONDecodeError:
            return _sanitize_text(stripped)
    return _sanitize_value(body)


def _sanitize_text(value: str) -> str:
    return _GENERATED_NOISE.sub("MailerMine API error", value).strip()


def _sanitize_value(value: object, seen: set[int] | None = None) -> object | None:
    if value is None or isinstance(value, (bool, int, float)):
        return value
    if isinstance(value, str):
        return _sanitize_text(value)
    if seen is None:
        seen = set()
    identity = id(value)
    if identity in seen:
        return None
    if isinstance(value, Mapping):
        seen.add(identity)
        return {
            _sanitize_text(str(key)): sanitized
            for key, item in value.items()
            if (sanitized := _sanitize_value(item, seen)) is not None
            or item is None
            or item is False
            or item == 0
        }
    if isinstance(value, Sequence) and not isinstance(value, (str, bytes, bytearray)):
        seen.add(identity)
        return [_sanitize_value(item, seen) for item in value]
    if hasattr(value, "to_dict") and callable(value.to_dict):
        try:
            return _sanitize_value(value.to_dict(), seen)
        except Exception:
            return None
    return None


# Ensure mapping helpers stay resilient without leaking generated types.
