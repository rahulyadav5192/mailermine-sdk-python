# SegmentCountResponseData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**contact_count** | **int** |  | 

## Example

```python
from mailermine_generated.models.segment_count_response_data import SegmentCountResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of SegmentCountResponseData from a JSON string
segment_count_response_data_instance = SegmentCountResponseData.from_json(json)
# print the JSON string representation of the object
print(SegmentCountResponseData.to_json())

# convert the object into a dict
segment_count_response_data_dict = segment_count_response_data_instance.to_dict()
# create an instance of SegmentCountResponseData from a dict
segment_count_response_data_from_dict = SegmentCountResponseData.from_dict(segment_count_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


