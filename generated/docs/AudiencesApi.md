# mailermine_generated.AudiencesApi

All URIs are relative to *https://mailermine.com/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_audience_members**](AudiencesApi.md#add_audience_members) | **POST** /audiences/{source}/{audience}/contacts | Add audience members
[**get_audience**](AudiencesApi.md#get_audience) | **GET** /audiences/{source}/{audience} | Get audience
[**list_audiences**](AudiencesApi.md#list_audiences) | **GET** /audiences | List audiences
[**remove_audience_members**](AudiencesApi.md#remove_audience_members) | **DELETE** /audiences/{source}/{audience}/contacts | Remove audience members


# **add_audience_members**
> AddAudienceMembers200Response add_audience_members(source, audience, list_contacts_membership_request)

Add audience members

Add contacts to a list-backed audience. Segment membership is dynamic and cannot be changed directly. Required scope: `contacts.write`.

### Example

* Bearer (API Key) Authentication (bearerAuth):

```python
import mailermine_generated
from mailermine_generated.models.add_audience_members200_response import AddAudienceMembers200Response
from mailermine_generated.models.list_contacts_membership_request import ListContactsMembershipRequest
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
    api_instance = mailermine_generated.AudiencesApi(api_client)
    source = 'list' # str | Audience source; must be `list` for membership changes.
    audience = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | Audience UUID.
    list_contacts_membership_request = mailermine_generated.ListContactsMembershipRequest() # ListContactsMembershipRequest | 

    try:
        # Add audience members
        api_response = api_instance.add_audience_members(source, audience, list_contacts_membership_request)
        print("The response of AudiencesApi->add_audience_members:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AudiencesApi->add_audience_members: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **source** | **str**| Audience source; must be &#x60;list&#x60; for membership changes. | 
 **audience** | **UUID**| Audience UUID. | 
 **list_contacts_membership_request** | [**ListContactsMembershipRequest**](ListContactsMembershipRequest.md)|  | 

### Return type

[**AddAudienceMembers200Response**](AddAudienceMembers200Response.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Contacts added to audience. |  * X-RateLimit-Limit - Maximum requests per window. <br>  * X-RateLimit-Remaining - Requests remaining in the current window. <br>  * X-RateLimit-Reset - Unix timestamp when the current window resets. <br>  |
**422** | Validation failed or plan limit exceeded. |  -  |
**400** | Malformed JSON or invalid request. |  -  |
**401** | Missing or invalid API key. |  -  |
**403** | Account suspended, feature denied, or cross-project access blocked. |  -  |
**404** | Resource not found. |  -  |
**409** | Request conflicts with current state. |  -  |
**429** | Rate limit exceeded. Retry after the &#x60;Retry-After&#x60; header value. |  -  |
**500** | Unexpected server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_audience**
> AudienceResponse get_audience(source, audience)

Get audience

Retrieve a list-backed or segment-backed audience. Required scope: `contacts.read`.

### Example

* Bearer (API Key) Authentication (bearerAuth):

```python
import mailermine_generated
from mailermine_generated.models.audience_response import AudienceResponse
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
    api_instance = mailermine_generated.AudiencesApi(api_client)
    source = 'list' # str | Audience source type.
    audience = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | List or segment UUID.

    try:
        # Get audience
        api_response = api_instance.get_audience(source, audience)
        print("The response of AudiencesApi->get_audience:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AudiencesApi->get_audience: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **source** | **str**| Audience source type. | 
 **audience** | **UUID**| List or segment UUID. | 

### Return type

[**AudienceResponse**](AudienceResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Audience retrieved successfully. |  * X-RateLimit-Limit - Maximum requests per window. <br>  * X-RateLimit-Remaining - Requests remaining in the current window. <br>  * X-RateLimit-Reset - Unix timestamp when the current window resets. <br>  |
**400** | Malformed JSON or invalid request. |  -  |
**401** | Missing or invalid API key. |  -  |
**403** | Account suspended, feature denied, or cross-project access blocked. |  -  |
**404** | Resource not found. |  -  |
**409** | Request conflicts with current state. |  -  |
**422** | Validation failed or plan limit exceeded. |  -  |
**429** | Rate limit exceeded. Retry after the &#x60;Retry-After&#x60; header value. |  -  |
**500** | Unexpected server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_audiences**
> AudienceCollection list_audiences(page=page, per_page=per_page)

List audiences

List static lists and dynamic segments through one paginated catalog. Required scope: `contacts.read`.

### Example

* Bearer (API Key) Authentication (bearerAuth):

```python
import mailermine_generated
from mailermine_generated.models.audience_collection import AudienceCollection
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
    api_instance = mailermine_generated.AudiencesApi(api_client)
    page = 1 # int | Page number. (optional) (default to 1)
    per_page = 25 # int | Items per page (maximum 100). (optional) (default to 25)

    try:
        # List audiences
        api_response = api_instance.list_audiences(page=page, per_page=per_page)
        print("The response of AudiencesApi->list_audiences:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AudiencesApi->list_audiences: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| Page number. | [optional] [default to 1]
 **per_page** | **int**| Items per page (maximum 100). | [optional] [default to 25]

### Return type

[**AudienceCollection**](AudienceCollection.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Audiences retrieved successfully. |  * X-RateLimit-Limit - Maximum requests per window. <br>  * X-RateLimit-Remaining - Requests remaining in the current window. <br>  * X-RateLimit-Reset - Unix timestamp when the current window resets. <br>  |
**400** | Malformed JSON or invalid request. |  -  |
**401** | Missing or invalid API key. |  -  |
**403** | Account suspended, feature denied, or cross-project access blocked. |  -  |
**404** | Resource not found. |  -  |
**409** | Request conflicts with current state. |  -  |
**422** | Validation failed or plan limit exceeded. |  -  |
**429** | Rate limit exceeded. Retry after the &#x60;Retry-After&#x60; header value. |  -  |
**500** | Unexpected server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_audience_members**
> RemoveAudienceMembers200Response remove_audience_members(source, audience, ids=ids)

Remove audience members

Remove contacts from a list-backed audience. Segment membership is dynamic and cannot be changed directly. Required scope: `contacts.write`.

### Example

* Bearer (API Key) Authentication (bearerAuth):

```python
import mailermine_generated
from mailermine_generated.models.remove_audience_members200_response import RemoveAudienceMembers200Response
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
    api_instance = mailermine_generated.AudiencesApi(api_client)
    source = 'list' # str | Audience source; must be `list` for membership changes.
    audience = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | Audience UUID.
    ids = None # List[UUID] |  (optional)

    try:
        # Remove audience members
        api_response = api_instance.remove_audience_members(source, audience, ids=ids)
        print("The response of AudiencesApi->remove_audience_members:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AudiencesApi->remove_audience_members: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **source** | **str**| Audience source; must be &#x60;list&#x60; for membership changes. | 
 **audience** | **UUID**| Audience UUID. | 
 **ids** | [**List[UUID]**](UUID.md)|  | [optional] 

### Return type

[**RemoveAudienceMembers200Response**](RemoveAudienceMembers200Response.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Contacts removed from audience. |  * X-RateLimit-Limit - Maximum requests per window. <br>  * X-RateLimit-Remaining - Requests remaining in the current window. <br>  * X-RateLimit-Reset - Unix timestamp when the current window resets. <br>  |
**422** | Validation failed or plan limit exceeded. |  -  |
**400** | Malformed JSON or invalid request. |  -  |
**401** | Missing or invalid API key. |  -  |
**403** | Account suspended, feature denied, or cross-project access blocked. |  -  |
**404** | Resource not found. |  -  |
**409** | Request conflicts with current state. |  -  |
**429** | Rate limit exceeded. Retry after the &#x60;Retry-After&#x60; header value. |  -  |
**500** | Unexpected server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

