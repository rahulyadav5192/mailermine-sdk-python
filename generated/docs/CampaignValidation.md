# CampaignValidation


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**valid** | **bool** |  | 
**errors** | **List[str]** | Blocking validation messages. @var list&lt;string&gt; | 
**warnings** | **List[str]** | Non-blocking validation messages. @var list&lt;string&gt; | 

## Example

```python
from mailermine_generated.models.campaign_validation import CampaignValidation

# TODO update the JSON string below
json = "{}"
# create an instance of CampaignValidation from a JSON string
campaign_validation_instance = CampaignValidation.from_json(json)
# print the JSON string representation of the object
print(CampaignValidation.to_json())

# convert the object into a dict
campaign_validation_dict = campaign_validation_instance.to_dict()
# create an instance of CampaignValidation from a dict
campaign_validation_from_dict = CampaignValidation.from_dict(campaign_validation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


