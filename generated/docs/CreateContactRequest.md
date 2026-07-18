# CreateContactRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email** | **str** | Unique email address within the project. | 
**first_name** | **str** | Given name. | [optional] 
**last_name** | **str** | Family name. | [optional] 
**status** | **str** | Initial contact lifecycle status. | [optional] 
**subscribed** | **bool** | Initial marketing subscription state. | [optional] [default to True]
**source** | **str** | Acquisition source. | [optional] [default to 'api']
**metadata** | [**SendEmailRequestVariables**](SendEmailRequestVariables.md) |  | [optional] 
**list_ids** | **List[UUID]** | List UUIDs to assign. | [optional] 
**tag_ids** | **List[UUID]** | Existing tag UUIDs to assign. | [optional] 
**tag_names** | **List[str]** | Tag names to resolve or create. | [optional] 
**custom_fields** | [**SendEmailRequestVariables**](SendEmailRequestVariables.md) |  | [optional] 

## Example

```python
from mailermine_generated.models.create_contact_request import CreateContactRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateContactRequest from a JSON string
create_contact_request_instance = CreateContactRequest.from_json(json)
# print the JSON string representation of the object
print(CreateContactRequest.to_json())

# convert the object into a dict
create_contact_request_dict = create_contact_request_instance.to_dict()
# create an instance of CreateContactRequest from a dict
create_contact_request_from_dict = CreateContactRequest.from_dict(create_contact_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


