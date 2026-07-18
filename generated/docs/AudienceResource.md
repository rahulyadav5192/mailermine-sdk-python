# AudienceResource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Audience backing type. @var &#39;list&#39;|&#39;segment&#39; @example list | 
**id** | **str** | Public list or segment UUID. @format uuid | 
**name** | **str** | Audience name. @example Product newsletter | 
**description** | **str** | Optional audience description. | 
**member_count** | **int** | Current list size or last evaluated segment size. @example 1250 | 
**source** | **str** | Backing resource discriminator. @var &#39;list&#39;|&#39;segment&#39; @example list | 

## Example

```python
from mailermine_generated.models.audience_resource import AudienceResource

# TODO update the JSON string below
json = "{}"
# create an instance of AudienceResource from a JSON string
audience_resource_instance = AudienceResource.from_json(json)
# print the JSON string representation of the object
print(AudienceResource.to_json())

# convert the object into a dict
audience_resource_dict = audience_resource_instance.to_dict()
# create an instance of AudienceResource from a dict
audience_resource_from_dict = AudienceResource.from_dict(audience_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


