"""List webhooks and demonstrate local signature verification.

Requires ``MAILERMINE_API_KEY`` in the environment.
"""

from __future__ import annotations

import hashlib
import hmac
import os
import sys

from mailermine import MailerMine, Webhooks


def main() -> int:
    api_key = os.environ.get("MAILERMINE_API_KEY")
    if not api_key:
        print("Set MAILERMINE_API_KEY before running this example.", file=sys.stderr)
        return 1

    client = MailerMine(api_key=api_key)
    hooks = client.webhooks.list(per_page=10)
    print(f"webhooks on page: {len(hooks)} / total {hooks.pagination.total}")
    for hook in hooks:
        print("-", hook.get("id") or hook.get("uuid"), hook.get("url"), hook.get("status"))

    # Local verify demo (no network) — replace with your webhook secret in production.
    secret = "whsec_demo"
    payload = b'{"type":"email.delivered"}'
    signature = hmac.new(secret.encode("utf-8"), payload, hashlib.sha256).hexdigest()
    print("verify ok:", Webhooks.verify(payload, f"sha256={signature}", secret))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
