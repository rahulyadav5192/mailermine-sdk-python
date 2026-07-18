# PreviewSegmentRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**rules** | [**PreviewSegmentRequestRules**](PreviewSegmentRequestRules.md) |  | 

## Example

```python
from mailermine_generated.models.preview_segment_request import PreviewSegmentRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PreviewSegmentRequest from a JSON string
preview_segment_request_instance = PreviewSegmentRequest.from_json(json)
# print the JSON string representation of the object
print(PreviewSegmentRequest.to_json())

# convert the object into a dict
preview_segment_request_dict = preview_segment_request_instance.to_dict()
# create an instance of PreviewSegmentRequest from a dict
preview_segment_request_from_dict = PreviewSegmentRequest.from_dict(preview_segment_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


