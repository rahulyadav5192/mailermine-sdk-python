# CampaignTimelineResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** |  | 
**message** | **str** |  | 
**data** | [**List[CampaignTimeline]**](CampaignTimeline.md) |  | 

## Example

```python
from mailermine_generated.models.campaign_timeline_response import CampaignTimelineResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CampaignTimelineResponse from a JSON string
campaign_timeline_response_instance = CampaignTimelineResponse.from_json(json)
# print the JSON string representation of the object
print(CampaignTimelineResponse.to_json())

# convert the object into a dict
campaign_timeline_response_dict = campaign_timeline_response_instance.to_dict()
# create an instance of CampaignTimelineResponse from a dict
campaign_timeline_response_from_dict = CampaignTimelineResponse.from_dict(campaign_timeline_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


