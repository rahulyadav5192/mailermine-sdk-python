# RemoveAudienceMembers200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** |  | 
**message** | **str** |  | 
**data** | [**RemoveAudienceMembers200ResponseData**](RemoveAudienceMembers200ResponseData.md) |  | 

## Example

```python
from mailermine_generated.models.remove_audience_members200_response import RemoveAudienceMembers200Response

# TODO update the JSON string below
json = "{}"
# create an instance of RemoveAudienceMembers200Response from a JSON string
remove_audience_members200_response_instance = RemoveAudienceMembers200Response.from_json(json)
# print the JSON string representation of the object
print(RemoveAudienceMembers200Response.to_json())

# convert the object into a dict
remove_audience_members200_response_dict = remove_audience_members200_response_instance.to_dict()
# create an instance of RemoveAudienceMembers200Response from a dict
remove_audience_members200_response_from_dict = RemoveAudienceMembers200Response.from_dict(remove_audience_members200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


