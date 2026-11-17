# mailermine_generated.ExportsApi

All URIs are relative to *https://mailermine.com/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**download_contact_export**](ExportsApi.md#download_contact_export) | **GET** /contacts/exports/{contactExport}/download | Download contact export
[**export_contacts**](ExportsApi.md#export_contacts) | **POST** /contacts/export | Export contacts
[**get_contact_export**](ExportsApi.md#get_contact_export) | **GET** /contacts/exports/{contactExport} | Get contact export


# **download_contact_export**
> str download_contact_export(contact_export)

Download contact export

Download a completed CSV contact export. Required scope: `contacts.read`.

### Example

* Bearer (API Key) Authentication (bearerAuth):

```python
import mailermine_generated
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
    api_instance = mailermine_generated.ExportsApi(api_client)
    contact_export = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | Contact export UUID.

    try:
        # Download contact export
        api_response = api_instance.download_contact_export(contact_export)
        print("The response of ExportsApi->download_contact_export:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ExportsApi->download_contact_export: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contact_export** | **UUID**| Contact export UUID. | 

### Return type

**str**

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**404** | Resource not found. |  -  |
**422** | Validation failed or plan limit exceeded. |  -  |
**200** | CSV contact export. |  * X-RateLimit-Limit - Maximum requests per window. <br>  * X-RateLimit-Remaining - Requests remaining in the current window. <br>  * X-RateLimit-Reset - Unix timestamp when the current window resets. <br>  |
**400** | Malformed JSON or invalid request. |  -  |
**401** | Missing or invalid API key. |  -  |
**403** | Account suspended, feature denied, or cross-project access blocked. |  -  |
**409** | Request conflicts with current state. |  -  |
**429** | Rate limit exceeded. Retry after the &#x60;Retry-After&#x60; header value. |  -  |
**500** | Unexpected server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **export_contacts**
> ExportJobResponse export_contacts(export_contacts_request=export_contacts_request)

Export contacts

Queue an asynchronous CSV contact export using optional filters or contact UUIDs. Required scope: `contacts.read`.

### Example

* Bearer (API Key) Authentication (bearerAuth):

```python
import mailermine_generated
from mailermine_generated.models.export_contacts_request import ExportContactsRequest
from mailermine_generated.models.export_job_response import ExportJobResponse
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
    api_instance = mailermine_generated.ExportsApi(api_client)
    export_contacts_request = mailermine_generated.ExportContactsRequest() # ExportContactsRequest |  (optional)

    try:
        # Export contacts
        api_response = api_instance.export_contacts(export_contacts_request=export_contacts_request)
        print("The response of ExportsApi->export_contacts:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ExportsApi->export_contacts: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **export_contacts_request** | [**ExportContactsRequest**](ExportContactsRequest.md)|  | [optional] 

### Return type

[**ExportJobResponse**](ExportJobResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Contact export queued. |  * X-RateLimit-Limit - Maximum requests per window. <br>  * X-RateLimit-Remaining - Requests remaining in the current window. <br>  * X-RateLimit-Reset - Unix timestamp when the current window resets. <br>  |
**401** | Missing or invalid API key. |  -  |
**400** | Malformed JSON or invalid request. |  -  |
**403** | Account suspended, feature denied, or cross-project access blocked. |  -  |
**404** | Resource not found. |  -  |
**409** | Request conflicts with current state. |  -  |
**422** | Validation failed or plan limit exceeded. |  -  |
**429** | Rate limit exceeded. Retry after the &#x60;Retry-After&#x60; header value. |  -  |
**500** | Unexpected server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_contact_export**
> ExportJobResponse get_contact_export(contact_export)

Get contact export

Retrieve export status and download availability. Required scope: `contacts.read`.

### Example

* Bearer (API Key) Authentication (bearerAuth):

```python
import mailermine_generated
from mailermine_generated.models.export_job_response import ExportJobResponse
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
    api_instance = mailermine_generated.ExportsApi(api_client)
    contact_export = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | Contact export UUID.

    try:
        # Get contact export
        api_response = api_instance.get_contact_export(contact_export)
        print("The response of ExportsApi->get_contact_export:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ExportsApi->get_contact_export: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contact_export** | **UUID**| Contact export UUID. | 

### Return type

[**ExportJobResponse**](ExportJobResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Export retrieved successfully. |  * X-RateLimit-Limit - Maximum requests per window. <br>  * X-RateLimit-Remaining - Requests remaining in the current window. <br>  * X-RateLimit-Reset - Unix timestamp when the current window resets. <br>  |
**400** | Malformed JSON or invalid request. |  -  |
**401** | Missing or invalid API key. |  -  |
**403** | Account suspended, feature denied, or cross-project access blocked. |  -  |
**404** | Resource not found. |  -  |
**409** | Request conflicts with current state. |  -  |
**422** | Validation failed or plan limit exceeded. |  -  |
**429** | Rate limit exceeded. Retry after the &#x60;Retry-After&#x60; header value. |  -  |
**500** | Unexpected server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

