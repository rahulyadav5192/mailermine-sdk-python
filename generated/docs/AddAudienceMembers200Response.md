# AddAudienceMembers200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** |  | 
**message** | **str** |  | 
**data** | [**AddAudienceMembers200ResponseData**](AddAudienceMembers200ResponseData.md) |  | 

## Example

```python
from mailermine_generated.models.add_audience_members200_response import AddAudienceMembers200Response

# TODO update the JSON string below
json = "{}"
# create an instance of AddAudienceMembers200Response from a JSON string
add_audience_members200_response_instance = AddAudienceMembers200Response.from_json(json)
# print the JSON string representation of the object
print(AddAudienceMembers200Response.to_json())

# convert the object into a dict
add_audience_members200_response_dict = add_audience_members200_response_instance.to_dict()
# create an instance of AddAudienceMembers200Response from a dict
add_audience_members200_response_from_dict = AddAudienceMembers200Response.from_dict(add_audience_members200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


