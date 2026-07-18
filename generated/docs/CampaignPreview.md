# CampaignPreview


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**subject** | **str** |  | 
**html** | **str** | Rendered HTML body. | 
**text** | **str** | Rendered plain-text body. | 
**preview_text** | **str** | Inbox preview text. | 

## Example

```python
from mailermine_generated.models.campaign_preview import CampaignPreview

# TODO update the JSON string below
json = "{}"
# create an instance of CampaignPreview from a JSON string
campaign_preview_instance = CampaignPreview.from_json(json)
# print the JSON string representation of the object
print(CampaignPreview.to_json())

# convert the object into a dict
campaign_preview_dict = campaign_preview_instance.to_dict()
# create an instance of CampaignPreview from a dict
campaign_preview_from_dict = CampaignPreview.from_dict(campaign_preview_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


