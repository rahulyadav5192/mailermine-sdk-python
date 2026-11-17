# MailerMine Python SDK: notes for Claude

This SDK mirrors the MailerMine API defined in `rahulyadav5192/resend`. Any
change that comes from an API change must follow the shared runbook:
**`docs/SDK_SYNC.md` in the resend repo** (https://github.com/rahulyadav5192/resend/blob/main/docs/SDK_SYNC.md).
`tests/test_parity.py` enforces method parity with `mailermine-node`. Update it when public methods change.

## Layout
- `generated/`: openapi-generator **7.23.0** `python` (urllib3) output via `scripts/generate.py`. Never edit it by hand.
- `openapi.json` + `openapi.normalized.json` (from `scripts/openapi_normalize.py`). Commit both.
- Hand-written: `mailermine/_internal/apis.py`, `mailermine/_internal/transport.py`
  (`ResilientApiClient`: retries, idempotency, rate limits), `mailermine/exceptions/__init__.py`,
  `mailermine/resources/*`, `mailermine/support/*`.

## Regenerate
```bash
python3 -m venv .venv && .venv/bin/pip install -e ".[dev]"
# put the 7.23.0 jar (SHA-256 cb087e40…9026) at .cache/openapi-generator/openapi-generator-cli-7.23.0.jar
.venv/bin/python scripts/generate.py --skip-download --skip-report   # git diff must be empty first
cp ../resend/public/openapi.json openapi.json
.venv/bin/python scripts/generate.py --skip-download --skip-report
.venv/bin/pip install -e ".[dev]"   # refresh the installed generated copy before running mypy
```

## Check
`.venv/bin/ruff check . && .venv/bin/ruff format --check mailermine tests && .venv/bin/mypy && .venv/bin/python -m pytest -q`

Success responses are parsed by strict pydantic models, so the spec must not mark omitted fields as required.

## Release
Bump `pyproject.toml`, `mailermine/constants.py` `VERSION`, and `CHANGELOG.md`.
