"""Campaign resource.

Provides a cohesive campaign API over the generated campaigns, lifecycle,
analytics, and events clients.
"""

from __future__ import annotations

from collections.abc import Mapping
from typing import Any

from mailermine_generated import (
    CampaignAnalyticsApi,
    CampaignEventsApi,
    CampaignLifecycleApi,
    CampaignsApi,
)

from mailermine.exceptions import ValidationError
from mailermine.resources.base import BaseResource
from mailermine.support import Collection, Response
from mailermine.support.serialization import (
    data_id,
    deleted_response,
    to_collection,
    to_generated_request,
    to_response,
)
from mailermine.types import JsonObject

_STATUS_KEYS = (
    "uuid",
    "status",
    "status_label",
    "send_immediately",
    "scheduled_at",
    "timezone",
    "sent_at",
    "started_at",
    "completed_at",
    "last_processed_at",
)

_NULLABLE_KEYS = frozenset(
    {
        "subject",
        "preview_text",
        "from_name",
        "from_email",
        "reply_to",
        "template_uuid",
        "segment_uuid",
        "scheduled_at",
        "timezone",
    }
)


class Campaigns(BaseResource):
    """Campaign operations spanning create, lifecycle, analytics, and events."""

    def __init__(
        self,
        campaigns_api: CampaignsApi,
        lifecycle_api: CampaignLifecycleApi,
        analytics_api: CampaignAnalyticsApi,
        events_api: CampaignEventsApi,
        *,
        timeout: float,
    ) -> None:
        super().__init__(timeout=timeout)
        self._campaigns = campaigns_api
        self._lifecycle = lifecycle_api
        self._analytics = analytics_api
        self._events = events_api

    # ------------------------------------------------------------------
    # Core CRUD
    # ------------------------------------------------------------------
    def create(
        self,
        payload: Mapping[str, Any] | None = None,
        /,
        **kwargs: Any,
    ) -> Response[object]:
        """Create a campaign.

        The create endpoint accepts only a name. Any extra configuration is
        applied immediately through a follow-up update so callers can create a
        fully configured draft in a single SDK call.

        Parameters
        ----------
        payload:
            Campaign fields as a mapping. Must include ``name``.
        **kwargs:
            Alternative keyword fields merged into the request body.

        Returns
        -------
        Response[object]
            Created campaign payload.

        Raises
        ------
        ValidationError
            When ``name`` is missing.
        ApiError
            On API or transport failures.

        Examples
        --------
        >>> client.campaigns.create(name="Launch", subject="Hello")
        """
        normalized = _normalize_params(_merge(payload, kwargs))
        name = normalized.get("name")
        if not isinstance(name, str) or name == "":
            raise ValidationError("The name field is required.")

        created = self.execute(
            lambda: to_response(
                self._campaigns.create_campaign(
                    create_campaign_request=to_generated_request({"name": name}),  # type: ignore[arg-type]
                    _request_timeout=self._timeout,
                )
            )
        )

        configuration = _extract_configuration(normalized)
        if not configuration:
            return created
        return self.update(data_id(created, "uuid", "id"), configuration)

    def list(self, **options: Any) -> Collection[object]:
        """List campaigns with filters and pagination.

        Parameters
        ----------
        **options:
            Optional filters such as ``search``, ``status``, ``page``,
            ``per_page``.

        Returns
        -------
        Collection[object]
            Paginated campaign list.

        Raises
        ------
        ApiError
            On API or transport failures.

        Examples
        --------
        >>> client.campaigns.list(status="draft")
        """
        return self.execute(
            lambda: to_collection(
                self._campaigns.list_campaigns(
                    **_query(options),
                    _request_timeout=self._timeout,
                )
            )
        )

    def get(self, campaign_id: str) -> Response[object]:
        """Retrieve a campaign by UUID.

        Parameters
        ----------
        campaign_id:
            Campaign UUID.

        Returns
        -------
        Response[object]
            Campaign payload.

        Raises
        ------
        NotFoundError
            When the campaign does not exist.
        ApiError
            On API or transport failures.

        Examples
        --------
        >>> client.campaigns.get("cmp_123")
        """
        return self.execute(
            lambda: to_response(
                self._campaigns.get_campaign(
                    campaign=campaign_id,  # type: ignore[arg-type]
                    _request_timeout=self._timeout,
                )
            )
        )

    def update(
        self,
        campaign_id: str,
        payload: Mapping[str, Any] | None = None,
        /,
        **kwargs: Any,
    ) -> Response[object]:
        """Partially update an editable campaign.

        Parameters
        ----------
        campaign_id:
            Campaign UUID.
        payload:
            Fields to update as a mapping.
        **kwargs:
            Alternative keyword fields merged into the request body.

        Returns
        -------
        Response[object]
            Updated campaign payload.

        Raises
        ------
        NotFoundError
            When the campaign does not exist.
        ValidationError
            When the update payload is invalid.
        ApiError
            On API or transport failures.

        Examples
        --------
        >>> client.campaigns.update("cmp_123", subject="New subject")
        """
        body = to_generated_request(_normalize_params(_merge(payload, kwargs)))
        return self._apply_update(campaign_id, body)

    def delete(self, campaign_id: str) -> Response[JsonObject]:
        """Soft-delete a campaign.

        Parameters
        ----------
        campaign_id:
            Campaign UUID.

        Returns
        -------
        Response[JsonObject]
            Delete acknowledgement (``{"deleted": True}``).

        Raises
        ------
        NotFoundError
            When the campaign does not exist.
        ApiError
            On API or transport failures.

        Examples
        --------
        >>> client.campaigns.delete("cmp_123")
        """

        def operation() -> Response[JsonObject]:
            envelope = to_response(
                self._campaigns.delete_campaign(
                    campaign=campaign_id,  # type: ignore[arg-type]
                    _request_timeout=self._timeout,
                )
            )
            return deleted_response(envelope.message, envelope.success)

        return self.execute(operation)

    def duplicate(
        self,
        campaign_id: str,
        payload: Mapping[str, Any] | None = None,
        /,
        **kwargs: Any,
    ) -> Response[object]:
        """Duplicate a campaign.

        Parameters
        ----------
        campaign_id:
            Campaign UUID.
        payload:
            Optional duplicate fields as a mapping (``include_schedule``, …).
        **kwargs:
            Alternative keyword fields merged into the request body.

        Returns
        -------
        Response[object]
            Duplicated campaign payload.

        Raises
        ------
        NotFoundError
            When the campaign does not exist.
        ApiError
            On API or transport failures.

        Examples
        --------
        >>> client.campaigns.duplicate("cmp_123")
        """
        merged = _merge(payload, kwargs)
        body = to_generated_request(merged) if merged else None
        return self.execute(
            lambda: to_response(
                self._lifecycle.duplicate_campaign(
                    campaign=campaign_id,  # type: ignore[arg-type]
                    duplicate_campaign_request=body,  # type: ignore[arg-type]
                    _request_timeout=self._timeout,
                )
            )
        )

    def archive(self, campaign_id: str) -> Response[object]:
        """Archive a campaign.

        Parameters
        ----------
        campaign_id:
            Campaign UUID.

        Returns
        -------
        Response[object]
            Archived campaign payload.

        Raises
        ------
        NotFoundError
            When the campaign does not exist.
        ApiError
            On API or transport failures.

        Examples
        --------
        >>> client.campaigns.archive("cmp_123")
        """
        return self.execute(
            lambda: to_response(
                self._lifecycle.archive_campaign(
                    campaign=campaign_id,  # type: ignore[arg-type]
                    _request_timeout=self._timeout,
                )
            )
        )

    def restore(self, campaign_id: str) -> Response[object]:
        """Restore an archived or soft-deleted campaign.

        Parameters
        ----------
        campaign_id:
            Campaign UUID.

        Returns
        -------
        Response[object]
            Restored campaign payload.

        Raises
        ------
        NotFoundError
            When the campaign does not exist.
        ApiError
            On API or transport failures.

        Examples
        --------
        >>> client.campaigns.restore("cmp_123")
        """
        return self.execute(
            lambda: to_response(
                self._lifecycle.restore_campaign(
                    campaign_uuid=campaign_id,  # type: ignore[arg-type]
                    _request_timeout=self._timeout,
                )
            )
        )

    # ------------------------------------------------------------------
    # Configuration setters
    # ------------------------------------------------------------------
    def set_subject(self, campaign_id: str, subject: str) -> Response[object]:
        """Set the campaign subject.

        Parameters
        ----------
        campaign_id:
            Campaign UUID.
        subject:
            New subject line.

        Returns
        -------
        Response[object]
            Updated campaign payload.

        Raises
        ------
        NotFoundError
            When the campaign does not exist.
        ApiError
            On API or transport failures.

        Examples
        --------
        >>> client.campaigns.set_subject("cmp_123", "Welcome!")
        """
        return self._apply_update(campaign_id, {"subject": subject})

    def set_sender(
        self,
        campaign_id: str,
        sender: str | Mapping[str, Any],
        from_name: str | None = None,
    ) -> Response[object]:
        """Set the campaign sender.

        Parameters
        ----------
        campaign_id:
            Campaign UUID.
        sender:
            Sender email string, or a mapping with ``from_email`` / ``from_name``.
        from_name:
            Optional sender display name when ``sender`` is a string.

        Returns
        -------
        Response[object]
            Updated campaign payload.

        Raises
        ------
        NotFoundError
            When the campaign does not exist.
        ApiError
            On API or transport failures.

        Examples
        --------
        >>> client.campaigns.set_sender("cmp_123", "hi@example.com", "Team")
        """
        body: dict[str, Any] = {}
        if isinstance(sender, Mapping):
            if "from_email" in sender:
                body["from_email"] = sender["from_email"]
            if "from_name" in sender:
                body["from_name"] = sender["from_name"]
        else:
            body["from_email"] = sender
            if from_name is not None:
                body["from_name"] = from_name
        return self._apply_update(campaign_id, body)

    def set_reply_to(self, campaign_id: str, reply_to: str | None) -> Response[object]:
        """Set the campaign reply-to address.

        Parameters
        ----------
        campaign_id:
            Campaign UUID.
        reply_to:
            Reply-to address, or ``None`` to clear it.

        Returns
        -------
        Response[object]
            Updated campaign payload.

        Raises
        ------
        NotFoundError
            When the campaign does not exist.
        ApiError
            On API or transport failures.

        Examples
        --------
        >>> client.campaigns.set_reply_to("cmp_123", "reply@example.com")
        """
        return self._apply_update(campaign_id, {"reply_to": reply_to})

    def set_preheader(self, campaign_id: str, preheader: str | None) -> Response[object]:
        """Set the campaign preheader / preview text.

        Parameters
        ----------
        campaign_id:
            Campaign UUID.
        preheader:
            Preview text, or ``None`` to clear it.

        Returns
        -------
        Response[object]
            Updated campaign payload.

        Raises
        ------
        NotFoundError
            When the campaign does not exist.
        ApiError
            On API or transport failures.

        Examples
        --------
        >>> client.campaigns.set_preheader("cmp_123", "A quick note")
        """
        return self._apply_update(campaign_id, {"preview_text": preheader})

    def set_template(self, campaign_id: str, template_id: str) -> Response[object]:
        """Set the campaign template.

        Parameters
        ----------
        campaign_id:
            Campaign UUID.
        template_id:
            Published template UUID.

        Returns
        -------
        Response[object]
            Updated campaign payload.

        Raises
        ------
        NotFoundError
            When the campaign does not exist.
        ApiError
            On API or transport failures.

        Examples
        --------
        >>> client.campaigns.set_template("cmp_123", "tpl_456")
        """
        return self._apply_update(campaign_id, {"template_uuid": template_id})

    def add_segment(self, campaign_id: str, segment_id: str) -> Response[object]:
        """Attach a segment to a campaign.

        Parameters
        ----------
        campaign_id:
            Campaign UUID.
        segment_id:
            Segment UUID.

        Returns
        -------
        Response[object]
            Updated campaign payload.

        Raises
        ------
        NotFoundError
            When the campaign does not exist.
        ApiError
            On API or transport failures.

        Examples
        --------
        >>> client.campaigns.add_segment("cmp_123", "seg_456")
        """
        return self._apply_update(campaign_id, {"segment_uuid": segment_id})

    def add_audience(self, campaign_id: str, audience_id: str) -> Response[object]:
        """Attach an audience (segment) to a campaign.

        Parameters
        ----------
        campaign_id:
            Campaign UUID.
        audience_id:
            Segment UUID backing the audience.

        Returns
        -------
        Response[object]
            Updated campaign payload.

        Raises
        ------
        NotFoundError
            When the campaign does not exist.
        ApiError
            On API or transport failures.

        Examples
        --------
        >>> client.campaigns.add_audience("cmp_123", "seg_456")
        """
        return self.add_segment(campaign_id, audience_id)

    def remove_segment(self, campaign_id: str) -> Response[object]:
        """Remove the attached segment from a campaign.

        Parameters
        ----------
        campaign_id:
            Campaign UUID.

        Returns
        -------
        Response[object]
            Updated campaign payload.

        Raises
        ------
        NotFoundError
            When the campaign does not exist.
        ApiError
            On API or transport failures.

        Examples
        --------
        >>> client.campaigns.remove_segment("cmp_123")
        """
        return self._apply_update(campaign_id, {"segment_uuid": None})

    def remove_audience(self, campaign_id: str) -> Response[object]:
        """Remove the attached audience from a campaign.

        Parameters
        ----------
        campaign_id:
            Campaign UUID.

        Returns
        -------
        Response[object]
            Updated campaign payload.

        Raises
        ------
        NotFoundError
            When the campaign does not exist.
        ApiError
            On API or transport failures.

        Examples
        --------
        >>> client.campaigns.remove_audience("cmp_123")
        """
        return self.remove_segment(campaign_id)

    # ------------------------------------------------------------------
    # Recipients & validation
    # ------------------------------------------------------------------
    def recipient_count(self, campaign_id: str) -> Response[JsonObject]:
        """Estimate recipient counts for a campaign.

        Parameters
        ----------
        campaign_id:
            Campaign UUID.

        Returns
        -------
        Response[JsonObject]
            Recipient count summary.

        Raises
        ------
        NotFoundError
            When the campaign does not exist.
        ApiError
            On API or transport failures.

        Examples
        --------
        >>> client.campaigns.recipient_count("cmp_123")
        """
        preview = self.preview_recipients(campaign_id)
        data = preview.data
        estimated = _get(data, "estimated_count")
        summary: JsonObject = {
            "count": estimated if isinstance(estimated, (int, float)) else 0,
            "estimated_count": estimated,
            "subscribed_count": _get(data, "subscribed_count"),
            "unsubscribed_count": _get(data, "unsubscribed_count"),
            "suppressed_count": _get(data, "suppressed_count"),
        }
        return Response(summary, message=preview.message, success=preview.success)

    def preview_recipients(self, campaign_id: str) -> Response[object]:
        """Preview estimated recipients for a campaign.

        Parameters
        ----------
        campaign_id:
            Campaign UUID.

        Returns
        -------
        Response[object]
            Recipient preview payload.

        Raises
        ------
        NotFoundError
            When the campaign does not exist.
        ApiError
            On API or transport failures.

        Examples
        --------
        >>> client.campaigns.preview_recipients("cmp_123")
        """
        return self.execute(
            lambda: to_response(
                self._campaigns.preview_campaign_recipients(
                    campaign=campaign_id,  # type: ignore[arg-type]
                    _request_timeout=self._timeout,
                )
            )
        )

    def validate(self, campaign_id: str) -> Response[object]:
        """Validate campaign readiness.

        Parameters
        ----------
        campaign_id:
            Campaign UUID.

        Returns
        -------
        Response[object]
            Validation result payload.

        Raises
        ------
        NotFoundError
            When the campaign does not exist.
        ApiError
            On API or transport failures.

        Examples
        --------
        >>> client.campaigns.validate("cmp_123")
        """
        return self.execute(
            lambda: to_response(
                self._campaigns.validate_campaign(
                    campaign=campaign_id,  # type: ignore[arg-type]
                    _request_timeout=self._timeout,
                )
            )
        )

    # ------------------------------------------------------------------
    # Lifecycle
    # ------------------------------------------------------------------
    def mark_ready(self, campaign_id: str) -> Response[object]:
        """Mark a campaign as ready to send or schedule.

        Parameters
        ----------
        campaign_id:
            Campaign UUID.

        Returns
        -------
        Response[object]
            Updated campaign payload.

        Raises
        ------
        NotFoundError
            When the campaign does not exist.
        ApiError
            On API or transport failures.

        Examples
        --------
        >>> client.campaigns.mark_ready("cmp_123")
        """
        return self.execute(
            lambda: to_response(
                self._lifecycle.ready_campaign(
                    campaign=campaign_id,  # type: ignore[arg-type]
                    _request_timeout=self._timeout,
                )
            )
        )

    def send(self, campaign_id: str) -> Response[object]:
        """Send a ready campaign immediately.

        Parameters
        ----------
        campaign_id:
            Campaign UUID.

        Returns
        -------
        Response[object]
            Updated campaign payload.

        Raises
        ------
        NotFoundError
            When the campaign does not exist.
        ApiError
            On API or transport failures.

        Examples
        --------
        >>> client.campaigns.send("cmp_123")
        """
        return self.execute(
            lambda: to_response(
                self._lifecycle.send_campaign(
                    campaign=campaign_id,  # type: ignore[arg-type]
                    _request_timeout=self._timeout,
                )
            )
        )

    def schedule(
        self,
        campaign_id: str,
        payload: Mapping[str, Any] | None = None,
        /,
        **kwargs: Any,
    ) -> Response[object]:
        """Schedule a campaign for later delivery.

        Parameters
        ----------
        campaign_id:
            Campaign UUID.
        payload:
            Schedule fields (``scheduled_at``, ``timezone``, ``send_immediately``).
        **kwargs:
            Alternative keyword fields merged into the request body.

        Returns
        -------
        Response[object]
            Updated campaign payload.

        Raises
        ------
        NotFoundError
            When the campaign does not exist.
        ValidationError
            When the schedule payload is invalid.
        ApiError
            On API or transport failures.

        Examples
        --------
        >>> client.campaigns.schedule("cmp_123", scheduled_at="2030-01-01T00:00:00Z")
        """
        options = _merge(payload, kwargs)
        body = to_generated_request(
            {
                "send_immediately": options.get("send_immediately", False),
                "scheduled_at": _iso(options.get("scheduled_at")),
                "timezone": options.get("timezone", "UTC"),
            }
        )
        return self.execute(
            lambda: to_response(
                self._lifecycle.schedule_campaign(
                    campaign=campaign_id,  # type: ignore[arg-type]
                    schedule_campaign_request=body,  # type: ignore[arg-type]
                    _request_timeout=self._timeout,
                )
            )
        )

    def reschedule(
        self,
        campaign_id: str,
        payload: Mapping[str, Any] | None = None,
        /,
        **kwargs: Any,
    ) -> Response[object]:
        """Reschedule an already scheduled campaign.

        Parameters
        ----------
        campaign_id:
            Campaign UUID.
        payload:
            Schedule fields (``scheduled_at``, ``timezone``).
        **kwargs:
            Alternative keyword fields merged into the request body.

        Returns
        -------
        Response[object]
            Updated campaign payload.

        Raises
        ------
        NotFoundError
            When the campaign does not exist.
        ApiError
            On API or transport failures.

        Examples
        --------
        >>> client.campaigns.reschedule("cmp_123", scheduled_at="2030-02-01T00:00:00Z")
        """
        return self.schedule(campaign_id, _merge(payload, kwargs))

    def unschedule(
        self,
        campaign_id: str,
        payload: Mapping[str, Any] | None = None,
        /,
        **kwargs: Any,
    ) -> Response[object]:
        """Clear a pending campaign schedule.

        Parameters
        ----------
        campaign_id:
            Campaign UUID.
        payload:
            Optional fields (``timezone``).
        **kwargs:
            Alternative keyword fields merged into the request body.

        Returns
        -------
        Response[object]
            Updated campaign payload.

        Raises
        ------
        NotFoundError
            When the campaign does not exist.
        ApiError
            On API or transport failures.

        Examples
        --------
        >>> client.campaigns.unschedule("cmp_123")
        """
        options = _merge(payload, kwargs)
        body: dict[str, Any] = {"send_immediately": False, "scheduled_at": None}
        if "timezone" in options:
            body["timezone"] = options["timezone"]
        return self._apply_update(campaign_id, body)

    def send_now(
        self,
        campaign_id: str,
        payload: Mapping[str, Any] | None = None,
        /,
        **kwargs: Any,
    ) -> Response[object]:
        """Queue a campaign for immediate delivery via the schedule endpoint.

        Parameters
        ----------
        campaign_id:
            Campaign UUID.
        payload:
            Optional fields (``timezone``).
        **kwargs:
            Alternative keyword fields merged into the request body.

        Returns
        -------
        Response[object]
            Updated campaign payload.

        Raises
        ------
        NotFoundError
            When the campaign does not exist.
        ApiError
            On API or transport failures.

        Examples
        --------
        >>> client.campaigns.send_now("cmp_123")
        """
        options = _merge(payload, kwargs)
        return self.schedule(
            campaign_id,
            {"send_immediately": True, "timezone": options.get("timezone", "UTC")},
        )

    def pause(self, campaign_id: str) -> Response[object]:
        """Pause a sending campaign.

        Parameters
        ----------
        campaign_id:
            Campaign UUID.

        Returns
        -------
        Response[object]
            Updated campaign payload.

        Raises
        ------
        NotFoundError
            When the campaign does not exist.
        ApiError
            On API or transport failures.

        Examples
        --------
        >>> client.campaigns.pause("cmp_123")
        """
        return self.execute(
            lambda: to_response(
                self._lifecycle.pause_campaign(
                    campaign=campaign_id,  # type: ignore[arg-type]
                    _request_timeout=self._timeout,
                )
            )
        )

    def resume(self, campaign_id: str) -> Response[object]:
        """Resume a paused campaign.

        Parameters
        ----------
        campaign_id:
            Campaign UUID.

        Returns
        -------
        Response[object]
            Updated campaign payload.

        Raises
        ------
        NotFoundError
            When the campaign does not exist.
        ApiError
            On API or transport failures.

        Examples
        --------
        >>> client.campaigns.resume("cmp_123")
        """
        return self.execute(
            lambda: to_response(
                self._lifecycle.resume_campaign(
                    campaign=campaign_id,  # type: ignore[arg-type]
                    _request_timeout=self._timeout,
                )
            )
        )

    def cancel(self, campaign_id: str) -> Response[object]:
        """Cancel a scheduled or sending campaign.

        Parameters
        ----------
        campaign_id:
            Campaign UUID.

        Returns
        -------
        Response[object]
            Updated campaign payload.

        Raises
        ------
        NotFoundError
            When the campaign does not exist.
        ApiError
            On API or transport failures.

        Examples
        --------
        >>> client.campaigns.cancel("cmp_123")
        """
        return self.execute(
            lambda: to_response(
                self._lifecycle.cancel_campaign(
                    campaign=campaign_id,  # type: ignore[arg-type]
                    _request_timeout=self._timeout,
                )
            )
        )

    def cancel_schedule(self, campaign_id: str) -> Response[object]:
        """Cancel a pending schedule.

        Parameters
        ----------
        campaign_id:
            Campaign UUID.

        Returns
        -------
        Response[object]
            Updated campaign payload.

        Raises
        ------
        NotFoundError
            When the campaign does not exist.
        ApiError
            On API or transport failures.

        Examples
        --------
        >>> client.campaigns.cancel_schedule("cmp_123")
        """
        return self.cancel(campaign_id)

    # ------------------------------------------------------------------
    # Content
    # ------------------------------------------------------------------
    def preview(self, campaign_id: str) -> Response[object]:
        """Preview rendered campaign content.

        Parameters
        ----------
        campaign_id:
            Campaign UUID.

        Returns
        -------
        Response[object]
            Rendered campaign preview payload.

        Raises
        ------
        NotFoundError
            When the campaign does not exist.
        ApiError
            On API or transport failures.

        Examples
        --------
        >>> client.campaigns.preview("cmp_123")
        """
        return self.execute(
            lambda: to_response(
                self._campaigns.preview_campaign(
                    campaign=campaign_id,  # type: ignore[arg-type]
                    _request_timeout=self._timeout,
                )
            )
        )

    def render(self, campaign_id: str) -> Response[object]:
        """Render campaign content.

        Alias of :meth:`preview` for content workflows.

        Parameters
        ----------
        campaign_id:
            Campaign UUID.

        Returns
        -------
        Response[object]
            Rendered campaign preview payload.

        Raises
        ------
        NotFoundError
            When the campaign does not exist.
        ApiError
            On API or transport failures.

        Examples
        --------
        >>> client.campaigns.render("cmp_123")
        """
        return self.preview(campaign_id)

    def status(self, campaign_id: str) -> Response[JsonObject]:
        """Retrieve a status summary for a campaign.

        Parameters
        ----------
        campaign_id:
            Campaign UUID.

        Returns
        -------
        Response[JsonObject]
            Compact status summary.

        Raises
        ------
        NotFoundError
            When the campaign does not exist.
        ApiError
            On API or transport failures.

        Examples
        --------
        >>> client.campaigns.status("cmp_123")
        """
        response = self.get(campaign_id)
        summary = _pick(response.data, _STATUS_KEYS)
        return Response(summary, message=response.message, success=response.success)

    def progress(self, campaign_id: str) -> Response[object]:
        """Retrieve campaign send progress.

        Parameters
        ----------
        campaign_id:
            Campaign UUID.

        Returns
        -------
        Response[object]
            Progress payload.

        Raises
        ------
        NotFoundError
            When the campaign does not exist.
        ApiError
            On API or transport failures.

        Examples
        --------
        >>> client.campaigns.progress("cmp_123")
        """
        return self.execute(
            lambda: to_response(
                self._lifecycle.get_campaign_progress(
                    campaign=campaign_id,  # type: ignore[arg-type]
                    _request_timeout=self._timeout,
                )
            )
        )

    # ------------------------------------------------------------------
    # Analytics
    # ------------------------------------------------------------------
    def analytics(self, campaign_id: str) -> Response[object]:
        """Retrieve campaign analytics.

        Parameters
        ----------
        campaign_id:
            Campaign UUID.

        Returns
        -------
        Response[object]
            Analytics payload.

        Raises
        ------
        NotFoundError
            When the campaign does not exist.
        ApiError
            On API or transport failures.

        Examples
        --------
        >>> client.campaigns.analytics("cmp_123")
        """
        return self.execute(
            lambda: to_response(
                self._analytics.campaign_analytics(
                    campaign=campaign_id,  # type: ignore[arg-type]
                    _request_timeout=self._timeout,
                )
            )
        )

    def opens(self, campaign_id: str) -> Response[JsonObject]:
        """Retrieve open metrics for a campaign.

        Parameters
        ----------
        campaign_id:
            Campaign UUID.

        Returns
        -------
        Response[JsonObject]
            Open metric slice.

        Raises
        ------
        ApiError
            On API or transport failures.

        Examples
        --------
        >>> client.campaigns.opens("cmp_123")
        """
        return self._analytics_slice(campaign_id, ("opened", "unique_opens", "open_rate"))

    def clicks(self, campaign_id: str) -> Response[JsonObject]:
        """Retrieve click metrics for a campaign.

        Parameters
        ----------
        campaign_id:
            Campaign UUID.

        Returns
        -------
        Response[JsonObject]
            Click metric slice.

        Raises
        ------
        ApiError
            On API or transport failures.

        Examples
        --------
        >>> client.campaigns.clicks("cmp_123")
        """
        return self._analytics_slice(campaign_id, ("clicked", "unique_clicks", "click_rate"))

    def bounces(self, campaign_id: str) -> Response[JsonObject]:
        """Retrieve bounce metrics for a campaign.

        Parameters
        ----------
        campaign_id:
            Campaign UUID.

        Returns
        -------
        Response[JsonObject]
            Bounce metric slice.

        Raises
        ------
        ApiError
            On API or transport failures.

        Examples
        --------
        >>> client.campaigns.bounces("cmp_123")
        """
        return self._analytics_slice(campaign_id, ("bounced", "bounce_rate"))

    def complaints(self, campaign_id: str) -> Response[JsonObject]:
        """Retrieve complaint metrics for a campaign.

        Parameters
        ----------
        campaign_id:
            Campaign UUID.

        Returns
        -------
        Response[JsonObject]
            Complaint metric slice.

        Raises
        ------
        ApiError
            On API or transport failures.

        Examples
        --------
        >>> client.campaigns.complaints("cmp_123")
        """
        return self._analytics_slice(campaign_id, ("complained", "complaint_rate"))

    def unsubscribes(self, campaign_id: str) -> Response[JsonObject]:
        """Retrieve unsubscribe metrics for a campaign.

        Parameters
        ----------
        campaign_id:
            Campaign UUID.

        Returns
        -------
        Response[JsonObject]
            Unsubscribe metric slice.

        Raises
        ------
        ApiError
            On API or transport failures.

        Examples
        --------
        >>> client.campaigns.unsubscribes("cmp_123")
        """
        return self._analytics_slice(campaign_id, ("unsubscribed", "unsubscribe_rate"))

    def deliveries(self, campaign_id: str) -> Response[JsonObject]:
        """Retrieve delivery count metrics for a campaign.

        Parameters
        ----------
        campaign_id:
            Campaign UUID.

        Returns
        -------
        Response[JsonObject]
            Delivery metric slice.

        Raises
        ------
        ApiError
            On API or transport failures.

        Examples
        --------
        >>> client.campaigns.deliveries("cmp_123")
        """
        return self._analytics_slice(campaign_id, ("delivered", "delivery_rate", "sent", "failed"))

    def delivery(self, campaign_id: str) -> Response[JsonObject]:
        """Retrieve delivery-focused analytics for a campaign.

        Parameters
        ----------
        campaign_id:
            Campaign UUID.

        Returns
        -------
        Response[JsonObject]
            Delivery-focused metric slice.

        Raises
        ------
        ApiError
            On API or transport failures.

        Examples
        --------
        >>> client.campaigns.delivery("cmp_123")
        """
        return self._analytics_slice(
            campaign_id,
            (
                "recipients",
                "queued",
                "sent",
                "delivered",
                "failed",
                "delivery_rate",
                "failure_rate",
                "average_delivery_time_seconds",
            ),
        )

    def links(self, campaign_id: str) -> Collection[object]:
        """Retrieve tracked campaign links.

        Parameters
        ----------
        campaign_id:
            Campaign UUID.

        Returns
        -------
        Collection[object]
            Tracked links.

        Raises
        ------
        NotFoundError
            When the campaign does not exist.
        ApiError
            On API or transport failures.

        Examples
        --------
        >>> client.campaigns.links("cmp_123")
        """
        return self.execute(
            lambda: to_collection(
                self._analytics.campaign_links(
                    campaign=campaign_id,  # type: ignore[arg-type]
                    _request_timeout=self._timeout,
                )
            )
        )

    # ------------------------------------------------------------------
    # Events
    # ------------------------------------------------------------------
    def events(self, campaign_id: str) -> Collection[object]:
        """Retrieve campaign events.

        Parameters
        ----------
        campaign_id:
            Campaign UUID.

        Returns
        -------
        Collection[object]
            Campaign events.

        Raises
        ------
        NotFoundError
            When the campaign does not exist.
        ApiError
            On API or transport failures.

        Examples
        --------
        >>> client.campaigns.events("cmp_123")
        """
        return self.execute(
            lambda: to_collection(
                self._events.campaign_events(
                    campaign=campaign_id,  # type: ignore[arg-type]
                    _request_timeout=self._timeout,
                )
            )
        )

    def activity(self, campaign_id: str) -> Collection[object]:
        """Retrieve campaign activity entries.

        Parameters
        ----------
        campaign_id:
            Campaign UUID.

        Returns
        -------
        Collection[object]
            Campaign activity entries.

        Raises
        ------
        NotFoundError
            When the campaign does not exist.
        ApiError
            On API or transport failures.

        Examples
        --------
        >>> client.campaigns.activity("cmp_123")
        """
        return self.execute(
            lambda: to_collection(
                self._events.campaign_activities(
                    campaign=campaign_id,  # type: ignore[arg-type]
                    _request_timeout=self._timeout,
                )
            )
        )

    def timeline(self, campaign_id: str) -> Collection[object]:
        """Retrieve the campaign timeline.

        Parameters
        ----------
        campaign_id:
            Campaign UUID.

        Returns
        -------
        Collection[object]
            Campaign timeline entries.

        Raises
        ------
        NotFoundError
            When the campaign does not exist.
        ApiError
            On API or transport failures.

        Examples
        --------
        >>> client.campaigns.timeline("cmp_123")
        """
        return self.execute(
            lambda: to_collection(
                self._events.campaign_timeline(
                    campaign=campaign_id,  # type: ignore[arg-type]
                    _request_timeout=self._timeout,
                )
            )
        )

    def recipients(self, campaign_id: str, **options: Any) -> Collection[object]:
        """List campaign recipients with optional filters.

        Parameters
        ----------
        campaign_id:
            Campaign UUID.
        **options:
            Optional filters such as ``search``, ``status``, ``page``.

        Returns
        -------
        Collection[object]
            Paginated recipient list.

        Raises
        ------
        NotFoundError
            When the campaign does not exist.
        ApiError
            On API or transport failures.

        Examples
        --------
        >>> client.campaigns.recipients("cmp_123", status="opened")
        """
        return self.execute(
            lambda: to_collection(
                self._events.campaign_recipients(
                    campaign=campaign_id,  # type: ignore[arg-type]
                    **_query(options),
                    _request_timeout=self._timeout,
                )
            )
        )

    # ------------------------------------------------------------------
    # Internal helpers
    # ------------------------------------------------------------------
    def _apply_update(self, campaign_id: str, body: Mapping[str, Any]) -> Response[object]:
        return self.execute(
            lambda: to_response(
                self._campaigns.update_campaign(
                    campaign=campaign_id,  # type: ignore[arg-type]
                    update_campaign_request=dict(body),  # type: ignore[arg-type]
                    _request_timeout=self._timeout,
                )
            )
        )

    def _analytics_slice(
        self,
        campaign_id: str,
        keys: tuple[str, ...],
    ) -> Response[JsonObject]:
        response = self.analytics(campaign_id)
        return Response(
            _pick(response.data, keys),
            message=response.message,
            success=response.success,
        )


def _normalize_params(parameters: Mapping[str, Any]) -> dict[str, Any]:
    normalized: dict[str, Any] = dict(parameters)
    if "template_id" in normalized and "template_uuid" not in normalized:
        normalized["template_uuid"] = normalized["template_id"]
    if "segment_id" in normalized and "segment_uuid" not in normalized:
        normalized["segment_uuid"] = normalized["segment_id"]
    if "audience_id" in normalized and "segment_uuid" not in normalized:
        normalized["segment_uuid"] = normalized["audience_id"]
    if "preheader" in normalized and "preview_text" not in normalized:
        normalized["preview_text"] = normalized["preheader"]
    for key in ("template_id", "segment_id", "audience_id", "preheader"):
        normalized.pop(key, None)
    return normalized


def _extract_configuration(parameters: Mapping[str, Any]) -> dict[str, Any]:
    result: dict[str, Any] = {}
    for key, value in parameters.items():
        if key == "name":
            continue
        if value is not None or key in _NULLABLE_KEYS:
            result[key] = value
    return result


def _iso(value: Any) -> Any:
    if value is None:
        return None
    if hasattr(value, "isoformat") and callable(value.isoformat):
        return value.isoformat()
    return value


def _merge(payload: Mapping[str, Any] | None, kwargs: Mapping[str, Any]) -> dict[str, Any]:
    merged: dict[str, Any] = dict(payload or {})
    merged.update({key: value for key, value in kwargs.items() if value is not None})
    return merged


def _query(options: Mapping[str, Any]) -> dict[str, Any]:
    return {key: value for key, value in options.items() if value is not None}


def _snake(value: str) -> str:
    chars: list[str] = []
    for index, char in enumerate(value):
        previous = value[index - 1] if index > 0 else ""
        if char.isupper() and (previous.islower() or previous.isdigit()):
            chars.append("_")
        chars.append(char.lower())
    return "".join(chars)


def _index(data: object) -> dict[str, Any]:
    if isinstance(data, Mapping):
        return {_snake(str(key)): value for key, value in data.items()}
    return {}


def _get(data: object, key: str) -> Any:
    return _index(data).get(_snake(key))


def _pick(data: object, keys: tuple[str, ...]) -> JsonObject:
    index = _index(data)
    return {key: index[_snake(key)] for key in keys if _snake(key) in index}
