# ProjectResource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Public project UUID. @example 550e8400-e29b-41d4-a716-446655440000 | 
**name** | **str** | Display name. @example Production Mail | 
**slug** | **str** | Workspace-unique slug. @example production-mail | 
**description** | **str** | Optional project description. @example Customer-facing transactional email | 
**environment** | **str** | Runtime environment. @var &#39;production&#39;|&#39;staging&#39;|&#39;development&#39;|&#39;test&#39; @example production | 
**timezone** | **str** | IANA timezone. @example UTC | 
**default_sender** | **str** | Default sender address hint. @example hello@example.com | 
**status** | **str** | Project lifecycle status. @var &#39;active&#39;|&#39;archived&#39;|&#39;inactive&#39; @example active | 
**settings** | [**SendEmailRequestVariables**](SendEmailRequestVariables.md) |  | 
**email_count** | **int** | Number of messages in the project. @example 1240 | 
**domain_count** | **int** | Number of sending domains. @example 2 | 
**api_key_count** | **int** | Number of API keys. @example 3 | 
**created_at** | **str** | Creation time (ISO-8601). @format date-time @example 2026-07-16T10:00:00.000000Z | 
**updated_at** | **str** | Last update time (ISO-8601). @format date-time @example 2026-07-16T11:00:00.000000Z | 

## Example

```python
from mailermine_generated.models.project_resource import ProjectResource

# TODO update the JSON string below
json = "{}"
# create an instance of ProjectResource from a JSON string
project_resource_instance = ProjectResource.from_json(json)
# print the JSON string representation of the object
print(ProjectResource.to_json())

# convert the object into a dict
project_resource_dict = project_resource_instance.to_dict()
# create an instance of ProjectResource from a dict
project_resource_from_dict = ProjectResource.from_dict(project_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


