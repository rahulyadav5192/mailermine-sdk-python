# AnalyticsProjectsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** |  | 
**message** | **str** |  | 
**data** | [**AnalyticsProjects**](AnalyticsProjects.md) |  | 

## Example

```python
from mailermine_generated.models.analytics_projects_response import AnalyticsProjectsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AnalyticsProjectsResponse from a JSON string
analytics_projects_response_instance = AnalyticsProjectsResponse.from_json(json)
# print the JSON string representation of the object
print(AnalyticsProjectsResponse.to_json())

# convert the object into a dict
analytics_projects_response_dict = analytics_projects_response_instance.to_dict()
# create an instance of AnalyticsProjectsResponse from a dict
analytics_projects_response_from_dict = AnalyticsProjectsResponse.from_dict(analytics_projects_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


