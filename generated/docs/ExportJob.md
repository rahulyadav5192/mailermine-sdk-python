# ExportJob


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Public export UUID. @format uuid | 
**status** | **str** | Export lifecycle status. @var &#39;pending&#39;|&#39;processing&#39;|&#39;completed&#39;|&#39;failed&#39; @example pending | 
**contact_count** | **int** | Number of contacts written to the export. @example 1250 | 
**filters** | [**SendEmailRequestVariables**](SendEmailRequestVariables.md) |  | 
**download_url** | **str** | Download URL, available only after completion. @format uri | 
**completed_at** | **str** | Processing completion time. @format date-time | 
**created_at** | **str** | Job creation time. @format date-time | 
**updated_at** | **str** | Last job update time. @format date-time | 

## Example

```python
from mailermine_generated.models.export_job import ExportJob

# TODO update the JSON string below
json = "{}"
# create an instance of ExportJob from a JSON string
export_job_instance = ExportJob.from_json(json)
# print the JSON string representation of the object
print(ExportJob.to_json())

# convert the object into a dict
export_job_dict = export_job_instance.to_dict()
# create an instance of ExportJob from a dict
export_job_from_dict = ExportJob.from_dict(export_job_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


