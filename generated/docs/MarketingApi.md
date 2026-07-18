# mailermine_generated.MarketingApi

All URIs are relative to *http://127.0.0.1:8000/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_custom_field**](MarketingApi.md#create_custom_field) | **POST** /custom-fields | Create custom field
[**delete_custom_field**](MarketingApi.md#delete_custom_field) | **DELETE** /custom-fields/{customField} | Delete custom field
[**get_custom_field**](MarketingApi.md#get_custom_field) | **GET** /custom-fields/{customField} | Get custom field
[**list_custom_fields**](MarketingApi.md#list_custom_fields) | **GET** /custom-fields | List custom fields
[**update_custom_field**](MarketingApi.md#update_custom_field) | **PATCH** /custom-fields/{customField} | Update custom field


# **create_custom_field**
> CustomFieldResponse create_custom_field(create_custom_field_request)

Create custom field

Create a typed custom field definition. Required scope: `contacts.write`.

### Example

* Bearer (API Key) Authentication (bearerAuth):

```python
import mailermine_generated
from mailermine_generated.models.create_custom_field_request import CreateCustomFieldRequest
from mailermine_generated.models.custom_field_response import CustomFieldResponse
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
    api_instance = mailermine_generated.MarketingApi(api_client)
    create_custom_field_request = mailermine_generated.CreateCustomFieldRequest() # CreateCustomFieldRequest | 

    try:
        # Create custom field
        api_response = api_instance.create_custom_field(create_custom_field_request)
        print("The response of MarketingApi->create_custom_field:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MarketingApi->create_custom_field: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_custom_field_request** | [**CreateCustomFieldRequest**](CreateCustomFieldRequest.md)|  | 

### Return type

[**CustomFieldResponse**](CustomFieldResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Custom field created successfully. |  * X-RateLimit-Limit - Maximum requests per window. <br>  * X-RateLimit-Remaining - Requests remaining in the current window. <br>  * X-RateLimit-Reset - Unix timestamp when the current window resets. <br>  |
**400** | Malformed JSON or invalid request. |  -  |
**401** | Missing or invalid API key. |  -  |
**403** | Account suspended, feature denied, or cross-project access blocked. |  -  |
**404** | Resource not found. |  -  |
**409** | Request conflicts with current state. |  -  |
**422** | Validation failed or plan limit exceeded. |  -  |
**429** | Rate limit exceeded. Retry after the &#x60;Retry-After&#x60; header value. |  -  |
**500** | Unexpected server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_custom_field**
> DeleteResponse delete_custom_field(custom_field)

Delete custom field

Delete a custom field definition. Required scope: `contacts.write`.

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
    api_instance = mailermine_generated.MarketingApi(api_client)
    custom_field = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | Custom field UUID.

    try:
        # Delete custom field
        api_response = api_instance.delete_custom_field(custom_field)
        print("The response of MarketingApi->delete_custom_field:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MarketingApi->delete_custom_field: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **custom_field** | **UUID**| Custom field UUID. | 

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
**200** | Custom field deleted successfully. |  * X-RateLimit-Limit - Maximum requests per window. <br>  * X-RateLimit-Remaining - Requests remaining in the current window. <br>  * X-RateLimit-Reset - Unix timestamp when the current window resets. <br>  |
**400** | Malformed JSON or invalid request. |  -  |
**401** | Missing or invalid API key. |  -  |
**403** | Account suspended, feature denied, or cross-project access blocked. |  -  |
**404** | Resource not found. |  -  |
**409** | Request conflicts with current state. |  -  |
**422** | Validation failed or plan limit exceeded. |  -  |
**429** | Rate limit exceeded. Retry after the &#x60;Retry-After&#x60; header value. |  -  |
**500** | Unexpected server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_custom_field**
> CustomFieldResponse get_custom_field(custom_field)

Get custom field

Retrieve a custom field definition. Required scope: `contacts.read`.

### Example

* Bearer (API Key) Authentication (bearerAuth):

```python
import mailermine_generated
from mailermine_generated.models.custom_field_response import CustomFieldResponse
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
    api_instance = mailermine_generated.MarketingApi(api_client)
    custom_field = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | Custom field UUID.

    try:
        # Get custom field
        api_response = api_instance.get_custom_field(custom_field)
        print("The response of MarketingApi->get_custom_field:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MarketingApi->get_custom_field: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **custom_field** | **UUID**| Custom field UUID. | 

### Return type

[**CustomFieldResponse**](CustomFieldResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Custom field retrieved successfully. |  * X-RateLimit-Limit - Maximum requests per window. <br>  * X-RateLimit-Remaining - Requests remaining in the current window. <br>  * X-RateLimit-Reset - Unix timestamp when the current window resets. <br>  |
**400** | Malformed JSON or invalid request. |  -  |
**401** | Missing or invalid API key. |  -  |
**403** | Account suspended, feature denied, or cross-project access blocked. |  -  |
**404** | Resource not found. |  -  |
**409** | Request conflicts with current state. |  -  |
**422** | Validation failed or plan limit exceeded. |  -  |
**429** | Rate limit exceeded. Retry after the &#x60;Retry-After&#x60; header value. |  -  |
**500** | Unexpected server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_custom_fields**
> CustomFieldCollection list_custom_fields(search=search, sort=sort, direction=direction, page=page, per_page=per_page)

List custom fields

List custom field definitions. Required scope: `contacts.read`.

### Example

* Bearer (API Key) Authentication (bearerAuth):

```python
import mailermine_generated
from mailermine_generated.models.custom_field_collection import CustomFieldCollection
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
    api_instance = mailermine_generated.MarketingApi(api_client)
    search = 'company' # str | Search names and slugs. (optional)
    sort = 'name' # str | Sort field. (optional) (default to 'name')
    direction = 'asc' # str | Sort direction. (optional) (default to 'asc')
    page = 1 # int | Page number. (optional) (default to 1)
    per_page = 25 # int | Items per page. (optional) (default to 25)

    try:
        # List custom fields
        api_response = api_instance.list_custom_fields(search=search, sort=sort, direction=direction, page=page, per_page=per_page)
        print("The response of MarketingApi->list_custom_fields:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MarketingApi->list_custom_fields: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **search** | **str**| Search names and slugs. | [optional] 
 **sort** | **str**| Sort field. | [optional] [default to &#39;name&#39;]
 **direction** | **str**| Sort direction. | [optional] [default to &#39;asc&#39;]
 **page** | **int**| Page number. | [optional] [default to 1]
 **per_page** | **int**| Items per page. | [optional] [default to 25]

### Return type

[**CustomFieldCollection**](CustomFieldCollection.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Custom fields retrieved successfully. |  * X-RateLimit-Limit - Maximum requests per window. <br>  * X-RateLimit-Remaining - Requests remaining in the current window. <br>  * X-RateLimit-Reset - Unix timestamp when the current window resets. <br>  |
**400** | Malformed JSON or invalid request. |  -  |
**401** | Missing or invalid API key. |  -  |
**403** | Account suspended, feature denied, or cross-project access blocked. |  -  |
**404** | Resource not found. |  -  |
**409** | Request conflicts with current state. |  -  |
**422** | Validation failed or plan limit exceeded. |  -  |
**429** | Rate limit exceeded. Retry after the &#x60;Retry-After&#x60; header value. |  -  |
**500** | Unexpected server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_custom_field**
> CustomFieldResponse update_custom_field(custom_field, update_custom_field_request=update_custom_field_request)

Update custom field

Update a custom field definition. Required scope: `contacts.write`.

### Example

* Bearer (API Key) Authentication (bearerAuth):

```python
import mailermine_generated
from mailermine_generated.models.custom_field_response import CustomFieldResponse
from mailermine_generated.models.update_custom_field_request import UpdateCustomFieldRequest
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
    api_instance = mailermine_generated.MarketingApi(api_client)
    custom_field = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | Custom field UUID.
    update_custom_field_request = mailermine_generated.UpdateCustomFieldRequest() # UpdateCustomFieldRequest |  (optional)

    try:
        # Update custom field
        api_response = api_instance.update_custom_field(custom_field, update_custom_field_request=update_custom_field_request)
        print("The response of MarketingApi->update_custom_field:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MarketingApi->update_custom_field: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **custom_field** | **UUID**| Custom field UUID. | 
 **update_custom_field_request** | [**UpdateCustomFieldRequest**](UpdateCustomFieldRequest.md)|  | [optional] 

### Return type

[**CustomFieldResponse**](CustomFieldResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Custom field updated successfully. |  * X-RateLimit-Limit - Maximum requests per window. <br>  * X-RateLimit-Remaining - Requests remaining in the current window. <br>  * X-RateLimit-Reset - Unix timestamp when the current window resets. <br>  |
**400** | Malformed JSON or invalid request. |  -  |
**401** | Missing or invalid API key. |  -  |
**403** | Account suspended, feature denied, or cross-project access blocked. |  -  |
**404** | Resource not found. |  -  |
**409** | Request conflicts with current state. |  -  |
**422** | Validation failed or plan limit exceeded. |  -  |
**429** | Rate limit exceeded. Retry after the &#x60;Retry-After&#x60; header value. |  -  |
**500** | Unexpected server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

