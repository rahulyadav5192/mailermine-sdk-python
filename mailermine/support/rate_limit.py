"""Rate-limit information reported by the API."""

from __future__ import annotations

import time
from collections.abc import Mapping
from dataclasses import dataclass
from datetime import datetime, timezone


@dataclass(frozen=True, slots=True)
class RateLimitInfo:
    """Rate-limit state from ``X-RateLimit-*`` response headers.

    Examples
    --------
    >>> client.emails.send(...)
    >>> client.rate_limit.remaining if client.rate_limit else None
    """

    limit: int
    remaining: int
    resets_at: datetime | None

    @property
    def seconds_until_reset(self) -> int:
        """Seconds until the window resets (0 when unknown or past)."""
        if self.resets_at is None:
            return 0
        return max(0, int(self.resets_at.timestamp() - time.time()))

    @classmethod
    def from_headers(cls, headers: Mapping[str, str] | None) -> RateLimitInfo | None:
        """Parse rate-limit headers (case-insensitive); ``None`` when absent."""
        if not headers:
            return None
        lowered = {str(k).lower(): v for k, v in headers.items()}
        try:
            limit = int(lowered["x-ratelimit-limit"])
            remaining = int(lowered["x-ratelimit-remaining"])
        except (KeyError, TypeError, ValueError):
            return None
        reset_raw = lowered.get("x-ratelimit-reset")
        resets_at: datetime | None = None
        if reset_raw is not None:
            try:
                resets_at = datetime.fromtimestamp(int(reset_raw), tz=timezone.utc)
            except (TypeError, ValueError, OverflowError, OSError):
                resets_at = None
        return cls(limit=limit, remaining=remaining, resets_at=resets_at)
