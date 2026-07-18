# Phase 3 — Handwritten Wrapper

**Status:** Complete  
**Deliverable:** [WRAPPER_REPORT.md](WRAPPER_REPORT.md)

## Summary

- Public client: `from mailermine import MailerMine`
- 18 resources with Node/Laravel method parity (snake_case)
- `Response` / `Collection` / `Pagination`
- Exception hierarchy with generated-error mapping
- Configuration + env vars (`MAILERMINE_API_KEY`, `MAILERMINE_BASE_URL`, `MAILERMINE_TIMEOUT`)
- Generated package never re-exported

## Commands

```bash
ruff check mailermine tests
mypy mailermine
pytest
```
