# ImportProgress


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uuid** | **str** | Import UUID. @format uuid | 
**status** | **str** | Current status. @var &#39;draft&#39;|&#39;pending&#39;|&#39;queued&#39;|&#39;processing&#39;|&#39;completed&#39;|&#39;failed&#39; | 
**status_label** | **str** | Human-readable status label. | 
**progress** | **int** | Completion percentage. @example 65 | 
**rows_total** | **int** |  | 
**rows_processed** | **int** |  | 
**rows_remaining** | **int** |  | 
**rows_imported** | **int** |  | 
**rows_updated** | **int** |  | 
**rows_failed** | **int** |  | 
**rows_skipped** | **int** |  | 
**current_batch** | **int** |  | 
**total_batches** | **int** |  | 
**eta_seconds** | **int** | Estimated seconds remaining. | 
**speed_per_minute** | **int** | Processing speed in rows per minute. | 
**summary** | [**ImportJobSummary**](ImportJobSummary.md) |  | 
**original_filename** | **str** |  | 
**started_at** | **datetime** |  | 
**completed_at** | **datetime** |  | 
**has_failures** | **bool** |  | 

## Example

```python
from mailermine_generated.models.import_progress import ImportProgress

# TODO update the JSON string below
json = "{}"
# create an instance of ImportProgress from a JSON string
import_progress_instance = ImportProgress.from_json(json)
# print the JSON string representation of the object
print(ImportProgress.to_json())

# convert the object into a dict
import_progress_dict = import_progress_instance.to_dict()
# create an instance of ImportProgress from a dict
import_progress_from_dict = ImportProgress.from_dict(import_progress_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


