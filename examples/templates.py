"""List templates and preview the first one when present.

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
    templates = client.templates.list(per_page=10)
    print(f"templates on page: {len(templates)} / total {templates.pagination.total}")

    if not templates.items:
        print("No templates yet.")
        return 0

    first = templates.items[0]
    template_id = str(first.get("id") or first.get("uuid"))
    print("template:", template_id, first.get("name"))

    preview = client.templates.preview(template_id, variables={"first_name": "Alex"})
    print("preview:", preview.data)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
