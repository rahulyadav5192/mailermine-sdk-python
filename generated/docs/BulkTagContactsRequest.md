# BulkTagContactsRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**contact_ids** | **List[UUID]** | Contact UUIDs to mutate. | 
**tag_ids** | **List[UUID]** | Tag UUIDs to assign or remove. | 

## Example

```python
from mailermine_generated.models.bulk_tag_contacts_request import BulkTagContactsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of BulkTagContactsRequest from a JSON string
bulk_tag_contacts_request_instance = BulkTagContactsRequest.from_json(json)
# print the JSON string representation of the object
print(BulkTagContactsRequest.to_json())

# convert the object into a dict
bulk_tag_contacts_request_dict = bulk_tag_contacts_request_instance.to_dict()
# create an instance of BulkTagContactsRequest from a dict
bulk_tag_contacts_request_from_dict = BulkTagContactsRequest.from_dict(bulk_tag_contacts_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


