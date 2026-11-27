# TestTemplateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**to** | **str** | Recipient email for the test send. | 
**email** | **str** | Backward-compatible alias of to. | [optional] 
**variables** | **Dict[str, object]** | Runtime template variables. | [optional] 
**subject** | **str** | Optional subject override. | [optional] 

## Example

```python
from mailermine_generated.models.test_template_request import TestTemplateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of TestTemplateRequest from a JSON string
test_template_request_instance = TestTemplateRequest.from_json(json)
# print the JSON string representation of the object
print(TestTemplateRequest.to_json())

# convert the object into a dict
test_template_request_dict = test_template_request_instance.to_dict()
# create an instance of TestTemplateRequest from a dict
test_template_request_from_dict = TestTemplateRequest.from_dict(test_template_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


