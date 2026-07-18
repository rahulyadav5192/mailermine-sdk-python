# TagResource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Public tag UUID. @format uuid @example 8cb52aa6-b31c-4b87-8f63-11408ea21c72 | 
**name** | **str** | Project-unique tag name. Tags do not include a description field. @example vip | 
**color** | **str** | Display color in hex notation. @example #7C3AED | 
**usage_count** | **int** | Number of contacts using the tag. @example 42 | 
**created_at** | **str** | Creation time. @format date-time | 
**updated_at** | **str** | Last update time. @format date-time | 

## Example

```python
from mailermine_generated.models.tag_resource import TagResource

# TODO update the JSON string below
json = "{}"
# create an instance of TagResource from a JSON string
tag_resource_instance = TagResource.from_json(json)
# print the JSON string representation of the object
print(TagResource.to_json())

# convert the object into a dict
tag_resource_dict = tag_resource_instance.to_dict()
# create an instance of TagResource from a dict
tag_resource_from_dict = TagResource.from_dict(tag_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


