# AnalyticsMessagesDailyInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_date** | **str** |  | 
**sent** | **int** |  | 
**delivered** | **int** |  | 
**opened** | **int** |  | 
**clicked** | **int** |  | 
**bounced** | **int** |  | 
**complained** | **int** |  | 

## Example

```python
from mailermine_generated.models.analytics_messages_daily_inner import AnalyticsMessagesDailyInner

# TODO update the JSON string below
json = "{}"
# create an instance of AnalyticsMessagesDailyInner from a JSON string
analytics_messages_daily_inner_instance = AnalyticsMessagesDailyInner.from_json(json)
# print the JSON string representation of the object
print(AnalyticsMessagesDailyInner.to_json())

# convert the object into a dict
analytics_messages_daily_inner_dict = analytics_messages_daily_inner_instance.to_dict()
# create an instance of AnalyticsMessagesDailyInner from a dict
analytics_messages_daily_inner_from_dict = AnalyticsMessagesDailyInner.from_dict(analytics_messages_daily_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


