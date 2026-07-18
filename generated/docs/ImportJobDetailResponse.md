# ImportJobDetailResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** |  | 
**message** | **str** |  | 
**data** | [**ImportJobDetail**](ImportJobDetail.md) |  | 

## Example

```python
from mailermine_generated.models.import_job_detail_response import ImportJobDetailResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ImportJobDetailResponse from a JSON string
import_job_detail_response_instance = ImportJobDetailResponse.from_json(json)
# print the JSON string representation of the object
print(ImportJobDetailResponse.to_json())

# convert the object into a dict
import_job_detail_response_dict = import_job_detail_response_instance.to_dict()
# create an instance of ImportJobDetailResponse from a dict
import_job_detail_response_from_dict = ImportJobDetailResponse.from_dict(import_job_detail_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


