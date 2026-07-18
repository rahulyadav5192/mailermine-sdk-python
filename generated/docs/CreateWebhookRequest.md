# CreateWebhookRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Human-readable label for the endpoint. | 
**url** | **str** | HTTPS URL that will receive signed event deliveries. | 
**subscribed_events** | **List[str]** | Event types to subscribe to. | 
**is_active** | **bool** | Whether the endpoint is active on creation. Defaults to true. | [optional] 

## Example

```python
from mailermine_generated.models.create_webhook_request import CreateWebhookRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateWebhookRequest from a JSON string
create_webhook_request_instance = CreateWebhookRequest.from_json(json)
# print the JSON string representation of the object
print(CreateWebhookRequest.to_json())

# convert the object into a dict
create_webhook_request_dict = create_webhook_request_instance.to_dict()
# create an instance of CreateWebhookRequest from a dict
create_webhook_request_from_dict = CreateWebhookRequest.from_dict(create_webhook_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


