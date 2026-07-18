# CreateCampaignRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Campaign display name. | 
**subject** | **str** |  | [optional] 
**preview_text** | **str** |  | [optional] 
**from_name** | **str** |  | [optional] 
**from_email** | **str** |  | [optional] 
**reply_to** | **str** |  | [optional] 
**template_uuid** | **UUID** | Published template UUID. | [optional] 
**template_id** | **UUID** | Published template UUID (alias of &#x60;template_uuid&#x60;). | [optional] 
**segment_uuid** | **UUID** | Audience segment UUID. | [optional] 
**segment_id** | **UUID** | Audience segment UUID (alias of &#x60;segment_uuid&#x60;). | [optional] 
**send_immediately** | **bool** | Whether delivery should be immediate. Defaults to true (draft). | [optional] 
**scheduled_at** | **datetime** | Required when &#x60;send_immediately&#x60; is false. ISO-8601 date-time. | [optional] 
**timezone** | **str** | IANA timezone used to interpret &#x60;scheduled_at&#x60;. Required when scheduling. | [optional] 

## Example

```python
from mailermine_generated.models.create_campaign_request import CreateCampaignRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateCampaignRequest from a JSON string
create_campaign_request_instance = CreateCampaignRequest.from_json(json)
# print the JSON string representation of the object
print(CreateCampaignRequest.to_json())

# convert the object into a dict
create_campaign_request_dict = create_campaign_request_instance.to_dict()
# create an instance of CreateCampaignRequest from a dict
create_campaign_request_from_dict = CreateCampaignRequest.from_dict(create_campaign_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


