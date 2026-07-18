# WebhookProject

Owning project summary. Present when the project relation is loaded.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**name** | **str** |  | 

## Example

```python
from mailermine_generated.models.webhook_project import WebhookProject

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookProject from a JSON string
webhook_project_instance = WebhookProject.from_json(json)
# print the JSON string representation of the object
print(WebhookProject.to_json())

# convert the object into a dict
webhook_project_dict = webhook_project_instance.to_dict()
# create an instance of WebhookProject from a dict
webhook_project_from_dict = WebhookProject.from_dict(webhook_project_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


