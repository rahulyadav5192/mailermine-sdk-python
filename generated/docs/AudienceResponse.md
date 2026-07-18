# AudienceResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** |  | 
**message** | **str** |  | 
**data** | [**AudienceResource**](AudienceResource.md) |  | 

## Example

```python
from mailermine_generated.models.audience_response import AudienceResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AudienceResponse from a JSON string
audience_response_instance = AudienceResponse.from_json(json)
# print the JSON string representation of the object
print(AudienceResponse.to_json())

# convert the object into a dict
audience_response_dict = audience_response_instance.to_dict()
# create an instance of AudienceResponse from a dict
audience_response_from_dict = AudienceResponse.from_dict(audience_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


