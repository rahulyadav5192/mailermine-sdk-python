# ListContactsMembershipRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ids** | **List[UUID]** | Contact UUIDs to add or remove. | 

## Example

```python
from mailermine_generated.models.list_contacts_membership_request import ListContactsMembershipRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ListContactsMembershipRequest from a JSON string
list_contacts_membership_request_instance = ListContactsMembershipRequest.from_json(json)
# print the JSON string representation of the object
print(ListContactsMembershipRequest.to_json())

# convert the object into a dict
list_contacts_membership_request_dict = list_contacts_membership_request_instance.to_dict()
# create an instance of ListContactsMembershipRequest from a dict
list_contacts_membership_request_from_dict = ListContactsMembershipRequest.from_dict(list_contacts_membership_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


