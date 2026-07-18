# CreateTemplateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Project-unique template name. | 
**description** | **str** | Optional internal description. | [optional] 
**subject** | **str** | Subject with optional &#x60;{{variable}}&#x60; placeholders. | 
**html** | **str** | HTML body; required when no other body field is provided. | [optional] 
**html_content** | **str** | Backward-compatible alias of html. | [optional] 
**text** | **str** | Plain-text body. | [optional] 
**text_content** | **str** | Backward-compatible alias of text. | [optional] 
**status** | [**TemplateStatus**](TemplateStatus.md) | Initial publication status. | [optional] 
**editor_type** | **str** | Editor/layout identifier. | [optional] 
**category** | **str** | Template category. | [optional] 
**tags** | **List[str]** | Searchable labels. | [optional] 
**variables** | [**List[CreateTemplateRequestVariablesInner]**](CreateTemplateRequestVariablesInner.md) | Template variable definitions. | [optional] 
**branding** | [**CreateTemplateRequestBranding**](CreateTemplateRequestBranding.md) |  | [optional] 

## Example

```python
from mailermine_generated.models.create_template_request import CreateTemplateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateTemplateRequest from a JSON string
create_template_request_instance = CreateTemplateRequest.from_json(json)
# print the JSON string representation of the object
print(CreateTemplateRequest.to_json())

# convert the object into a dict
create_template_request_dict = create_template_request_instance.to_dict()
# create an instance of CreateTemplateRequest from a dict
create_template_request_from_dict = CreateTemplateRequest.from_dict(create_template_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


