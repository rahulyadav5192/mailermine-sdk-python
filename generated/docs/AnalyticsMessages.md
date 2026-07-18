# AnalyticsMessages


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_from** | **str** | Range start (ISO-8601). | 
**to** | **str** | Range end (ISO-8601). | 
**totals** | [**AnalyticsMessagesTotals**](AnalyticsMessagesTotals.md) |  | 
**by_status** | [**SendEmailRequestVariables**](SendEmailRequestVariables.md) |  | 
**daily** | [**List[AnalyticsMessagesDailyInner]**](AnalyticsMessagesDailyInner.md) | Daily message metrics. | 

## Example

```python
from mailermine_generated.models.analytics_messages import AnalyticsMessages

# TODO update the JSON string below
json = "{}"
# create an instance of AnalyticsMessages from a JSON string
analytics_messages_instance = AnalyticsMessages.from_json(json)
# print the JSON string representation of the object
print(AnalyticsMessages.to_json())

# convert the object into a dict
analytics_messages_dict = analytics_messages_instance.to_dict()
# create an instance of AnalyticsMessages from a dict
analytics_messages_from_dict = AnalyticsMessages.from_dict(analytics_messages_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


