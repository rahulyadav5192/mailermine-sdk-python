# AnalyticsEngagementResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** |  | 
**message** | **str** |  | 
**data** | [**AnalyticsEngagement**](AnalyticsEngagement.md) |  | 

## Example

```python
from mailermine_generated.models.analytics_engagement_response import AnalyticsEngagementResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AnalyticsEngagementResponse from a JSON string
analytics_engagement_response_instance = AnalyticsEngagementResponse.from_json(json)
# print the JSON string representation of the object
print(AnalyticsEngagementResponse.to_json())

# convert the object into a dict
analytics_engagement_response_dict = analytics_engagement_response_instance.to_dict()
# create an instance of AnalyticsEngagementResponse from a dict
analytics_engagement_response_from_dict = AnalyticsEngagementResponse.from_dict(analytics_engagement_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


