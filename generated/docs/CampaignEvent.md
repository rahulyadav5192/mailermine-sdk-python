# CampaignEvent


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uuid** | **str** | Event UUID. @format uuid | 
**event_type** | **str** | Delivery or engagement event type. @example clicked | 
**event_label** | **str** |  | 
**source** | **str** | Event ingestion source. | 
**payload** | [**CampaignActivityPayload**](CampaignActivityPayload.md) |  | 
**occurred_at** | **str** | Provider occurrence time. @format date-time | 
**created_at** | **str** | Event persistence time. @format date-time | 
**message_uuid** | **str** | Related message UUID when loaded. @format uuid | 

## Example

```python
from mailermine_generated.models.campaign_event import CampaignEvent

# TODO update the JSON string below
json = "{}"
# create an instance of CampaignEvent from a JSON string
campaign_event_instance = CampaignEvent.from_json(json)
# print the JSON string representation of the object
print(CampaignEvent.to_json())

# convert the object into a dict
campaign_event_dict = campaign_event_instance.to_dict()
# create an instance of CampaignEvent from a dict
campaign_event_from_dict = CampaignEvent.from_dict(campaign_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


