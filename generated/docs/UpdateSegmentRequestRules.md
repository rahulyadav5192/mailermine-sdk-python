# UpdateSegmentRequestRules


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**logic** | **str** |  | 
**rules** | [**List[PreviewSegmentRequestRulesRulesInner]**](PreviewSegmentRequestRulesRulesInner.md) | &#x60;present&#x60; allows an empty rule tree (e.g. All Contacts); &#x60;required&#x60; would reject []. | 

## Example

```python
from mailermine_generated.models.update_segment_request_rules import UpdateSegmentRequestRules

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateSegmentRequestRules from a JSON string
update_segment_request_rules_instance = UpdateSegmentRequestRules.from_json(json)
# print the JSON string representation of the object
print(UpdateSegmentRequestRules.to_json())

# convert the object into a dict
update_segment_request_rules_dict = update_segment_request_rules_instance.to_dict()
# create an instance of UpdateSegmentRequestRules from a dict
update_segment_request_rules_from_dict = UpdateSegmentRequestRules.from_dict(update_segment_request_rules_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


