# AnalyticsProjectsProjectsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**name** | **str** |  | 
**sent** | **int** |  | 
**delivered** | **int** |  | 
**opened** | **int** |  | 
**clicked** | **int** |  | 

## Example

```python
from mailermine_generated.models.analytics_projects_projects_inner import AnalyticsProjectsProjectsInner

# TODO update the JSON string below
json = "{}"
# create an instance of AnalyticsProjectsProjectsInner from a JSON string
analytics_projects_projects_inner_instance = AnalyticsProjectsProjectsInner.from_json(json)
# print the JSON string representation of the object
print(AnalyticsProjectsProjectsInner.to_json())

# convert the object into a dict
analytics_projects_projects_inner_dict = analytics_projects_projects_inner_instance.to_dict()
# create an instance of AnalyticsProjectsProjectsInner from a dict
analytics_projects_projects_inner_from_dict = AnalyticsProjectsProjectsInner.from_dict(analytics_projects_projects_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


