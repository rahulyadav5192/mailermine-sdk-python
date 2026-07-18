# MessageDetailResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** |  | 
**message** | **str** |  | 
**data** | [**DeliveryLog**](DeliveryLog.md) |  | 

## Example

```python
from mailermine_generated.models.message_detail_response import MessageDetailResponse

# TODO update the JSON string below
json = "{}"
# create an instance of MessageDetailResponse from a JSON string
message_detail_response_instance = MessageDetailResponse.from_json(json)
# print the JSON string representation of the object
print(MessageDetailResponse.to_json())

# convert the object into a dict
message_detail_response_dict = message_detail_response_instance.to_dict()
# create an instance of MessageDetailResponse from a dict
message_detail_response_from_dict = MessageDetailResponse.from_dict(message_detail_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


