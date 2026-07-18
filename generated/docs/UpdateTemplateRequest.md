# UpdateTemplateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Updated project-unique name. | [optional] 
**description** | **str** | Updated description; null clears it. | [optional] 
**subject** | **str** | Updated subject. | [optional] 
**html** | **str** | Updated HTML body. | [optional] 
**html_content** | **str** | Backward-compatible alias of html. | [optional] 
**text** | **str** | Updated plain-text body. | [optional] 
**text_content** | **str** | Backward-compatible alias of text. | [optional] 
**status** | [**TemplateStatus**](TemplateStatus.md) | Publication status. | [optional] 
**editor_type** | **str** | Editor/layout identifier. | [optional] 
**category** | **str** | Template category. | [optional] 
**tags** | **List[str]** | Replacement labels. | [optional] 
**variables** | [**List[CreateTemplateRequestVariablesInner]**](CreateTemplateRequestVariablesInner.md) | Replacement variable definitions. | [optional] 
**branding** | [**CreateTemplateRequestBranding**](CreateTemplateRequestBranding.md) |  | [optional] 

## Example

```python
from mailermine_generated.models.update_template_request import UpdateTemplateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateTemplateRequest from a JSON string
update_template_request_instance = UpdateTemplateRequest.from_json(json)
# print the JSON string representation of the object
print(UpdateTemplateRequest.to_json())

# convert the object into a dict
update_template_request_dict = update_template_request_instance.to_dict()
# create an instance of UpdateTemplateRequest from a dict
update_template_request_from_dict = UpdateTemplateRequest.from_dict(update_template_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


