# MessageEventsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[TimelineEvent]**](TimelineEvent.md) |  | 

## Example

```python
from mailermine_generated.models.message_events_response import MessageEventsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of MessageEventsResponse from a JSON string
message_events_response_instance = MessageEventsResponse.from_json(json)
# print the JSON string representation of the object
print(MessageEventsResponse.to_json())

# convert the object into a dict
message_events_response_dict = message_events_response_instance.to_dict()
# create an instance of MessageEventsResponse from a dict
message_events_response_from_dict = MessageEventsResponse.from_dict(message_events_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


