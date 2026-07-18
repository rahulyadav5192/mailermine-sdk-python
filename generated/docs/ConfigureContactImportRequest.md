# ConfigureContactImportRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**field_mappings** | **Dict[str, str]** | Map of CSV column names to MailerMine contact fields. | 
**duplicate_strategy** | **str** |  | [optional] 
**default_status** | **str** |  | [optional] 
**import_source** | **str** |  | [optional] 
**timezone** | **str** |  | [optional] 
**country** | **str** |  | [optional] 
**double_opt_in** | **bool** |  | [optional] 
**tag_separator** | **str** |  | [optional] 
**create_missing_tags** | **bool** |  | [optional] 
**audience_mode** | **str** |  | [optional] 
**audience_uuid** | **UUID** |  | [optional] 
**create_missing_audiences** | **bool** |  | [optional] 
**new_properties** | **List[str]** |  | [optional] 

## Example

```python
from mailermine_generated.models.configure_contact_import_request import ConfigureContactImportRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ConfigureContactImportRequest from a JSON string
configure_contact_import_request_instance = ConfigureContactImportRequest.from_json(json)
# print the JSON string representation of the object
print(ConfigureContactImportRequest.to_json())

# convert the object into a dict
configure_contact_import_request_dict = configure_contact_import_request_instance.to_dict()
# create an instance of ConfigureContactImportRequest from a dict
configure_contact_import_request_from_dict = ConfigureContactImportRequest.from_dict(configure_contact_import_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


