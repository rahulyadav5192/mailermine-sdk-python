# CustomField


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Public custom field UUID. @format uuid | 
**name** | **str** | Human-readable field name. @example Company | 
**slug** | **str** | Stable value key used in contact payloads. @example company | 
**type** | **str** | Field value type. @var &#39;text&#39;|&#39;textarea&#39;|&#39;number&#39;|&#39;boolean&#39;|&#39;date&#39;|&#39;datetime&#39;|&#39;select&#39;|&#39;multi_select&#39;|&#39;email&#39;|&#39;url&#39;|&#39;phone&#39;|&#39;json&#39; @example text | 
**description** | **str** | Optional field description. @example Contact employer | 
**required** | **bool** | Whether imports and writes require a value. @example false | 
**default_value** | [**CampaignActivityPayload**](CampaignActivityPayload.md) |  | 
**options** | **List[Dict[str, object]]** | Allowed choices for select fields. @var list&lt;mixed&gt;|null | 
**created_at** | **str** | Creation time. @format date-time | 
**updated_at** | **str** | Last update time. @format date-time | 

## Example

```python
from mailermine_generated.models.custom_field import CustomField

# TODO update the JSON string below
json = "{}"
# create an instance of CustomField from a JSON string
custom_field_instance = CustomField.from_json(json)
# print the JSON string representation of the object
print(CustomField.to_json())

# convert the object into a dict
custom_field_dict = custom_field_instance.to_dict()
# create an instance of CustomField from a dict
custom_field_from_dict = CustomField.from_dict(custom_field_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


