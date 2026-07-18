# AnalyticsOverviewResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** |  | 
**message** | **str** |  | 
**data** | [**AnalyticsOverview**](AnalyticsOverview.md) |  | 

## Example

```python
from mailermine_generated.models.analytics_overview_response import AnalyticsOverviewResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AnalyticsOverviewResponse from a JSON string
analytics_overview_response_instance = AnalyticsOverviewResponse.from_json(json)
# print the JSON string representation of the object
print(AnalyticsOverviewResponse.to_json())

# convert the object into a dict
analytics_overview_response_dict = analytics_overview_response_instance.to_dict()
# create an instance of AnalyticsOverviewResponse from a dict
analytics_overview_response_from_dict = AnalyticsOverviewResponse.from_dict(analytics_overview_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


