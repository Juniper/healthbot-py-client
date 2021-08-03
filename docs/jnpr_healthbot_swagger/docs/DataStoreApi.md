# swagger_client.DataStoreApi

All URIs are relative to *http://api-server/api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_data_store**](DataStoreApi.md#create_data_store) | **POST** /config/data-store/{group_name}/ | Create dashboard details.
[**delete_data_store**](DataStoreApi.md#delete_data_store) | **DELETE** /config/data-store/{group_name}/ | Delete dashboard details.
[**retrieve_data_store**](DataStoreApi.md#retrieve_data_store) | **GET** /config/data-store/{group_name}/ | Delete dashboard details.
[**update_data_store**](DataStoreApi.md#update_data_store) | **PUT** /config/data-store/{group_name}/ | Update data_store details.


# **create_data_store**
> create_data_store(key, data, group_name, x_iam_token=x_iam_token)

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
api_instance = swagger_client.DataStoreApi()
key = 'key_example' # str | Key of data_store object
data = swagger_client.DatastoreSchema() # DatastoreSchema | Value of data_store object
group_name = 'group_name_example' # str | Group name
x_iam_token = 'x_iam_token_example' # str | authentication header object (optional)

try:
    # Create dashboard details.
    api_instance.create_data_store(key, data, group_name, x_iam_token=x_iam_token)
except ApiException as e:
    print("Exception when calling DataStoreApi->create_data_store: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key** | **str**| Key of data_store object | 
 **data** | [**DatastoreSchema**](DatastoreSchema.md)| Value of data_store object | 
 **group_name** | **str**| Group name | 
 **x_iam_token** | **str**| authentication header object | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_data_store**
> delete_data_store(group_name, x_iam_token=x_iam_token, key=key)

Delete dashboard details.

Delete data_store details for the given group-name, or as per the keys passed in query.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DataStoreApi()
group_name = 'group_name_example' # str | Group name
x_iam_token = 'x_iam_token_example' # str | authentication header object (optional)
key = ['key_example'] # list[str] | ID of dashboard (optional)

try:
    # Delete dashboard details.
    api_instance.delete_data_store(group_name, x_iam_token=x_iam_token, key=key)
except ApiException as e:
    print("Exception when calling DataStoreApi->delete_data_store: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_name** | **str**| Group name | 
 **x_iam_token** | **str**| authentication header object | [optional] 
 **key** | [**list[str]**](str.md)| ID of dashboard | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_data_store**
> DatastoreSchema retrieve_data_store(group_name, x_iam_token=x_iam_token, key=key)

Delete dashboard details.

Retrieve data_store details for the given group-name, or as per the keys passed in query.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DataStoreApi()
group_name = 'group_name_example' # str | Group name
x_iam_token = 'x_iam_token_example' # str | authentication header object (optional)
key = ['key_example'] # list[str] | Key of data_store object (optional)

try:
    # Delete dashboard details.
    api_response = api_instance.retrieve_data_store(group_name, x_iam_token=x_iam_token, key=key)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DataStoreApi->retrieve_data_store: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_name** | **str**| Group name | 
 **x_iam_token** | **str**| authentication header object | [optional] 
 **key** | [**list[str]**](str.md)| Key of data_store object | [optional] 

### Return type

[**DatastoreSchema**](DatastoreSchema.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_data_store**
> update_data_store(key, data, group_name, x_iam_token=x_iam_token)

Update data_store details.

Update data-store details in database for the requested group name and key.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DataStoreApi()
key = 'key_example' # str | key of data_store
data = swagger_client.DatastoreSchema() # DatastoreSchema | value of data_store object
group_name = 'group_name_example' # str | Group name
x_iam_token = 'x_iam_token_example' # str | authentication header object (optional)

try:
    # Update data_store details.
    api_instance.update_data_store(key, data, group_name, x_iam_token=x_iam_token)
except ApiException as e:
    print("Exception when calling DataStoreApi->update_data_store: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key** | **str**| key of data_store | 
 **data** | [**DatastoreSchema**](DatastoreSchema.md)| value of data_store object | 
 **group_name** | **str**| Group name | 
 **x_iam_token** | **str**| authentication header object | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

