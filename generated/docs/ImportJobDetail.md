# ImportJobDetail


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Public import UUID. @format uuid | 
**status** | **str** | Import lifecycle status. @var &#39;draft&#39;|&#39;pending&#39;|&#39;queued&#39;|&#39;processing&#39;|&#39;completed&#39;|&#39;failed&#39; @example processing | 
**progress** | **int** | Completion percentage from 0 through 100. @example 65 | 
**original_filename** | **str** | Uploaded source filename. @example contacts.xlsx | 
**summary** | [**ImportJobSummary**](ImportJobSummary.md) |  | 
**metadata** | [**SendEmailRequestVariables**](SendEmailRequestVariables.md) |  | 
**counters** | [**SendEmailRequestVariables**](SendEmailRequestVariables.md) |  | 
**has_failures** | **bool** | Whether a downloadable failure CSV exists. @example false | 
**started_at** | **str** | Processing start time. @format date-time | 
**completed_at** | **str** | Processing completion time. @format date-time | 
**created_at** | **str** | Job creation time. @format date-time | 
**updated_at** | **str** | Last job update time. @format date-time | 
**progress_payload** | [**ImportProgress**](ImportProgress.md) | Live processing metrics for polling clients. | 

## Example

```python
from mailermine_generated.models.import_job_detail import ImportJobDetail

# TODO update the JSON string below
json = "{}"
# create an instance of ImportJobDetail from a JSON string
import_job_detail_instance = ImportJobDetail.from_json(json)
# print the JSON string representation of the object
print(ImportJobDetail.to_json())

# convert the object into a dict
import_job_detail_dict = import_job_detail_instance.to_dict()
# create an instance of ImportJobDetail from a dict
import_job_detail_from_dict = ImportJobDetail.from_dict(import_job_detail_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


