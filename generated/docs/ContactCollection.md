# ContactCollection


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** |  | 
**message** | **str** |  | 
**data** | [**List[ContactResource]**](ContactResource.md) |  | 
**meta** | [**PaginationMeta**](PaginationMeta.md) |  | 

## Example

```python
from mailermine_generated.models.contact_collection import ContactCollection

# TODO update the JSON string below
json = "{}"
# create an instance of ContactCollection from a JSON string
contact_collection_instance = ContactCollection.from_json(json)
# print the JSON string representation of the object
print(ContactCollection.to_json())

# convert the object into a dict
contact_collection_dict = contact_collection_instance.to_dict()
# create an instance of ContactCollection from a dict
contact_collection_from_dict = ContactCollection.from_dict(contact_collection_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


