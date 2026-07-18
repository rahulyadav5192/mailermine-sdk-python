# mailermine_generated.MessagesApi

All URIs are relative to *http://127.0.0.1:8000/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_message**](MessagesApi.md#get_message) | **GET** /delivery-logs/{message} | Get message
[**list_messages**](MessagesApi.md#list_messages) | **GET** /delivery-logs | List messages
[**message_events**](MessagesApi.md#message_events) | **GET** /messages/{message}/events | Message events


# **get_message**
> MessageDetailResponse get_message(message)

Get message

Retrieve a single message by UUID with delivery timeline events.

### Example

* Bearer (API Key) Authentication (bearerAuth):

```python
import mailermine_generated
from mailermine_generated.models.message_detail_response import MessageDetailResponse
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
    api_instance = mailermine_generated.MessagesApi(api_client)
    message = 'message_example' # str | The message UUID

    try:
        # Get message
        api_response = api_instance.get_message(message)
        print("The response of MessagesApi->get_message:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MessagesApi->get_message: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **message** | **str**| The message UUID | 

### Return type

[**MessageDetailResponse**](MessageDetailResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Message retrieved successfully. |  * X-RateLimit-Limit - Maximum requests per window. <br>  * X-RateLimit-Remaining - Requests remaining in the current window. <br>  * X-RateLimit-Reset - Unix timestamp when the current window resets. <br>  |
**404** | Resource not found. |  -  |
**401** | Missing or invalid API key. |  -  |
**403** | Account suspended, feature denied, or cross-project access blocked. |  -  |
**429** | Rate limit exceeded. Retry after the &#x60;Retry-After&#x60; header value. |  -  |
**400** | Malformed JSON or invalid request. |  -  |
**409** | Request conflicts with current state. |  -  |
**422** | Validation failed or plan limit exceeded. |  -  |
**500** | Unexpected server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_messages**
> MessageListResponse list_messages(search=search, status=status, provider=provider, var_from=var_from, to=to, page=page, per_page=per_page)

List messages

List sent and queued messages for your project with optional filters and pagination.

### Example

* Bearer (API Key) Authentication (bearerAuth):

```python
import mailermine_generated
from mailermine_generated.models.message_list_response import MessageListResponse
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
    api_instance = mailermine_generated.MessagesApi(api_client)
    search = 'invoice' # str | Free-text search across subject and recipient. (optional)
    status = 'sent' # str | Filter by message status. (optional)
    provider = 'aws' # str | Filter by delivery provider. (optional)
    var_from = '2013-10-20T19:20:30+01:00' # datetime | Filter messages sent on or after this ISO-8601 date. (optional)
    to = '2013-10-20T19:20:30+01:00' # datetime | Filter messages sent on or before this ISO-8601 date. (optional)
    page = 1 # int | Page number (1-based). (optional)
    per_page = 25 # int | Items per page (default 25). (optional)

    try:
        # List messages
        api_response = api_instance.list_messages(search=search, status=status, provider=provider, var_from=var_from, to=to, page=page, per_page=per_page)
        print("The response of MessagesApi->list_messages:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MessagesApi->list_messages: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **search** | **str**| Free-text search across subject and recipient. | [optional] 
 **status** | **str**| Filter by message status. | [optional] 
 **provider** | **str**| Filter by delivery provider. | [optional] 
 **var_from** | **datetime**| Filter messages sent on or after this ISO-8601 date. | [optional] 
 **to** | **datetime**| Filter messages sent on or before this ISO-8601 date. | [optional] 
 **page** | **int**| Page number (1-based). | [optional] 
 **per_page** | **int**| Items per page (default 25). | [optional] 

### Return type

[**MessageListResponse**](MessageListResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Messages retrieved successfully. |  * X-RateLimit-Limit - Maximum requests per window. <br>  * X-RateLimit-Remaining - Requests remaining in the current window. <br>  * X-RateLimit-Reset - Unix timestamp when the current window resets. <br>  |
**401** | Missing or invalid API key. |  -  |
**403** | Account suspended, feature denied, or cross-project access blocked. |  -  |
**422** | Validation failed or plan limit exceeded. |  -  |
**429** | Rate limit exceeded. Retry after the &#x60;Retry-After&#x60; header value. |  -  |
**400** | Malformed JSON or invalid request. |  -  |
**404** | Resource not found. |  -  |
**409** | Request conflicts with current state. |  -  |
**500** | Unexpected server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **message_events**
> MessageEventsResponse message_events(message)

Message events

Retrieve lifecycle events for a single message.

### Example

* Bearer (API Key) Authentication (bearerAuth):

```python
import mailermine_generated
from mailermine_generated.models.message_events_response import MessageEventsResponse
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
    api_instance = mailermine_generated.MessagesApi(api_client)
    message = 'message_example' # str | The message UUID

    try:
        # Message events
        api_response = api_instance.message_events(message)
        print("The response of MessagesApi->message_events:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MessagesApi->message_events: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **message** | **str**| The message UUID | 

### Return type

[**MessageEventsResponse**](MessageEventsResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Message events retrieved. |  * X-RateLimit-Limit - Maximum requests per window. <br>  * X-RateLimit-Remaining - Requests remaining in the current window. <br>  * X-RateLimit-Reset - Unix timestamp when the current window resets. <br>  |
**404** | Resource not found. |  -  |
**401** | Missing or invalid API key. |  -  |
**403** | Account suspended, feature denied, or cross-project access blocked. |  -  |
**429** | Rate limit exceeded. Retry after the &#x60;Retry-After&#x60; header value. |  -  |
**400** | Malformed JSON or invalid request. |  -  |
**409** | Request conflicts with current state. |  -  |
**422** | Validation failed or plan limit exceeded. |  -  |
**500** | Unexpected server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

