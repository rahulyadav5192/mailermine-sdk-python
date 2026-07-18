# DuplicateTemplateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name for the copy; generated when omitted. | [optional] 

## Example

```python
from mailermine_generated.models.duplicate_template_request import DuplicateTemplateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DuplicateTemplateRequest from a JSON string
duplicate_template_request_instance = DuplicateTemplateRequest.from_json(json)
# print the JSON string representation of the object
print(DuplicateTemplateRequest.to_json())

# convert the object into a dict
duplicate_template_request_dict = duplicate_template_request_instance.to_dict()
# create an instance of DuplicateTemplateRequest from a dict
duplicate_template_request_from_dict = DuplicateTemplateRequest.from_dict(duplicate_template_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


