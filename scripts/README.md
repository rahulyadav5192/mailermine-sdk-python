# Scripts

| Script | Purpose |
| --- | --- |
| `generate.py` | Download https://www.mailermine.com/openapi.json and regenerate `../generated/` with OpenAPI Generator (`python` / `urllib3`) |

```bash
python scripts/generate.py
# or reuse a local pin:
python scripts/generate.py --skip-download
```

Never edit `generated/` by hand. See [GENERATION_REPORT.md](../GENERATION_REPORT.md).
