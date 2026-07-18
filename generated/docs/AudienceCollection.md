# AudienceCollection


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** |  | 
**message** | **str** |  | 
**data** | [**List[AudienceResource]**](AudienceResource.md) |  | 
**meta** | [**PaginationMeta**](PaginationMeta.md) |  | 

## Example

```python
from mailermine_generated.models.audience_collection import AudienceCollection

# TODO update the JSON string below
json = "{}"
# create an instance of AudienceCollection from a JSON string
audience_collection_instance = AudienceCollection.from_json(json)
# print the JSON string representation of the object
print(AudienceCollection.to_json())

# convert the object into a dict
audience_collection_dict = audience_collection_instance.to_dict()
# create an instance of AudienceCollection from a dict
audience_collection_from_dict = AudienceCollection.from_dict(audience_collection_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


