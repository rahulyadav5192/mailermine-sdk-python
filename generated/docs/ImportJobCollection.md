# ImportJobCollection


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** |  | 
**message** | **str** |  | 
**data** | [**List[ImportJob]**](ImportJob.md) |  | 

## Example

```python
from mailermine_generated.models.import_job_collection import ImportJobCollection

# TODO update the JSON string below
json = "{}"
# create an instance of ImportJobCollection from a JSON string
import_job_collection_instance = ImportJobCollection.from_json(json)
# print the JSON string representation of the object
print(ImportJobCollection.to_json())

# convert the object into a dict
import_job_collection_dict = import_job_collection_instance.to_dict()
# create an instance of ImportJobCollection from a dict
import_job_collection_from_dict = ImportJobCollection.from_dict(import_job_collection_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


