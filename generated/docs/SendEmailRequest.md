# SendEmailRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_from** | **str** | Sender address. Format: &#x60;Name &lt;email@domain.com&gt;&#x60; or &#x60;email@domain.com&#x60;. | 
**to** | **List[str]** | Recipient email address(es). A single string is accepted for backward compatibility. | 
**cc** | **List[str]** | Carbon copy recipients. | [optional] 
**bcc** | **List[str]** | Blind carbon copy recipients. | [optional] 
**template_id** | **UUID** | Template UUID to render instead of inline content. | [optional] 
**variables** | **Dict[str, object]** | Template variables (key-value object). | [optional] 
**subject** | **str** | Email subject. Required when not using a template. | [optional] 
**html** | **str** | HTML body. Required with &#x60;text&#x60; when not using a template. | [optional] 
**text** | **str** | Plain text body. Required with &#x60;html&#x60; when not using a template. | [optional] 
**reply_to** | **str** | Reply-to address. | [optional] 
**metadata** | **Dict[str, object]** | Custom metadata stored with the message. | [optional] 
**tags** | **List[str]** | Tags for filtering and analytics. | [optional] 
**headers** | **Dict[str, object]** | Custom email headers (requires &#x60;allow_custom_headers&#x60; plan capability). | [optional] 
**tracking** | [**SendEmailRequestTracking**](SendEmailRequestTracking.md) |  | [optional] 
**attachments** | [**List[SendEmailRequestAttachmentsInner]**](SendEmailRequestAttachmentsInner.md) | Base64-encoded file attachments. | [optional] 

## Example

```python
from mailermine_generated.models.send_email_request import SendEmailRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SendEmailRequest from a JSON string
send_email_request_instance = SendEmailRequest.from_json(json)
# print the JSON string representation of the object
print(SendEmailRequest.to_json())

# convert the object into a dict
send_email_request_dict = send_email_request_instance.to_dict()
# create an instance of SendEmailRequest from a dict
send_email_request_from_dict = SendEmailRequest.from_dict(send_email_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


