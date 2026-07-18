# UpdateCampaignRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Campaign name. | [optional] 
**subject** | **str** | Rendered email subject. | [optional] 
**preview_text** | **str** | Inbox preview text. | [optional] 
**from_name** | **str** | Sender display name. | [optional] 
**from_email** | **str** | Verified sender address. | [optional] 
**reply_to** | **str** | Optional reply address. | [optional] 
**template_uuid** | **UUID** | Published template UUID; empty string clears it. | [optional] 
**segment_uuid** | **UUID** | Audience segment UUID; empty string clears it. | [optional] 
**send_immediately** | **bool** | Whether delivery should be immediate. | [optional] 
**scheduled_at** | **datetime** | Scheduled date/time interpreted in &#x60;timezone&#x60;. ISO-8601 with offset. | [optional] 
**timezone** | **str** | IANA delivery timezone. | [optional] 
**builder_step** | **int** | Last completed builder step (1-6). | [optional] 

## Example

```python
from mailermine_generated.models.update_campaign_request import UpdateCampaignRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateCampaignRequest from a JSON string
update_campaign_request_instance = UpdateCampaignRequest.from_json(json)
# print the JSON string representation of the object
print(UpdateCampaignRequest.to_json())

# convert the object into a dict
update_campaign_request_dict = update_campaign_request_instance.to_dict()
# create an instance of UpdateCampaignRequest from a dict
update_campaign_request_from_dict = UpdateCampaignRequest.from_dict(update_campaign_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


