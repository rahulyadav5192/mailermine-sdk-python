"""Send a transactional email with the MailerMine Python SDK.

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

    try:
        response = client.emails.send(
            from_="info@example.com",
            to=["john@example.com"],
            subject="Hello from MailerMine",
            html="<h1>Hello</h1><p>Sent with the official Python SDK.</p>",
            text="Hello — sent with the official Python SDK.",
        )
    except ValidationError as exc:
        print(f"Validation failed: {exc.errors}", file=sys.stderr)
        return 1

    print("success:", response.success)
    print("message:", response.message)
    print("data:", response.data)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
