# WebhookDeliveryWebhook

Owning webhook summary. Present when the webhook relation is loaded.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**name** | **str** |  | 
**url** | **str** |  | 

## Example

```python
from mailermine_generated.models.webhook_delivery_webhook import WebhookDeliveryWebhook

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookDeliveryWebhook from a JSON string
webhook_delivery_webhook_instance = WebhookDeliveryWebhook.from_json(json)
# print the JSON string representation of the object
print(WebhookDeliveryWebhook.to_json())

# convert the object into a dict
webhook_delivery_webhook_dict = webhook_delivery_webhook_instance.to_dict()
# create an instance of WebhookDeliveryWebhook from a dict
webhook_delivery_webhook_from_dict = WebhookDeliveryWebhook.from_dict(webhook_delivery_webhook_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


