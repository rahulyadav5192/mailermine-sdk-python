# CampaignAnalyticsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**CampaignAnalytics**](CampaignAnalytics.md) |  | 
**top_links** | [**List[CampaignLink]**](CampaignLink.md) |  | 

## Example

```python
from mailermine_generated.models.campaign_analytics_response import CampaignAnalyticsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CampaignAnalyticsResponse from a JSON string
campaign_analytics_response_instance = CampaignAnalyticsResponse.from_json(json)
# print the JSON string representation of the object
print(CampaignAnalyticsResponse.to_json())

# convert the object into a dict
campaign_analytics_response_dict = campaign_analytics_response_instance.to_dict()
# create an instance of CampaignAnalyticsResponse from a dict
campaign_analytics_response_from_dict = CampaignAnalyticsResponse.from_dict(campaign_analytics_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


