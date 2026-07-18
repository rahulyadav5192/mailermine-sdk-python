# ReplayWebhookRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**failed_only** | **bool** | Replay only failed deliveries in the range. | [optional] 
**var_from** | **datetime** | Replay deliveries created on or after this ISO-8601 date. | [optional] 
**to** | **datetime** | Replay deliveries created on or before this ISO-8601 date. | [optional] 
**event_types** | **List[str]** | Restrict replay to these event types. | [optional] 
**delivery_ids** | **List[UUID]** | Replay these specific delivery UUIDs. Overrides range filters. | [optional] 

## Example

```python
from mailermine_generated.models.replay_webhook_request import ReplayWebhookRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ReplayWebhookRequest from a JSON string
replay_webhook_request_instance = ReplayWebhookRequest.from_json(json)
# print the JSON string representation of the object
print(ReplayWebhookRequest.to_json())

# convert the object into a dict
replay_webhook_request_dict = replay_webhook_request_instance.to_dict()
# create an instance of ReplayWebhookRequest from a dict
replay_webhook_request_from_dict = ReplayWebhookRequest.from_dict(replay_webhook_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


