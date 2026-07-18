"""Create a contact export job and poll its status.

Requires ``MAILERMINE_API_KEY`` in the environment.

Set ``MAILERMINE_EXPORT_DOWNLOAD=1`` to attempt downloading CSV when the job is ready.
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
    created = client.exports.create()
    export_id = str(
        (created.data or {}).get("id") or (created.data or {}).get("uuid")
        if isinstance(created.data, dict)
        else created.data
    )
    print("created export:", export_id, created.message)

    status = client.exports.status(export_id)
    print("status:", status.data)

    if os.environ.get("MAILERMINE_EXPORT_DOWNLOAD") == "1":
        download = client.exports.download(export_id)
        payload = download.data if hasattr(download, "data") else download
        preview = str(payload)[:200]
        print("download preview:", preview)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
