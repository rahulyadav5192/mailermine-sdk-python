# SegmentPreviewResponseData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** |  | 
**contacts** | [**List[ContactResource]**](ContactResource.md) |  | 

## Example

```python
from mailermine_generated.models.segment_preview_response_data import SegmentPreviewResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of SegmentPreviewResponseData from a JSON string
segment_preview_response_data_instance = SegmentPreviewResponseData.from_json(json)
# print the JSON string representation of the object
print(SegmentPreviewResponseData.to_json())

# convert the object into a dict
segment_preview_response_data_dict = segment_preview_response_data_instance.to_dict()
# create an instance of SegmentPreviewResponseData from a dict
segment_preview_response_data_from_dict = SegmentPreviewResponseData.from_dict(segment_preview_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


