# CreateSegmentRequestRules

Dynamic membership rule tree.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**logic** | **str** |  | 
**rules** | [**List[PreviewSegmentRequestRulesRulesInner]**](PreviewSegmentRequestRulesRulesInner.md) |  | 

## Example

```python
from mailermine_generated.models.create_segment_request_rules import CreateSegmentRequestRules

# TODO update the JSON string below
json = "{}"
# create an instance of CreateSegmentRequestRules from a JSON string
create_segment_request_rules_instance = CreateSegmentRequestRules.from_json(json)
# print the JSON string representation of the object
print(CreateSegmentRequestRules.to_json())

# convert the object into a dict
create_segment_request_rules_dict = create_segment_request_rules_instance.to_dict()
# create an instance of CreateSegmentRequestRules from a dict
create_segment_request_rules_from_dict = CreateSegmentRequestRules.from_dict(create_segment_request_rules_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


