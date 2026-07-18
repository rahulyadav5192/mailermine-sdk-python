# mailermine_generated.ListsApi

All URIs are relative to *http://127.0.0.1:8000/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_contacts_to_list**](ListsApi.md#add_contacts_to_list) | **POST** /lists/{list}/contacts | Add contacts to list
[**bulk_add_contacts_to_list**](ListsApi.md#bulk_add_contacts_to_list) | **POST** /lists/{list}/contacts/bulk-add | Add contacts to list
[**bulk_remove_contacts_from_list**](ListsApi.md#bulk_remove_contacts_from_list) | **POST** /lists/{list}/contacts/bulk-remove | Remove contacts from list
[**create_list**](ListsApi.md#create_list) | **POST** /lists | Create contact list
[**delete_list**](ListsApi.md#delete_list) | **DELETE** /lists/{list} | Delete contact list
[**get_list**](ListsApi.md#get_list) | **GET** /lists/{list} | Get contact list
[**list_lists**](ListsApi.md#list_lists) | **GET** /lists | List contact lists
[**remove_contacts_from_list**](ListsApi.md#remove_contacts_from_list) | **DELETE** /lists/{list}/contacts | Remove contacts from list
[**remove_contacts_from_list_legacy**](ListsApi.md#remove_contacts_from_list_legacy) | **POST** /lists/{list}/contacts/remove | Remove contacts from list
[**update_list**](ListsApi.md#update_list) | **PUT** /lists/{list} | Update contact list


# **add_contacts_to_list**
> AddContactsToList200Response add_contacts_to_list(list, list_contacts_membership_request)

Add contacts to list

Add contacts to a static list. Compatibility bulk routes expose the same behavior with route-specific operation IDs. Required scope: `contacts.write`.

### Example

* Bearer (API Key) Authentication (bearerAuth):

```python
import mailermine_generated
from mailermine_generated.models.add_contacts_to_list200_response import AddContactsToList200Response
from mailermine_generated.models.list_contacts_membership_request import ListContactsMembershipRequest
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
    api_instance = mailermine_generated.ListsApi(api_client)
    list = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | List UUID.
    list_contacts_membership_request = mailermine_generated.ListContactsMembershipRequest() # ListContactsMembershipRequest | 

    try:
        # Add contacts to list
        api_response = api_instance.add_contacts_to_list(list, list_contacts_membership_request)
        print("The response of ListsApi->add_contacts_to_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ListsApi->add_contacts_to_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **list** | **UUID**| List UUID. | 
 **list_contacts_membership_request** | [**ListContactsMembershipRequest**](ListContactsMembershipRequest.md)|  | 

### Return type

[**AddContactsToList200Response**](AddContactsToList200Response.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Contacts added to list. |  * X-RateLimit-Limit - Maximum requests per window. <br>  * X-RateLimit-Remaining - Requests remaining in the current window. <br>  * X-RateLimit-Reset - Unix timestamp when the current window resets. <br>  |
**400** | Malformed JSON or invalid request. |  -  |
**401** | Missing or invalid API key. |  -  |
**403** | Account suspended, feature denied, or cross-project access blocked. |  -  |
**404** | Resource not found. |  -  |
**409** | Request conflicts with current state. |  -  |
**422** | Validation failed or plan limit exceeded. |  -  |
**429** | Rate limit exceeded. Retry after the &#x60;Retry-After&#x60; header value. |  -  |
**500** | Unexpected server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **bulk_add_contacts_to_list**
> AddContactsToList200Response bulk_add_contacts_to_list(list, list_contacts_membership_request)

Add contacts to list

Add contacts to a static list. Compatibility bulk routes expose the same behavior with route-specific operation IDs. Required scope: `contacts.write`.

### Example

* Bearer (API Key) Authentication (bearerAuth):

```python
import mailermine_generated
from mailermine_generated.models.add_contacts_to_list200_response import AddContactsToList200Response
from mailermine_generated.models.list_contacts_membership_request import ListContactsMembershipRequest
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
    api_instance = mailermine_generated.ListsApi(api_client)
    list = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | List UUID.
    list_contacts_membership_request = mailermine_generated.ListContactsMembershipRequest() # ListContactsMembershipRequest | 

    try:
        # Add contacts to list
        api_response = api_instance.bulk_add_contacts_to_list(list, list_contacts_membership_request)
        print("The response of ListsApi->bulk_add_contacts_to_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ListsApi->bulk_add_contacts_to_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **list** | **UUID**| List UUID. | 
 **list_contacts_membership_request** | [**ListContactsMembershipRequest**](ListContactsMembershipRequest.md)|  | 

### Return type

[**AddContactsToList200Response**](AddContactsToList200Response.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Contacts added to list. |  * X-RateLimit-Limit - Maximum requests per window. <br>  * X-RateLimit-Remaining - Requests remaining in the current window. <br>  * X-RateLimit-Reset - Unix timestamp when the current window resets. <br>  |
**400** | Malformed JSON or invalid request. |  -  |
**401** | Missing or invalid API key. |  -  |
**403** | Account suspended, feature denied, or cross-project access blocked. |  -  |
**404** | Resource not found. |  -  |
**409** | Request conflicts with current state. |  -  |
**422** | Validation failed or plan limit exceeded. |  -  |
**429** | Rate limit exceeded. Retry after the &#x60;Retry-After&#x60; header value. |  -  |
**500** | Unexpected server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **bulk_remove_contacts_from_list**
> RemoveContactsFromList200Response bulk_remove_contacts_from_list(list, list_contacts_membership_request)

Remove contacts from list

Remove contacts from a static list. Compatibility POST routes expose the same behavior with route-specific operation IDs. Required scope: `contacts.write`.

### Example

* Bearer (API Key) Authentication (bearerAuth):

```python
import mailermine_generated
from mailermine_generated.models.list_contacts_membership_request import ListContactsMembershipRequest
from mailermine_generated.models.remove_contacts_from_list200_response import RemoveContactsFromList200Response
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
    api_instance = mailermine_generated.ListsApi(api_client)
    list = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | List UUID.
    list_contacts_membership_request = mailermine_generated.ListContactsMembershipRequest() # ListContactsMembershipRequest | 

    try:
        # Remove contacts from list
        api_response = api_instance.bulk_remove_contacts_from_list(list, list_contacts_membership_request)
        print("The response of ListsApi->bulk_remove_contacts_from_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ListsApi->bulk_remove_contacts_from_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **list** | **UUID**| List UUID. | 
 **list_contacts_membership_request** | [**ListContactsMembershipRequest**](ListContactsMembershipRequest.md)|  | 

### Return type

[**RemoveContactsFromList200Response**](RemoveContactsFromList200Response.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Contacts removed from list. |  * X-RateLimit-Limit - Maximum requests per window. <br>  * X-RateLimit-Remaining - Requests remaining in the current window. <br>  * X-RateLimit-Reset - Unix timestamp when the current window resets. <br>  |
**400** | Malformed JSON or invalid request. |  -  |
**401** | Missing or invalid API key. |  -  |
**403** | Account suspended, feature denied, or cross-project access blocked. |  -  |
**404** | Resource not found. |  -  |
**409** | Request conflicts with current state. |  -  |
**422** | Validation failed or plan limit exceeded. |  -  |
**429** | Rate limit exceeded. Retry after the &#x60;Retry-After&#x60; header value. |  -  |
**500** | Unexpected server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_list**
> ListResponse create_list(create_list_request)

Create contact list

Create a static contact list. Required scope: `contacts.write`.

### Example

* Bearer (API Key) Authentication (bearerAuth):

```python
import mailermine_generated
from mailermine_generated.models.create_list_request import CreateListRequest
from mailermine_generated.models.list_response import ListResponse
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
    api_instance = mailermine_generated.ListsApi(api_client)
    create_list_request = mailermine_generated.CreateListRequest() # CreateListRequest | 

    try:
        # Create contact list
        api_response = api_instance.create_list(create_list_request)
        print("The response of ListsApi->create_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ListsApi->create_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_list_request** | [**CreateListRequest**](CreateListRequest.md)|  | 

### Return type

[**ListResponse**](ListResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | List created successfully. |  * X-RateLimit-Limit - Maximum requests per window. <br>  * X-RateLimit-Remaining - Requests remaining in the current window. <br>  * X-RateLimit-Reset - Unix timestamp when the current window resets. <br>  |
**400** | Malformed JSON or invalid request. |  -  |
**401** | Missing or invalid API key. |  -  |
**403** | Account suspended, feature denied, or cross-project access blocked. |  -  |
**404** | Resource not found. |  -  |
**409** | Request conflicts with current state. |  -  |
**422** | Validation failed or plan limit exceeded. |  -  |
**429** | Rate limit exceeded. Retry after the &#x60;Retry-After&#x60; header value. |  -  |
**500** | Unexpected server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_list**
> DeleteResponse delete_list(list)

Delete contact list

Delete a static contact list. Required scope: `contacts.write`.

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
    api_instance = mailermine_generated.ListsApi(api_client)
    list = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | List UUID.

    try:
        # Delete contact list
        api_response = api_instance.delete_list(list)
        print("The response of ListsApi->delete_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ListsApi->delete_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **list** | **UUID**| List UUID. | 

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
**200** | List deleted successfully. |  * X-RateLimit-Limit - Maximum requests per window. <br>  * X-RateLimit-Remaining - Requests remaining in the current window. <br>  * X-RateLimit-Reset - Unix timestamp when the current window resets. <br>  |
**400** | Malformed JSON or invalid request. |  -  |
**401** | Missing or invalid API key. |  -  |
**403** | Account suspended, feature denied, or cross-project access blocked. |  -  |
**404** | Resource not found. |  -  |
**409** | Request conflicts with current state. |  -  |
**422** | Validation failed or plan limit exceeded. |  -  |
**429** | Rate limit exceeded. Retry after the &#x60;Retry-After&#x60; header value. |  -  |
**500** | Unexpected server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_list**
> ListResponse get_list(list)

Get contact list

Retrieve a contact list and its subscriber count. Required scope: `contacts.read`.

### Example

* Bearer (API Key) Authentication (bearerAuth):

```python
import mailermine_generated
from mailermine_generated.models.list_response import ListResponse
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
    api_instance = mailermine_generated.ListsApi(api_client)
    list = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | List UUID.

    try:
        # Get contact list
        api_response = api_instance.get_list(list)
        print("The response of ListsApi->get_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ListsApi->get_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **list** | **UUID**| List UUID. | 

### Return type

[**ListResponse**](ListResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List retrieved successfully. |  * X-RateLimit-Limit - Maximum requests per window. <br>  * X-RateLimit-Remaining - Requests remaining in the current window. <br>  * X-RateLimit-Reset - Unix timestamp when the current window resets. <br>  |
**400** | Malformed JSON or invalid request. |  -  |
**401** | Missing or invalid API key. |  -  |
**403** | Account suspended, feature denied, or cross-project access blocked. |  -  |
**404** | Resource not found. |  -  |
**409** | Request conflicts with current state. |  -  |
**422** | Validation failed or plan limit exceeded. |  -  |
**429** | Rate limit exceeded. Retry after the &#x60;Retry-After&#x60; header value. |  -  |
**500** | Unexpected server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_lists**
> ListCollection list_lists(search=search, sort=sort, direction=direction, page=page, per_page=per_page)

List contact lists

List static contact lists with subscriber counts. Required scope: `contacts.read`.

### Example

* Bearer (API Key) Authentication (bearerAuth):

```python
import mailermine_generated
from mailermine_generated.models.list_collection import ListCollection
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
    api_instance = mailermine_generated.ListsApi(api_client)
    search = 'Newsletter' # str | Search list names. (optional)
    sort = 'created_at' # str | Sort field. (optional) (default to 'created_at')
    direction = 'desc' # str | Sort direction. (optional) (default to 'desc')
    page = 1 # int | Page number. (optional) (default to 1)
    per_page = 25 # int | Items per page. (optional) (default to 25)

    try:
        # List contact lists
        api_response = api_instance.list_lists(search=search, sort=sort, direction=direction, page=page, per_page=per_page)
        print("The response of ListsApi->list_lists:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ListsApi->list_lists: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **search** | **str**| Search list names. | [optional] 
 **sort** | **str**| Sort field. | [optional] [default to &#39;created_at&#39;]
 **direction** | **str**| Sort direction. | [optional] [default to &#39;desc&#39;]
 **page** | **int**| Page number. | [optional] [default to 1]
 **per_page** | **int**| Items per page. | [optional] [default to 25]

### Return type

[**ListCollection**](ListCollection.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Lists retrieved successfully. |  * X-RateLimit-Limit - Maximum requests per window. <br>  * X-RateLimit-Remaining - Requests remaining in the current window. <br>  * X-RateLimit-Reset - Unix timestamp when the current window resets. <br>  |
**400** | Malformed JSON or invalid request. |  -  |
**401** | Missing or invalid API key. |  -  |
**403** | Account suspended, feature denied, or cross-project access blocked. |  -  |
**404** | Resource not found. |  -  |
**409** | Request conflicts with current state. |  -  |
**422** | Validation failed or plan limit exceeded. |  -  |
**429** | Rate limit exceeded. Retry after the &#x60;Retry-After&#x60; header value. |  -  |
**500** | Unexpected server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_contacts_from_list**
> RemoveContactsFromList200Response remove_contacts_from_list(list, ids=ids)

Remove contacts from list

Remove contacts from a static list. Compatibility POST routes expose the same behavior with route-specific operation IDs. Required scope: `contacts.write`.

### Example

* Bearer (API Key) Authentication (bearerAuth):

```python
import mailermine_generated
from mailermine_generated.models.remove_contacts_from_list200_response import RemoveContactsFromList200Response
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
    api_instance = mailermine_generated.ListsApi(api_client)
    list = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | List UUID.
    ids = None # List[UUID] |  (optional)

    try:
        # Remove contacts from list
        api_response = api_instance.remove_contacts_from_list(list, ids=ids)
        print("The response of ListsApi->remove_contacts_from_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ListsApi->remove_contacts_from_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **list** | **UUID**| List UUID. | 
 **ids** | [**List[UUID]**](UUID.md)|  | [optional] 

### Return type

[**RemoveContactsFromList200Response**](RemoveContactsFromList200Response.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Contacts removed from list. |  * X-RateLimit-Limit - Maximum requests per window. <br>  * X-RateLimit-Remaining - Requests remaining in the current window. <br>  * X-RateLimit-Reset - Unix timestamp when the current window resets. <br>  |
**400** | Malformed JSON or invalid request. |  -  |
**401** | Missing or invalid API key. |  -  |
**403** | Account suspended, feature denied, or cross-project access blocked. |  -  |
**404** | Resource not found. |  -  |
**409** | Request conflicts with current state. |  -  |
**422** | Validation failed or plan limit exceeded. |  -  |
**429** | Rate limit exceeded. Retry after the &#x60;Retry-After&#x60; header value. |  -  |
**500** | Unexpected server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_contacts_from_list_legacy**
> RemoveContactsFromList200Response remove_contacts_from_list_legacy(list, list_contacts_membership_request)

Remove contacts from list

Remove contacts from a static list. Compatibility POST routes expose the same behavior with route-specific operation IDs. Required scope: `contacts.write`.

### Example

* Bearer (API Key) Authentication (bearerAuth):

```python
import mailermine_generated
from mailermine_generated.models.list_contacts_membership_request import ListContactsMembershipRequest
from mailermine_generated.models.remove_contacts_from_list200_response import RemoveContactsFromList200Response
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
    api_instance = mailermine_generated.ListsApi(api_client)
    list = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | List UUID.
    list_contacts_membership_request = mailermine_generated.ListContactsMembershipRequest() # ListContactsMembershipRequest | 

    try:
        # Remove contacts from list
        api_response = api_instance.remove_contacts_from_list_legacy(list, list_contacts_membership_request)
        print("The response of ListsApi->remove_contacts_from_list_legacy:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ListsApi->remove_contacts_from_list_legacy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **list** | **UUID**| List UUID. | 
 **list_contacts_membership_request** | [**ListContactsMembershipRequest**](ListContactsMembershipRequest.md)|  | 

### Return type

[**RemoveContactsFromList200Response**](RemoveContactsFromList200Response.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Contacts removed from list. |  * X-RateLimit-Limit - Maximum requests per window. <br>  * X-RateLimit-Remaining - Requests remaining in the current window. <br>  * X-RateLimit-Reset - Unix timestamp when the current window resets. <br>  |
**400** | Malformed JSON or invalid request. |  -  |
**401** | Missing or invalid API key. |  -  |
**403** | Account suspended, feature denied, or cross-project access blocked. |  -  |
**404** | Resource not found. |  -  |
**409** | Request conflicts with current state. |  -  |
**422** | Validation failed or plan limit exceeded. |  -  |
**429** | Rate limit exceeded. Retry after the &#x60;Retry-After&#x60; header value. |  -  |
**500** | Unexpected server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_list**
> ListResponse update_list(list, update_list_request=update_list_request)

Update contact list

Update a static contact list. Required scope: `contacts.write`.

### Example

* Bearer (API Key) Authentication (bearerAuth):

```python
import mailermine_generated
from mailermine_generated.models.list_response import ListResponse
from mailermine_generated.models.update_list_request import UpdateListRequest
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
    api_instance = mailermine_generated.ListsApi(api_client)
    list = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | List UUID.
    update_list_request = mailermine_generated.UpdateListRequest() # UpdateListRequest |  (optional)

    try:
        # Update contact list
        api_response = api_instance.update_list(list, update_list_request=update_list_request)
        print("The response of ListsApi->update_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ListsApi->update_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **list** | **UUID**| List UUID. | 
 **update_list_request** | [**UpdateListRequest**](UpdateListRequest.md)|  | [optional] 

### Return type

[**ListResponse**](ListResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List updated successfully. |  * X-RateLimit-Limit - Maximum requests per window. <br>  * X-RateLimit-Remaining - Requests remaining in the current window. <br>  * X-RateLimit-Reset - Unix timestamp when the current window resets. <br>  |
**400** | Malformed JSON or invalid request. |  -  |
**401** | Missing or invalid API key. |  -  |
**403** | Account suspended, feature denied, or cross-project access blocked. |  -  |
**404** | Resource not found. |  -  |
**409** | Request conflicts with current state. |  -  |
**422** | Validation failed or plan limit exceeded. |  -  |
**429** | Rate limit exceeded. Retry after the &#x60;Retry-After&#x60; header value. |  -  |
**500** | Unexpected server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

