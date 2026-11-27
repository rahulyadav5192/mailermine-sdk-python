"""Open/click tracking options on sends and project settings."""

from __future__ import annotations

import json
from typing import Any

from test_resilience import EMAIL, _client, _response, _sent


def _body(history: list[dict[str, Any]], index: int = 0) -> dict[str, Any]:
    body = history[index]["body"]
    return body if isinstance(body, dict) else json.loads(body)


def test_send_passes_tracking_overrides() -> None:
    client, history = _client([_sent(), _sent()])

    client.emails.send({**EMAIL, "tracking": {"opens": True, "clicks": False}})
    client.emails.send(EMAIL)

    assert _body(history)["tracking"] == {"opens": True, "clicks": False}
    assert "tracking" not in _body(history, 1)


def test_send_accepts_tracking_as_keyword() -> None:
    client, history = _client([_sent()])

    client.emails.send(EMAIL, tracking={"clicks": False})

    assert _body(history)["tracking"] == {"clicks": False}


def test_project_settings_keep_tracking_and_custom_keys() -> None:
    project = {"success": True, "data": {"id": "p1", "name": "P"}}
    client, history = _client([_response(201, project), _response(200, project)])

    client.projects.create(
        {
            "name": "P",
            "settings": {"region": "eu-west-1", "tracking": {"opens": True, "clicks": False}},
        }
    )
    client.projects.update(
        "2f6c1f0e-9a7b-4c1d-8e2f-3a4b5c6d7e8f", {"settings": {"tracking": {"clicks": True}}}
    )

    assert _body(history)["settings"] == {
        "region": "eu-west-1",
        "tracking": {"opens": True, "clicks": False},
    }
    assert _body(history, 1)["settings"] == {"tracking": {"clicks": True}}


def test_free_form_request_fields_are_sent_intact() -> None:
    """Regression: metadata/headers/variables used to be sent as None."""
    client, history = _client([_sent()])

    client.emails.send(
        {
            **EMAIL,
            "metadata": {"order_id": "1042"},
            "headers": {"X-Customer-ID": "42"},
            "variables": {"first_name": "Ada"},
        }
    )

    body = _body(history)
    assert body["metadata"] == {"order_id": "1042"}
    assert body["headers"] == {"X-Customer-ID": "42"}
    assert body["variables"] == {"first_name": "Ada"}


def test_webhook_payload_types_are_public() -> None:
    from mailermine import WebhookClick, WebhookEventPayload, WebhookOpen

    click: WebhookClick = {
        "url": "https://example.com",
        "link_id": "l1",
        "is_unique": True,
        "clicked_at": None,
    }
    opened: WebhookOpen = {"is_unique": False, "opened_at": None}
    payload: WebhookEventPayload = {"type": "email.clicked", "click": click, "open": opened}
    assert payload["click"]["url"] == "https://example.com"


_ENGAGEMENT_BASE = {
    "from": "2026-11-01T00:00:00+00:00",
    "to": "2026-11-27T00:00:00+00:00",
    "opens": 2,
    "unique_opens": 2,
    "clicks": 1,
    "unique_clicks": 1,
    "open_rate": 50.0,
    "ctr": 25.0,
    "ctor": 50.0,
    "sent": 8,
    "delivered": 8,
}


def test_engagement_model_accepts_responses_with_and_without_tracking_fields() -> None:
    """Strict models must parse both new servers and servers deployed before the fields existed."""
    from mailermine_generated.models.analytics_engagement import AnalyticsEngagement

    old = AnalyticsEngagement.from_dict(_ENGAGEMENT_BASE)
    assert old is not None
    assert old.by_tracking_domain is None

    new = AnalyticsEngagement.from_dict(
        {
            **_ENGAGEMENT_BASE,
            "opens_tracked_delivered": 4,
            "clicks_tracked_delivered": 4,
            "by_tracking_domain": [
                {
                    "id": "2f6c1f0e-9a7b-4c1d-8e2f-3a4b5c6d7e8f",
                    "hostname": "links.acme.com",
                    "status": "verified",
                    "status_label": "Active",
                    "is_default": True,
                    "last_checked_at": None,
                    "last_error": None,
                    "sent": 2,
                    "delivered": 2,
                    "unique_opens": 1,
                    "unique_clicks": 1,
                    "open_rate": 50.0,
                    "click_rate": 50.0,
                },
                {
                    "id": None,
                    "hostname": None,
                    "status": "shared",
                    "status_label": "Shared host",
                    "is_default": False,
                    "last_checked_at": None,
                    "last_error": None,
                    "sent": 6,
                    "delivered": 6,
                    "unique_opens": 1,
                    "unique_clicks": 0,
                    "open_rate": 16.7,
                    "click_rate": 0.0,
                },
            ],
        }
    )
    assert new is not None
    assert new.opens_tracked_delivered == 4
    assert new.by_tracking_domain is not None
    assert new.by_tracking_domain[0].hostname == "links.acme.com"
    assert new.by_tracking_domain[1].hostname is None
