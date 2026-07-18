# AnalyticsMessagesResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** |  | 
**message** | **str** |  | 
**data** | [**AnalyticsMessages**](AnalyticsMessages.md) |  | 

## Example

```python
from mailermine_generated.models.analytics_messages_response import AnalyticsMessagesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AnalyticsMessagesResponse from a JSON string
analytics_messages_response_instance = AnalyticsMessagesResponse.from_json(json)
# print the JSON string representation of the object
print(AnalyticsMessagesResponse.to_json())

# convert the object into a dict
analytics_messages_response_dict = analytics_messages_response_instance.to_dict()
# create an instance of AnalyticsMessagesResponse from a dict
analytics_messages_response_from_dict = AnalyticsMessagesResponse.from_dict(analytics_messages_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


