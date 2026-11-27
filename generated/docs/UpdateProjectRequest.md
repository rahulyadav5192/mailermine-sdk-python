# UpdateProjectRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Updated project name. | [optional] 
**slug** | **str** | Updated lowercase kebab-case slug. | [optional] 
**description** | **str** | Updated description; null clears it. | [optional] 
**environment** | **str** | Runtime environment. | [optional] 
**timezone** | **str** | IANA timezone. | [optional] 
**default_sender** | **str** | Default sender; null clears it. | [optional] 
**settings** | **Dict[str, object]** | Replacement settings object. | [optional] 
**status** | **str** | Archive or restore the project. | [optional] 

## Example

```python
from mailermine_generated.models.update_project_request import UpdateProjectRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateProjectRequest from a JSON string
update_project_request_instance = UpdateProjectRequest.from_json(json)
# print the JSON string representation of the object
print(UpdateProjectRequest.to_json())

# convert the object into a dict
update_project_request_dict = update_project_request_instance.to_dict()
# create an instance of UpdateProjectRequest from a dict
update_project_request_from_dict = UpdateProjectRequest.from_dict(update_project_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


