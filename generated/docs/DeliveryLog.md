# DeliveryLog


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Public message UUID. | 
**from_email** | **str** |  | 
**from_name** | **str** |  | 
**to_email** | **str** |  | 
**subject** | **str** |  | 
**status** | [**MessageStatus**](MessageStatus.md) |  | 
**provider** | **str** |  | 
**provider_message_id** | **str** |  | 
**error_message** | **str** |  | 
**metadata** | [**AnalyticsMessagesByStatus**](AnalyticsMessagesByStatus.md) |  | 
**tags** | **List[str]** |  | 
**sent_at** | **str** |  | 
**created_at** | **str** |  | 
**updated_at** | **str** |  | 
**timeline** | **List[Dict[str, object]]** | Present on detail responses only. | 
**project** | [**CampaignActivityPayload**](CampaignActivityPayload.md) |  | 

## Example

```python
from mailermine_generated.models.delivery_log import DeliveryLog

# TODO update the JSON string below
json = "{}"
# create an instance of DeliveryLog from a JSON string
delivery_log_instance = DeliveryLog.from_json(json)
# print the JSON string representation of the object
print(DeliveryLog.to_json())

# convert the object into a dict
delivery_log_dict = delivery_log_instance.to_dict()
# create an instance of DeliveryLog from a dict
delivery_log_from_dict = DeliveryLog.from_dict(delivery_log_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


