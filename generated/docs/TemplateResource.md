# TemplateResource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Public template UUID. @format uuid | 
**name** | **str** | Template name. @example Welcome Email | 
**slug** | **str** | Project-unique slug. @example welcome-email | 
**description** | **str** | Optional description. | 
**subject** | **str** | Renderable subject. @example Welcome {{first_name}} | 
**status** | **str** | Publication status. @var &#39;draft&#39;|&#39;published&#39;|&#39;archived&#39; @example published | 
**editor_type** | **str** | Editor/layout type. @example html | 
**category** | **str** | Optional template category. @example onboarding | 
**tags** | **List[str]** | Searchable labels. @var list&lt;string&gt; | 
**created_at** | **str** | Creation time. @format date-time | 
**updated_at** | **str** | Last update time. @format date-time | 
**html** | **str** | HTML body; present on detailed responses. | 
**text** | **str** | Plain-text body; present on detailed responses. | 
**html_content** | **str** | Backward-compatible alias of html. | 
**text_content** | **str** | Backward-compatible alias of text. | 
**branding** | [**CampaignActivityPayload**](CampaignActivityPayload.md) |  | 
**metadata** | [**CampaignActivityPayload**](CampaignActivityPayload.md) |  | 
**variables** | [**List[TemplateVariable]**](TemplateVariable.md) | Variable definitions. | 
**project** | [**CampaignActivityPayload**](CampaignActivityPayload.md) |  | 
**usage** | [**CampaignActivityPayload**](CampaignActivityPayload.md) |  | 

## Example

```python
from mailermine_generated.models.template_resource import TemplateResource

# TODO update the JSON string below
json = "{}"
# create an instance of TemplateResource from a JSON string
template_resource_instance = TemplateResource.from_json(json)
# print the JSON string representation of the object
print(TemplateResource.to_json())

# convert the object into a dict
template_resource_dict = template_resource_instance.to_dict()
# create an instance of TemplateResource from a dict
template_resource_from_dict = TemplateResource.from_dict(template_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


