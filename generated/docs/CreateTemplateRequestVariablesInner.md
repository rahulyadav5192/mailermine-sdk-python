# CreateTemplateRequestVariablesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**type** | [**TemplateVariableType**](TemplateVariableType.md) |  | 
**required** | **bool** |  | [optional] 
**default_value** | **str** |  | [optional] 

## Example

```python
from mailermine_generated.models.create_template_request_variables_inner import CreateTemplateRequestVariablesInner

# TODO update the JSON string below
json = "{}"
# create an instance of CreateTemplateRequestVariablesInner from a JSON string
create_template_request_variables_inner_instance = CreateTemplateRequestVariablesInner.from_json(json)
# print the JSON string representation of the object
print(CreateTemplateRequestVariablesInner.to_json())

# convert the object into a dict
create_template_request_variables_inner_dict = create_template_request_variables_inner_instance.to_dict()
# create an instance of CreateTemplateRequestVariablesInner from a dict
create_template_request_variables_inner_from_dict = CreateTemplateRequestVariablesInner.from_dict(create_template_request_variables_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


