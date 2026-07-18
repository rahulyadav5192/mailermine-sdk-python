"""List sending domains and print DNS / status helpers for the first domain.

Requires ``MAILERMINE_API_KEY`` in the environment.
"""

from __future__ import annotations

import os
import sys

from mailermine import MailerMine


def main() -> int:
    api_key = os.environ.get("MAILERMINE_API_KEY")
    if not api_key:
        print("Set MAILERMINE_API_KEY before running this example.", file=sys.stderr)
        return 1

    client = MailerMine(api_key=api_key)
    domains = client.domains.list(per_page=10)
    print(f"domains on page: {len(domains)} / total {domains.pagination.total}")

    if not domains.items:
        print("No domains configured yet.")
        return 0

    first = domains.items[0]
    domain_id = str(first.get("id") or first.get("uuid"))
    print("domain:", domain_id, first.get("domain") or first.get("name"))

    print("status:", client.domains.status(domain_id).data)
    print("dns_records:", client.domains.dns_records(domain_id).data)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
