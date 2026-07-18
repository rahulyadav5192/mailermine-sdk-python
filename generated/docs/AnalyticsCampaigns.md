# AnalyticsCampaigns


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_from** | **str** | Range start (ISO-8601). | 
**to** | **str** | Range end (ISO-8601). | 
**campaigns** | [**List[AnalyticsCampaignsCampaignsInner]**](AnalyticsCampaignsCampaignsInner.md) | Campaigns ranked by send volume. | 

## Example

```python
from mailermine_generated.models.analytics_campaigns import AnalyticsCampaigns

# TODO update the JSON string below
json = "{}"
# create an instance of AnalyticsCampaigns from a JSON string
analytics_campaigns_instance = AnalyticsCampaigns.from_json(json)
# print the JSON string representation of the object
print(AnalyticsCampaigns.to_json())

# convert the object into a dict
analytics_campaigns_dict = analytics_campaigns_instance.to_dict()
# create an instance of AnalyticsCampaigns from a dict
analytics_campaigns_from_dict = AnalyticsCampaigns.from_dict(analytics_campaigns_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


