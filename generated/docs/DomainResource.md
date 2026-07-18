# DomainResource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Public domain UUID. @format uuid | 
**domain** | **str** | Sending domain. @example mail.example.com | 
**status** | **str** | Provisioning status. @example pending | 
**verified** | **bool** | Whether ownership is verified. @example false | 
**verification_status** | **str** | Verification status. @var &#39;provisioning&#39;|&#39;pending&#39;|&#39;verified&#39;|&#39;failed&#39; | 
**provider** | **str** | Delivery provider label. @example Amazon SES | 
**created_at** | **str** | Creation time. @format date-time | 
**verified_at** | **str** | Verification completion time. @format date-time | 
**last_checked_at** | **str** | Last verification check. @format date-time | 
**dns_status** | **str** | Aggregate DNS status. | 
**dkim_status** | **str** | DKIM verification status. | 
**spf_status** | **str** | SPF verification status. | 
**tracking_status** | **str** | Tracking-domain status. @example not_configured | 
**mail_from** | **str** | MAIL FROM domain; present on detailed responses. | 
**verification_error** | **str** | Last provider verification error. | 
**verification_token** | **str** | Provider verification token. | 
**dmarc_recommendation** | [**CampaignActivityPayload**](CampaignActivityPayload.md) |  | 
**dns_records** | [**List[DNSRecord]**](DNSRecord.md) | DNS records required for verification. | 
**dns_summary** | [**CampaignActivityPayload**](CampaignActivityPayload.md) |  | 
**project** | [**CampaignActivityPayload**](CampaignActivityPayload.md) |  | 

## Example

```python
from mailermine_generated.models.domain_resource import DomainResource

# TODO update the JSON string below
json = "{}"
# create an instance of DomainResource from a JSON string
domain_resource_instance = DomainResource.from_json(json)
# print the JSON string representation of the object
print(DomainResource.to_json())

# convert the object into a dict
domain_resource_dict = domain_resource_instance.to_dict()
# create an instance of DomainResource from a dict
domain_resource_from_dict = DomainResource.from_dict(domain_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


