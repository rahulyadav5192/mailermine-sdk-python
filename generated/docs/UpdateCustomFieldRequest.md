# UpdateCustomFieldRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**type** | [**CustomFieldType**](CustomFieldType.md) |  | [optional] 
**field_type** | [**CustomFieldType**](CustomFieldType.md) |  | [optional] 
**description** | **str** |  | [optional] 
**required** | **bool** |  | [optional] 
**is_required** | **bool** |  | [optional] 
**default_value** | **str** |  | [optional] 
**options** | **List[str]** |  | [optional] 

## Example

```python
from mailermine_generated.models.update_custom_field_request import UpdateCustomFieldRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateCustomFieldRequest from a JSON string
update_custom_field_request_instance = UpdateCustomFieldRequest.from_json(json)
# print the JSON string representation of the object
print(UpdateCustomFieldRequest.to_json())

# convert the object into a dict
update_custom_field_request_dict = update_custom_field_request_instance.to_dict()
# create an instance of UpdateCustomFieldRequest from a dict
update_custom_field_request_from_dict = UpdateCustomFieldRequest.from_dict(update_custom_field_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


