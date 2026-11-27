# UpdateContactRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email** | **str** | Replacement email address. | [optional] 
**first_name** | **str** | Replacement given name. | [optional] 
**last_name** | **str** |  | [optional] 
**status** | **str** | Replacement lifecycle status. | [optional] 
**subscribed** | **bool** | Replacement subscription state. | [optional] 
**metadata** | **Dict[str, object]** | Replacement metadata object when present. | [optional] 
**list_ids** | **List[UUID]** |  | [optional] 
**tag_ids** | **List[UUID]** |  | [optional] 
**tag_names** | **List[str]** |  | [optional] 
**custom_fields** | **Dict[str, object]** | Replacement custom-field map when present. | [optional] 

## Example

```python
from mailermine_generated.models.update_contact_request import UpdateContactRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateContactRequest from a JSON string
update_contact_request_instance = UpdateContactRequest.from_json(json)
# print the JSON string representation of the object
print(UpdateContactRequest.to_json())

# convert the object into a dict
update_contact_request_dict = update_contact_request_instance.to_dict()
# create an instance of UpdateContactRequest from a dict
update_contact_request_from_dict = UpdateContactRequest.from_dict(update_contact_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


