# PreviewTemplateByIdRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**template_id** | **UUID** | Published template UUID. | 
**variables** | **Dict[str, object]** | Runtime values used to render placeholders. | [optional] 

## Example

```python
from mailermine_generated.models.preview_template_by_id_request import PreviewTemplateByIdRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PreviewTemplateByIdRequest from a JSON string
preview_template_by_id_request_instance = PreviewTemplateByIdRequest.from_json(json)
# print the JSON string representation of the object
print(PreviewTemplateByIdRequest.to_json())

# convert the object into a dict
preview_template_by_id_request_dict = preview_template_by_id_request_instance.to_dict()
# create an instance of PreviewTemplateByIdRequest from a dict
preview_template_by_id_request_from_dict = PreviewTemplateByIdRequest.from_dict(preview_template_by_id_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


