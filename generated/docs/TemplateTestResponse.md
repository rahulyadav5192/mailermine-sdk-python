# TemplateTestResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** |  | 
**message** | **str** |  | 
**data** | [**TemplateTestResponseData**](TemplateTestResponseData.md) |  | 

## Example

```python
from mailermine_generated.models.template_test_response import TemplateTestResponse

# TODO update the JSON string below
json = "{}"
# create an instance of TemplateTestResponse from a JSON string
template_test_response_instance = TemplateTestResponse.from_json(json)
# print the JSON string representation of the object
print(TemplateTestResponse.to_json())

# convert the object into a dict
template_test_response_dict = template_test_response_instance.to_dict()
# create an instance of TemplateTestResponse from a dict
template_test_response_from_dict = TemplateTestResponse.from_dict(template_test_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


