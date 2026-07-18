"""List campaigns and fetch analytics for the first result.

Requires ``MAILERMINE_API_KEY`` in the environment.
"""

from __future__ import annotations

import os
import sys

from mailermine import MailerMine, NotFoundError


def main() -> int:
    api_key = os.environ.get("MAILERMINE_API_KEY")
    if not api_key:
        print("Set MAILERMINE_API_KEY before running this example.", file=sys.stderr)
        return 1

    client = MailerMine(api_key=api_key)
    campaigns = client.campaigns.list(per_page=5)
    print(f"Found {len(campaigns)} campaign(s) on this page (total={campaigns.pagination.total})")

    if not campaigns.items:
        print("No campaigns yet — create one in the dashboard, then re-run.")
        return 0

    first = campaigns.items[0]
    campaign_id = str(first.get("id") or first.get("uuid"))
    print("campaign:", campaign_id, first.get("name"), first.get("status"))

    try:
        status = client.campaigns.status(campaign_id)
        analytics = client.campaigns.analytics(campaign_id)
    except NotFoundError:
        print("Campaign disappeared before analytics could be loaded.", file=sys.stderr)
        return 1

    print("status:", status.data)
    print("analytics:", analytics.data)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
