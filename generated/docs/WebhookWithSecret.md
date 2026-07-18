# WebhookWithSecret


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
**signing_secret** | **str** | HMAC signing secret. Returned only when creating a webhook or rotating its secret — store it securely, it is never shown again. | 

## Example

```python
from mailermine_generated.models.webhook_with_secret import WebhookWithSecret

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookWithSecret from a JSON string
webhook_with_secret_instance = WebhookWithSecret.from_json(json)
# print the JSON string representation of the object
print(WebhookWithSecret.to_json())

# convert the object into a dict
webhook_with_secret_dict = webhook_with_secret_instance.to_dict()
# create an instance of WebhookWithSecret from a dict
webhook_with_secret_from_dict = WebhookWithSecret.from_dict(webhook_with_secret_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


