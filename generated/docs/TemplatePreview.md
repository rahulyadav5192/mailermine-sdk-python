# TemplatePreview


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**subject** | **str** | Rendered subject. @example Welcome Alex | 
**html** | **str** | Rendered HTML body. @example &lt;p&gt;Hello Alex&lt;/p&gt; | 
**text** | **str** | Rendered plain-text body. @example Hello Alex | 

## Example

```python
from mailermine_generated.models.template_preview import TemplatePreview

# TODO update the JSON string below
json = "{}"
# create an instance of TemplatePreview from a JSON string
template_preview_instance = TemplatePreview.from_json(json)
# print the JSON string representation of the object
print(TemplatePreview.to_json())

# convert the object into a dict
template_preview_dict = template_preview_instance.to_dict()
# create an instance of TemplatePreview from a dict
template_preview_from_dict = TemplatePreview.from_dict(template_preview_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


