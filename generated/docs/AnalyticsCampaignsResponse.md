# AnalyticsCampaignsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** |  | 
**message** | **str** |  | 
**data** | [**AnalyticsCampaigns**](AnalyticsCampaigns.md) |  | 

## Example

```python
from mailermine_generated.models.analytics_campaigns_response import AnalyticsCampaignsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AnalyticsCampaignsResponse from a JSON string
analytics_campaigns_response_instance = AnalyticsCampaignsResponse.from_json(json)
# print the JSON string representation of the object
print(AnalyticsCampaignsResponse.to_json())

# convert the object into a dict
analytics_campaigns_response_dict = analytics_campaigns_response_instance.to_dict()
# create an instance of AnalyticsCampaignsResponse from a dict
analytics_campaigns_response_from_dict = AnalyticsCampaignsResponse.from_dict(analytics_campaigns_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


