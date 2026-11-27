# SendEmailRequestTracking

Turn open and click tracking on or off for this email, overriding the project default. Omitted or null keys use the project default. Plan limits and sender trust rules still apply, so tracking may stay off even when requested. Add `data-mm-notrack` to an `<a>` tag to exclude a single link.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**opens** | **bool** |  | [optional] 
**clicks** | **bool** |  | [optional] 

## Example

```python
from mailermine_generated.models.send_email_request_tracking import SendEmailRequestTracking

# TODO update the JSON string below
json = "{}"
# create an instance of SendEmailRequestTracking from a JSON string
send_email_request_tracking_instance = SendEmailRequestTracking.from_json(json)
# print the JSON string representation of the object
print(SendEmailRequestTracking.to_json())

# convert the object into a dict
send_email_request_tracking_dict = send_email_request_tracking_instance.to_dict()
# create an instance of SendEmailRequestTracking from a dict
send_email_request_tracking_from_dict = SendEmailRequestTracking.from_dict(send_email_request_tracking_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


