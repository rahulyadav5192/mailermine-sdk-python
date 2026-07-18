# CreateTemplateRequestBranding

Branding, layout, colors, and footer settings.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**layout** | [**TemplateLayoutStyle**](TemplateLayoutStyle.md) |  | [optional] 
**logo_url** | **str** |  | [optional] 
**logo_alt** | **str** |  | [optional] 
**company_name** | **str** |  | [optional] 
**primary_color** | **str** |  | [optional] 
**background_color** | **str** |  | [optional] 
**content_background_color** | **str** |  | [optional] 
**text_color** | **str** |  | [optional] 
**muted_text_color** | **str** |  | [optional] 
**button_text_color** | **str** |  | [optional] 
**font_family** | **str** |  | [optional] 
**footer_text** | **str** |  | [optional] 
**support_email** | **str** |  | [optional] 
**website_url** | **str** |  | [optional] 
**category** | **str** |  | [optional] 
**template_type** | **str** |  | [optional] 
**preview_text** | **str** |  | [optional] 
**tags** | **List[str]** |  | [optional] 
**variable_meta** | **List[str]** |  | [optional] 

## Example

```python
from mailermine_generated.models.create_template_request_branding import CreateTemplateRequestBranding

# TODO update the JSON string below
json = "{}"
# create an instance of CreateTemplateRequestBranding from a JSON string
create_template_request_branding_instance = CreateTemplateRequestBranding.from_json(json)
# print the JSON string representation of the object
print(CreateTemplateRequestBranding.to_json())

# convert the object into a dict
create_template_request_branding_dict = create_template_request_branding_instance.to_dict()
# create an instance of CreateTemplateRequestBranding from a dict
create_template_request_branding_from_dict = CreateTemplateRequestBranding.from_dict(create_template_request_branding_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


