# swagger_client.FactsApi

All URIs are relative to *http://api-server/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**retrieve_iceberg_device_device_facts_by_id**](FactsApi.md#retrieve_iceberg_device_device_facts_by_id) | **GET** /device/{device_id}/facts/ | Get a device&#39;s facts.
[**retrieve_iceberg_devices_devices_facts**](FactsApi.md#retrieve_iceberg_devices_devices_facts) | **GET** /devices/facts/ | Get devices facts.
[**retrieve_iceberg_devices_facts_by_group**](FactsApi.md#retrieve_iceberg_devices_facts_by_group) | **GET** /device-group/{device_group_name}/facts/ | Get a devices facts for given group.


# **retrieve_iceberg_device_device_facts_by_id**
> DeviceSchema retrieve_iceberg_device_device_facts_by_id(device_id, authorization=authorization, working=working, update=update, timeout=timeout)

Get a device's facts.

Get the fact details of a device by its `device-id`.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.FactsApi()
device_id = 'device_id_example' # str | ID of device-id
authorization = 'authorization_example' # str | authentication header object (optional)
working = true # bool | true queries un-committed configuration (optional)
update = true # bool | true will first update facts from device and then return facts (optional)
timeout = 56 # int | timeout in seconds to wait for facts from given device id (optional)

try:
    # Get a device's facts.
    api_response = api_instance.retrieve_iceberg_device_device_facts_by_id(device_id, authorization=authorization, working=working, update=update, timeout=timeout)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FactsApi->retrieve_iceberg_device_device_facts_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **str**| ID of device-id | 
 **authorization** | **str**| authentication header object | [optional] 
 **working** | **bool**| true queries un-committed configuration | [optional] 
 **update** | **bool**| true will first update facts from device and then return facts | [optional] 
 **timeout** | **int**| timeout in seconds to wait for facts from given device id | [optional] 

### Return type

[**DeviceSchema**](DeviceSchema.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_iceberg_devices_devices_facts**
> DeviceSchema retrieve_iceberg_devices_devices_facts(authorization=authorization, working=working, update=update, timeout=timeout)

Get devices facts.

Get the fact details of every device

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.FactsApi()
authorization = 'authorization_example' # str | authentication header object (optional)
working = true # bool | true queries un-committed configuration (optional)
update = true # bool | true will first update facts from device and then return facts (optional)
timeout = 56 # int | timeout in seconds to wait for facts from every device (optional)

try:
    # Get devices facts.
    api_response = api_instance.retrieve_iceberg_devices_devices_facts(authorization=authorization, working=working, update=update, timeout=timeout)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FactsApi->retrieve_iceberg_devices_devices_facts: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| authentication header object | [optional] 
 **working** | **bool**| true queries un-committed configuration | [optional] 
 **update** | **bool**| true will first update facts from device and then return facts | [optional] 
 **timeout** | **int**| timeout in seconds to wait for facts from every device | [optional] 

### Return type

[**DeviceSchema**](DeviceSchema.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_iceberg_devices_facts_by_group**
> DeviceSchema retrieve_iceberg_devices_facts_by_group(device_group_name, authorization=authorization, working=working, update=update, timeout=timeout)

Get a devices facts for given group.

Get the fact details of every device under given group

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.FactsApi()
device_group_name = 'device_group_name_example' # str | ID of group
authorization = 'authorization_example' # str | authentication header object (optional)
working = true # bool | true queries un-committed configuration (optional)
update = true # bool | true will first update facts from device and then return facts (optional)
timeout = 56 # int | timeout in seconds to wait for facts from every device (optional)

try:
    # Get a devices facts for given group.
    api_response = api_instance.retrieve_iceberg_devices_facts_by_group(device_group_name, authorization=authorization, working=working, update=update, timeout=timeout)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FactsApi->retrieve_iceberg_devices_facts_by_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_group_name** | **str**| ID of group | 
 **authorization** | **str**| authentication header object | [optional] 
 **working** | **bool**| true queries un-committed configuration | [optional] 
 **update** | **bool**| true will first update facts from device and then return facts | [optional] 
 **timeout** | **int**| timeout in seconds to wait for facts from every device | [optional] 

### Return type

[**DeviceSchema**](DeviceSchema.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

