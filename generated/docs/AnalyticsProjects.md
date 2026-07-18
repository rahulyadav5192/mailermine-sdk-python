# AnalyticsProjects


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_from** | **str** | Range start (ISO-8601). | 
**to** | **str** | Range end (ISO-8601). | 
**projects** | [**List[AnalyticsProjectsProjectsInner]**](AnalyticsProjectsProjectsInner.md) | Project metrics for the authenticated project. | 
**note** | **str** | Present when multiple projects are requested with a single-project key. | 

## Example

```python
from mailermine_generated.models.analytics_projects import AnalyticsProjects

# TODO update the JSON string below
json = "{}"
# create an instance of AnalyticsProjects from a JSON string
analytics_projects_instance = AnalyticsProjects.from_json(json)
# print the JSON string representation of the object
print(AnalyticsProjects.to_json())

# convert the object into a dict
analytics_projects_dict = analytics_projects_instance.to_dict()
# create an instance of AnalyticsProjects from a dict
analytics_projects_from_dict = AnalyticsProjects.from_dict(analytics_projects_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


