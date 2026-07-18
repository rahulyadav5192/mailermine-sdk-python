"""List contact import jobs and print status for the first result.

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
    imports = client.imports.list()
    print(f"imports on page: {len(imports)}")

    if not imports.items:
        print("No import jobs yet.")
        return 0

    first = imports.items[0]
    import_id = str(first.get("id") or first.get("uuid"))
    status = client.imports.status(import_id)
    print("import:", import_id)
    print("status:", status.data)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
