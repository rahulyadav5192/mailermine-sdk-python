"""Resilient transport wrapped around the generated ``ApiClient``.

This module is private. Application code must never import it.
"""

from __future__ import annotations

import random
import re
import time
import uuid
from email.utils import parsedate_to_datetime
from typing import Any
from urllib.parse import urlparse

import urllib3
from mailermine_generated import ApiClient

from mailermine.support.rate_limit import RateLimitInfo

IDEMPOTENCY_HEADER = "Idempotency-Key"
_SAFE_METHODS = frozenset({"GET", "HEAD", "OPTIONS", "PUT", "DELETE"})
_RETRYABLE_STATUSES = frozenset({502, 503, 504})
_EMAILS_PATH = re.compile(r"/emails/?$")


class ResilientApiClient(ApiClient):
    """``ApiClient`` that retries, adds idempotency keys and records rate limits.

    - Adds an ``Idempotency-Key`` to ``POST /emails`` when none is set, reused
      across retries so a retried send is never delivered twice.
    - Retries 429 and 502/503/504 responses and transport errors with
      exponential backoff and jitter, honouring ``Retry-After``. Requests that
      are not idempotent (POST/PATCH without an ``Idempotency-Key``) are only
      retried on 429, which the API returns before doing any work.
    - Keeps the latest ``X-RateLimit-*`` state in :attr:`last_rate_limit`.
    """

    def __init__(
        self, *args: Any, max_retries: int = 2, max_retry_delay: float = 30.0, **kwargs: Any
    ):
        super().__init__(*args, **kwargs)
        self.max_retries = max_retries
        self.max_retry_delay = max_retry_delay
        self.last_rate_limit: RateLimitInfo | None = None
        self._sleep = time.sleep

    def call_api(
        self,
        method: str,
        url: str,
        header_params: dict[str, str] | None = None,
        body: Any = None,
        post_params: Any = None,
        _request_timeout: Any = None,
    ) -> Any:
        method = method.upper()
        headers = dict(header_params or {})
        if (
            method == "POST"
            and not any(k.lower() == "idempotency-key" for k in headers)
            and _EMAILS_PATH.search(urlparse(url).path)
        ):
            headers[IDEMPOTENCY_HEADER] = str(uuid.uuid4())

        replayable = method in _SAFE_METHODS or any(k.lower() == "idempotency-key" for k in headers)

        attempt = 0
        while True:
            try:
                response = super().call_api(
                    method,
                    url,
                    header_params=headers,
                    body=body,
                    post_params=post_params,
                    _request_timeout=_request_timeout,
                )
            except urllib3.exceptions.HTTPError:
                if not replayable or attempt >= self.max_retries:
                    raise
                self._sleep(self._backoff(attempt))
                attempt += 1
                continue

            response_headers = _headers(response)
            rate_limit = RateLimitInfo.from_headers(response_headers)
            if rate_limit is not None:
                self.last_rate_limit = rate_limit

            if attempt >= self.max_retries:
                return response

            status = int(getattr(response, "status", 0) or 0)
            delay: float | None = None
            retry_after = _retry_after_seconds(response_headers)

            if status == 429:
                if retry_after is None:
                    delay = self._backoff(attempt)
                elif retry_after <= self.max_retry_delay:
                    delay = retry_after
            elif status in _RETRYABLE_STATUSES and replayable:
                delay = min(
                    retry_after if retry_after is not None else self._backoff(attempt),
                    self.max_retry_delay,
                )

            if delay is None:
                return response

            self._sleep(delay)
            attempt += 1

    def _backoff(self, attempt: int) -> float:
        delay: float = 0.5 * (2**attempt) + random.uniform(0, 0.25)
        return float(min(delay, self.max_retry_delay))


def _headers(response: Any) -> dict[str, str]:
    try:
        raw = response.getheaders()
    except Exception:
        return {}
    try:
        return {str(k): str(v) for k, v in dict(raw).items()}
    except Exception:
        return {}


def _retry_after_seconds(headers: dict[str, str]) -> float | None:
    value = next((v for k, v in headers.items() if k.lower() == "retry-after"), None)
    if value is None or value.strip() == "":
        return None
    try:
        return max(0.0, float(value))
    except ValueError:
        pass
    try:
        return max(0.0, parsedate_to_datetime(value).timestamp() - time.time())
    except (TypeError, ValueError):
        return None
