# mailermine_generated.CampaignEventsApi

All URIs are relative to *https://mailermine.com/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**campaign_activities**](CampaignEventsApi.md#campaign_activities) | **GET** /campaigns/{campaign}/activities | List campaign activities
[**campaign_events**](CampaignEventsApi.md#campaign_events) | **GET** /campaigns/{campaign}/events | List campaign events
[**campaign_recipients**](CampaignEventsApi.md#campaign_recipients) | **GET** /campaigns/{campaign}/recipients | List campaign recipients
[**campaign_timeline**](CampaignEventsApi.md#campaign_timeline) | **GET** /campaigns/{campaign}/timeline | Get campaign timeline


# **campaign_activities**
> CampaignActivityCollection campaign_activities(campaign)

List campaign activities

List campaign-level lifecycle activities. Required scope: `campaigns.read`.

### Example

* Bearer (API Key) Authentication (bearerAuth):

```python
import mailermine_generated
from mailermine_generated.models.campaign_activity_collection import CampaignActivityCollection
from mailermine_generated.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://mailermine.com/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = mailermine_generated.Configuration(
    host = "https://mailermine.com/api/v1"
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
    api_instance = mailermine_generated.CampaignEventsApi(api_client)
    campaign = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | Campaign UUID.

    try:
        # List campaign activities
        api_response = api_instance.campaign_activities(campaign)
        print("The response of CampaignEventsApi->campaign_activities:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CampaignEventsApi->campaign_activities: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **campaign** | **UUID**| Campaign UUID. | 

### Return type

[**CampaignActivityCollection**](CampaignActivityCollection.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Campaign activities retrieved. |  * X-RateLimit-Limit - Maximum requests per window. <br>  * X-RateLimit-Remaining - Requests remaining in the current window. <br>  * X-RateLimit-Reset - Unix timestamp when the current window resets. <br>  |
**400** | Malformed JSON or invalid request. |  -  |
**401** | Missing or invalid API key. |  -  |
**403** | Account suspended, feature denied, or cross-project access blocked. |  -  |
**404** | Resource not found. |  -  |
**409** | Request conflicts with current state. |  -  |
**422** | Validation failed or plan limit exceeded. |  -  |
**429** | Rate limit exceeded. Retry after the &#x60;Retry-After&#x60; header value. |  -  |
**500** | Unexpected server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **campaign_events**
> CampaignEventsResponse campaign_events(campaign)

List campaign events

Return paginated recipient delivery and engagement events. Required scope: `analytics.read`.

### Example

* Bearer (API Key) Authentication (bearerAuth):

```python
import mailermine_generated
from mailermine_generated.models.campaign_events_response import CampaignEventsResponse
from mailermine_generated.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://mailermine.com/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = mailermine_generated.Configuration(
    host = "https://mailermine.com/api/v1"
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
    api_instance = mailermine_generated.CampaignEventsApi(api_client)
    campaign = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | Campaign UUID.

    try:
        # List campaign events
        api_response = api_instance.campaign_events(campaign)
        print("The response of CampaignEventsApi->campaign_events:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CampaignEventsApi->campaign_events: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **campaign** | **UUID**| Campaign UUID. | 

### Return type

[**CampaignEventsResponse**](CampaignEventsResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Campaign events retrieved. |  * X-RateLimit-Limit - Maximum requests per window. <br>  * X-RateLimit-Remaining - Requests remaining in the current window. <br>  * X-RateLimit-Reset - Unix timestamp when the current window resets. <br>  |
**400** | Malformed JSON or invalid request. |  -  |
**401** | Missing or invalid API key. |  -  |
**403** | Account suspended, feature denied, or cross-project access blocked. |  -  |
**404** | Resource not found. |  -  |
**409** | Request conflicts with current state. |  -  |
**422** | Validation failed or plan limit exceeded. |  -  |
**429** | Rate limit exceeded. Retry after the &#x60;Retry-After&#x60; header value. |  -  |
**500** | Unexpected server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **campaign_recipients**
> CampaignRecipientCollection campaign_recipients(campaign, search=search, status=status, page=page, per_page=per_page)

List campaign recipients

List recipient snapshots with delivery and message status. Required scope: `campaigns.read`.

### Example

* Bearer (API Key) Authentication (bearerAuth):

```python
import mailermine_generated
from mailermine_generated.models.campaign_recipient_collection import CampaignRecipientCollection
from mailermine_generated.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://mailermine.com/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = mailermine_generated.Configuration(
    host = "https://mailermine.com/api/v1"
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
    api_instance = mailermine_generated.CampaignEventsApi(api_client)
    campaign = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | Campaign UUID.
    search = 'ada@example.com' # str | Search recipient email or name. (optional)
    status = 'delivered' # str | Filter by recipient status. (optional)
    page = 1 # int | Page number. (optional) (default to 1)
    per_page = 56 # int | Number of recipients per page. (optional)

    try:
        # List campaign recipients
        api_response = api_instance.campaign_recipients(campaign, search=search, status=status, page=page, per_page=per_page)
        print("The response of CampaignEventsApi->campaign_recipients:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CampaignEventsApi->campaign_recipients: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **campaign** | **UUID**| Campaign UUID. | 
 **search** | **str**| Search recipient email or name. | [optional] 
 **status** | **str**| Filter by recipient status. | [optional] 
 **page** | **int**| Page number. | [optional] [default to 1]
 **per_page** | **int**| Number of recipients per page. | [optional] 

### Return type

[**CampaignRecipientCollection**](CampaignRecipientCollection.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Campaign recipients retrieved. |  * X-RateLimit-Limit - Maximum requests per window. <br>  * X-RateLimit-Remaining - Requests remaining in the current window. <br>  * X-RateLimit-Reset - Unix timestamp when the current window resets. <br>  |
**400** | Malformed JSON or invalid request. |  -  |
**401** | Missing or invalid API key. |  -  |
**403** | Account suspended, feature denied, or cross-project access blocked. |  -  |
**404** | Resource not found. |  -  |
**409** | Request conflicts with current state. |  -  |
**422** | Validation failed or plan limit exceeded. |  -  |
**429** | Rate limit exceeded. Retry after the &#x60;Retry-After&#x60; header value. |  -  |
**500** | Unexpected server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **campaign_timeline**
> CampaignTimelineResponse campaign_timeline(campaign)

Get campaign timeline

Return recent delivery and recipient-failure events. Required scope: `campaigns.read`.

### Example

* Bearer (API Key) Authentication (bearerAuth):

```python
import mailermine_generated
from mailermine_generated.models.campaign_timeline_response import CampaignTimelineResponse
from mailermine_generated.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://mailermine.com/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = mailermine_generated.Configuration(
    host = "https://mailermine.com/api/v1"
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
    api_instance = mailermine_generated.CampaignEventsApi(api_client)
    campaign = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | Campaign UUID.

    try:
        # Get campaign timeline
        api_response = api_instance.campaign_timeline(campaign)
        print("The response of CampaignEventsApi->campaign_timeline:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CampaignEventsApi->campaign_timeline: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **campaign** | **UUID**| Campaign UUID. | 

### Return type

[**CampaignTimelineResponse**](CampaignTimelineResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Campaign timeline retrieved. |  * X-RateLimit-Limit - Maximum requests per window. <br>  * X-RateLimit-Remaining - Requests remaining in the current window. <br>  * X-RateLimit-Reset - Unix timestamp when the current window resets. <br>  |
**400** | Malformed JSON or invalid request. |  -  |
**401** | Missing or invalid API key. |  -  |
**403** | Account suspended, feature denied, or cross-project access blocked. |  -  |
**404** | Resource not found. |  -  |
**409** | Request conflicts with current state. |  -  |
**422** | Validation failed or plan limit exceeded. |  -  |
**429** | Rate limit exceeded. Retry after the &#x60;Retry-After&#x60; header value. |  -  |
**500** | Unexpected server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

