# CampaignActivityCollection


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** |  | 
**message** | **str** |  | 
**data** | [**List[CampaignActivity]**](CampaignActivity.md) |  | 

## Example

```python
from mailermine_generated.models.campaign_activity_collection import CampaignActivityCollection

# TODO update the JSON string below
json = "{}"
# create an instance of CampaignActivityCollection from a JSON string
campaign_activity_collection_instance = CampaignActivityCollection.from_json(json)
# print the JSON string representation of the object
print(CampaignActivityCollection.to_json())

# convert the object into a dict
campaign_activity_collection_dict = campaign_activity_collection_instance.to_dict()
# create an instance of CampaignActivityCollection from a dict
campaign_activity_collection_from_dict = CampaignActivityCollection.from_dict(campaign_activity_collection_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


