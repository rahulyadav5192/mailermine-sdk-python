# WebhookLastDelivery

Most recent delivery summary, or `null` when no deliveries exist yet.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**event_type** | **str** |  | 
**status** | **str** |  | 
**created_at** | **str** |  | 

## Example

```python
from mailermine_generated.models.webhook_last_delivery import WebhookLastDelivery

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookLastDelivery from a JSON string
webhook_last_delivery_instance = WebhookLastDelivery.from_json(json)
# print the JSON string representation of the object
print(WebhookLastDelivery.to_json())

# convert the object into a dict
webhook_last_delivery_dict = webhook_last_delivery_instance.to_dict()
# create an instance of WebhookLastDelivery from a dict
webhook_last_delivery_from_dict = WebhookLastDelivery.from_dict(webhook_last_delivery_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


