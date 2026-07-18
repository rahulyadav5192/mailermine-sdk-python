# BulkDeleteContacts200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** |  | 
**message** | **str** |  | 
**data** | [**BulkDeleteContacts200ResponseData**](BulkDeleteContacts200ResponseData.md) |  | 

## Example

```python
from mailermine_generated.models.bulk_delete_contacts200_response import BulkDeleteContacts200Response

# TODO update the JSON string below
json = "{}"
# create an instance of BulkDeleteContacts200Response from a JSON string
bulk_delete_contacts200_response_instance = BulkDeleteContacts200Response.from_json(json)
# print the JSON string representation of the object
print(BulkDeleteContacts200Response.to_json())

# convert the object into a dict
bulk_delete_contacts200_response_dict = bulk_delete_contacts200_response_instance.to_dict()
# create an instance of BulkDeleteContacts200Response from a dict
bulk_delete_contacts200_response_from_dict = BulkDeleteContacts200Response.from_dict(bulk_delete_contacts200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


