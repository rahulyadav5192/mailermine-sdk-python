# CampaignEventsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[CampaignEvent]**](CampaignEvent.md) |  | 

## Example

```python
from mailermine_generated.models.campaign_events_response import CampaignEventsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CampaignEventsResponse from a JSON string
campaign_events_response_instance = CampaignEventsResponse.from_json(json)
# print the JSON string representation of the object
print(CampaignEventsResponse.to_json())

# convert the object into a dict
campaign_events_response_dict = campaign_events_response_instance.to_dict()
# create an instance of CampaignEventsResponse from a dict
campaign_events_response_from_dict = CampaignEventsResponse.from_dict(campaign_events_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


