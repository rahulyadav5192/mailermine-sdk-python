# TemplateTestResponseData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**to** | **str** |  | 
**template_id** | **str** |  | 

## Example

```python
from mailermine_generated.models.template_test_response_data import TemplateTestResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of TemplateTestResponseData from a JSON string
template_test_response_data_instance = TemplateTestResponseData.from_json(json)
# print the JSON string representation of the object
print(TemplateTestResponseData.to_json())

# convert the object into a dict
template_test_response_data_dict = template_test_response_data_instance.to_dict()
# create an instance of TemplateTestResponseData from a dict
template_test_response_data_from_dict = TemplateTestResponseData.from_dict(template_test_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


