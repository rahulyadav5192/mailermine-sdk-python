# TemplateVariable


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Variable identifier used in &#x60;{{name}}&#x60; placeholders. @example first_name | 
**type** | **str** | Variable validation type. @var &#39;string&#39;|&#39;number&#39;|&#39;email&#39;|&#39;url&#39; @example string | 
**required** | **bool** | Whether callers must provide a value. @example true | 
**default_value** | **str** | Optional fallback value. @example Customer | 

## Example

```python
from mailermine_generated.models.template_variable import TemplateVariable

# TODO update the JSON string below
json = "{}"
# create an instance of TemplateVariable from a JSON string
template_variable_instance = TemplateVariable.from_json(json)
# print the JSON string representation of the object
print(TemplateVariable.to_json())

# convert the object into a dict
template_variable_dict = template_variable_instance.to_dict()
# create an instance of TemplateVariable from a dict
template_variable_from_dict = TemplateVariable.from_dict(template_variable_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


