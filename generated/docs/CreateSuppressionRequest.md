# CreateSuppressionRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email** | **str** | Email address to suppress. | 
**reason** | [**SuppressionReason**](SuppressionReason.md) | Reason for suppression. | 
**notes** | **str** | Optional operator notes. | [optional] 

## Example

```python
from mailermine_generated.models.create_suppression_request import CreateSuppressionRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateSuppressionRequest from a JSON string
create_suppression_request_instance = CreateSuppressionRequest.from_json(json)
# print the JSON string representation of the object
print(CreateSuppressionRequest.to_json())

# convert the object into a dict
create_suppression_request_dict = create_suppression_request_instance.to_dict()
# create an instance of CreateSuppressionRequest from a dict
create_suppression_request_from_dict = CreateSuppressionRequest.from_dict(create_suppression_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


