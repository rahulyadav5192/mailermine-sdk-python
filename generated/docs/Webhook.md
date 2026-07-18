# Webhook


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Public webhook UUID. | 
**name** | **str** | Human-readable label for the endpoint. | 
**url** | **str** | HTTPS URL that receives signed event deliveries. | 
**is_active** | **bool** | Whether the endpoint is currently active. | 
**enabled** | **bool** | Alias of &#x60;is_active&#x60; retained for backward compatibility. | 
**subscribed_events** | **List[str]** | Subscribed event types. Values match the webhook event catalog (for example &#x60;email.delivered&#x60;, &#x60;email.bounced&#x60;, &#x60;campaign.completed&#x60;). | 
**retry_policy** | [**WebhookRetryPolicy**](WebhookRetryPolicy.md) |  | 
**last_delivery** | [**WebhookLastDelivery**](WebhookLastDelivery.md) |  | 
**created_at** | **str** | Creation timestamp (ISO-8601). | 
**updated_at** | **str** | Last update timestamp (ISO-8601). | 
**project** | [**WebhookProject**](WebhookProject.md) |  | 

## Example

```python
from mailermine_generated.models.webhook import Webhook

# TODO update the JSON string below
json = "{}"
# create an instance of Webhook from a JSON string
webhook_instance = Webhook.from_json(json)
# print the JSON string representation of the object
print(Webhook.to_json())

# convert the object into a dict
webhook_dict = webhook_instance.to_dict()
# create an instance of Webhook from a dict
webhook_from_dict = Webhook.from_dict(webhook_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


