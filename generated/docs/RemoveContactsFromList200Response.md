# RemoveContactsFromList200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** |  | 
**message** | **str** |  | 
**data** | [**RemoveAudienceMembers200ResponseData**](RemoveAudienceMembers200ResponseData.md) |  | 

## Example

```python
from mailermine_generated.models.remove_contacts_from_list200_response import RemoveContactsFromList200Response

# TODO update the JSON string below
json = "{}"
# create an instance of RemoveContactsFromList200Response from a JSON string
remove_contacts_from_list200_response_instance = RemoveContactsFromList200Response.from_json(json)
# print the JSON string representation of the object
print(RemoveContactsFromList200Response.to_json())

# convert the object into a dict
remove_contacts_from_list200_response_dict = remove_contacts_from_list200_response_instance.to_dict()
# create an instance of RemoveContactsFromList200Response from a dict
remove_contacts_from_list200_response_from_dict = RemoveContactsFromList200Response.from_dict(remove_contacts_from_list200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


