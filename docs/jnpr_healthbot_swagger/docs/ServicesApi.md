# swagger_client.ServicesApi

All URIs are relative to *http://api-server/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_services_device_groups_device_group_by_device_group_name**](ServicesApi.md#create_services_device_groups_device_group_by_device_group_name) | **POST** /services/device-group/{device_group_name}/ | Start a device-group&#39;s services.
[**create_services_network_group_by_network_group_name**](ServicesApi.md#create_services_network_group_by_network_group_name) | **POST** /services/network-group/{network_group_name}/ | Start a network-group&#39;s services.
[**delete_services_device_groups_device_group_by_device_group_name**](ServicesApi.md#delete_services_device_groups_device_group_by_device_group_name) | **DELETE** /services/device-group/{device_group_name}/ | Stop and remove a device-group&#39;s services.
[**delete_services_network_group_by_network_group_name**](ServicesApi.md#delete_services_network_group_by_network_group_name) | **DELETE** /services/network-group/{network_group_name}/ | Stop and remove a network-group&#39;s services.
[**retrieve_services_device_groups_device_group_device_group**](ServicesApi.md#retrieve_services_device_groups_device_group_device_group) | **GET** /services/device-group/ | Get running &#x60;device-group-name&#x60;s.
[**retrieve_services_network_group**](ServicesApi.md#retrieve_services_network_group) | **GET** /services/network-group/ | Get running &#x60;network-group-name&#x60;s


# **create_services_device_groups_device_group_by_device_group_name**
> create_services_device_groups_device_group_by_device_group_name(device_group_name, authorization=authorization)

Start a device-group's services.

Start services of a device group. Use this to start stopped services.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ServicesApi()
device_group_name = 'device_group_name_example' # str | Name of device group
authorization = 'authorization_example' # str | authentication header object (optional)

try:
    # Start a device-group's services.
    api_instance.create_services_device_groups_device_group_by_device_group_name(device_group_name, authorization=authorization)
except ApiException as e:
    print("Exception when calling ServicesApi->create_services_device_groups_device_group_by_device_group_name: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_group_name** | **str**| Name of device group | 
 **authorization** | **str**| authentication header object | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, multipart/form-data
 - **Accept**: application/json, application/octet-stream

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_services_network_group_by_network_group_name**
> create_services_network_group_by_network_group_name(network_group_name, authorization=authorization)

Start a network-group's services.

Start services of a network group. Use this to start stopped services.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ServicesApi()
network_group_name = 'network_group_name_example' # str | Name of network group
authorization = 'authorization_example' # str | authentication header object (optional)

try:
    # Start a network-group's services.
    api_instance.create_services_network_group_by_network_group_name(network_group_name, authorization=authorization)
except ApiException as e:
    print("Exception when calling ServicesApi->create_services_network_group_by_network_group_name: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **network_group_name** | **str**| Name of network group | 
 **authorization** | **str**| authentication header object | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, multipart/form-data
 - **Accept**: application/json, application/octet-stream

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_services_device_groups_device_group_by_device_group_name**
> delete_services_device_groups_device_group_by_device_group_name(device_group_name, authorization=authorization)

Stop and remove a device-group's services.

Stop and clean services of a device-group. This will remove all the services for a device-group, however, it  will not clean up the collected data.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ServicesApi()
device_group_name = 'device_group_name_example' # str | Name of device group
authorization = 'authorization_example' # str | authentication header object (optional)

try:
    # Stop and remove a device-group's services.
    api_instance.delete_services_device_groups_device_group_by_device_group_name(device_group_name, authorization=authorization)
except ApiException as e:
    print("Exception when calling ServicesApi->delete_services_device_groups_device_group_by_device_group_name: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_group_name** | **str**| Name of device group | 
 **authorization** | **str**| authentication header object | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, multipart/form-data
 - **Accept**: application/json, application/octet-stream

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_services_network_group_by_network_group_name**
> delete_services_network_group_by_network_group_name(network_group_name, authorization=authorization)

Stop and remove a network-group's services.

Stop and clean the services of a network group. This will remove all the services for a network-group, however, it will not clean up the collected data.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ServicesApi()
network_group_name = 'network_group_name_example' # str | Name of network group
authorization = 'authorization_example' # str | authentication header object (optional)

try:
    # Stop and remove a network-group's services.
    api_instance.delete_services_network_group_by_network_group_name(network_group_name, authorization=authorization)
except ApiException as e:
    print("Exception when calling ServicesApi->delete_services_network_group_by_network_group_name: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **network_group_name** | **str**| Name of network group | 
 **authorization** | **str**| authentication header object | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, multipart/form-data
 - **Accept**: application/json, application/octet-stream

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_services_device_groups_device_group_device_group**
> list[str] retrieve_services_device_groups_device_group_device_group(authorization=authorization)

Get running `device-group-name`s.

Get the list of `device-group-name`s of device-groups whose services are running.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ServicesApi()
authorization = 'authorization_example' # str | authentication header object (optional)

try:
    # Get running `device-group-name`s.
    api_response = api_instance.retrieve_services_device_groups_device_group_device_group(authorization=authorization)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ServicesApi->retrieve_services_device_groups_device_group_device_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| authentication header object | [optional] 

### Return type

**list[str]**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_services_network_group**
> list[str] retrieve_services_network_group(authorization=authorization)

Get running `network-group-name`s

Get the list of `network-group-name`s of network-groups whose services are running.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ServicesApi()
authorization = 'authorization_example' # str | authentication header object (optional)

try:
    # Get running `network-group-name`s
    api_response = api_instance.retrieve_services_network_group(authorization=authorization)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ServicesApi->retrieve_services_network_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| authentication header object | [optional] 

### Return type

**list[str]**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

