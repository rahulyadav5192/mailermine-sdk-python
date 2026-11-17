# mailermine_generated.SegmentsApi

All URIs are relative to *https://mailermine.com/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**count_segment**](SegmentsApi.md#count_segment) | **GET** /segments/{segment}/count | Refresh segment count
[**create_segment**](SegmentsApi.md#create_segment) | **POST** /segments | Create segment
[**delete_segment**](SegmentsApi.md#delete_segment) | **DELETE** /segments/{segment} | Delete segment
[**get_segment**](SegmentsApi.md#get_segment) | **GET** /segments/{segment} | Get segment
[**list_segments**](SegmentsApi.md#list_segments) | **GET** /segments | List segments
[**preview_segment**](SegmentsApi.md#preview_segment) | **POST** /segments/{segment}/preview | Preview segment
[**preview_segment_rules**](SegmentsApi.md#preview_segment_rules) | **POST** /segments/preview | Preview segment rules
[**update_segment**](SegmentsApi.md#update_segment) | **PUT** /segments/{segment} | Update segment


# **count_segment**
> SegmentCountResponse count_segment(segment)

Refresh segment count

Recalculate and persist the saved segment contact count. Required scope: `contacts.read`.

### Example

* Bearer (API Key) Authentication (bearerAuth):

```python
import mailermine_generated
from mailermine_generated.models.segment_count_response import SegmentCountResponse
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
    api_instance = mailermine_generated.SegmentsApi(api_client)
    segment = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | Segment UUID.

    try:
        # Refresh segment count
        api_response = api_instance.count_segment(segment)
        print("The response of SegmentsApi->count_segment:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SegmentsApi->count_segment: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **segment** | **UUID**| Segment UUID. | 

### Return type

[**SegmentCountResponse**](SegmentCountResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Segment contact count refreshed. |  * X-RateLimit-Limit - Maximum requests per window. <br>  * X-RateLimit-Remaining - Requests remaining in the current window. <br>  * X-RateLimit-Reset - Unix timestamp when the current window resets. <br>  |
**400** | Malformed JSON or invalid request. |  -  |
**401** | Missing or invalid API key. |  -  |
**403** | Account suspended, feature denied, or cross-project access blocked. |  -  |
**404** | Resource not found. |  -  |
**409** | Request conflicts with current state. |  -  |
**422** | Validation failed or plan limit exceeded. |  -  |
**429** | Rate limit exceeded. Retry after the &#x60;Retry-After&#x60; header value. |  -  |
**500** | Unexpected server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_segment**
> SegmentResponse create_segment(create_segment_request)

Create segment

Create a dynamic contact segment from validated rules. Required scope: `contacts.write`.

### Example

* Bearer (API Key) Authentication (bearerAuth):

```python
import mailermine_generated
from mailermine_generated.models.create_segment_request import CreateSegmentRequest
from mailermine_generated.models.segment_response import SegmentResponse
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
    api_instance = mailermine_generated.SegmentsApi(api_client)
    create_segment_request = mailermine_generated.CreateSegmentRequest() # CreateSegmentRequest | 

    try:
        # Create segment
        api_response = api_instance.create_segment(create_segment_request)
        print("The response of SegmentsApi->create_segment:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SegmentsApi->create_segment: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_segment_request** | [**CreateSegmentRequest**](CreateSegmentRequest.md)|  | 

### Return type

[**SegmentResponse**](SegmentResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Segment created successfully. |  * X-RateLimit-Limit - Maximum requests per window. <br>  * X-RateLimit-Remaining - Requests remaining in the current window. <br>  * X-RateLimit-Reset - Unix timestamp when the current window resets. <br>  |
**400** | Malformed JSON or invalid request. |  -  |
**401** | Missing or invalid API key. |  -  |
**403** | Account suspended, feature denied, or cross-project access blocked. |  -  |
**404** | Resource not found. |  -  |
**409** | Request conflicts with current state. |  -  |
**422** | Validation failed or plan limit exceeded. |  -  |
**429** | Rate limit exceeded. Retry after the &#x60;Retry-After&#x60; header value. |  -  |
**500** | Unexpected server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_segment**
> DeleteResponse delete_segment(segment)

Delete segment

Delete a dynamic segment. Required scope: `contacts.write`.

### Example

* Bearer (API Key) Authentication (bearerAuth):

```python
import mailermine_generated
from mailermine_generated.models.delete_response import DeleteResponse
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
    api_instance = mailermine_generated.SegmentsApi(api_client)
    segment = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | Segment UUID.

    try:
        # Delete segment
        api_response = api_instance.delete_segment(segment)
        print("The response of SegmentsApi->delete_segment:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SegmentsApi->delete_segment: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **segment** | **UUID**| Segment UUID. | 

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
**200** | Segment deleted successfully. |  * X-RateLimit-Limit - Maximum requests per window. <br>  * X-RateLimit-Remaining - Requests remaining in the current window. <br>  * X-RateLimit-Reset - Unix timestamp when the current window resets. <br>  |
**400** | Malformed JSON or invalid request. |  -  |
**401** | Missing or invalid API key. |  -  |
**403** | Account suspended, feature denied, or cross-project access blocked. |  -  |
**404** | Resource not found. |  -  |
**409** | Request conflicts with current state. |  -  |
**422** | Validation failed or plan limit exceeded. |  -  |
**429** | Rate limit exceeded. Retry after the &#x60;Retry-After&#x60; header value. |  -  |
**500** | Unexpected server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_segment**
> SegmentResponse get_segment(segment)

Get segment

Retrieve a dynamic segment. Required scope: `contacts.read`.

### Example

* Bearer (API Key) Authentication (bearerAuth):

```python
import mailermine_generated
from mailermine_generated.models.segment_response import SegmentResponse
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
    api_instance = mailermine_generated.SegmentsApi(api_client)
    segment = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | Segment UUID.

    try:
        # Get segment
        api_response = api_instance.get_segment(segment)
        print("The response of SegmentsApi->get_segment:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SegmentsApi->get_segment: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **segment** | **UUID**| Segment UUID. | 

### Return type

[**SegmentResponse**](SegmentResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Segment retrieved successfully. |  * X-RateLimit-Limit - Maximum requests per window. <br>  * X-RateLimit-Remaining - Requests remaining in the current window. <br>  * X-RateLimit-Reset - Unix timestamp when the current window resets. <br>  |
**400** | Malformed JSON or invalid request. |  -  |
**401** | Missing or invalid API key. |  -  |
**403** | Account suspended, feature denied, or cross-project access blocked. |  -  |
**404** | Resource not found. |  -  |
**409** | Request conflicts with current state. |  -  |
**422** | Validation failed or plan limit exceeded. |  -  |
**429** | Rate limit exceeded. Retry after the &#x60;Retry-After&#x60; header value. |  -  |
**500** | Unexpected server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_segments**
> SegmentCollection list_segments(search=search, sort=sort, direction=direction, page=page, per_page=per_page)

List segments

List dynamic contact segments. Required scope: `contacts.read`.

### Example

* Bearer (API Key) Authentication (bearerAuth):

```python
import mailermine_generated
from mailermine_generated.models.segment_collection import SegmentCollection
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
    api_instance = mailermine_generated.SegmentsApi(api_client)
    search = 'Engaged' # str | Search segment names. (optional)
    sort = 'created_at' # str | Sort field. (optional) (default to 'created_at')
    direction = 'desc' # str | Sort direction. (optional) (default to 'desc')
    page = 1 # int | Page number. (optional) (default to 1)
    per_page = 25 # int | Items per page. (optional) (default to 25)

    try:
        # List segments
        api_response = api_instance.list_segments(search=search, sort=sort, direction=direction, page=page, per_page=per_page)
        print("The response of SegmentsApi->list_segments:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SegmentsApi->list_segments: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **search** | **str**| Search segment names. | [optional] 
 **sort** | **str**| Sort field. | [optional] [default to &#39;created_at&#39;]
 **direction** | **str**| Sort direction. | [optional] [default to &#39;desc&#39;]
 **page** | **int**| Page number. | [optional] [default to 1]
 **per_page** | **int**| Items per page. | [optional] [default to 25]

### Return type

[**SegmentCollection**](SegmentCollection.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Segments retrieved successfully. |  * X-RateLimit-Limit - Maximum requests per window. <br>  * X-RateLimit-Remaining - Requests remaining in the current window. <br>  * X-RateLimit-Reset - Unix timestamp when the current window resets. <br>  |
**400** | Malformed JSON or invalid request. |  -  |
**401** | Missing or invalid API key. |  -  |
**403** | Account suspended, feature denied, or cross-project access blocked. |  -  |
**404** | Resource not found. |  -  |
**409** | Request conflicts with current state. |  -  |
**422** | Validation failed or plan limit exceeded. |  -  |
**429** | Rate limit exceeded. Retry after the &#x60;Retry-After&#x60; header value. |  -  |
**500** | Unexpected server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **preview_segment**
> SegmentPreviewResponse preview_segment(segment)

Preview segment

Return a count and up to ten contacts matching a saved segment. Required scope: `contacts.read`.

### Example

* Bearer (API Key) Authentication (bearerAuth):

```python
import mailermine_generated
from mailermine_generated.models.segment_preview_response import SegmentPreviewResponse
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
    api_instance = mailermine_generated.SegmentsApi(api_client)
    segment = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | Segment UUID.

    try:
        # Preview segment
        api_response = api_instance.preview_segment(segment)
        print("The response of SegmentsApi->preview_segment:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SegmentsApi->preview_segment: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **segment** | **UUID**| Segment UUID. | 

### Return type

[**SegmentPreviewResponse**](SegmentPreviewResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Segment preview generated successfully. |  * X-RateLimit-Limit - Maximum requests per window. <br>  * X-RateLimit-Remaining - Requests remaining in the current window. <br>  * X-RateLimit-Reset - Unix timestamp when the current window resets. <br>  |
**400** | Malformed JSON or invalid request. |  -  |
**401** | Missing or invalid API key. |  -  |
**403** | Account suspended, feature denied, or cross-project access blocked. |  -  |
**404** | Resource not found. |  -  |
**409** | Request conflicts with current state. |  -  |
**422** | Validation failed or plan limit exceeded. |  -  |
**429** | Rate limit exceeded. Retry after the &#x60;Retry-After&#x60; header value. |  -  |
**500** | Unexpected server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **preview_segment_rules**
> SegmentPreviewResponse preview_segment_rules(preview_segment_request)

Preview segment rules

Validate unsaved rules and return a count plus up to ten matching contacts. Required scope: `contacts.read`.

### Example

* Bearer (API Key) Authentication (bearerAuth):

```python
import mailermine_generated
from mailermine_generated.models.preview_segment_request import PreviewSegmentRequest
from mailermine_generated.models.segment_preview_response import SegmentPreviewResponse
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
    api_instance = mailermine_generated.SegmentsApi(api_client)
    preview_segment_request = mailermine_generated.PreviewSegmentRequest() # PreviewSegmentRequest | 

    try:
        # Preview segment rules
        api_response = api_instance.preview_segment_rules(preview_segment_request)
        print("The response of SegmentsApi->preview_segment_rules:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SegmentsApi->preview_segment_rules: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **preview_segment_request** | [**PreviewSegmentRequest**](PreviewSegmentRequest.md)|  | 

### Return type

[**SegmentPreviewResponse**](SegmentPreviewResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Segment preview generated successfully. |  * X-RateLimit-Limit - Maximum requests per window. <br>  * X-RateLimit-Remaining - Requests remaining in the current window. <br>  * X-RateLimit-Reset - Unix timestamp when the current window resets. <br>  |
**400** | Malformed JSON or invalid request. |  -  |
**401** | Missing or invalid API key. |  -  |
**403** | Account suspended, feature denied, or cross-project access blocked. |  -  |
**404** | Resource not found. |  -  |
**409** | Request conflicts with current state. |  -  |
**422** | Validation failed or plan limit exceeded. |  -  |
**429** | Rate limit exceeded. Retry after the &#x60;Retry-After&#x60; header value. |  -  |
**500** | Unexpected server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_segment**
> SegmentResponse update_segment(segment, update_segment_request)

Update segment

Update segment metadata or rules. Required scope: `contacts.write`.

### Example

* Bearer (API Key) Authentication (bearerAuth):

```python
import mailermine_generated
from mailermine_generated.models.segment_response import SegmentResponse
from mailermine_generated.models.update_segment_request import UpdateSegmentRequest
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
    api_instance = mailermine_generated.SegmentsApi(api_client)
    segment = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | Segment UUID.
    update_segment_request = mailermine_generated.UpdateSegmentRequest() # UpdateSegmentRequest | 

    try:
        # Update segment
        api_response = api_instance.update_segment(segment, update_segment_request)
        print("The response of SegmentsApi->update_segment:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SegmentsApi->update_segment: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **segment** | **UUID**| Segment UUID. | 
 **update_segment_request** | [**UpdateSegmentRequest**](UpdateSegmentRequest.md)|  | 

### Return type

[**SegmentResponse**](SegmentResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Segment updated successfully. |  * X-RateLimit-Limit - Maximum requests per window. <br>  * X-RateLimit-Remaining - Requests remaining in the current window. <br>  * X-RateLimit-Reset - Unix timestamp when the current window resets. <br>  |
**400** | Malformed JSON or invalid request. |  -  |
**401** | Missing or invalid API key. |  -  |
**403** | Account suspended, feature denied, or cross-project access blocked. |  -  |
**404** | Resource not found. |  -  |
**409** | Request conflicts with current state. |  -  |
**422** | Validation failed or plan limit exceeded. |  -  |
**429** | Rate limit exceeded. Retry after the &#x60;Retry-After&#x60; header value. |  -  |
**500** | Unexpected server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

