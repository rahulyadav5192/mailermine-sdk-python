# WebhookDelivery


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Public delivery UUID. | 
**event_type** | **str** | Event type that triggered the delivery (for example &#x60;email.delivered&#x60;). | 
**status** | [**WebhookDeliveryStatus**](WebhookDeliveryStatus.md) | Delivery status. | 
**status_label** | **str** | Human-readable status label. | 
**attempt** | **int** | Attempt number (1-based). | 
**http_status** | **int** | HTTP status code returned by the endpoint, or &#x60;null&#x60; if not yet attempted. | 
**response_headers** | [**CampaignActivityPayload**](CampaignActivityPayload.md) |  | 
**response_body** | **str** | Truncated response body returned by the endpoint. | 
**request_body** | **str** | Signed JSON payload that was sent to the endpoint. | 
**duration_ms** | **int** | Request duration in milliseconds. | 
**next_retry_at** | **str** | Scheduled time of the next retry (ISO-8601), or &#x60;null&#x60;. | 
**delivered_at** | **str** | Time the delivery succeeded (ISO-8601), or &#x60;null&#x60;. | 
**created_at** | **str** | Creation timestamp (ISO-8601). | 
**webhook** | [**WebhookDeliveryWebhook**](WebhookDeliveryWebhook.md) |  | 
**message** | [**WebhookDeliveryMessage**](WebhookDeliveryMessage.md) |  | 

## Example

```python
from mailermine_generated.models.webhook_delivery import WebhookDelivery

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookDelivery from a JSON string
webhook_delivery_instance = WebhookDelivery.from_json(json)
# print the JSON string representation of the object
print(WebhookDelivery.to_json())

# convert the object into a dict
webhook_delivery_dict = webhook_delivery_instance.to_dict()
# create an instance of WebhookDelivery from a dict
webhook_delivery_from_dict = WebhookDelivery.from_dict(webhook_delivery_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


