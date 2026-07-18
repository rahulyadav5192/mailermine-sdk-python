# CampaignLink


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**destination_url** | **str** | Tracked destination URL. @format uri | 
**clicks** | **int** |  | 
**unique_clicks** | **int** |  | 
**ctr** | **float** | Unique click-through rate against delivered messages. | 
**last_clicked_at** | **str** | Last click time. @format date-time | 

## Example

```python
from mailermine_generated.models.campaign_link import CampaignLink

# TODO update the JSON string below
json = "{}"
# create an instance of CampaignLink from a JSON string
campaign_link_instance = CampaignLink.from_json(json)
# print the JSON string representation of the object
print(CampaignLink.to_json())

# convert the object into a dict
campaign_link_dict = campaign_link_instance.to_dict()
# create an instance of CampaignLink from a dict
campaign_link_from_dict = CampaignLink.from_dict(campaign_link_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


