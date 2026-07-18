# CampaignActivity


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**event** | [**CampaignActivityEvent**](CampaignActivityEvent.md) |  | 
**event_label** | **str** |  | 
**payload** | [**CampaignActivityPayload**](CampaignActivityPayload.md) |  | 
**created_at** | **str** | Activity time. @format date-time | 

## Example

```python
from mailermine_generated.models.campaign_activity import CampaignActivity

# TODO update the JSON string below
json = "{}"
# create an instance of CampaignActivity from a JSON string
campaign_activity_instance = CampaignActivity.from_json(json)
# print the JSON string representation of the object
print(CampaignActivity.to_json())

# convert the object into a dict
campaign_activity_dict = campaign_activity_instance.to_dict()
# create an instance of CampaignActivity from a dict
campaign_activity_from_dict = CampaignActivity.from_dict(campaign_activity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


