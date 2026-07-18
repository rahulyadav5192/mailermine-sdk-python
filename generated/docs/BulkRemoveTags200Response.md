# BulkRemoveTags200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** |  | 
**message** | **str** |  | 
**data** | [**RemoveAudienceMembers200ResponseData**](RemoveAudienceMembers200ResponseData.md) |  | 

## Example

```python
from mailermine_generated.models.bulk_remove_tags200_response import BulkRemoveTags200Response

# TODO update the JSON string below
json = "{}"
# create an instance of BulkRemoveTags200Response from a JSON string
bulk_remove_tags200_response_instance = BulkRemoveTags200Response.from_json(json)
# print the JSON string representation of the object
print(BulkRemoveTags200Response.to_json())

# convert the object into a dict
bulk_remove_tags200_response_dict = bulk_remove_tags200_response_instance.to_dict()
# create an instance of BulkRemoveTags200Response from a dict
bulk_remove_tags200_response_from_dict = BulkRemoveTags200Response.from_dict(bulk_remove_tags200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


