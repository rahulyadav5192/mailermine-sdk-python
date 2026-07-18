# MailerMine Python SDK

Official MailerMine SDK for Python — send transactional email, run campaigns, manage
contacts, and read analytics with a clean, typed API.

[![PyPI](https://img.shields.io/pypi/v/mailermine.svg)](https://pypi.org/project/mailermine/)
[![Python](https://img.shields.io/pypi/pyversions/mailermine.svg)](https://pypi.org/project/mailermine/)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)

Parity with [`@mailermine/node`](https://www.npmjs.com/package/@mailermine/node) and
[`mailermine/mailermine`](https://packagist.org/packages/mailermine/mailermine) across
all **18** resources.

---

## Installation

```bash
pip install mailermine
```

```bash
poetry add mailermine
```

```bash
uv add mailermine
```

**Requirements:** Python 3.10+

---

## Quick Start

```python
from mailermine import MailerMine

client = MailerMine(
    api_key="relay_live_xxx"
)

response = client.emails.send(
    from_="info@example.com",
    to=["john@example.com"],
    subject="Hello",
    html="<h1>Hello</h1>",
)

print(response.data)
```

Or load credentials from the environment:

```python
import os
from mailermine import MailerMine

client = MailerMine(api_key=os.environ["MAILERMINE_API_KEY"])
```

---

## Configuration

```python
from mailermine import MailerMine, Configuration

client = MailerMine(
    api_key="relay_live_xxx",
    base_url="https://mailermine.com/api/v1",
    timeout=30.0,
)

# Or build configuration explicitly:
config = Configuration.create(
    api_key="relay_live_xxx",
    base_url="https://mailermine.com/api/v1",
    timeout=30.0,
)
client = MailerMine(configuration=config)
```

### Environment variables

| Variable | Purpose |
| --- | --- |
| `MAILERMINE_API_KEY` | Bearer API key (used when `api_key` is omitted) |
| `MAILERMINE_BASE_URL` | API base URL (default `https://mailermine.com/api/v1`) |
| `MAILERMINE_TIMEOUT` | Request timeout in **seconds** (default `30`) |

```python
# Reads MAILERMINE_API_KEY / MAILERMINE_BASE_URL / MAILERMINE_TIMEOUT
client = MailerMine()
```

| Option | Type | Default | Description |
| --- | --- | --- | --- |
| `api_key` | `str` | — | Required MailerMine API key |
| `base_url` | `str` | `https://mailermine.com/api/v1` | API base URL |
| `timeout` | `float` | `30.0` | Request timeout in seconds |
| `user_agent` | `str` | `mailermine-python/1.0.0` | User-Agent header |

---

## Resources

### Projects

```python
client.projects.create(name="Production", environment="production")
client.projects.list()
client.projects.get(project_id)
client.projects.update(project_id, name="Prod")
client.projects.delete(project_id)
```

### API Keys

```python
client.api_keys.create(project_id, name="CI", scopes=["send"])
client.api_keys.list(project_id)
client.api_keys.get(project_id, api_key_id)
client.api_keys.update(project_id, api_key_id, name="CI Bot")
client.api_keys.rotate(project_id, api_key_id)
client.api_keys.reveal(project_id, api_key_id)
client.api_keys.delete(project_id, api_key_id)
```

### Emails

```python
client.emails.send(
    from_="MailerMine <hello@example.com>",
    to=["user@example.com"],
    subject="Invoice ready",
    html="<p>Your invoice is ready.</p>",
    text="Your invoice is ready.",
    reply_to="support@example.com",
    tags=["invoice"],
    metadata={"order_id": "123"},
)

client.emails.list(status="delivered", per_page=25)
client.emails.get(message_id)
client.emails.events(message_id)
```

> Use `from_` as a keyword argument (or pass `"from"` inside a dict) because `from` is reserved in Python.

### Domains

```python
created = client.domains.create(domain="mail.example.com")
domain_id = created.data["id"]

client.domains.list()
client.domains.get(domain_id)
client.domains.dns_records(domain_id)
client.domains.status(domain_id)
client.domains.verify(domain_id)
client.domains.delete(domain_id)
```

### Templates

```python
client.templates.create(
    name="Welcome",
    subject="Welcome {{first_name}}",
    html="<h1>Welcome {{first_name}}</h1>",
)
client.templates.list(search="welcome")
client.templates.get(template_id)
client.templates.update(template_id, subject="Hey {{first_name}}")
client.templates.preview(template_id, variables={"first_name": "John"})
client.templates.duplicate(template_id, name="Welcome (copy)")
client.templates.test(template_id, to="you@example.com")
client.templates.delete(template_id)
```

### Contacts

```python
client.contacts.create(email="john@example.com", first_name="John")
client.contacts.upsert(email="john@example.com", first_name="Johnny")
client.contacts.list(page=1, per_page=25)
client.contacts.get(contact_id)
client.contacts.identify("john@example.com")
client.contacts.search("john")
client.contacts.update(contact_id, last_name="Doe")
client.contacts.subscribe(contact_id)
client.contacts.unsubscribe(contact_id)
client.contacts.delete(contact_id)
```

### Lists

```python
client.lists.create(name="Newsletter")
client.lists.list()
client.lists.get(list_id)
client.lists.update(list_id, name="Weekly")
client.lists.add_contact(list_id, contact_ids)
client.lists.remove_contact(list_id, contact_ids)
client.lists.delete(list_id)
```

### Segments

```python
client.segments.create(name="Active users", rules={...})
client.segments.list()
client.segments.get(segment_id)
client.segments.update(segment_id, name="Engaged")
client.segments.preview(segment_id)
client.segments.delete(segment_id)
```

### Tags

```python
client.tags.create(name="vip")
client.tags.list()
client.tags.get(tag_id)
client.tags.update(tag_id, name="VIP")
client.tags.assign(contact_ids=[...], tag_ids=[...])
client.tags.remove(contact_ids=[...], tag_ids=[...])
client.tags.delete(tag_id)
```

### Audiences

```python
client.audiences.list()
client.audiences.get("list", audience_id)
client.audiences.create(source="list", name="Launch list")
client.audiences.contacts("list", audience_id)
client.audiences.add_contacts(audience_id, contact_ids)
client.audiences.remove_contacts(audience_id, contact_ids)
```

### Campaigns

```python
client.campaigns.create(name="Spring launch")
client.campaigns.list(status="draft")
client.campaigns.get(campaign_id)
client.campaigns.update(campaign_id, subject="Hello")
client.campaigns.set_template(campaign_id, template_id)
client.campaigns.set_subject(campaign_id, "Spring sale")
client.campaigns.set_sender(campaign_id, from_email="hello@example.com", from_name="Team")
client.campaigns.set_reply_to(campaign_id, "support@example.com")
client.campaigns.set_preheader(campaign_id, "Don't miss it")
client.campaigns.preview(campaign_id)
client.campaigns.render(campaign_id)
client.campaigns.validate(campaign_id)
client.campaigns.mark_ready(campaign_id)
client.campaigns.send(campaign_id)
client.campaigns.schedule(campaign_id, scheduled_at="2026-07-20T10:00:00Z")
client.campaigns.pause(campaign_id)
client.campaigns.resume(campaign_id)
client.campaigns.cancel(campaign_id)
client.campaigns.analytics(campaign_id)
client.campaigns.events(campaign_id)
client.campaigns.timeline(campaign_id)
client.campaigns.activity(campaign_id)
client.campaigns.progress(campaign_id)
client.campaigns.status(campaign_id)
```

### Analytics

```python
client.analytics.overview()
client.analytics.usage()
client.analytics.messages()
client.analytics.engagement()
client.analytics.campaigns()
client.analytics.domains()
client.analytics.projects()
client.analytics.providers()
client.analytics.activity()
client.analytics.opens()
client.analytics.clicks()
client.analytics.deliveries()
client.analytics.bounces()
client.analytics.complaints()
client.analytics.unsubscribes()
```

### Events

```python
client.events.list(event_type="delivered")
client.events.get(event_id)
client.events.timeline(message_id)
client.events.history(message_id)
client.events.message(message_id)
```

### Messages

```python
client.messages.list(status="delivered")
client.messages.search("invoice")
client.messages.filter(status="bounced")
client.messages.get(message_id)
client.messages.events(message_id)
client.messages.timeline(message_id)
```

### Webhooks

```python
client.webhooks.create(url="https://example.com/hooks/mailermine", events=["email.delivered"])
client.webhooks.list()
client.webhooks.get(webhook_id)
client.webhooks.update(webhook_id, url="https://example.com/hooks/v2")
client.webhooks.enable(webhook_id)
client.webhooks.disable(webhook_id)
client.webhooks.rotate_secret(webhook_id)
client.webhooks.test(webhook_id)
client.webhooks.deliveries(webhook_id)
client.webhooks.delivery(delivery_id)
client.webhooks.logs(webhook_id)
client.webhooks.failures(webhook_id)
client.webhooks.replay(webhook_id)
client.webhooks.retry(delivery_id)
client.webhooks.delete(webhook_id)

# Local signature verification (no network):
from mailermine import Webhooks

Webhooks.verify(raw_body, signature_header, signing_secret)
```

### Suppressions

```python
client.suppressions.add(email="bounce@example.com", reason="hard_bounce")
client.suppressions.list()
client.suppressions.get(suppression_id)
client.suppressions.check("bounce@example.com")
client.suppressions.restore(suppression_id)
client.suppressions.remove(suppression_id)
```

### Imports

```python
client.imports.create(...)
client.imports.list()
client.imports.status(import_id)
client.imports.configure(import_id, ...)
client.imports.start(import_id)
```

### Exports

```python
job = client.exports.create()
client.exports.status(job.data["id"])
csv_body = client.exports.download(job.data["id"])
```

---

## Response Objects

Successful calls return `Response` or `Collection` — never generated OpenAPI models.

### Response

```python
response = client.emails.send(...)

response.success   # bool
response.message   # str
response.data      # primary payload (dict / list / scalar)
response.meta      # optional metadata
response.to_dict() # JSON-serializable envelope
```

### Collection

```python
page = client.contacts.list(page=1, per_page=25)

page.items                 # list of items on this page
page.pagination            # Pagination
len(page)                  # page size
page[0]                    # index access
for contact in page:       # iterable
    print(contact["email"])
```

### Pagination

```python
meta = page.pagination
meta.current_page
meta.per_page
meta.total
meta.last_page
meta.has_next_page
meta.has_previous_page
```

---

## Exception Handling

```python
from mailermine import (
    MailerMine,
    AuthenticationError,
    ValidationError,
    NotFoundError,
    PlanError,
    RateLimitError,
    ApiError,
)

client = MailerMine(api_key="relay_live_xxx")

try:
    client.emails.send(from_="hello@example.com", to="user@example.com", subject="Hi", html="<p>Hi</p>")
except ValidationError as e:
    print(e.errors)          # field -> messages
except AuthenticationError:
    print("Check your API key")
except PlanError as e:
    print(e.upgrade_url)
except NotFoundError:
    print("Missing resource")
except RateLimitError as e:
    print(e.retry_after)     # seconds, or None
except ApiError as e:
    print(e.status, e.request_id, e.body)
```

| Exception | Typical cause |
| --- | --- |
| `AuthenticationError` | Invalid / missing API key (401) |
| `PlanError` | Plan or scope restriction (403) |
| `NotFoundError` | Missing object (404) |
| `ValidationError` | Invalid payload (422) |
| `RateLimitError` | Too many requests (429) |
| `ApiError` | Other HTTP / transport failures |
| `MailerMineError` | Base type for all SDK errors |

Generated OpenAPI exceptions are never exposed.

---

## Examples

Runnable scripts live in [`examples/`](examples):

| File | Topic |
| --- | --- |
| `send_email.py` | Transactional send |
| `campaign.py` | Campaign lifecycle |
| `contacts.py` | Contacts + lists |
| `analytics.py` | Account analytics |
| `domains.py` | Domains + DNS |
| `templates.py` | Templates |
| `webhooks.py` | Webhooks + verify |
| `messages.py` | Message history |
| `events.py` | Event stream |
| `imports.py` | Contact imports |
| `exports.py` | Contact exports |

```bash
export MAILERMINE_API_KEY=relay_live_xxx
python examples/send_email.py
```

---

## Development

```bash
python -m venv .venv
source .venv/bin/activate
pip install -e ".[dev]"
ruff check mailermine tests
mypy mailermine
pytest
python -m build
```

OpenAPI client code is generated into `generated/` and must not be edited by hand.
See [ARCHITECTURE.md](ARCHITECTURE.md), [GENERATION_REPORT.md](GENERATION_REPORT.md),
[WRAPPER_REPORT.md](WRAPPER_REPORT.md), and [PARITY_REPORT.md](PARITY_REPORT.md).

---

## Support

- Docs: https://mailermine.com/docs
- Issues: https://github.com/rahulyadav5192/mailermine-sdk-python/issues
- Email: support@mailermine.com

## License

MIT — see [LICENSE](LICENSE).
# mailermine-sdk-python
