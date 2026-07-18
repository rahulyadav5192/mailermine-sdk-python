# CampaignStatisticsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** |  | 
**message** | **str** |  | 
**data** | [**CampaignStatistics**](CampaignStatistics.md) |  | 

## Example

```python
from mailermine_generated.models.campaign_statistics_response import CampaignStatisticsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CampaignStatisticsResponse from a JSON string
campaign_statistics_response_instance = CampaignStatisticsResponse.from_json(json)
# print the JSON string representation of the object
print(CampaignStatisticsResponse.to_json())

# convert the object into a dict
campaign_statistics_response_dict = campaign_statistics_response_instance.to_dict()
# create an instance of CampaignStatisticsResponse from a dict
campaign_statistics_response_from_dict = CampaignStatisticsResponse.from_dict(campaign_statistics_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


