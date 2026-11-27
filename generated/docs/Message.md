# Message


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uuid** | **str** | Public message UUID. | 
**from_email** | **str** |  | 
**from_name** | **str** |  | 
**to_email** | **str** | Primary recipient email. | 
**to_emails** | **List[str]** | All &#x60;to&#x60; recipients. | 
**cc** | **List[str]** | Carbon copy recipients. | 
**bcc** | **List[str]** | Blind carbon copy recipients. | 
**reply_to** | **str** |  | 
**headers** | [**AnalyticsMessagesByStatus**](AnalyticsMessagesByStatus.md) |  | 
**subject** | **str** |  | 
**status** | [**MessageStatus**](MessageStatus.md) | Delivery status. | 
**status_label** | **str** |  | 
**provider** | **str** |  | 
**provider_label** | **str** |  | 
**provider_message_id** | **str** |  | 
**error_message** | **str** |  | 
**metadata** | [**AnalyticsMessagesByStatus**](AnalyticsMessagesByStatus.md) |  | 
**tags** | **List[str]** | Tags for filtering and analytics. | 
**attachments** | [**List[EmailAttachment]**](EmailAttachment.md) |  | 
**scheduled_at** | **str** |  | 
**sent_at** | **str** |  | 
**created_at** | **str** |  | 
**updated_at** | **str** |  | 

## Example

```python
from mailermine_generated.models.message import Message

# TODO update the JSON string below
json = "{}"
# create an instance of Message from a JSON string
message_instance = Message.from_json(json)
# print the JSON string representation of the object
print(Message.to_json())

# convert the object into a dict
message_dict = message_instance.to_dict()
# create an instance of Message from a dict
message_from_dict = Message.from_dict(message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


