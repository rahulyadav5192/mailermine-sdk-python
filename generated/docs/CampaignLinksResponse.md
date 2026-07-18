# CampaignLinksResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** |  | 
**message** | **str** |  | 
**data** | [**List[CampaignLink]**](CampaignLink.md) |  | 

## Example

```python
from mailermine_generated.models.campaign_links_response import CampaignLinksResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CampaignLinksResponse from a JSON string
campaign_links_response_instance = CampaignLinksResponse.from_json(json)
# print the JSON string representation of the object
print(CampaignLinksResponse.to_json())

# convert the object into a dict
campaign_links_response_dict = campaign_links_response_instance.to_dict()
# create an instance of CampaignLinksResponse from a dict
campaign_links_response_from_dict = CampaignLinksResponse.from_dict(campaign_links_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


