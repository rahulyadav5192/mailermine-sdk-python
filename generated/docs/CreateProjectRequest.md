# CreateProjectRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Project display name. | 
**slug** | **str** | Lowercase kebab-case slug; generated when omitted. | [optional] 
**description** | **str** | Optional project description. | [optional] 
**environment** | **str** | Runtime environment. | [optional] 
**timezone** | **str** | IANA timezone. | [optional] 
**default_sender** | **str** | Default sender address hint. | [optional] 
**settings** | **Dict[str, object]** | Extensible project settings. &#x60;tracking.opens&#x60; and &#x60;tracking.clicks&#x60; (booleans, default true) set the project default for open and click tracking. | [optional] 

## Example

```python
from mailermine_generated.models.create_project_request import CreateProjectRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateProjectRequest from a JSON string
create_project_request_instance = CreateProjectRequest.from_json(json)
# print the JSON string representation of the object
print(CreateProjectRequest.to_json())

# convert the object into a dict
create_project_request_dict = create_project_request_instance.to_dict()
# create an instance of CreateProjectRequest from a dict
create_project_request_from_dict = CreateProjectRequest.from_dict(create_project_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


