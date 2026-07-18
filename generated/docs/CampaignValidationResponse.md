# CampaignValidationResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** |  | 
**message** | **str** |  | 
**data** | [**CampaignValidation**](CampaignValidation.md) |  | 

## Example

```python
from mailermine_generated.models.campaign_validation_response import CampaignValidationResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CampaignValidationResponse from a JSON string
campaign_validation_response_instance = CampaignValidationResponse.from_json(json)
# print the JSON string representation of the object
print(CampaignValidationResponse.to_json())

# convert the object into a dict
campaign_validation_response_dict = campaign_validation_response_instance.to_dict()
# create an instance of CampaignValidationResponse from a dict
campaign_validation_response_from_dict = CampaignValidationResponse.from_dict(campaign_validation_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


