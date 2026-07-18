# DuplicateCampaignRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**include_schedule** | **bool** | Copy delivery timing into the draft duplicate. | [optional] [default to False]

## Example

```python
from mailermine_generated.models.duplicate_campaign_request import DuplicateCampaignRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DuplicateCampaignRequest from a JSON string
duplicate_campaign_request_instance = DuplicateCampaignRequest.from_json(json)
# print the JSON string representation of the object
print(DuplicateCampaignRequest.to_json())

# convert the object into a dict
duplicate_campaign_request_dict = duplicate_campaign_request_instance.to_dict()
# create an instance of DuplicateCampaignRequest from a dict
duplicate_campaign_request_from_dict = DuplicateCampaignRequest.from_dict(duplicate_campaign_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


