# ExportContactsRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**search** | **str** | Optional email or name filter. | [optional] 
**status** | **str** | Optional status filter. | [optional] 
**subscribed** | **bool** | Optional subscription filter. | [optional] 
**list** | **UUID** | Optional list UUID filter. | [optional] 
**tag_name** | **str** | Optional tag-name filter. | [optional] 
**ids** | **List[UUID]** | Optional contact UUID selection. | [optional] 

## Example

```python
from mailermine_generated.models.export_contacts_request import ExportContactsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ExportContactsRequest from a JSON string
export_contacts_request_instance = ExportContactsRequest.from_json(json)
# print the JSON string representation of the object
print(ExportContactsRequest.to_json())

# convert the object into a dict
export_contacts_request_dict = export_contacts_request_instance.to_dict()
# create an instance of ExportContactsRequest from a dict
export_contacts_request_from_dict = ExportContactsRequest.from_dict(export_contacts_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


