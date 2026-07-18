# CampaignPreviewResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** |  | 
**message** | **str** |  | 
**data** | [**CampaignPreview**](CampaignPreview.md) |  | 

## Example

```python
from mailermine_generated.models.campaign_preview_response import CampaignPreviewResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CampaignPreviewResponse from a JSON string
campaign_preview_response_instance = CampaignPreviewResponse.from_json(json)
# print the JSON string representation of the object
print(CampaignPreviewResponse.to_json())

# convert the object into a dict
campaign_preview_response_dict = campaign_preview_response_instance.to_dict()
# create an instance of CampaignPreviewResponse from a dict
campaign_preview_response_from_dict = CampaignPreviewResponse.from_dict(campaign_preview_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


