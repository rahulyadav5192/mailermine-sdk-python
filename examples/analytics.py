"""Print account-level analytics overview slices.

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

    overview = client.analytics.overview()
    engagement = client.analytics.engagement()
    messages = client.analytics.messages()

    print("overview:", overview.data)
    print("engagement:", engagement.data)
    print("messages:", messages.data)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
