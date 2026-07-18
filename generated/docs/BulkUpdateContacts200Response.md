# BulkUpdateContacts200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** |  | 
**message** | **str** |  | 
**data** | [**BulkUpdateContacts200ResponseData**](BulkUpdateContacts200ResponseData.md) |  | 

## Example

```python
from mailermine_generated.models.bulk_update_contacts200_response import BulkUpdateContacts200Response

# TODO update the JSON string below
json = "{}"
# create an instance of BulkUpdateContacts200Response from a JSON string
bulk_update_contacts200_response_instance = BulkUpdateContacts200Response.from_json(json)
# print the JSON string representation of the object
print(BulkUpdateContacts200Response.to_json())

# convert the object into a dict
bulk_update_contacts200_response_dict = bulk_update_contacts200_response_instance.to_dict()
# create an instance of BulkUpdateContacts200Response from a dict
bulk_update_contacts200_response_from_dict = BulkUpdateContacts200Response.from_dict(bulk_update_contacts200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


