"""Account-wide analytics resource."""

from __future__ import annotations

from collections.abc import Mapping, Sequence
from typing import TYPE_CHECKING, Any, cast

from mailermine_generated import AnalyticsApi

from mailermine.resources.base import BaseResource
from mailermine.support import Collection, Pagination, Response
from mailermine.support.serialization import to_response
from mailermine.types import JsonObject, JsonValue

if TYPE_CHECKING:
    from mailermine.resources.campaigns import Campaigns
    from mailermine.resources.events import Events


class Analytics(BaseResource):
    """Account-wide delivery and engagement analytics.

    Campaign-scoped filters are delegated to the campaigns resource so callers
    get consistent per-campaign metrics through the analytics API.
    """

    def __init__(
        self,
        analytics_api: AnalyticsApi,
        campaigns_resource: Campaigns,
        events_resource: Events,
        *,
        timeout: float,
    ) -> None:
        super().__init__(timeout=timeout)
        self._api = analytics_api
        self._campaigns = campaigns_resource
        self._events = events_resource

    def overview(
        self,
        filters: Mapping[str, Any] | None = None,
        /,
        **kwargs: Any,
    ) -> Response[object]:
        """Retrieve the analytics overview for a date range.

        Parameters
        ----------
        filters:
            Optional filters (``from``, ``to``, ``campaign``/``campaign_id``).
        **kwargs:
            Alternative keyword filters.

        Returns
        -------
        Response[object]
            Overview analytics payload.

        Raises
        ------
        ApiError
            On API or transport failures.

        Examples
        --------
        >>> client.analytics.overview(**{"from": "2030-01-01", "to": "2030-02-01"})
        """
        options = _merge(filters, kwargs)
        campaign_id = _campaign_id(options)
        if campaign_id is not None:
            return self._campaigns.analytics(campaign_id)
        return self._request("analytics_overview", options)

    def deliveries(
        self,
        filters: Mapping[str, Any] | None = None,
        /,
        **kwargs: Any,
    ) -> Response[JsonObject]:
        """Retrieve delivery metrics.

        Parameters
        ----------
        filters:
            Optional filters (``from``, ``to``, ``campaign``/``campaign_id``).
        **kwargs:
            Alternative keyword filters.

        Returns
        -------
        Response[object]
            Delivery metrics payload.

        Raises
        ------
        ApiError
            On API or transport failures.

        Examples
        --------
        >>> client.analytics.deliveries()
        """
        options = _merge(filters, kwargs)
        campaign_id = _campaign_id(options)
        if campaign_id is not None:
            return self._campaigns.deliveries(campaign_id)
        return self._message_slice(options, ("sent", "delivered"))

    def opens(
        self,
        filters: Mapping[str, Any] | None = None,
        /,
        **kwargs: Any,
    ) -> Response[JsonObject]:
        """Retrieve open metrics.

        Parameters
        ----------
        filters:
            Optional filters (``from``, ``to``, ``campaign``/``campaign_id``).
        **kwargs:
            Alternative keyword filters.

        Returns
        -------
        Response[object]
            Open metrics payload.

        Raises
        ------
        ApiError
            On API or transport failures.

        Examples
        --------
        >>> client.analytics.opens()
        """
        options = _merge(filters, kwargs)
        campaign_id = _campaign_id(options)
        if campaign_id is not None:
            return self._campaigns.opens(campaign_id)
        return self._engagement_slice(
            options, ("opens", "unique_opens", "open_rate", "sent", "delivered")
        )

    def clicks(
        self,
        filters: Mapping[str, Any] | None = None,
        /,
        **kwargs: Any,
    ) -> Response[JsonObject]:
        """Retrieve click metrics.

        Parameters
        ----------
        filters:
            Optional filters (``from``, ``to``, ``campaign``/``campaign_id``).
        **kwargs:
            Alternative keyword filters.

        Returns
        -------
        Response[object]
            Click metrics payload.

        Raises
        ------
        ApiError
            On API or transport failures.

        Examples
        --------
        >>> client.analytics.clicks()
        """
        options = _merge(filters, kwargs)
        campaign_id = _campaign_id(options)
        if campaign_id is not None:
            return self._campaigns.clicks(campaign_id)
        return self._engagement_slice(
            options, ("clicks", "unique_clicks", "ctr", "ctor", "sent", "delivered")
        )

    def bounces(
        self,
        filters: Mapping[str, Any] | None = None,
        /,
        **kwargs: Any,
    ) -> Response[JsonObject]:
        """Retrieve bounce metrics.

        Parameters
        ----------
        filters:
            Optional filters (``from``, ``to``, ``campaign``/``campaign_id``).
        **kwargs:
            Alternative keyword filters.

        Returns
        -------
        Response[object]
            Bounce metrics payload.

        Raises
        ------
        ApiError
            On API or transport failures.

        Examples
        --------
        >>> client.analytics.bounces()
        """
        options = _merge(filters, kwargs)
        campaign_id = _campaign_id(options)
        if campaign_id is not None:
            return self._campaigns.bounces(campaign_id)
        return self._message_slice(options, ("bounced", "sent", "delivered"))

    def complaints(
        self,
        filters: Mapping[str, Any] | None = None,
        /,
        **kwargs: Any,
    ) -> Response[JsonObject]:
        """Retrieve complaint metrics.

        Parameters
        ----------
        filters:
            Optional filters (``from``, ``to``, ``campaign``/``campaign_id``).
        **kwargs:
            Alternative keyword filters.

        Returns
        -------
        Response[object]
            Complaint metrics payload.

        Raises
        ------
        ApiError
            On API or transport failures.

        Examples
        --------
        >>> client.analytics.complaints()
        """
        options = _merge(filters, kwargs)
        campaign_id = _campaign_id(options)
        if campaign_id is not None:
            return self._campaigns.complaints(campaign_id)
        return self._message_slice(options, ("complained", "sent", "delivered"))

    def unsubscribes(
        self,
        filters: Mapping[str, Any] | None = None,
        /,
        **kwargs: Any,
    ) -> Response[JsonObject]:
        """Retrieve unsubscribe metrics or an event summary.

        Parameters
        ----------
        filters:
            Optional filters (``from``, ``to``, ``campaign``/``campaign_id``,
            ``per_page``).
        **kwargs:
            Alternative keyword filters.

        Returns
        -------
        Response[object]
            Unsubscribe metrics or event summary payload.

        Raises
        ------
        ApiError
            On API or transport failures.

        Examples
        --------
        >>> client.analytics.unsubscribes()
        """
        options = _merge(filters, kwargs)
        campaign_id = _campaign_id(options)
        if campaign_id is not None:
            return self._campaigns.unsubscribes(campaign_id)

        events = self._events.list(
            event_type="email.unsubscribed",
            from_=options.get("from", options.get("from_")),
            to=options.get("to"),
            per_page=options.get("per_page", 100),
        )
        summary: JsonObject = {
            "count": len(events),
            "events": cast("list[JsonValue]", list(events.items)),
        }
        return Response(summary, message="OK")

    def usage(
        self,
        filters: Mapping[str, Any] | None = None,
        /,
        **kwargs: Any,
    ) -> Response[JsonObject]:
        """Retrieve usage-oriented message totals.

        Parameters
        ----------
        filters:
            Optional filters (``from``, ``to``, ``campaign``/``campaign_id``).
        **kwargs:
            Alternative keyword filters.

        Returns
        -------
        Response[object]
            Usage totals payload.

        Raises
        ------
        ApiError
            On API or transport failures.

        Examples
        --------
        >>> client.analytics.usage()
        """
        options = _merge(filters, kwargs)
        campaign_id = _campaign_id(options)
        if campaign_id is not None:
            return self._campaigns.delivery(campaign_id)

        response = self.messages(options)
        totals = _totals(response.data)
        summary = _pick(totals, ("sent", "delivered", "opened", "clicked", "bounced", "complained"))
        return Response(summary, message=response.message, success=response.success)

    def activity(
        self,
        filters: Mapping[str, Any] | None = None,
        /,
        **kwargs: Any,
    ) -> Collection[object]:
        """Retrieve recent analytics activity.

        Parameters
        ----------
        filters:
            Optional filters (``from``, ``to``).
        **kwargs:
            Alternative keyword filters.

        Returns
        -------
        Collection[object]
            Recent activity entries.

        Raises
        ------
        ApiError
            On API or transport failures.

        Examples
        --------
        >>> client.analytics.activity()
        """
        options = _merge(filters, kwargs)
        response = self.overview(options)
        raw = _get(response.data, "recent_activity")
        items: list[object]
        if isinstance(raw, Sequence) and not isinstance(raw, (str, bytes, bytearray)):
            items = list(raw)
        else:
            items = []
        pagination = Pagination(
            current_page=1,
            per_page=len(items) or 1,
            total=len(items),
            last_page=1,
        )
        return Collection(
            items,
            pagination,
            message=response.message,
            success=response.success,
        )

    def messages(
        self,
        filters: Mapping[str, Any] | None = None,
        /,
        **kwargs: Any,
    ) -> Response[object]:
        """Retrieve message analytics.

        Parameters
        ----------
        filters:
            Optional filters (``from``, ``to``).
        **kwargs:
            Alternative keyword filters.

        Returns
        -------
        Response[object]
            Message analytics payload.

        Raises
        ------
        ApiError
            On API or transport failures.

        Examples
        --------
        >>> client.analytics.messages()
        """
        return self._request("analytics_messages", _merge(filters, kwargs))

    def engagement(
        self,
        filters: Mapping[str, Any] | None = None,
        /,
        **kwargs: Any,
    ) -> Response[object]:
        """Retrieve engagement analytics.

        Parameters
        ----------
        filters:
            Optional filters (``from``, ``to``).
        **kwargs:
            Alternative keyword filters.

        Returns
        -------
        Response[object]
            Engagement analytics payload.

        Raises
        ------
        ApiError
            On API or transport failures.

        Examples
        --------
        >>> client.analytics.engagement()
        """
        return self._request("analytics_engagement", _merge(filters, kwargs))

    def campaigns(
        self,
        filters: Mapping[str, Any] | None = None,
        /,
        **kwargs: Any,
    ) -> Response[object]:
        """Retrieve campaign ranking analytics.

        Parameters
        ----------
        filters:
            Optional filters (``from``, ``to``).
        **kwargs:
            Alternative keyword filters.

        Returns
        -------
        Response[object]
            Campaign ranking analytics payload.

        Raises
        ------
        ApiError
            On API or transport failures.

        Examples
        --------
        >>> client.analytics.campaigns()
        """
        return self._request("analytics_campaigns", _merge(filters, kwargs))

    def domains(
        self,
        filters: Mapping[str, Any] | None = None,
        /,
        **kwargs: Any,
    ) -> Response[object]:
        """Retrieve domain analytics.

        Parameters
        ----------
        filters:
            Optional filters (``from``, ``to``).
        **kwargs:
            Alternative keyword filters.

        Returns
        -------
        Response[object]
            Domain analytics payload.

        Raises
        ------
        ApiError
            On API or transport failures.

        Examples
        --------
        >>> client.analytics.domains()
        """
        return self._request("analytics_domains", _merge(filters, kwargs))

    def projects(
        self,
        filters: Mapping[str, Any] | None = None,
        /,
        **kwargs: Any,
    ) -> Response[object]:
        """Retrieve project analytics.

        Parameters
        ----------
        filters:
            Optional filters (``from``, ``to``).
        **kwargs:
            Alternative keyword filters.

        Returns
        -------
        Response[object]
            Project analytics payload.

        Raises
        ------
        ApiError
            On API or transport failures.

        Examples
        --------
        >>> client.analytics.projects()
        """
        return self._request("analytics_projects", _merge(filters, kwargs))

    def providers(
        self,
        filters: Mapping[str, Any] | None = None,
        /,
        **kwargs: Any,
    ) -> Response[object]:
        """Retrieve provider analytics.

        Parameters
        ----------
        filters:
            Optional filters (``from``, ``to``).
        **kwargs:
            Alternative keyword filters.

        Returns
        -------
        Response[object]
            Provider analytics payload.

        Raises
        ------
        ApiError
            On API or transport failures.

        Examples
        --------
        >>> client.analytics.providers()
        """
        return self._request("analytics_providers", _merge(filters, kwargs))

    # ------------------------------------------------------------------
    # Internal helpers
    # ------------------------------------------------------------------
    def _request(self, operation: str, filters: Mapping[str, Any]) -> Response[object]:
        method = getattr(self._api, operation)
        query = _date_query(filters)
        return self.execute(lambda: to_response(method(**query, _request_timeout=self._timeout)))

    def _message_slice(
        self,
        filters: Mapping[str, Any],
        keys: tuple[str, ...],
    ) -> Response[JsonObject]:
        response = self.messages(filters)
        totals = _totals(response.data)
        return Response(_pick(totals, keys), message=response.message, success=response.success)

    def _engagement_slice(
        self,
        filters: Mapping[str, Any],
        keys: tuple[str, ...],
    ) -> Response[JsonObject]:
        response = self.engagement(filters)
        return Response(
            _pick(response.data, keys),
            message=response.message,
            success=response.success,
        )


def _campaign_id(filters: Mapping[str, Any]) -> str | None:
    value = filters.get("campaign") or filters.get("campaign_id")
    if isinstance(value, str) and value != "":
        return value
    return None


def _date_query(filters: Mapping[str, Any]) -> dict[str, Any]:
    query: dict[str, Any] = {}
    from_value = filters.get("from", filters.get("from_"))
    if from_value is not None:
        query["var_from"] = _iso(from_value)
    to_value = filters.get("to")
    if to_value is not None:
        query["to"] = _iso(to_value)
    return query


def _totals(data: object) -> dict[str, Any]:
    index = _index(data)
    totals = index.get("totals")
    if isinstance(totals, Mapping):
        return _index(totals)
    return index


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
