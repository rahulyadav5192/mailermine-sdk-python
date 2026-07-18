# CustomFieldResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** |  | 
**message** | **str** |  | 
**data** | [**CustomField**](CustomField.md) |  | 

## Example

```python
from mailermine_generated.models.custom_field_response import CustomFieldResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CustomFieldResponse from a JSON string
custom_field_response_instance = CustomFieldResponse.from_json(json)
# print the JSON string representation of the object
print(CustomFieldResponse.to_json())

# convert the object into a dict
custom_field_response_dict = custom_field_response_instance.to_dict()
# create an instance of CustomFieldResponse from a dict
custom_field_response_from_dict = CustomFieldResponse.from_dict(custom_field_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


