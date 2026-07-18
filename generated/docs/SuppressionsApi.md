# mailermine_generated.SuppressionsApi

All URIs are relative to *http://127.0.0.1:8000/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_suppression**](SuppressionsApi.md#create_suppression) | **POST** /suppressions | Create suppression
[**delete_suppression**](SuppressionsApi.md#delete_suppression) | **DELETE** /suppressions/{suppression} | Delete suppression
[**get_suppression**](SuppressionsApi.md#get_suppression) | **GET** /suppressions/{suppression} | Get suppression
[**list_suppressions**](SuppressionsApi.md#list_suppressions) | **GET** /suppressions | List suppressions
[**restore_suppression**](SuppressionsApi.md#restore_suppression) | **POST** /suppressions/{suppression}/restore | Restore suppression


# **create_suppression**
> SuppressionResponse create_suppression(create_suppression_request)

Create suppression

Add a recipient address to the project suppression list. Required scope: `suppressions.write`.

### Example

* Bearer (API Key) Authentication (bearerAuth):

```python
import mailermine_generated
from mailermine_generated.models.create_suppression_request import CreateSuppressionRequest
from mailermine_generated.models.suppression_response import SuppressionResponse
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
    api_instance = mailermine_generated.SuppressionsApi(api_client)
    create_suppression_request = mailermine_generated.CreateSuppressionRequest() # CreateSuppressionRequest | 

    try:
        # Create suppression
        api_response = api_instance.create_suppression(create_suppression_request)
        print("The response of SuppressionsApi->create_suppression:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SuppressionsApi->create_suppression: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_suppression_request** | [**CreateSuppressionRequest**](CreateSuppressionRequest.md)|  | 

### Return type

[**SuppressionResponse**](SuppressionResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Suppression created successfully. |  * X-RateLimit-Limit - Maximum requests per window. <br>  * X-RateLimit-Remaining - Requests remaining in the current window. <br>  * X-RateLimit-Reset - Unix timestamp when the current window resets. <br>  |
**400** | Malformed JSON or invalid request. |  -  |
**401** | Missing or invalid API key. |  -  |
**403** | Account suspended, feature denied, or cross-project access blocked. |  -  |
**404** | Resource not found. |  -  |
**409** | Request conflicts with current state. |  -  |
**422** | Validation failed or plan limit exceeded. |  -  |
**429** | Rate limit exceeded. Retry after the &#x60;Retry-After&#x60; header value. |  -  |
**500** | Unexpected server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_suppression**
> DeleteResponse delete_suppression(suppression)

Delete suppression

Permanently remove a suppression, allowing the address to receive mail again. Required scope: `suppressions.write`.

### Example

* Bearer (API Key) Authentication (bearerAuth):

```python
import mailermine_generated
from mailermine_generated.models.delete_response import DeleteResponse
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
    api_instance = mailermine_generated.SuppressionsApi(api_client)
    suppression = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | Suppression UUID.

    try:
        # Delete suppression
        api_response = api_instance.delete_suppression(suppression)
        print("The response of SuppressionsApi->delete_suppression:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SuppressionsApi->delete_suppression: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **suppression** | **UUID**| Suppression UUID. | 

### Return type

[**DeleteResponse**](DeleteResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Suppression removed successfully. |  * X-RateLimit-Limit - Maximum requests per window. <br>  * X-RateLimit-Remaining - Requests remaining in the current window. <br>  * X-RateLimit-Reset - Unix timestamp when the current window resets. <br>  |
**404** | Resource not found. |  -  |
**400** | Malformed JSON or invalid request. |  -  |
**401** | Missing or invalid API key. |  -  |
**403** | Account suspended, feature denied, or cross-project access blocked. |  -  |
**409** | Request conflicts with current state. |  -  |
**422** | Validation failed or plan limit exceeded. |  -  |
**429** | Rate limit exceeded. Retry after the &#x60;Retry-After&#x60; header value. |  -  |
**500** | Unexpected server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_suppression**
> SuppressionResponse get_suppression(suppression)

Get suppression

Retrieve a suppressed address by UUID. Required scope: `suppressions.read`.

### Example

* Bearer (API Key) Authentication (bearerAuth):

```python
import mailermine_generated
from mailermine_generated.models.suppression_response import SuppressionResponse
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
    api_instance = mailermine_generated.SuppressionsApi(api_client)
    suppression = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | Suppression UUID (returned as `id` from create/list).

    try:
        # Get suppression
        api_response = api_instance.get_suppression(suppression)
        print("The response of SuppressionsApi->get_suppression:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SuppressionsApi->get_suppression: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **suppression** | **UUID**| Suppression UUID (returned as &#x60;id&#x60; from create/list). | 

### Return type

[**SuppressionResponse**](SuppressionResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Suppression retrieved successfully. |  * X-RateLimit-Limit - Maximum requests per window. <br>  * X-RateLimit-Remaining - Requests remaining in the current window. <br>  * X-RateLimit-Reset - Unix timestamp when the current window resets. <br>  |
**404** | Resource not found. |  -  |
**400** | Malformed JSON or invalid request. |  -  |
**401** | Missing or invalid API key. |  -  |
**403** | Account suspended, feature denied, or cross-project access blocked. |  -  |
**409** | Request conflicts with current state. |  -  |
**422** | Validation failed or plan limit exceeded. |  -  |
**429** | Rate limit exceeded. Retry after the &#x60;Retry-After&#x60; header value. |  -  |
**500** | Unexpected server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_suppressions**
> SuppressionListResponse list_suppressions(search=search, reason=reason, per_page=per_page)

List suppressions

List suppressed recipient addresses with optional search and reason filter. Required scope: `suppressions.read`.

### Example

* Bearer (API Key) Authentication (bearerAuth):

```python
import mailermine_generated
from mailermine_generated.models.suppression_list_response import SuppressionListResponse
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
    api_instance = mailermine_generated.SuppressionsApi(api_client)
    search = 'example.com' # str | Free-text search across email addresses. (optional)
    reason = 'bounce' # str | Filter by suppression reason (`bounce`, `complaint`, `manual`, `unsubscribe`). (optional)
    per_page = 25 # int | Items per page (default 25). (optional)

    try:
        # List suppressions
        api_response = api_instance.list_suppressions(search=search, reason=reason, per_page=per_page)
        print("The response of SuppressionsApi->list_suppressions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SuppressionsApi->list_suppressions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **search** | **str**| Free-text search across email addresses. | [optional] 
 **reason** | **str**| Filter by suppression reason (&#x60;bounce&#x60;, &#x60;complaint&#x60;, &#x60;manual&#x60;, &#x60;unsubscribe&#x60;). | [optional] 
 **per_page** | **int**| Items per page (default 25). | [optional] 

### Return type

[**SuppressionListResponse**](SuppressionListResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Suppressions retrieved successfully. |  * X-RateLimit-Limit - Maximum requests per window. <br>  * X-RateLimit-Remaining - Requests remaining in the current window. <br>  * X-RateLimit-Reset - Unix timestamp when the current window resets. <br>  |
**400** | Malformed JSON or invalid request. |  -  |
**401** | Missing or invalid API key. |  -  |
**403** | Account suspended, feature denied, or cross-project access blocked. |  -  |
**404** | Resource not found. |  -  |
**409** | Request conflicts with current state. |  -  |
**422** | Validation failed or plan limit exceeded. |  -  |
**429** | Rate limit exceeded. Retry after the &#x60;Retry-After&#x60; header value. |  -  |
**500** | Unexpected server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **restore_suppression**
> SuppressionResponse restore_suppression(suppression)

Restore suppression

Restore a soft-deleted suppression by UUID. Required scope: `suppressions.write`.

### Example

* Bearer (API Key) Authentication (bearerAuth):

```python
import mailermine_generated
from mailermine_generated.models.suppression_response import SuppressionResponse
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
    api_instance = mailermine_generated.SuppressionsApi(api_client)
    suppression = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | Suppression UUID.

    try:
        # Restore suppression
        api_response = api_instance.restore_suppression(suppression)
        print("The response of SuppressionsApi->restore_suppression:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SuppressionsApi->restore_suppression: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **suppression** | **UUID**| Suppression UUID. | 

### Return type

[**SuppressionResponse**](SuppressionResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Suppression restored successfully. |  * X-RateLimit-Limit - Maximum requests per window. <br>  * X-RateLimit-Remaining - Requests remaining in the current window. <br>  * X-RateLimit-Reset - Unix timestamp when the current window resets. <br>  |
**404** | Resource not found. |  -  |
**400** | Malformed JSON or invalid request. |  -  |
**401** | Missing or invalid API key. |  -  |
**403** | Account suspended, feature denied, or cross-project access blocked. |  -  |
**409** | Request conflicts with current state. |  -  |
**422** | Validation failed or plan limit exceeded. |  -  |
**429** | Rate limit exceeded. Retry after the &#x60;Retry-After&#x60; header value. |  -  |
**500** | Unexpected server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

