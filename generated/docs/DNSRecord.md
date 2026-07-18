# DNSRecord


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**record_type** | **str** | DNS record type. @var &#39;TXT&#39;|&#39;CNAME&#39;|&#39;MX&#39; @example CNAME | 
**record_name** | **str** | DNS host/name. @example selector1._domainkey.mail.example.com | 
**record_value** | **str** | DNS record value. @example selector1.dkim.provider.example | 
**name** | **str** | Alias of record_name. | 
**value** | **str** | Alias of record_value. | 
**purpose** | **str** | Record purpose. @var &#39;verification&#39;|&#39;spf&#39;|&#39;dkim&#39;|&#39;mail_from&#39;|&#39;dmarc&#39; @example dkim | 
**priority** | **int** | Optional provider priority, primarily for MX records. @example 10 | 
**ttl** | **int** | DNS TTL in seconds. @example 300 | 
**status** | **str** | Verification state. @var &#39;pending&#39;|&#39;verified&#39;|&#39;failed&#39; @example pending | 
**purpose_label** | **str** | Human-readable purpose. @example DKIM | 

## Example

```python
from mailermine_generated.models.dns_record import DNSRecord

# TODO update the JSON string below
json = "{}"
# create an instance of DNSRecord from a JSON string
dns_record_instance = DNSRecord.from_json(json)
# print the JSON string representation of the object
print(DNSRecord.to_json())

# convert the object into a dict
dns_record_dict = dns_record_instance.to_dict()
# create an instance of DNSRecord from a dict
dns_record_from_dict = DNSRecord.from_dict(dns_record_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


