# AnalyticsOverview


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**emails_sent** | **int** | Total emails sent in the selected range. | 
**campaigns** | **int** | Number of campaigns that sent in the selected range. | 
**delivery_rate** | **float** | Delivered / sent as a percentage. | 
**open_rate** | **float** | Unique opens / delivered as a percentage. | 
**click_rate** | **float** | Unique clicks / delivered as a percentage. | 
**bounce_rate** | **float** | Bounced / sent as a percentage. | 
**complaint_rate** | **float** | Complaints / sent as a percentage. | 
**daily_series** | [**List[AnalyticsOverviewDailySeriesInner]**](AnalyticsOverviewDailySeriesInner.md) | Daily performance series. | 
**top_campaigns** | [**List[AnalyticsOverviewTopCampaignsInner]**](AnalyticsOverviewTopCampaignsInner.md) | Top campaigns by volume. | 
**top_links** | [**List[AnalyticsOverviewTopLinksInner]**](AnalyticsOverviewTopLinksInner.md) | Top tracked links by clicks. | 
**recent_activity** | [**List[AnalyticsOverviewRecentActivityInner]**](AnalyticsOverviewRecentActivityInner.md) | Recent recipient activity. | 

## Example

```python
from mailermine_generated.models.analytics_overview import AnalyticsOverview

# TODO update the JSON string below
json = "{}"
# create an instance of AnalyticsOverview from a JSON string
analytics_overview_instance = AnalyticsOverview.from_json(json)
# print the JSON string representation of the object
print(AnalyticsOverview.to_json())

# convert the object into a dict
analytics_overview_dict = analytics_overview_instance.to_dict()
# create an instance of AnalyticsOverview from a dict
analytics_overview_from_dict = AnalyticsOverview.from_dict(analytics_overview_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


