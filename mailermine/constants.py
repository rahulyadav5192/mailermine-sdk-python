"""Shared constants for the MailerMine Python SDK."""

from __future__ import annotations

VERSION: str = "1.2.0"

DEFAULT_BASE_URL: str = "https://mailermine.com/api/v1"

DEFAULT_TIMEOUT: float = 30.0

DEFAULT_MAX_RETRIES: int = 2

DEFAULT_MAX_RETRY_DELAY: float = 30.0

DEFAULT_USER_AGENT: str = f"mailermine-python/{VERSION}"

UPGRADE_URL: str = "https://mailermine.com/billing"
