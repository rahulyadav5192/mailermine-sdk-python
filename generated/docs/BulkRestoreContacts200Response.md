# BulkRestoreContacts200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** |  | 
**message** | **str** |  | 
**data** | [**BulkRestoreContacts200ResponseData**](BulkRestoreContacts200ResponseData.md) |  | 

## Example

```python
from mailermine_generated.models.bulk_restore_contacts200_response import BulkRestoreContacts200Response

# TODO update the JSON string below
json = "{}"
# create an instance of BulkRestoreContacts200Response from a JSON string
bulk_restore_contacts200_response_instance = BulkRestoreContacts200Response.from_json(json)
# print the JSON string representation of the object
print(BulkRestoreContacts200Response.to_json())

# convert the object into a dict
bulk_restore_contacts200_response_dict = bulk_restore_contacts200_response_instance.to_dict()
# create an instance of BulkRestoreContacts200Response from a dict
bulk_restore_contacts200_response_from_dict = BulkRestoreContacts200Response.from_dict(bulk_restore_contacts200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


