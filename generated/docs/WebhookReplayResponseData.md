# WebhookReplayResponseData

Replay outcome.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**replayed** | **int** |  | 

## Example

```python
from mailermine_generated.models.webhook_replay_response_data import WebhookReplayResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookReplayResponseData from a JSON string
webhook_replay_response_data_instance = WebhookReplayResponseData.from_json(json)
# print the JSON string representation of the object
print(WebhookReplayResponseData.to_json())

# convert the object into a dict
webhook_replay_response_data_dict = webhook_replay_response_data_instance.to_dict()
# create an instance of WebhookReplayResponseData from a dict
webhook_replay_response_data_from_dict = WebhookReplayResponseData.from_dict(webhook_replay_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


