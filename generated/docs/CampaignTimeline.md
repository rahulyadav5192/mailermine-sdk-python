# CampaignTimeline


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**event_type** | **str** | Machine-readable delivery event type. @example delivered | 
**event_label** | **str** |  | 
**occurred_at** | **str** | Event time. @format date-time | 
**payload** | [**CampaignActivityPayload**](CampaignActivityPayload.md) |  | 

## Example

```python
from mailermine_generated.models.campaign_timeline import CampaignTimeline

# TODO update the JSON string below
json = "{}"
# create an instance of CampaignTimeline from a JSON string
campaign_timeline_instance = CampaignTimeline.from_json(json)
# print the JSON string representation of the object
print(CampaignTimeline.to_json())

# convert the object into a dict
campaign_timeline_dict = campaign_timeline_instance.to_dict()
# create an instance of CampaignTimeline from a dict
campaign_timeline_from_dict = CampaignTimeline.from_dict(campaign_timeline_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


