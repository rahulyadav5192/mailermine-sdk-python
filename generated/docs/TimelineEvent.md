# TimelineEvent


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Event UUID. | 
**event_type** | **str** | Machine-readable event type, e.g. &#x60;sent&#x60;, &#x60;delivered&#x60;, &#x60;bounced&#x60;. | 
**event_label** | **str** |  | 
**source** | **str** |  | 
**payload** | [**CampaignActivityPayload**](CampaignActivityPayload.md) |  | 
**occurred_at** | **str** | When the event occurred (ISO-8601). | 
**message_id** | **str** |  | 
**recipient** | **str** |  | 
**metadata** | [**CampaignActivityPayload**](CampaignActivityPayload.md) |  | 
**tags** | **List[str]** |  | 

## Example

```python
from mailermine_generated.models.timeline_event import TimelineEvent

# TODO update the JSON string below
json = "{}"
# create an instance of TimelineEvent from a JSON string
timeline_event_instance = TimelineEvent.from_json(json)
# print the JSON string representation of the object
print(TimelineEvent.to_json())

# convert the object into a dict
timeline_event_dict = timeline_event_instance.to_dict()
# create an instance of TimelineEvent from a dict
timeline_event_from_dict = TimelineEvent.from_dict(timeline_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


