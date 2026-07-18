# AnalyticsOverviewTopLinksInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**destination_url** | **str** |  | 
**clicks** | **int** |  | 
**unique_clicks** | **int** |  | 
**ctr** | **float** |  | 
**last_clicked_at** | **str** |  | 

## Example

```python
from mailermine_generated.models.analytics_overview_top_links_inner import AnalyticsOverviewTopLinksInner

# TODO update the JSON string below
json = "{}"
# create an instance of AnalyticsOverviewTopLinksInner from a JSON string
analytics_overview_top_links_inner_instance = AnalyticsOverviewTopLinksInner.from_json(json)
# print the JSON string representation of the object
print(AnalyticsOverviewTopLinksInner.to_json())

# convert the object into a dict
analytics_overview_top_links_inner_dict = analytics_overview_top_links_inner_instance.to_dict()
# create an instance of AnalyticsOverviewTopLinksInner from a dict
analytics_overview_top_links_inner_from_dict = AnalyticsOverviewTopLinksInner.from_dict(analytics_overview_top_links_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


