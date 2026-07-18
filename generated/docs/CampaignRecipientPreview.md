# CampaignRecipientPreview


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**estimated_count** | **int** |  | 
**subscribed_count** | **int** |  | 
**unsubscribed_count** | **int** |  | 
**suppressed_count** | **int** |  | 
**sample_contacts** | **List[Dict[str, object]]** | Up to ten representative matching contacts. @var list&lt;array&lt;string, mixed&gt;&gt; | 
**warnings** | **List[str]** | Audience warnings discovered during preview. @var list&lt;string&gt; | 

## Example

```python
from mailermine_generated.models.campaign_recipient_preview import CampaignRecipientPreview

# TODO update the JSON string below
json = "{}"
# create an instance of CampaignRecipientPreview from a JSON string
campaign_recipient_preview_instance = CampaignRecipientPreview.from_json(json)
# print the JSON string representation of the object
print(CampaignRecipientPreview.to_json())

# convert the object into a dict
campaign_recipient_preview_dict = campaign_recipient_preview_instance.to_dict()
# create an instance of CampaignRecipientPreview from a dict
campaign_recipient_preview_from_dict = CampaignRecipientPreview.from_dict(campaign_recipient_preview_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


