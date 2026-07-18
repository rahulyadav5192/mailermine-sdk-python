# mailermine_generated.EventsApi

All URIs are relative to *http://127.0.0.1:8000/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_event**](EventsApi.md#get_event) | **GET** /events/{emailEvent} | Get event
[**list_events**](EventsApi.md#list_events) | **GET** /events | List events


# **get_event**
> EventResponse get_event(email_event)

Get event

Retrieve a single email event by UUID. Required scope: `events.read`.

### Example

* Bearer (API Key) Authentication (bearerAuth):

```python
import mailermine_generated
from mailermine_generated.models.event_response import EventResponse
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
    api_instance = mailermine_generated.EventsApi(api_client)
    email_event = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | Event UUID.

    try:
        # Get event
        api_response = api_instance.get_event(email_event)
        print("The response of EventsApi->get_event:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EventsApi->get_event: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **email_event** | **UUID**| Event UUID. | 

### Return type

[**EventResponse**](EventResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Event retrieved successfully. |  * X-RateLimit-Limit - Maximum requests per window. <br>  * X-RateLimit-Remaining - Requests remaining in the current window. <br>  * X-RateLimit-Reset - Unix timestamp when the current window resets. <br>  |
**404** | Resource not found. |  -  |
**400** | Malformed JSON or invalid request. |  -  |
**401** | Missing or invalid API key. |  -  |
**403** | Account suspended, feature denied, or cross-project access blocked. |  -  |
**409** | Request conflicts with current state. |  -  |
**422** | Validation failed or plan limit exceeded. |  -  |
**429** | Rate limit exceeded. Retry after the &#x60;Retry-After&#x60; header value. |  -  |
**500** | Unexpected server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_events**
> EventListResponse list_events(event_type=event_type, source=source, campaign=campaign, message=message, search=search, var_from=var_from, to=to, per_page=per_page)

List events

List recipient delivery and engagement events with filters for type, source, campaign, message, and date range. Required scope: `events.read`.

### Example

* Bearer (API Key) Authentication (bearerAuth):

```python
import mailermine_generated
from mailermine_generated.models.event_list_response import EventListResponse
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
    api_instance = mailermine_generated.EventsApi(api_client)
    event_type = 'delivered' # str | Filter by event type (for example `delivered`, `opened`, `clicked`). (optional)
    source = 'transactional' # str | Filter by event source. (optional)
    campaign = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | Filter by campaign UUID. (optional)
    message = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | Filter by message UUID. (optional)
    search = 'search_example' # str | Free-text search across recipient and payload. (optional)
    var_from = '2013-10-20T19:20:30+01:00' # datetime | Filter events on or after this ISO-8601 date. (optional)
    to = '2013-10-20T19:20:30+01:00' # datetime | Filter events on or before this ISO-8601 date. (optional)
    per_page = 25 # int | Items per page (default 25). (optional)

    try:
        # List events
        api_response = api_instance.list_events(event_type=event_type, source=source, campaign=campaign, message=message, search=search, var_from=var_from, to=to, per_page=per_page)
        print("The response of EventsApi->list_events:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EventsApi->list_events: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **event_type** | **str**| Filter by event type (for example &#x60;delivered&#x60;, &#x60;opened&#x60;, &#x60;clicked&#x60;). | [optional] 
 **source** | **str**| Filter by event source. | [optional] 
 **campaign** | **UUID**| Filter by campaign UUID. | [optional] 
 **message** | **UUID**| Filter by message UUID. | [optional] 
 **search** | **str**| Free-text search across recipient and payload. | [optional] 
 **var_from** | **datetime**| Filter events on or after this ISO-8601 date. | [optional] 
 **to** | **datetime**| Filter events on or before this ISO-8601 date. | [optional] 
 **per_page** | **int**| Items per page (default 25). | [optional] 

### Return type

[**EventListResponse**](EventListResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Events retrieved successfully. |  * X-RateLimit-Limit - Maximum requests per window. <br>  * X-RateLimit-Remaining - Requests remaining in the current window. <br>  * X-RateLimit-Reset - Unix timestamp when the current window resets. <br>  |
**400** | Malformed JSON or invalid request. |  -  |
**401** | Missing or invalid API key. |  -  |
**403** | Account suspended, feature denied, or cross-project access blocked. |  -  |
**404** | Resource not found. |  -  |
**409** | Request conflicts with current state. |  -  |
**422** | Validation failed or plan limit exceeded. |  -  |
**429** | Rate limit exceeded. Retry after the &#x60;Retry-After&#x60; header value. |  -  |
**500** | Unexpected server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

