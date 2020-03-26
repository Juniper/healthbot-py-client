# swagger_client.DataSourceApi

All URIs are relative to *http://api-server/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_data_store**](DataSourceApi.md#create_data_store) | **POST** /data-store/{group_name}/ | Create dashboard details.


# **create_data_store**
> create_data_store(key, data, group_name, authorization=authorization)

Create dashboard details.

Store data-store details in database for the requested group name and key.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DataSourceApi()
key = 'key_example' # str | Key of data_store object
data = swagger_client.DatastoreSchema() # DatastoreSchema | Value of data_store object
group_name = 'group_name_example' # str | Group name
authorization = 'authorization_example' # str | authentication header object (optional)

try:
    # Create dashboard details.
    api_instance.create_data_store(key, data, group_name, authorization=authorization)
except ApiException as e:
    print("Exception when calling DataSourceApi->create_data_store: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key** | **str**| Key of data_store object | 
 **data** | [**DatastoreSchema**](DatastoreSchema.md)| Value of data_store object | 
 **group_name** | **str**| Group name | 
 **authorization** | **str**| authentication header object | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

