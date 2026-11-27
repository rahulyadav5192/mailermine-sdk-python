# Suppression


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Public suppression UUID. | 
**email** | **str** | Suppressed email address. | 
**reason** | [**SuppressionReason**](SuppressionReason.md) | Reason the address was suppressed. | 
**reason_label** | **str** | Human-readable reason label. | 
**source** | **str** | Origin of the suppression (for example &#x60;bounce&#x60;, &#x60;manual&#x60;, &#x60;api&#x60;). | 
**notes** | **str** | Optional operator notes. | 
**metadata** | [**AnalyticsMessagesByStatus**](AnalyticsMessagesByStatus.md) |  | 
**restored_at** | **str** | Time the suppression was restored (ISO-8601), or &#x60;null&#x60; if active. | 
**created_at** | **str** | Creation timestamp (ISO-8601). | 
**updated_at** | **str** | Last update timestamp (ISO-8601). | 

## Example

```python
from mailermine_generated.models.suppression import Suppression

# TODO update the JSON string below
json = "{}"
# create an instance of Suppression from a JSON string
suppression_instance = Suppression.from_json(json)
# print the JSON string representation of the object
print(Suppression.to_json())

# convert the object into a dict
suppression_dict = suppression_instance.to_dict()
# create an instance of Suppression from a dict
suppression_from_dict = Suppression.from_dict(suppression_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


