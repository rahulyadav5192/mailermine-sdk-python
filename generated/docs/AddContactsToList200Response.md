# AddContactsToList200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** |  | 
**message** | **str** |  | 
**data** | [**AddAudienceMembers200ResponseData**](AddAudienceMembers200ResponseData.md) |  | 

## Example

```python
from mailermine_generated.models.add_contacts_to_list200_response import AddContactsToList200Response

# TODO update the JSON string below
json = "{}"
# create an instance of AddContactsToList200Response from a JSON string
add_contacts_to_list200_response_instance = AddContactsToList200Response.from_json(json)
# print the JSON string representation of the object
print(AddContactsToList200Response.to_json())

# convert the object into a dict
add_contacts_to_list200_response_dict = add_contacts_to_list200_response_instance.to_dict()
# create an instance of AddContactsToList200Response from a dict
add_contacts_to_list200_response_from_dict = AddContactsToList200Response.from_dict(add_contacts_to_list200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


