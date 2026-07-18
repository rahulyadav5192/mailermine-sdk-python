# WebhookDeliveryMessage

Related message summary, when the delivery is tied to a message.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**subject** | **str** |  | 
**to_email** | **str** |  | 

## Example

```python
from mailermine_generated.models.webhook_delivery_message import WebhookDeliveryMessage

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookDeliveryMessage from a JSON string
webhook_delivery_message_instance = WebhookDeliveryMessage.from_json(json)
# print the JSON string representation of the object
print(WebhookDeliveryMessage.to_json())

# convert the object into a dict
webhook_delivery_message_dict = webhook_delivery_message_instance.to_dict()
# create an instance of WebhookDeliveryMessage from a dict
webhook_delivery_message_from_dict = WebhookDeliveryMessage.from_dict(webhook_delivery_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


