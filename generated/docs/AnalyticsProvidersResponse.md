# AnalyticsProvidersResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** |  | 
**message** | **str** |  | 
**data** | [**AnalyticsProviders**](AnalyticsProviders.md) |  | 

## Example

```python
from mailermine_generated.models.analytics_providers_response import AnalyticsProvidersResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AnalyticsProvidersResponse from a JSON string
analytics_providers_response_instance = AnalyticsProvidersResponse.from_json(json)
# print the JSON string representation of the object
print(AnalyticsProvidersResponse.to_json())

# convert the object into a dict
analytics_providers_response_dict = analytics_providers_response_instance.to_dict()
# create an instance of AnalyticsProvidersResponse from a dict
analytics_providers_response_from_dict = AnalyticsProvidersResponse.from_dict(analytics_providers_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


