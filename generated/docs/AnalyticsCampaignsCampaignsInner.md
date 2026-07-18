# AnalyticsCampaignsCampaignsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**name** | **str** |  | 
**sent** | **int** |  | 
**delivered** | **int** |  | 
**opened** | **int** |  | 
**clicked** | **int** |  | 
**open_rate** | **float** |  | 
**click_rate** | **float** |  | 

## Example

```python
from mailermine_generated.models.analytics_campaigns_campaigns_inner import AnalyticsCampaignsCampaignsInner

# TODO update the JSON string below
json = "{}"
# create an instance of AnalyticsCampaignsCampaignsInner from a JSON string
analytics_campaigns_campaigns_inner_instance = AnalyticsCampaignsCampaignsInner.from_json(json)
# print the JSON string representation of the object
print(AnalyticsCampaignsCampaignsInner.to_json())

# convert the object into a dict
analytics_campaigns_campaigns_inner_dict = analytics_campaigns_campaigns_inner_instance.to_dict()
# create an instance of AnalyticsCampaignsCampaignsInner from a dict
analytics_campaigns_campaigns_inner_from_dict = AnalyticsCampaignsCampaignsInner.from_dict(analytics_campaigns_campaigns_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


