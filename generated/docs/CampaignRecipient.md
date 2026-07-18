# CampaignRecipient


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | [**CampaignRecipientStatus**](CampaignRecipientStatus.md) |  | 
**status_label** | **str** | Human-readable recipient status. | 
**queued_at** | **datetime** |  | 
**sent_at** | **datetime** |  | 
**delivered_at** | **datetime** |  | 
**failed_at** | **datetime** |  | 
**failure_reason** | **str** | Failure detail, present for failed recipients. | 
**contact** | [**CampaignActivityPayload**](CampaignActivityPayload.md) |  | 
**message** | [**CampaignActivityPayload**](CampaignActivityPayload.md) |  | 

## Example

```python
from mailermine_generated.models.campaign_recipient import CampaignRecipient

# TODO update the JSON string below
json = "{}"
# create an instance of CampaignRecipient from a JSON string
campaign_recipient_instance = CampaignRecipient.from_json(json)
# print the JSON string representation of the object
print(CampaignRecipient.to_json())

# convert the object into a dict
campaign_recipient_dict = campaign_recipient_instance.to_dict()
# create an instance of CampaignRecipient from a dict
campaign_recipient_from_dict = CampaignRecipient.from_dict(campaign_recipient_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


