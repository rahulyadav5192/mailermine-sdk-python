"""List project events from the global event stream.

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
    events = client.events.list(per_page=20)
    print(f"events on page: {len(events)}")
    for event in events:
        print(
            "-",
            event.get("id") or event.get("uuid"),
            event.get("type") or event.get("event_type"),
            event.get("occurred_at"),
        )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
