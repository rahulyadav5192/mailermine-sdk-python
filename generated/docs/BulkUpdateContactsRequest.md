# BulkUpdateContactsRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ids** | **List[UUID]** | Contact UUIDs to update. | 
**status** | **str** | Status applied to every selected contact. | 

## Example

```python
from mailermine_generated.models.bulk_update_contacts_request import BulkUpdateContactsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of BulkUpdateContactsRequest from a JSON string
bulk_update_contacts_request_instance = BulkUpdateContactsRequest.from_json(json)
# print the JSON string representation of the object
print(BulkUpdateContactsRequest.to_json())

# convert the object into a dict
bulk_update_contacts_request_dict = bulk_update_contacts_request_instance.to_dict()
# create an instance of BulkUpdateContactsRequest from a dict
bulk_update_contacts_request_from_dict = BulkUpdateContactsRequest.from_dict(bulk_update_contacts_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


