# SegmentPreviewResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** |  | 
**message** | **str** |  | 
**data** | [**SegmentPreviewResponseData**](SegmentPreviewResponseData.md) |  | 

## Example

```python
from mailermine_generated.models.segment_preview_response import SegmentPreviewResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SegmentPreviewResponse from a JSON string
segment_preview_response_instance = SegmentPreviewResponse.from_json(json)
# print the JSON string representation of the object
print(SegmentPreviewResponse.to_json())

# convert the object into a dict
segment_preview_response_dict = segment_preview_response_instance.to_dict()
# create an instance of SegmentPreviewResponse from a dict
segment_preview_response_from_dict = SegmentPreviewResponse.from_dict(segment_preview_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


