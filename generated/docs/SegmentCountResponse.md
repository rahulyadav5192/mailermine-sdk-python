# SegmentCountResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** |  | 
**message** | **str** |  | 
**data** | [**SegmentCountResponseData**](SegmentCountResponseData.md) |  | 

## Example

```python
from mailermine_generated.models.segment_count_response import SegmentCountResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SegmentCountResponse from a JSON string
segment_count_response_instance = SegmentCountResponse.from_json(json)
# print the JSON string representation of the object
print(SegmentCountResponse.to_json())

# convert the object into a dict
segment_count_response_dict = segment_count_response_instance.to_dict()
# create an instance of SegmentCountResponse from a dict
segment_count_response_from_dict = SegmentCountResponse.from_dict(segment_count_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


