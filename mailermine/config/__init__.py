"""Immutable SDK configuration."""

from __future__ import annotations

import os
from collections.abc import Mapping
from dataclasses import dataclass
from urllib.parse import urlparse

from mailermine.constants import (
    DEFAULT_BASE_URL,
    DEFAULT_TIMEOUT,
    DEFAULT_USER_AGENT,
)


@dataclass(frozen=True, slots=True)
class Configuration:
    """Validated, immutable MailerMine client configuration.

    Parameters
    ----------
    api_key:
        Bearer API key. Required unless provided via ``MAILERMINE_API_KEY``.
    base_url:
        API base URL. Defaults to production.
    timeout:
        Request timeout in seconds.
    user_agent:
        ``User-Agent`` header value.
    """

    api_key: str
    base_url: str = DEFAULT_BASE_URL
    timeout: float = DEFAULT_TIMEOUT
    user_agent: str = DEFAULT_USER_AGENT

    def __post_init__(self) -> None:
        object.__setattr__(self, "api_key", _normalize_api_key(self.api_key))
        object.__setattr__(self, "base_url", _normalize_base_url(self.base_url))
        object.__setattr__(self, "timeout", _normalize_timeout(self.timeout))
        object.__setattr__(self, "user_agent", _normalize_user_agent(self.user_agent))

    @classmethod
    def create(
        cls,
        api_key: str | None = None,
        *,
        base_url: str | None = None,
        timeout: float | None = None,
        user_agent: str | None = None,
    ) -> Configuration:
        """Build configuration from explicit values and environment variables.

        Environment variables
        ---------------------
        ``MAILERMINE_API_KEY``
            Used when ``api_key`` is omitted.
        ``MAILERMINE_BASE_URL``
            Used when ``base_url`` is omitted.
        ``MAILERMINE_TIMEOUT``
            Used when ``timeout`` is omitted (seconds).

        Parameters
        ----------
        api_key:
            Bearer API key.
        base_url:
            Optional API base URL override.
        timeout:
            Optional timeout override in seconds.
        user_agent:
            Optional User-Agent override.

        Returns
        -------
        Configuration
            Validated configuration instance.

        Raises
        ------
        ValueError
            If the API key is missing or any option is invalid.
        """
        resolved_api_key = api_key if api_key is not None else os.environ.get("MAILERMINE_API_KEY")
        if base_url is not None:
            resolved_base_url = base_url
        else:
            resolved_base_url = os.environ.get("MAILERMINE_BASE_URL", DEFAULT_BASE_URL)
        if timeout is not None:
            resolved_timeout = timeout
        elif "MAILERMINE_TIMEOUT" in os.environ:
            resolved_timeout = float(os.environ["MAILERMINE_TIMEOUT"])
        else:
            resolved_timeout = DEFAULT_TIMEOUT

        if resolved_api_key is None or str(resolved_api_key).strip() == "":
            raise ValueError(
                "MailerMine requires an api_key argument or "
                "MAILERMINE_API_KEY environment variable."
            )

        return cls(
            api_key=str(resolved_api_key),
            base_url=str(resolved_base_url),
            timeout=float(resolved_timeout),
            user_agent=user_agent if user_agent is not None else DEFAULT_USER_AGENT,
        )

    @classmethod
    def from_mapping(cls, values: Mapping[str, object]) -> Configuration:
        """Create configuration from a mapping of options.

        Parameters
        ----------
        values:
            Mapping that may include ``api_key`` / ``apiKey``, ``base_url`` /
            ``baseUrl``, ``timeout``, and ``user_agent`` / ``userAgent``.

        Returns
        -------
        Configuration
            Validated configuration.
        """
        api_key = values.get("api_key", values.get("apiKey"))
        base_url = values.get("base_url", values.get("baseUrl"))
        timeout = values.get("timeout")
        user_agent = values.get("user_agent", values.get("userAgent"))
        return cls.create(
            api_key=str(api_key) if api_key is not None else None,
            base_url=str(base_url) if isinstance(base_url, str) else None,
            timeout=float(timeout) if isinstance(timeout, (int, float)) else None,
            user_agent=str(user_agent) if isinstance(user_agent, str) else None,
        )

    def to_dict(self) -> dict[str, str | float]:
        """Return a plain snapshot of the resolved configuration."""
        return {
            "api_key": self.api_key,
            "base_url": self.base_url,
            "timeout": self.timeout,
            "user_agent": self.user_agent,
        }


def _normalize_api_key(api_key: str) -> str:
    if not isinstance(api_key, str) or api_key.strip() == "":
        raise ValueError("MailerMine Configuration requires a non-empty api_key string.")
    return api_key.strip()


def _normalize_base_url(base_url: str) -> str:
    if not isinstance(base_url, str) or base_url.strip() == "":
        raise ValueError("MailerMine Configuration base_url must be a non-empty string.")
    trimmed = base_url.strip().rstrip("/")
    parsed = urlparse(trimmed)
    if parsed.scheme not in {"http", "https"} or not parsed.netloc:
        raise ValueError(f"MailerMine Configuration base_url is not a valid URL: {base_url}")
    return trimmed


def _normalize_timeout(timeout: float) -> float:
    if not isinstance(timeout, (int, float)) or isinstance(timeout, bool):
        raise ValueError("MailerMine Configuration timeout must be a positive number (seconds).")
    value = float(timeout)
    if value <= 0 or value != value:  # NaN check
        raise ValueError("MailerMine Configuration timeout must be a positive number (seconds).")
    return value


def _normalize_user_agent(user_agent: str) -> str:
    if not isinstance(user_agent, str) or user_agent.strip() == "":
        raise ValueError("MailerMine Configuration user_agent must be a non-empty string.")
    return user_agent.strip()
