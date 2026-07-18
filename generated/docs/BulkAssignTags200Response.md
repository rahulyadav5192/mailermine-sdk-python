# BulkAssignTags200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** |  | 
**message** | **str** |  | 
**data** | [**BulkAssignTags200ResponseData**](BulkAssignTags200ResponseData.md) |  | 

## Example

```python
from mailermine_generated.models.bulk_assign_tags200_response import BulkAssignTags200Response

# TODO update the JSON string below
json = "{}"
# create an instance of BulkAssignTags200Response from a JSON string
bulk_assign_tags200_response_instance = BulkAssignTags200Response.from_json(json)
# print the JSON string representation of the object
print(BulkAssignTags200Response.to_json())

# convert the object into a dict
bulk_assign_tags200_response_dict = bulk_assign_tags200_response_instance.to_dict()
# create an instance of BulkAssignTags200Response from a dict
bulk_assign_tags200_response_from_dict = BulkAssignTags200Response.from_dict(bulk_assign_tags200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


