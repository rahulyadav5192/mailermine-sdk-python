# SegmentResource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Public segment UUID. @format uuid | 
**name** | **str** | Project-unique segment name. @example Active customers | 
**description** | **str** | Optional segment description. | 
**rules** | [**SendEmailRequestVariables**](SendEmailRequestVariables.md) |  | 
**contact_count** | **int** | Last evaluated matching contact count. @example 342 | 
**created_at** | **str** | Creation time. @format date-time | 
**updated_at** | **str** | Last update time. @format date-time | 

## Example

```python
from mailermine_generated.models.segment_resource import SegmentResource

# TODO update the JSON string below
json = "{}"
# create an instance of SegmentResource from a JSON string
segment_resource_instance = SegmentResource.from_json(json)
# print the JSON string representation of the object
print(SegmentResource.to_json())

# convert the object into a dict
segment_resource_dict = segment_resource_instance.to_dict()
# create an instance of SegmentResource from a dict
segment_resource_from_dict = SegmentResource.from_dict(segment_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


