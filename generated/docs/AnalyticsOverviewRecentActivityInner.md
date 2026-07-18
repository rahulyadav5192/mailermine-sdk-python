# AnalyticsOverviewRecentActivityInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**event_type** | **str** |  | 
**event_label** | **str** |  | 
**occurred_at** | **str** |  | 
**message_uuid** | **str** |  | 

## Example

```python
from mailermine_generated.models.analytics_overview_recent_activity_inner import AnalyticsOverviewRecentActivityInner

# TODO update the JSON string below
json = "{}"
# create an instance of AnalyticsOverviewRecentActivityInner from a JSON string
analytics_overview_recent_activity_inner_instance = AnalyticsOverviewRecentActivityInner.from_json(json)
# print the JSON string representation of the object
print(AnalyticsOverviewRecentActivityInner.to_json())

# convert the object into a dict
analytics_overview_recent_activity_inner_dict = analytics_overview_recent_activity_inner_instance.to_dict()
# create an instance of AnalyticsOverviewRecentActivityInner from a dict
analytics_overview_recent_activity_inner_from_dict = AnalyticsOverviewRecentActivityInner.from_dict(analytics_overview_recent_activity_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


