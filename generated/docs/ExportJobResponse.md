# ExportJobResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** |  | 
**message** | **str** |  | 
**data** | [**ExportJob**](ExportJob.md) |  | 

## Example

```python
from mailermine_generated.models.export_job_response import ExportJobResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ExportJobResponse from a JSON string
export_job_response_instance = ExportJobResponse.from_json(json)
# print the JSON string representation of the object
print(ExportJobResponse.to_json())

# convert the object into a dict
export_job_response_dict = export_job_response_instance.to_dict()
# create an instance of ExportJobResponse from a dict
export_job_response_from_dict = ExportJobResponse.from_dict(export_job_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


