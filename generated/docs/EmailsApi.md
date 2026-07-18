# mailermine_generated.EmailsApi

All URIs are relative to *http://127.0.0.1:8000/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**send_email**](EmailsApi.md#send_email) | **POST** /emails | Send email


# **send_email**
> SendEmailResponse send_email(send_email_request)

Send email

Queue a transactional email for delivery. Supports attachments, CC/BCC, reply-to, headers, tags, and metadata.

### Example

* Bearer (API Key) Authentication (bearerAuth):

```python
import mailermine_generated
from mailermine_generated.models.send_email_request import SendEmailRequest
from mailermine_generated.models.send_email_response import SendEmailResponse
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
    api_instance = mailermine_generated.EmailsApi(api_client)
    send_email_request = mailermine_generated.SendEmailRequest() # SendEmailRequest | 

    try:
        # Send email
        api_response = api_instance.send_email(send_email_request)
        print("The response of EmailsApi->send_email:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmailsApi->send_email: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **send_email_request** | [**SendEmailRequest**](SendEmailRequest.md)|  | 

### Return type

[**SendEmailResponse**](SendEmailResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Message accepted and queued. |  * X-RateLimit-Limit - Maximum requests per window. <br>  * X-RateLimit-Remaining - Requests remaining in the current window. <br>  * X-RateLimit-Reset - Unix timestamp when the current window resets. <br>  |
**422** | Validation failed or plan limit exceeded. |  -  |
**400** | Malformed JSON or invalid request. |  -  |
**401** | Missing or invalid API key. |  -  |
**403** | Account suspended, feature denied, or cross-project access blocked. |  -  |
**429** | Rate limit exceeded. Retry after the &#x60;Retry-After&#x60; header value. |  -  |
**500** | Unexpected server error. |  -  |
**404** | Resource not found. |  -  |
**409** | Request conflicts with current state. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

