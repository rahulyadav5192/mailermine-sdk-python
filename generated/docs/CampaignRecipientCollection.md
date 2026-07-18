# CampaignRecipientCollection


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** |  | 
**message** | **str** |  | 
**data** | [**List[CampaignRecipient]**](CampaignRecipient.md) |  | 
**meta** | [**PaginationMeta**](PaginationMeta.md) |  | 

## Example

```python
from mailermine_generated.models.campaign_recipient_collection import CampaignRecipientCollection

# TODO update the JSON string below
json = "{}"
# create an instance of CampaignRecipientCollection from a JSON string
campaign_recipient_collection_instance = CampaignRecipientCollection.from_json(json)
# print the JSON string representation of the object
print(CampaignRecipientCollection.to_json())

# convert the object into a dict
campaign_recipient_collection_dict = campaign_recipient_collection_instance.to_dict()
# create an instance of CampaignRecipientCollection from a dict
campaign_recipient_collection_from_dict = CampaignRecipientCollection.from_dict(campaign_recipient_collection_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


