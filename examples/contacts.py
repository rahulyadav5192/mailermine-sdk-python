"""Create or upsert a contact, then list recent contacts.

Requires ``MAILERMINE_API_KEY`` in the environment.
"""

from __future__ import annotations

import os
import sys

from mailermine import MailerMine, ValidationError


def main() -> int:
    api_key = os.environ.get("MAILERMINE_API_KEY")
    if not api_key:
        print("Set MAILERMINE_API_KEY before running this example.", file=sys.stderr)
        return 1

    client = MailerMine(api_key=api_key)
    email = os.environ.get("MAILERMINE_DEMO_EMAIL", "demo@example.com")

    try:
        contact = client.contacts.upsert(email=email, first_name="Demo")
    except ValidationError as exc:
        print(f"Validation failed: {exc.errors}", file=sys.stderr)
        return 1

    print("upserted:", contact.data)

    page = client.contacts.list(per_page=10)
    print(f"listing {len(page)} of {page.pagination.total} contacts")
    for item in page:
        print("-", item.get("email"), item.get("id") or item.get("uuid"))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
