# ListCollection


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** |  | 
**message** | **str** |  | 
**data** | [**List[ListResource]**](ListResource.md) |  | 
**meta** | [**PaginationMeta**](PaginationMeta.md) |  | 

## Example

```python
from mailermine_generated.models.list_collection import ListCollection

# TODO update the JSON string below
json = "{}"
# create an instance of ListCollection from a JSON string
list_collection_instance = ListCollection.from_json(json)
# print the JSON string representation of the object
print(ListCollection.to_json())

# convert the object into a dict
list_collection_dict = list_collection_instance.to_dict()
# create an instance of ListCollection from a dict
list_collection_from_dict = ListCollection.from_dict(list_collection_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


