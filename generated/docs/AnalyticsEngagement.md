# AnalyticsEngagement


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_from** | **str** | Range start (ISO-8601). | 
**to** | **str** | Range end (ISO-8601). | 
**opens** | **int** | Total opens. | 
**unique_opens** | **int** | Unique opens. | 
**clicks** | **int** | Total clicks. | 
**unique_clicks** | **int** | Unique clicks. | 
**open_rate** | **float** | Unique opens / delivered emails that had open tracking, as a percentage. | 
**ctr** | **float** | Click-through rate: unique clicks / delivered emails that had click tracking, as a percentage. | 
**ctor** | **float** | Click-to-open rate: clicks / opens as a percentage. | 
**sent** | **int** | Total sent. | 
**delivered** | **int** | Total delivered. | 
**opens_tracked_delivered** | **int** | Delivered emails that had open tracking (the open-rate denominator). | [optional] 
**clicks_tracked_delivered** | **int** | Delivered emails that had click tracking (the CTR denominator). | [optional] 
**by_tracking_domain** | [**List[AnalyticsEngagementByTrackingDomainInner]**](AnalyticsEngagementByTrackingDomainInner.md) | Volume and engagement per custom tracking domain. The row with &#x60;hostname: null&#x60; is the shared host. Empty when no tracking domain is configured. | [optional] 

## Example

```python
from mailermine_generated.models.analytics_engagement import AnalyticsEngagement

# TODO update the JSON string below
json = "{}"
# create an instance of AnalyticsEngagement from a JSON string
analytics_engagement_instance = AnalyticsEngagement.from_json(json)
# print the JSON string representation of the object
print(AnalyticsEngagement.to_json())

# convert the object into a dict
analytics_engagement_dict = analytics_engagement_instance.to_dict()
# create an instance of AnalyticsEngagement from a dict
analytics_engagement_from_dict = AnalyticsEngagement.from_dict(analytics_engagement_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


