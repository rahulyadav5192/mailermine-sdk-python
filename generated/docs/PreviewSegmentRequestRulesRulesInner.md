# PreviewSegmentRequestRulesRulesInner

A single condition (`field`, `operator`, `value`) or a nested rule group.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_field** | **str** | Contact attribute or custom field key. | [optional] 
**operator** | **str** | Comparison operator, e.g. &#x60;equals&#x60;, &#x60;contains&#x60;, &#x60;greater_than&#x60;. | [optional] 
**value** | **object** |  | [optional] 

## Example

```python
from mailermine_generated.models.preview_segment_request_rules_rules_inner import PreviewSegmentRequestRulesRulesInner

# TODO update the JSON string below
json = "{}"
# create an instance of PreviewSegmentRequestRulesRulesInner from a JSON string
preview_segment_request_rules_rules_inner_instance = PreviewSegmentRequestRulesRulesInner.from_json(json)
# print the JSON string representation of the object
print(PreviewSegmentRequestRulesRulesInner.to_json())

# convert the object into a dict
preview_segment_request_rules_rules_inner_dict = preview_segment_request_rules_rules_inner_instance.to_dict()
# create an instance of PreviewSegmentRequestRulesRulesInner from a dict
preview_segment_request_rules_rules_inner_from_dict = PreviewSegmentRequestRulesRulesInner.from_dict(preview_segment_request_rules_rules_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


