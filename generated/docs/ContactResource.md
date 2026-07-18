# ContactResource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Public contact UUID. @format uuid @example 550e8400-e29b-41d4-a716-446655440000 | 
**email** | **str** | Normalized email address. @format email @example ada@example.com | 
**first_name** | **str** | Given name. @example Ada | 
**last_name** | **str** | Family name. @example Lovelace | 
**status** | **str** | Contact lifecycle status. @var &#39;active&#39;|&#39;unsubscribed&#39;|&#39;suppressed&#39;|&#39;bounced&#39;|&#39;complained&#39;|&#39;archived&#39; @example active | 
**subscribed** | **bool** | Whether the contact is subscribed to marketing email. @example true | 
**source** | **str** | Acquisition source. @example api | 
**metadata** | [**SendEmailRequestVariables**](SendEmailRequestVariables.md) |  | 
**tags** | **List[Dict[str, object]]** | Loaded tag relationships. @var list&lt;array{id: string, name: string, color: string}&gt; | 
**lists** | **List[Dict[str, object]]** | Loaded list relationships. @var list&lt;array{id: string, name: string}&gt; | 
**custom_fields** | [**SendEmailRequestVariables**](SendEmailRequestVariables.md) |  | 
**created_at** | **str** | Creation time (ISO-8601). @format date-time @example 2026-07-16T10:00:00.000000Z | 
**updated_at** | **str** | Last update time (ISO-8601). @format date-time @example 2026-07-16T11:00:00.000000Z | 

## Example

```python
from mailermine_generated.models.contact_resource import ContactResource

# TODO update the JSON string below
json = "{}"
# create an instance of ContactResource from a JSON string
contact_resource_instance = ContactResource.from_json(json)
# print the JSON string representation of the object
print(ContactResource.to_json())

# convert the object into a dict
contact_resource_dict = contact_resource_instance.to_dict()
# create an instance of ContactResource from a dict
contact_resource_from_dict = ContactResource.from_dict(contact_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


