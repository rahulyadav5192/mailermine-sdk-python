# mailermine_generated.TemplatesApi

All URIs are relative to *http://127.0.0.1:8000/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_template**](TemplatesApi.md#create_template) | **POST** /templates | Create template
[**delete_template**](TemplatesApi.md#delete_template) | **DELETE** /templates/{template} | Delete template
[**duplicate_template**](TemplatesApi.md#duplicate_template) | **POST** /templates/{template}/duplicate | Duplicate template
[**get_template**](TemplatesApi.md#get_template) | **GET** /templates/{template} | Get template
[**list_templates**](TemplatesApi.md#list_templates) | **GET** /templates | List templates
[**preview_published_template**](TemplatesApi.md#preview_published_template) | **POST** /templates/preview | Preview published template
[**preview_template**](TemplatesApi.md#preview_template) | **POST** /templates/{template}/preview | Preview template
[**test_template**](TemplatesApi.md#test_template) | **POST** /templates/{template}/test | Test template
[**update_template**](TemplatesApi.md#update_template) | **PATCH** /templates/{template} | Update template


# **create_template**
> TemplateResponse create_template(create_template_request)

Create template

Create a reusable template with content, variables, and branding. Required scope: `templates.write`.

### Example

* Bearer (API Key) Authentication (bearerAuth):

```python
import mailermine_generated
from mailermine_generated.models.create_template_request import CreateTemplateRequest
from mailermine_generated.models.template_response import TemplateResponse
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
    api_instance = mailermine_generated.TemplatesApi(api_client)
    create_template_request = mailermine_generated.CreateTemplateRequest() # CreateTemplateRequest | 

    try:
        # Create template
        api_response = api_instance.create_template(create_template_request)
        print("The response of TemplatesApi->create_template:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TemplatesApi->create_template: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_template_request** | [**CreateTemplateRequest**](CreateTemplateRequest.md)|  | 

### Return type

[**TemplateResponse**](TemplateResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Template created successfully. |  * X-RateLimit-Limit - Maximum requests per window. <br>  * X-RateLimit-Remaining - Requests remaining in the current window. <br>  * X-RateLimit-Reset - Unix timestamp when the current window resets. <br>  |
**400** | Malformed JSON or invalid request. |  -  |
**401** | Missing or invalid API key. |  -  |
**403** | Account suspended, feature denied, or cross-project access blocked. |  -  |
**404** | Resource not found. |  -  |
**409** | Request conflicts with current state. |  -  |
**422** | Validation failed or plan limit exceeded. |  -  |
**429** | Rate limit exceeded. Retry after the &#x60;Retry-After&#x60; header value. |  -  |
**500** | Unexpected server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_template**
> DeleteResponse delete_template(template)

Delete template

Soft-delete a template. Blocked while scheduled or active campaigns reference it. Required scope: `templates.write`.

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
    api_instance = mailermine_generated.TemplatesApi(api_client)
    template = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | Template UUID.

    try:
        # Delete template
        api_response = api_instance.delete_template(template)
        print("The response of TemplatesApi->delete_template:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TemplatesApi->delete_template: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **template** | **UUID**| Template UUID. | 

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
**200** | Template deleted successfully. |  * X-RateLimit-Limit - Maximum requests per window. <br>  * X-RateLimit-Remaining - Requests remaining in the current window. <br>  * X-RateLimit-Reset - Unix timestamp when the current window resets. <br>  |
**400** | Malformed JSON or invalid request. |  -  |
**401** | Missing or invalid API key. |  -  |
**403** | Account suspended, feature denied, or cross-project access blocked. |  -  |
**404** | Resource not found. |  -  |
**409** | Request conflicts with current state. |  -  |
**422** | Validation failed or plan limit exceeded. |  -  |
**429** | Rate limit exceeded. Retry after the &#x60;Retry-After&#x60; header value. |  -  |
**500** | Unexpected server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **duplicate_template**
> TemplateResponse duplicate_template(template, duplicate_template_request=duplicate_template_request)

Duplicate template

Copy content, variables, metadata, and branding into a new draft. Required scope: `templates.write`.

### Example

* Bearer (API Key) Authentication (bearerAuth):

```python
import mailermine_generated
from mailermine_generated.models.duplicate_template_request import DuplicateTemplateRequest
from mailermine_generated.models.template_response import TemplateResponse
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
    api_instance = mailermine_generated.TemplatesApi(api_client)
    template = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | Source template UUID.
    duplicate_template_request = mailermine_generated.DuplicateTemplateRequest() # DuplicateTemplateRequest |  (optional)

    try:
        # Duplicate template
        api_response = api_instance.duplicate_template(template, duplicate_template_request=duplicate_template_request)
        print("The response of TemplatesApi->duplicate_template:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TemplatesApi->duplicate_template: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **template** | **UUID**| Source template UUID. | 
 **duplicate_template_request** | [**DuplicateTemplateRequest**](DuplicateTemplateRequest.md)|  | [optional] 

### Return type

[**TemplateResponse**](TemplateResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Template duplicated successfully. |  * X-RateLimit-Limit - Maximum requests per window. <br>  * X-RateLimit-Remaining - Requests remaining in the current window. <br>  * X-RateLimit-Reset - Unix timestamp when the current window resets. <br>  |
**400** | Malformed JSON or invalid request. |  -  |
**401** | Missing or invalid API key. |  -  |
**403** | Account suspended, feature denied, or cross-project access blocked. |  -  |
**404** | Resource not found. |  -  |
**409** | Request conflicts with current state. |  -  |
**422** | Validation failed or plan limit exceeded. |  -  |
**429** | Rate limit exceeded. Retry after the &#x60;Retry-After&#x60; header value. |  -  |
**500** | Unexpected server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_template**
> TemplateResponse get_template(template)

Get template

Retrieve full template content, variables, branding, project, and usage. Required scope: `templates.read`.

### Example

* Bearer (API Key) Authentication (bearerAuth):

```python
import mailermine_generated
from mailermine_generated.models.template_response import TemplateResponse
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
    api_instance = mailermine_generated.TemplatesApi(api_client)
    template = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | Template UUID.

    try:
        # Get template
        api_response = api_instance.get_template(template)
        print("The response of TemplatesApi->get_template:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TemplatesApi->get_template: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **template** | **UUID**| Template UUID. | 

### Return type

[**TemplateResponse**](TemplateResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Template retrieved successfully. |  * X-RateLimit-Limit - Maximum requests per window. <br>  * X-RateLimit-Remaining - Requests remaining in the current window. <br>  * X-RateLimit-Reset - Unix timestamp when the current window resets. <br>  |
**400** | Malformed JSON or invalid request. |  -  |
**401** | Missing or invalid API key. |  -  |
**403** | Account suspended, feature denied, or cross-project access blocked. |  -  |
**404** | Resource not found. |  -  |
**409** | Request conflicts with current state. |  -  |
**422** | Validation failed or plan limit exceeded. |  -  |
**429** | Rate limit exceeded. Retry after the &#x60;Retry-After&#x60; header value. |  -  |
**500** | Unexpected server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_templates**
> TemplateListResponse list_templates(search=search, status=status, editor_type=editor_type, sort=sort, direction=direction, page=page, per_page=per_page)

List templates

List templates for the authenticated project. Full HTML is omitted from list items. Required scope: `templates.read`.

### Example

* Bearer (API Key) Authentication (bearerAuth):

```python
import mailermine_generated
from mailermine_generated.models.template_list_response import TemplateListResponse
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
    api_instance = mailermine_generated.TemplatesApi(api_client)
    search = 'search_example' # str | Filter by name, slug, or subject. (optional)
    status = 'published' # str | Filter by publication status. (optional)
    editor_type = 'html' # str | Filter by editor/layout type. (optional)
    sort = 'created_at' # str | Sort field. (optional) (default to 'created_at')
    direction = 'desc' # str | Sort direction. (optional) (default to 'desc')
    page = 1 # int | Page number (1-based). (optional) (default to 1)
    per_page = 25 # int | Items per page. (optional) (default to 25)

    try:
        # List templates
        api_response = api_instance.list_templates(search=search, status=status, editor_type=editor_type, sort=sort, direction=direction, page=page, per_page=per_page)
        print("The response of TemplatesApi->list_templates:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TemplatesApi->list_templates: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **search** | **str**| Filter by name, slug, or subject. | [optional] 
 **status** | **str**| Filter by publication status. | [optional] 
 **editor_type** | **str**| Filter by editor/layout type. | [optional] 
 **sort** | **str**| Sort field. | [optional] [default to &#39;created_at&#39;]
 **direction** | **str**| Sort direction. | [optional] [default to &#39;desc&#39;]
 **page** | **int**| Page number (1-based). | [optional] [default to 1]
 **per_page** | **int**| Items per page. | [optional] [default to 25]

### Return type

[**TemplateListResponse**](TemplateListResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Templates retrieved successfully. |  * X-RateLimit-Limit - Maximum requests per window. <br>  * X-RateLimit-Remaining - Requests remaining in the current window. <br>  * X-RateLimit-Reset - Unix timestamp when the current window resets. <br>  |
**400** | Malformed JSON or invalid request. |  -  |
**401** | Missing or invalid API key. |  -  |
**403** | Account suspended, feature denied, or cross-project access blocked. |  -  |
**404** | Resource not found. |  -  |
**409** | Request conflicts with current state. |  -  |
**422** | Validation failed or plan limit exceeded. |  -  |
**429** | Rate limit exceeded. Retry after the &#x60;Retry-After&#x60; header value. |  -  |
**500** | Unexpected server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **preview_published_template**
> TemplatePreviewResponse preview_published_template(preview_template_by_id_request)

Preview published template

Legacy preview operation that selects a published template by `template_id`. Required scope: `templates.read`.

### Example

* Bearer (API Key) Authentication (bearerAuth):

```python
import mailermine_generated
from mailermine_generated.models.preview_template_by_id_request import PreviewTemplateByIdRequest
from mailermine_generated.models.template_preview_response import TemplatePreviewResponse
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
    api_instance = mailermine_generated.TemplatesApi(api_client)
    preview_template_by_id_request = mailermine_generated.PreviewTemplateByIdRequest() # PreviewTemplateByIdRequest | 

    try:
        # Preview published template
        api_response = api_instance.preview_published_template(preview_template_by_id_request)
        print("The response of TemplatesApi->preview_published_template:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TemplatesApi->preview_published_template: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **preview_template_by_id_request** | [**PreviewTemplateByIdRequest**](PreviewTemplateByIdRequest.md)|  | 

### Return type

[**TemplatePreviewResponse**](TemplatePreviewResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Published template rendered successfully. |  * X-RateLimit-Limit - Maximum requests per window. <br>  * X-RateLimit-Remaining - Requests remaining in the current window. <br>  * X-RateLimit-Reset - Unix timestamp when the current window resets. <br>  |
**400** | Malformed JSON or invalid request. |  -  |
**401** | Missing or invalid API key. |  -  |
**403** | Account suspended, feature denied, or cross-project access blocked. |  -  |
**404** | Resource not found. |  -  |
**409** | Request conflicts with current state. |  -  |
**422** | Validation failed or plan limit exceeded. |  -  |
**429** | Rate limit exceeded. Retry after the &#x60;Retry-After&#x60; header value. |  -  |
**500** | Unexpected server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **preview_template**
> TemplatePreviewResponse preview_template(template, preview_template_request=preview_template_request)

Preview template

Render a template with runtime variables without saving or sending. Required scope: `templates.read`.

### Example

* Bearer (API Key) Authentication (bearerAuth):

```python
import mailermine_generated
from mailermine_generated.models.preview_template_request import PreviewTemplateRequest
from mailermine_generated.models.template_preview_response import TemplatePreviewResponse
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
    api_instance = mailermine_generated.TemplatesApi(api_client)
    template = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | Template UUID.
    preview_template_request = mailermine_generated.PreviewTemplateRequest() # PreviewTemplateRequest |  (optional)

    try:
        # Preview template
        api_response = api_instance.preview_template(template, preview_template_request=preview_template_request)
        print("The response of TemplatesApi->preview_template:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TemplatesApi->preview_template: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **template** | **UUID**| Template UUID. | 
 **preview_template_request** | [**PreviewTemplateRequest**](PreviewTemplateRequest.md)|  | [optional] 

### Return type

[**TemplatePreviewResponse**](TemplatePreviewResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Template preview rendered successfully. |  * X-RateLimit-Limit - Maximum requests per window. <br>  * X-RateLimit-Remaining - Requests remaining in the current window. <br>  * X-RateLimit-Reset - Unix timestamp when the current window resets. <br>  |
**400** | Malformed JSON or invalid request. |  -  |
**401** | Missing or invalid API key. |  -  |
**403** | Account suspended, feature denied, or cross-project access blocked. |  -  |
**404** | Resource not found. |  -  |
**409** | Request conflicts with current state. |  -  |
**422** | Validation failed or plan limit exceeded. |  -  |
**429** | Rate limit exceeded. Retry after the &#x60;Retry-After&#x60; header value. |  -  |
**500** | Unexpected server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **test_template**
> TemplateTestResponse test_template(template, test_template_request)

Test template

Queue a test email from the template. Required scopes: `templates.write` and `emails.send`.

### Example

* Bearer (API Key) Authentication (bearerAuth):

```python
import mailermine_generated
from mailermine_generated.models.template_test_response import TemplateTestResponse
from mailermine_generated.models.test_template_request import TestTemplateRequest
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
    api_instance = mailermine_generated.TemplatesApi(api_client)
    template = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | Template UUID.
    test_template_request = mailermine_generated.TestTemplateRequest() # TestTemplateRequest | 

    try:
        # Test template
        api_response = api_instance.test_template(template, test_template_request)
        print("The response of TemplatesApi->test_template:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TemplatesApi->test_template: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **template** | **UUID**| Template UUID. | 
 **test_template_request** | [**TestTemplateRequest**](TestTemplateRequest.md)|  | 

### Return type

[**TemplateTestResponse**](TemplateTestResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Test email queued successfully. |  * X-RateLimit-Limit - Maximum requests per window. <br>  * X-RateLimit-Remaining - Requests remaining in the current window. <br>  * X-RateLimit-Reset - Unix timestamp when the current window resets. <br>  |
**400** | Malformed JSON or invalid request. |  -  |
**401** | Missing or invalid API key. |  -  |
**403** | Account suspended, feature denied, or cross-project access blocked. |  -  |
**404** | Resource not found. |  -  |
**409** | Request conflicts with current state. |  -  |
**422** | Validation failed or plan limit exceeded. |  -  |
**429** | Rate limit exceeded. Retry after the &#x60;Retry-After&#x60; header value. |  -  |
**500** | Unexpected server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_template**
> TemplateResponse update_template(template, update_template_request=update_template_request)

Update template

Partially update template content, variables, status, or branding. Required scope: `templates.write`.

### Example

* Bearer (API Key) Authentication (bearerAuth):

```python
import mailermine_generated
from mailermine_generated.models.template_response import TemplateResponse
from mailermine_generated.models.update_template_request import UpdateTemplateRequest
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
    api_instance = mailermine_generated.TemplatesApi(api_client)
    template = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | Template UUID.
    update_template_request = mailermine_generated.UpdateTemplateRequest() # UpdateTemplateRequest |  (optional)

    try:
        # Update template
        api_response = api_instance.update_template(template, update_template_request=update_template_request)
        print("The response of TemplatesApi->update_template:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TemplatesApi->update_template: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **template** | **UUID**| Template UUID. | 
 **update_template_request** | [**UpdateTemplateRequest**](UpdateTemplateRequest.md)|  | [optional] 

### Return type

[**TemplateResponse**](TemplateResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Template updated successfully. |  * X-RateLimit-Limit - Maximum requests per window. <br>  * X-RateLimit-Remaining - Requests remaining in the current window. <br>  * X-RateLimit-Reset - Unix timestamp when the current window resets. <br>  |
**400** | Malformed JSON or invalid request. |  -  |
**401** | Missing or invalid API key. |  -  |
**403** | Account suspended, feature denied, or cross-project access blocked. |  -  |
**404** | Resource not found. |  -  |
**409** | Request conflicts with current state. |  -  |
**422** | Validation failed or plan limit exceeded. |  -  |
**429** | Rate limit exceeded. Retry after the &#x60;Retry-After&#x60; header value. |  -  |
**500** | Unexpected server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

