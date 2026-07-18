# ImportJobResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** |  | 
**message** | **str** |  | 
**data** | [**ImportJob**](ImportJob.md) |  | 

## Example

```python
from mailermine_generated.models.import_job_response import ImportJobResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ImportJobResponse from a JSON string
import_job_response_instance = ImportJobResponse.from_json(json)
# print the JSON string representation of the object
print(ImportJobResponse.to_json())

# convert the object into a dict
import_job_response_dict = import_job_response_instance.to_dict()
# create an instance of ImportJobResponse from a dict
import_job_response_from_dict = ImportJobResponse.from_dict(import_job_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


