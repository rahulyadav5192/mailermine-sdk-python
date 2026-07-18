# PreviewSegmentRequestRules

Unsaved dynamic membership rule tree.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**logic** | **str** |  | 
**rules** | [**List[PreviewSegmentRequestRulesRulesInner]**](PreviewSegmentRequestRulesRulesInner.md) |  | 

## Example

```python
from mailermine_generated.models.preview_segment_request_rules import PreviewSegmentRequestRules

# TODO update the JSON string below
json = "{}"
# create an instance of PreviewSegmentRequestRules from a JSON string
preview_segment_request_rules_instance = PreviewSegmentRequestRules.from_json(json)
# print the JSON string representation of the object
print(PreviewSegmentRequestRules.to_json())

# convert the object into a dict
preview_segment_request_rules_dict = preview_segment_request_rules_instance.to_dict()
# create an instance of PreviewSegmentRequestRules from a dict
preview_segment_request_rules_from_dict = PreviewSegmentRequestRules.from_dict(preview_segment_request_rules_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


