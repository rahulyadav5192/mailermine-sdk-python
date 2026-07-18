# ListResource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Public list UUID. @format uuid | 
**name** | **str** | Project-unique list name. @example Product newsletter | 
**description** | **str** | Optional list description. @example Customers subscribed to product updates | 
**color** | **str** | Display color in hex notation. @example #22C55E | 
**subscriber_count** | **int** | Current number of list members. @example 1250 | 
**created_at** | **str** | Creation time. @format date-time | 
**updated_at** | **str** | Last update time. @format date-time | 

## Example

```python
from mailermine_generated.models.list_resource import ListResource

# TODO update the JSON string below
json = "{}"
# create an instance of ListResource from a JSON string
list_resource_instance = ListResource.from_json(json)
# print the JSON string representation of the object
print(ListResource.to_json())

# convert the object into a dict
list_resource_dict = list_resource_instance.to_dict()
# create an instance of ListResource from a dict
list_resource_from_dict = ListResource.from_dict(list_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


