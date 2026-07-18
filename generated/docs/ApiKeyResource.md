# ApiKeyResource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Public key UUID. @format uuid @example 550e8400-e29b-41d4-a716-446655440000 | 
**name** | **str** | Human-readable key name. @example CI Production | 
**prefix** | **str** | Safe display prefix. @example mm_live_abcd... | 
**masked_key** | **str** | Alias of prefix. @example mm_live_abcd... | 
**status** | **str** | Key lifecycle status. @var &#39;active&#39;|&#39;disabled&#39;|&#39;revoked&#39;|&#39;expired&#39; @example active | 
**scopes** | **List[str]** | Granted scopes; null means full legacy access. @var list&lt;string&gt;|null | 
**permissions** | **List[str]** | Backward-compatible alias of scopes. @var list&lt;string&gt;|null | 
**environment** | **str** | Parent project environment. @example production | 
**last_used_at** | **str** | Last successful authentication time. @format date-time | 
**expires_at** | **str** | Expiration time; null means no expiry. @format date-time | 
**created_at** | **str** | Creation time. @format date-time | 
**updated_at** | **str** | Last update time. @format date-time | 
**secret** | **str** | One-time plaintext secret, returned only on create/rotate. @example mm_live_secret | 
**key** | **str** | Backward-compatible alias of secret, returned only on create/rotate. | 

## Example

```python
from mailermine_generated.models.api_key_resource import ApiKeyResource

# TODO update the JSON string below
json = "{}"
# create an instance of ApiKeyResource from a JSON string
api_key_resource_instance = ApiKeyResource.from_json(json)
# print the JSON string representation of the object
print(ApiKeyResource.to_json())

# convert the object into a dict
api_key_resource_dict = api_key_resource_instance.to_dict()
# create an instance of ApiKeyResource from a dict
api_key_resource_from_dict = ApiKeyResource.from_dict(api_key_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


