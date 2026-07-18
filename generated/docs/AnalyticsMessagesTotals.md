# AnalyticsMessagesTotals

Aggregate totals for the range.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sent** | **int** |  | 
**delivered** | **int** |  | 
**opened** | **int** |  | 
**clicked** | **int** |  | 
**bounced** | **int** |  | 
**complained** | **int** |  | 

## Example

```python
from mailermine_generated.models.analytics_messages_totals import AnalyticsMessagesTotals

# TODO update the JSON string below
json = "{}"
# create an instance of AnalyticsMessagesTotals from a JSON string
analytics_messages_totals_instance = AnalyticsMessagesTotals.from_json(json)
# print the JSON string representation of the object
print(AnalyticsMessagesTotals.to_json())

# convert the object into a dict
analytics_messages_totals_dict = analytics_messages_totals_instance.to_dict()
# create an instance of AnalyticsMessagesTotals from a dict
analytics_messages_totals_from_dict = AnalyticsMessagesTotals.from_dict(analytics_messages_totals_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


