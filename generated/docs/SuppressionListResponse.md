# SuppressionListResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** |  | 
**message** | **str** |  | 
**data** | [**List[Suppression]**](Suppression.md) |  | 
**meta** | [**PaginationMeta**](PaginationMeta.md) |  | 

## Example

```python
from mailermine_generated.models.suppression_list_response import SuppressionListResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SuppressionListResponse from a JSON string
suppression_list_response_instance = SuppressionListResponse.from_json(json)
# print the JSON string representation of the object
print(SuppressionListResponse.to_json())

# convert the object into a dict
suppression_list_response_dict = suppression_list_response_instance.to_dict()
# create an instance of SuppressionListResponse from a dict
suppression_list_response_from_dict = SuppressionListResponse.from_dict(suppression_list_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


