# AnalyticsOverviewTracking

Delivered emails and how many had opens / clicks tracked (the rate denominators).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**delivered** | **int** |  | 
**opens_tracked** | **int** |  | 
**clicks_tracked** | **int** |  | 

## Example

```python
from mailermine_generated.models.analytics_overview_tracking import AnalyticsOverviewTracking

# TODO update the JSON string below
json = "{}"
# create an instance of AnalyticsOverviewTracking from a JSON string
analytics_overview_tracking_instance = AnalyticsOverviewTracking.from_json(json)
# print the JSON string representation of the object
print(AnalyticsOverviewTracking.to_json())

# convert the object into a dict
analytics_overview_tracking_dict = analytics_overview_tracking_instance.to_dict()
# create an instance of AnalyticsOverviewTracking from a dict
analytics_overview_tracking_from_dict = AnalyticsOverviewTracking.from_dict(analytics_overview_tracking_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


