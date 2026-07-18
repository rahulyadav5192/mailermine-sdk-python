# UpdateApiKeyRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Updated key name. | [optional] 
**expires_at** | **datetime** | Future expiration time; null clears expiry. | [optional] 
**status** | **str** | Key lifecycle status. | [optional] 
**scopes** | **List[str]** | Replacement scope list; null restores full legacy access. | [optional] 
**permissions** | **List[str]** | Backward-compatible alias of scopes. | [optional] 

## Example

```python
from mailermine_generated.models.update_api_key_request import UpdateApiKeyRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateApiKeyRequest from a JSON string
update_api_key_request_instance = UpdateApiKeyRequest.from_json(json)
# print the JSON string representation of the object
print(UpdateApiKeyRequest.to_json())

# convert the object into a dict
update_api_key_request_dict = update_api_key_request_instance.to_dict()
# create an instance of UpdateApiKeyRequest from a dict
update_api_key_request_from_dict = UpdateApiKeyRequest.from_dict(update_api_key_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


