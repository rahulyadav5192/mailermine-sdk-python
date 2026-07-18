# TemplatePreviewResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** |  | 
**message** | **str** | Omitted by the legacy &#x60;/templates/preview&#x60; operation. | 
**data** | [**TemplatePreview**](TemplatePreview.md) |  | 

## Example

```python
from mailermine_generated.models.template_preview_response import TemplatePreviewResponse

# TODO update the JSON string below
json = "{}"
# create an instance of TemplatePreviewResponse from a JSON string
template_preview_response_instance = TemplatePreviewResponse.from_json(json)
# print the JSON string representation of the object
print(TemplatePreviewResponse.to_json())

# convert the object into a dict
template_preview_response_dict = template_preview_response_instance.to_dict()
# create an instance of TemplatePreviewResponse from a dict
template_preview_response_from_dict = TemplatePreviewResponse.from_dict(template_preview_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


