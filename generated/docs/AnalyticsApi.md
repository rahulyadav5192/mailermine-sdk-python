# mailermine_generated.AnalyticsApi

All URIs are relative to *http://127.0.0.1:8000/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**analytics_campaigns**](AnalyticsApi.md#analytics_campaigns) | **GET** /analytics/campaigns | Campaign analytics breakdown
[**analytics_domains**](AnalyticsApi.md#analytics_domains) | **GET** /analytics/domains | Domain analytics
[**analytics_engagement**](AnalyticsApi.md#analytics_engagement) | **GET** /analytics/engagement | Engagement analytics
[**analytics_messages**](AnalyticsApi.md#analytics_messages) | **GET** /analytics/messages | Message analytics
[**analytics_overview**](AnalyticsApi.md#analytics_overview) | **GET** /analytics/overview | Analytics overview
[**analytics_projects**](AnalyticsApi.md#analytics_projects) | **GET** /analytics/projects | Project analytics
[**analytics_providers**](AnalyticsApi.md#analytics_providers) | **GET** /analytics/providers | Provider analytics


# **analytics_campaigns**
> AnalyticsCampaignsResponse analytics_campaigns(var_from=var_from, to=to)

Campaign analytics breakdown

Return the top campaigns by volume with open and click rates. Required scope: `analytics.read`.

### Example

* Bearer (API Key) Authentication (bearerAuth):

```python
import mailermine_generated
from mailermine_generated.models.analytics_campaigns_response import AnalyticsCampaignsResponse
from mailermine_generated.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://127.0.0.1:8000/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = mailermine_generated.Configuration(
    host = "http://127.0.0.1:8000/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (API Key): bearerAuth
configuration = mailermine_generated.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with mailermine_generated.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = mailermine_generated.AnalyticsApi(api_client)
    var_from = '2013-10-20T19:20:30+01:00' # datetime | Range start (ISO-8601). Defaults to 30 days ago. (optional)
    to = '2013-10-20T19:20:30+01:00' # datetime | Range end (ISO-8601). Defaults to now. (optional)

    try:
        # Campaign analytics breakdown
        api_response = api_instance.analytics_campaigns(var_from=var_from, to=to)
        print("The response of AnalyticsApi->analytics_campaigns:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AnalyticsApi->analytics_campaigns: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **var_from** | **datetime**| Range start (ISO-8601). Defaults to 30 days ago. | [optional] 
 **to** | **datetime**| Range end (ISO-8601). Defaults to now. | [optional] 

### Return type

[**AnalyticsCampaignsResponse**](AnalyticsCampaignsResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Campaigns analytics retrieved successfully. |  * X-RateLimit-Limit - Maximum requests per window. <br>  * X-RateLimit-Remaining - Requests remaining in the current window. <br>  * X-RateLimit-Reset - Unix timestamp when the current window resets. <br>  |
**400** | Malformed JSON or invalid request. |  -  |
**401** | Missing or invalid API key. |  -  |
**403** | Account suspended, feature denied, or cross-project access blocked. |  -  |
**404** | Resource not found. |  -  |
**409** | Request conflicts with current state. |  -  |
**422** | Validation failed or plan limit exceeded. |  -  |
**429** | Rate limit exceeded. Retry after the &#x60;Retry-After&#x60; header value. |  -  |
**500** | Unexpected server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **analytics_domains**
> AnalyticsDomainsResponse analytics_domains(var_from=var_from, to=to)

Domain analytics

Return message volume grouped by sending domain (top 50). Required scope: `analytics.read`.

### Example

* Bearer (API Key) Authentication (bearerAuth):

```python
import mailermine_generated
from mailermine_generated.models.analytics_domains_response import AnalyticsDomainsResponse
from mailermine_generated.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://127.0.0.1:8000/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = mailermine_generated.Configuration(
    host = "http://127.0.0.1:8000/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (API Key): bearerAuth
configuration = mailermine_generated.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with mailermine_generated.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = mailermine_generated.AnalyticsApi(api_client)
    var_from = '2013-10-20T19:20:30+01:00' # datetime | Range start (ISO-8601). Defaults to 30 days ago. (optional)
    to = '2013-10-20T19:20:30+01:00' # datetime | Range end (ISO-8601). Defaults to now. (optional)

    try:
        # Domain analytics
        api_response = api_instance.analytics_domains(var_from=var_from, to=to)
        print("The response of AnalyticsApi->analytics_domains:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AnalyticsApi->analytics_domains: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **var_from** | **datetime**| Range start (ISO-8601). Defaults to 30 days ago. | [optional] 
 **to** | **datetime**| Range end (ISO-8601). Defaults to now. | [optional] 

### Return type

[**AnalyticsDomainsResponse**](AnalyticsDomainsResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Domains analytics retrieved successfully. |  * X-RateLimit-Limit - Maximum requests per window. <br>  * X-RateLimit-Remaining - Requests remaining in the current window. <br>  * X-RateLimit-Reset - Unix timestamp when the current window resets. <br>  |
**400** | Malformed JSON or invalid request. |  -  |
**401** | Missing or invalid API key. |  -  |
**403** | Account suspended, feature denied, or cross-project access blocked. |  -  |
**404** | Resource not found. |  -  |
**409** | Request conflicts with current state. |  -  |
**422** | Validation failed or plan limit exceeded. |  -  |
**429** | Rate limit exceeded. Retry after the &#x60;Retry-After&#x60; header value. |  -  |
**500** | Unexpected server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **analytics_engagement**
> AnalyticsEngagementResponse analytics_engagement(var_from=var_from, to=to)

Engagement analytics

Return open, click, CTR, and CTOR engagement rates. Required scope: `analytics.read`.

### Example

* Bearer (API Key) Authentication (bearerAuth):

```python
import mailermine_generated
from mailermine_generated.models.analytics_engagement_response import AnalyticsEngagementResponse
from mailermine_generated.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://127.0.0.1:8000/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = mailermine_generated.Configuration(
    host = "http://127.0.0.1:8000/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (API Key): bearerAuth
configuration = mailermine_generated.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with mailermine_generated.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = mailermine_generated.AnalyticsApi(api_client)
    var_from = '2013-10-20T19:20:30+01:00' # datetime | Range start (ISO-8601). Defaults to 30 days ago. (optional)
    to = '2013-10-20T19:20:30+01:00' # datetime | Range end (ISO-8601). Defaults to now. (optional)

    try:
        # Engagement analytics
        api_response = api_instance.analytics_engagement(var_from=var_from, to=to)
        print("The response of AnalyticsApi->analytics_engagement:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AnalyticsApi->analytics_engagement: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **var_from** | **datetime**| Range start (ISO-8601). Defaults to 30 days ago. | [optional] 
 **to** | **datetime**| Range end (ISO-8601). Defaults to now. | [optional] 

### Return type

[**AnalyticsEngagementResponse**](AnalyticsEngagementResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Engagement analytics retrieved successfully. |  * X-RateLimit-Limit - Maximum requests per window. <br>  * X-RateLimit-Remaining - Requests remaining in the current window. <br>  * X-RateLimit-Reset - Unix timestamp when the current window resets. <br>  |
**400** | Malformed JSON or invalid request. |  -  |
**401** | Missing or invalid API key. |  -  |
**403** | Account suspended, feature denied, or cross-project access blocked. |  -  |
**404** | Resource not found. |  -  |
**409** | Request conflicts with current state. |  -  |
**422** | Validation failed or plan limit exceeded. |  -  |
**429** | Rate limit exceeded. Retry after the &#x60;Retry-After&#x60; header value. |  -  |
**500** | Unexpected server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **analytics_messages**
> AnalyticsMessagesResponse analytics_messages(var_from=var_from, to=to)

Message analytics

Return message totals, status breakdown, and daily metrics. Required scope: `analytics.read`.

### Example

* Bearer (API Key) Authentication (bearerAuth):

```python
import mailermine_generated
from mailermine_generated.models.analytics_messages_response import AnalyticsMessagesResponse
from mailermine_generated.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://127.0.0.1:8000/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = mailermine_generated.Configuration(
    host = "http://127.0.0.1:8000/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (API Key): bearerAuth
configuration = mailermine_generated.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with mailermine_generated.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = mailermine_generated.AnalyticsApi(api_client)
    var_from = '2013-10-20T19:20:30+01:00' # datetime | Range start (ISO-8601). Defaults to 30 days ago. (optional)
    to = '2013-10-20T19:20:30+01:00' # datetime | Range end (ISO-8601). Defaults to now. (optional)

    try:
        # Message analytics
        api_response = api_instance.analytics_messages(var_from=var_from, to=to)
        print("The response of AnalyticsApi->analytics_messages:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AnalyticsApi->analytics_messages: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **var_from** | **datetime**| Range start (ISO-8601). Defaults to 30 days ago. | [optional] 
 **to** | **datetime**| Range end (ISO-8601). Defaults to now. | [optional] 

### Return type

[**AnalyticsMessagesResponse**](AnalyticsMessagesResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Messages analytics retrieved successfully. |  * X-RateLimit-Limit - Maximum requests per window. <br>  * X-RateLimit-Remaining - Requests remaining in the current window. <br>  * X-RateLimit-Reset - Unix timestamp when the current window resets. <br>  |
**400** | Malformed JSON or invalid request. |  -  |
**401** | Missing or invalid API key. |  -  |
**403** | Account suspended, feature denied, or cross-project access blocked. |  -  |
**404** | Resource not found. |  -  |
**409** | Request conflicts with current state. |  -  |
**422** | Validation failed or plan limit exceeded. |  -  |
**429** | Rate limit exceeded. Retry after the &#x60;Retry-After&#x60; header value. |  -  |
**500** | Unexpected server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **analytics_overview**
> AnalyticsOverviewResponse analytics_overview(var_from=var_from, to=to)

Analytics overview

Return aggregate performance metrics, daily series, top campaigns, and recent activity. Required scope: `analytics.read`.

### Example

* Bearer (API Key) Authentication (bearerAuth):

```python
import mailermine_generated
from mailermine_generated.models.analytics_overview_response import AnalyticsOverviewResponse
from mailermine_generated.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://127.0.0.1:8000/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = mailermine_generated.Configuration(
    host = "http://127.0.0.1:8000/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (API Key): bearerAuth
configuration = mailermine_generated.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with mailermine_generated.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = mailermine_generated.AnalyticsApi(api_client)
    var_from = '2013-10-20T19:20:30+01:00' # datetime | Range start (ISO-8601). Defaults to 30 days ago. (optional)
    to = '2013-10-20T19:20:30+01:00' # datetime | Range end (ISO-8601). Defaults to now. (optional)

    try:
        # Analytics overview
        api_response = api_instance.analytics_overview(var_from=var_from, to=to)
        print("The response of AnalyticsApi->analytics_overview:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AnalyticsApi->analytics_overview: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **var_from** | **datetime**| Range start (ISO-8601). Defaults to 30 days ago. | [optional] 
 **to** | **datetime**| Range end (ISO-8601). Defaults to now. | [optional] 

### Return type

[**AnalyticsOverviewResponse**](AnalyticsOverviewResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Analytics overview retrieved successfully. |  * X-RateLimit-Limit - Maximum requests per window. <br>  * X-RateLimit-Remaining - Requests remaining in the current window. <br>  * X-RateLimit-Reset - Unix timestamp when the current window resets. <br>  |
**400** | Malformed JSON or invalid request. |  -  |
**401** | Missing or invalid API key. |  -  |
**403** | Account suspended, feature denied, or cross-project access blocked. |  -  |
**404** | Resource not found. |  -  |
**409** | Request conflicts with current state. |  -  |
**422** | Validation failed or plan limit exceeded. |  -  |
**429** | Rate limit exceeded. Retry after the &#x60;Retry-After&#x60; header value. |  -  |
**500** | Unexpected server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **analytics_projects**
> AnalyticsProjectsResponse analytics_projects(var_from=var_from, to=to)

Project analytics

Return performance metrics for the authenticated project. Required scope: `analytics.read`.

### Example

* Bearer (API Key) Authentication (bearerAuth):

```python
import mailermine_generated
from mailermine_generated.models.analytics_projects_response import AnalyticsProjectsResponse
from mailermine_generated.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://127.0.0.1:8000/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = mailermine_generated.Configuration(
    host = "http://127.0.0.1:8000/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (API Key): bearerAuth
configuration = mailermine_generated.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with mailermine_generated.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = mailermine_generated.AnalyticsApi(api_client)
    var_from = '2013-10-20T19:20:30+01:00' # datetime | Range start (ISO-8601). Defaults to 30 days ago. (optional)
    to = '2013-10-20T19:20:30+01:00' # datetime | Range end (ISO-8601). Defaults to now. (optional)

    try:
        # Project analytics
        api_response = api_instance.analytics_projects(var_from=var_from, to=to)
        print("The response of AnalyticsApi->analytics_projects:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AnalyticsApi->analytics_projects: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **var_from** | **datetime**| Range start (ISO-8601). Defaults to 30 days ago. | [optional] 
 **to** | **datetime**| Range end (ISO-8601). Defaults to now. | [optional] 

### Return type

[**AnalyticsProjectsResponse**](AnalyticsProjectsResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Projects analytics retrieved successfully. |  * X-RateLimit-Limit - Maximum requests per window. <br>  * X-RateLimit-Remaining - Requests remaining in the current window. <br>  * X-RateLimit-Reset - Unix timestamp when the current window resets. <br>  |
**400** | Malformed JSON or invalid request. |  -  |
**401** | Missing or invalid API key. |  -  |
**403** | Account suspended, feature denied, or cross-project access blocked. |  -  |
**404** | Resource not found. |  -  |
**409** | Request conflicts with current state. |  -  |
**422** | Validation failed or plan limit exceeded. |  -  |
**429** | Rate limit exceeded. Retry after the &#x60;Retry-After&#x60; header value. |  -  |
**500** | Unexpected server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **analytics_providers**
> AnalyticsProvidersResponse analytics_providers(var_from=var_from, to=to)

Provider analytics

Return message volume grouped by delivery provider. Required scope: `analytics.read`.

### Example

* Bearer (API Key) Authentication (bearerAuth):

```python
import mailermine_generated
from mailermine_generated.models.analytics_providers_response import AnalyticsProvidersResponse
from mailermine_generated.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://127.0.0.1:8000/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = mailermine_generated.Configuration(
    host = "http://127.0.0.1:8000/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (API Key): bearerAuth
configuration = mailermine_generated.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with mailermine_generated.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = mailermine_generated.AnalyticsApi(api_client)
    var_from = '2013-10-20T19:20:30+01:00' # datetime | Range start (ISO-8601). Defaults to 30 days ago. (optional)
    to = '2013-10-20T19:20:30+01:00' # datetime | Range end (ISO-8601). Defaults to now. (optional)

    try:
        # Provider analytics
        api_response = api_instance.analytics_providers(var_from=var_from, to=to)
        print("The response of AnalyticsApi->analytics_providers:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AnalyticsApi->analytics_providers: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **var_from** | **datetime**| Range start (ISO-8601). Defaults to 30 days ago. | [optional] 
 **to** | **datetime**| Range end (ISO-8601). Defaults to now. | [optional] 

### Return type

[**AnalyticsProvidersResponse**](AnalyticsProvidersResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Providers analytics retrieved successfully. |  * X-RateLimit-Limit - Maximum requests per window. <br>  * X-RateLimit-Remaining - Requests remaining in the current window. <br>  * X-RateLimit-Reset - Unix timestamp when the current window resets. <br>  |
**400** | Malformed JSON or invalid request. |  -  |
**401** | Missing or invalid API key. |  -  |
**403** | Account suspended, feature denied, or cross-project access blocked. |  -  |
**404** | Resource not found. |  -  |
**409** | Request conflicts with current state. |  -  |
**422** | Validation failed or plan limit exceeded. |  -  |
**429** | Rate limit exceeded. Retry after the &#x60;Retry-After&#x60; header value. |  -  |
**500** | Unexpected server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

