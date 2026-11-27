# AnalyticsEngagementByTrackingDomainInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**hostname** | **str** |  | 
**status** | **str** |  | 
**status_label** | **str** |  | 
**is_default** | **bool** |  | 
**last_checked_at** | **str** |  | 
**last_error** | **str** |  | 
**sent** | **int** |  | 
**delivered** | **int** |  | 
**unique_opens** | **int** |  | 
**unique_clicks** | **int** |  | 
**open_rate** | **float** |  | 
**click_rate** | **float** |  | 

## Example

```python
from mailermine_generated.models.analytics_engagement_by_tracking_domain_inner import AnalyticsEngagementByTrackingDomainInner

# TODO update the JSON string below
json = "{}"
# create an instance of AnalyticsEngagementByTrackingDomainInner from a JSON string
analytics_engagement_by_tracking_domain_inner_instance = AnalyticsEngagementByTrackingDomainInner.from_json(json)
# print the JSON string representation of the object
print(AnalyticsEngagementByTrackingDomainInner.to_json())

# convert the object into a dict
analytics_engagement_by_tracking_domain_inner_dict = analytics_engagement_by_tracking_domain_inner_instance.to_dict()
# create an instance of AnalyticsEngagementByTrackingDomainInner from a dict
analytics_engagement_by_tracking_domain_inner_from_dict = AnalyticsEngagementByTrackingDomainInner.from_dict(analytics_engagement_by_tracking_domain_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


