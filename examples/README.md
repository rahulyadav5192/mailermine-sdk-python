# Examples

Independent scripts for the MailerMine Python SDK.

```bash
export MAILERMINE_API_KEY=relay_live_xxx
python examples/send_email.py
```

| Script | Description |
| --- | --- |
| `send_email.py` | Send a transactional email |
| `campaign.py` | List campaigns and read analytics |
| `contacts.py` | Upsert a contact and list contacts |
| `analytics.py` | Account analytics overview |
| `domains.py` | Domains, status, DNS records |
| `templates.py` | List and preview templates |
| `webhooks.py` | List webhooks + local `verify` demo |
| `messages.py` | Message history + timeline |
| `events.py` | Global event stream |
| `imports.py` | Import job status |
| `exports.py` | Create/status (optional download) |

Install the SDK first (`pip install mailermine` or `pip install -e .` from the repo root).
