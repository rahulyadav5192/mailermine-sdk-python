# CampaignRecipientPreviewResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** |  | 
**message** | **str** |  | 
**data** | [**CampaignRecipientPreview**](CampaignRecipientPreview.md) |  | 

## Example

```python
from mailermine_generated.models.campaign_recipient_preview_response import CampaignRecipientPreviewResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CampaignRecipientPreviewResponse from a JSON string
campaign_recipient_preview_response_instance = CampaignRecipientPreviewResponse.from_json(json)
# print the JSON string representation of the object
print(CampaignRecipientPreviewResponse.to_json())

# convert the object into a dict
campaign_recipient_preview_response_dict = campaign_recipient_preview_response_instance.to_dict()
# create an instance of CampaignRecipientPreviewResponse from a dict
campaign_recipient_preview_response_from_dict = CampaignRecipientPreviewResponse.from_dict(campaign_recipient_preview_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


