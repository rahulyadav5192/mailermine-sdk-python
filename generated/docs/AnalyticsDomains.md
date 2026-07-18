# AnalyticsDomains


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_from** | **str** | Range start (ISO-8601). | 
**to** | **str** | Range end (ISO-8601). | 
**domains** | [**List[AnalyticsDomainsDomainsInner]**](AnalyticsDomainsDomainsInner.md) | Sending domain volume, ordered by count descending (top 50). | 

## Example

```python
from mailermine_generated.models.analytics_domains import AnalyticsDomains

# TODO update the JSON string below
json = "{}"
# create an instance of AnalyticsDomains from a JSON string
analytics_domains_instance = AnalyticsDomains.from_json(json)
# print the JSON string representation of the object
print(AnalyticsDomains.to_json())

# convert the object into a dict
analytics_domains_dict = analytics_domains_instance.to_dict()
# create an instance of AnalyticsDomains from a dict
analytics_domains_from_dict = AnalyticsDomains.from_dict(analytics_domains_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


