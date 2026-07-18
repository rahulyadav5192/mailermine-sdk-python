# CampaignAnalytics


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**recipients** | **int** |  | 
**queued** | **int** |  | 
**sent** | **int** |  | 
**delivered** | **int** |  | 
**opened** | **int** |  | 
**unique_opens** | **int** |  | 
**clicked** | **int** |  | 
**unique_clicks** | **int** |  | 
**bounced** | **int** |  | 
**complained** | **int** |  | 
**failed** | **int** |  | 
**unsubscribed** | **int** |  | 
**delivery_rate** | **float** | Delivered divided by recipients or sent, as a percentage. @example 98.4 | 
**open_rate** | **float** | Unique opens divided by delivered, as a percentage. @example 48.2 | 
**click_rate** | **float** | Unique clicks divided by delivered, as a percentage. @example 12.7 | 
**bounce_rate** | **float** | Bounces divided by recipients or sent, as a percentage. | 
**complaint_rate** | **float** | Complaints divided by recipients or sent, as a percentage. | 
**failure_rate** | **float** |  | 
**unsubscribe_rate** | **float** |  | 
**average_delivery_time_seconds** | **float** | Mean provider delivery latency in seconds. | 

## Example

```python
from mailermine_generated.models.campaign_analytics import CampaignAnalytics

# TODO update the JSON string below
json = "{}"
# create an instance of CampaignAnalytics from a JSON string
campaign_analytics_instance = CampaignAnalytics.from_json(json)
# print the JSON string representation of the object
print(CampaignAnalytics.to_json())

# convert the object into a dict
campaign_analytics_dict = campaign_analytics_instance.to_dict()
# create an instance of CampaignAnalytics from a dict
campaign_analytics_from_dict = CampaignAnalytics.from_dict(campaign_analytics_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


