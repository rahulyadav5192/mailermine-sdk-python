# CampaignStatistics


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | [**CampaignStatus**](CampaignStatus.md) |  | 
**status_label** | **str** |  | 
**total_recipients** | **int** |  | 
**queued_count** | **int** |  | 
**sending_count** | **int** |  | 
**sent_count** | **int** |  | 
**failed_count** | **int** |  | 
**completed_count** | **int** |  | 
**completion_percentage** | **float** | Completion percentage. | 
**estimated_remaining** | **int** |  | 
**started_at** | **datetime** |  | 
**completed_at** | **datetime** |  | 
**last_processed_at** | **datetime** |  | 

## Example

```python
from mailermine_generated.models.campaign_statistics import CampaignStatistics

# TODO update the JSON string below
json = "{}"
# create an instance of CampaignStatistics from a JSON string
campaign_statistics_instance = CampaignStatistics.from_json(json)
# print the JSON string representation of the object
print(CampaignStatistics.to_json())

# convert the object into a dict
campaign_statistics_dict = campaign_statistics_instance.to_dict()
# create an instance of CampaignStatistics from a dict
campaign_statistics_from_dict = CampaignStatistics.from_dict(campaign_statistics_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


