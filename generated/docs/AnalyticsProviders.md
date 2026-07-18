# AnalyticsProviders


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_from** | **str** | Range start (ISO-8601). | 
**to** | **str** | Range end (ISO-8601). | 
**providers** | [**List[AnalyticsProvidersProvidersInner]**](AnalyticsProvidersProvidersInner.md) | Provider volume, ordered by count descending. | 

## Example

```python
from mailermine_generated.models.analytics_providers import AnalyticsProviders

# TODO update the JSON string below
json = "{}"
# create an instance of AnalyticsProviders from a JSON string
analytics_providers_instance = AnalyticsProviders.from_json(json)
# print the JSON string representation of the object
print(AnalyticsProviders.to_json())

# convert the object into a dict
analytics_providers_dict = analytics_providers_instance.to_dict()
# create an instance of AnalyticsProviders from a dict
analytics_providers_from_dict = AnalyticsProviders.from_dict(analytics_providers_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


