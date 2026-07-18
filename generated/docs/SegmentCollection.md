# SegmentCollection


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** |  | 
**message** | **str** |  | 
**data** | [**List[SegmentResource]**](SegmentResource.md) |  | 
**meta** | [**PaginationMeta**](PaginationMeta.md) |  | 

## Example

```python
from mailermine_generated.models.segment_collection import SegmentCollection

# TODO update the JSON string below
json = "{}"
# create an instance of SegmentCollection from a JSON string
segment_collection_instance = SegmentCollection.from_json(json)
# print the JSON string representation of the object
print(SegmentCollection.to_json())

# convert the object into a dict
segment_collection_dict = segment_collection_instance.to_dict()
# create an instance of SegmentCollection from a dict
segment_collection_from_dict = SegmentCollection.from_dict(segment_collection_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


