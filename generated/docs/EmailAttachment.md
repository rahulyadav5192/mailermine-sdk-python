# EmailAttachment


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**filename** | **str** | Safe filename (no path traversal). | 
**content_type** | **str** | MIME type, e.g. &#x60;application/pdf&#x60;. | 
**size** | **int** | Decoded file size in bytes. | 

## Example

```python
from mailermine_generated.models.email_attachment import EmailAttachment

# TODO update the JSON string below
json = "{}"
# create an instance of EmailAttachment from a JSON string
email_attachment_instance = EmailAttachment.from_json(json)
# print the JSON string representation of the object
print(EmailAttachment.to_json())

# convert the object into a dict
email_attachment_dict = email_attachment_instance.to_dict()
# create an instance of EmailAttachment from a dict
email_attachment_from_dict = EmailAttachment.from_dict(email_attachment_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


