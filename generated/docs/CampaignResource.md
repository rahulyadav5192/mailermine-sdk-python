# CampaignResource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uuid** | **str** | Public campaign UUID. @format uuid | 
**name** | **str** | Campaign display name. @example August product newsletter | 
**subject** | **str** | Email subject after campaign configuration. @example What is new in August | 
**preview_text** | **str** | Inbox preview text. | 
**from_name** | **str** | Sender display name. @example MailerMine | 
**from_email** | **str** | Verified sender email. @format email | 
**reply_to** | **str** | Optional reply address. @format email | 
**status** | [**CampaignStatus**](CampaignStatus.md) | Current lifecycle status. | 
**status_label** | **str** | Human-readable lifecycle status. @example Scheduled | 
**send_immediately** | **bool** | Whether delivery is configured as immediate. | 
**scheduled_at** | **str** | Scheduled delivery time. @format date-time | 
**timezone** | **str** | IANA delivery timezone. @example America/New_York | 
**sent_at** | **str** | Actual send time. @format date-time | 
**estimated_recipients** | **int** |  | 
**total_recipients** | **int** |  | 
**queued_count** | **int** |  | 
**sending_count** | **int** |  | 
**sent_count** | **int** |  | 
**failed_count** | **int** |  | 
**completed_count** | **int** |  | 
**completion_percentage** | **float** | Completion percentage from 0 through 100. @example 72.5 | 
**started_at** | **str** | Processing start time. @format date-time | 
**completed_at** | **str** | Processing completion time. @format date-time | 
**last_processed_at** | **str** | Last recipient processing time. @format date-time | 
**builder_step** | **int** | Last completed campaign-builder step (1-6). | 
**created_at** | **str** | Creation time. @format date-time | 
**updated_at** | **str** | Last update time. @format date-time | 
**project** | [**CampaignActivityPayload**](CampaignActivityPayload.md) |  | 
**template** | [**CampaignActivityPayload**](CampaignActivityPayload.md) |  | 
**segment** | [**CampaignActivityPayload**](CampaignActivityPayload.md) |  | 

## Example

```python
from mailermine_generated.models.campaign_resource import CampaignResource

# TODO update the JSON string below
json = "{}"
# create an instance of CampaignResource from a JSON string
campaign_resource_instance = CampaignResource.from_json(json)
# print the JSON string representation of the object
print(CampaignResource.to_json())

# convert the object into a dict
campaign_resource_dict = campaign_resource_instance.to_dict()
# create an instance of CampaignResource from a dict
campaign_resource_from_dict = CampaignResource.from_dict(campaign_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


