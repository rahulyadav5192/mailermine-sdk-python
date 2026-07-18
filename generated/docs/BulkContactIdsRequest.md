# BulkContactIdsRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ids** | **List[UUID]** |  | 

## Example

```python
from mailermine_generated.models.bulk_contact_ids_request import BulkContactIdsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of BulkContactIdsRequest from a JSON string
bulk_contact_ids_request_instance = BulkContactIdsRequest.from_json(json)
# print the JSON string representation of the object
print(BulkContactIdsRequest.to_json())

# convert the object into a dict
bulk_contact_ids_request_dict = bulk_contact_ids_request_instance.to_dict()
# create an instance of BulkContactIdsRequest from a dict
bulk_contact_ids_request_from_dict = BulkContactIdsRequest.from_dict(bulk_contact_ids_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


