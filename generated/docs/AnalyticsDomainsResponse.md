# AnalyticsDomainsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** |  | 
**message** | **str** |  | 
**data** | [**AnalyticsDomains**](AnalyticsDomains.md) |  | 

## Example

```python
from mailermine_generated.models.analytics_domains_response import AnalyticsDomainsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AnalyticsDomainsResponse from a JSON string
analytics_domains_response_instance = AnalyticsDomainsResponse.from_json(json)
# print the JSON string representation of the object
print(AnalyticsDomainsResponse.to_json())

# convert the object into a dict
analytics_domains_response_dict = analytics_domains_response_instance.to_dict()
# create an instance of AnalyticsDomainsResponse from a dict
analytics_domains_response_from_dict = AnalyticsDomainsResponse.from_dict(analytics_domains_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


