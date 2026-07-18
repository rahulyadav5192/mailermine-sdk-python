"""List recent messages and print timeline events for the first result.

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
    messages = client.messages.list(per_page=10)
    print(f"messages on page: {len(messages)} / total {messages.pagination.total}")

    if not messages.items:
        print("No messages yet — send one with examples/send_email.py")
        return 0

    first = messages.items[0]
    message_id = str(first.get("id") or first.get("uuid"))
    print("message:", message_id, first.get("subject"), first.get("status"))

    timeline = client.messages.timeline(message_id)
    for event in timeline:
        print("-", event.get("type") or event.get("event_type"), event.get("occurred_at"))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
