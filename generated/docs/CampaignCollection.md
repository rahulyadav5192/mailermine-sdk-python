# CampaignCollection


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** |  | 
**message** | **str** |  | 
**data** | [**List[CampaignResource]**](CampaignResource.md) |  | 
**meta** | [**PaginationMeta**](PaginationMeta.md) |  | 

## Example

```python
from mailermine_generated.models.campaign_collection import CampaignCollection

# TODO update the JSON string below
json = "{}"
# create an instance of CampaignCollection from a JSON string
campaign_collection_instance = CampaignCollection.from_json(json)
# print the JSON string representation of the object
print(CampaignCollection.to_json())

# convert the object into a dict
campaign_collection_dict = campaign_collection_instance.to_dict()
# create an instance of CampaignCollection from a dict
campaign_collection_from_dict = CampaignCollection.from_dict(campaign_collection_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


