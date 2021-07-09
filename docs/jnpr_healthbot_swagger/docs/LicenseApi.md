# swagger_client.LicenseApi

All URIs are relative to *http://api-server/api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_iceberg_add_license_from_file**](LicenseApi.md#create_iceberg_add_license_from_file) | **POST** /license/keys/ | Add license from file.
[**delete_iceberg_delete_all_license**](LicenseApi.md#delete_iceberg_delete_all_license) | **DELETE** /license/keys/ | Delete all licenses.
[**delete_iceberg_delete_license_by_id**](LicenseApi.md#delete_iceberg_delete_license_by_id) | **DELETE** /license/key/{license_id}/ | Delete a license.
[**retrieve_iceberg_get_all_license_id**](LicenseApi.md#retrieve_iceberg_get_all_license_id) | **GET** /license/keys/ | List of available license id&#39;s.
[**retrieve_iceberg_license_features_info**](LicenseApi.md#retrieve_iceberg_license_features_info) | **GET** /license/status/ | Status of all the licensed features.
[**retrieve_iceberg_license_file_by_license_id**](LicenseApi.md#retrieve_iceberg_license_file_by_license_id) | **GET** /license/key/{license_id}/ | Download license file.
[**retrieve_iceberg_license_key_contents**](LicenseApi.md#retrieve_iceberg_license_key_contents) | **GET** /license/keys/contents/ | Get the contents of all licenses.
[**retrieve_iceberg_license_key_contents_by_id**](LicenseApi.md#retrieve_iceberg_license_key_contents_by_id) | **GET** /license/key/{license_id}/contents/ | Get the contents of a license.
[**update_iceberg_replace_license**](LicenseApi.md#update_iceberg_replace_license) | **PUT** /license/keys/ | Update the license.


# **create_iceberg_add_license_from_file**
> InlineResponse2001 create_iceberg_add_license_from_file(license_file, x_iam_token=x_iam_token)

Add license from file.

Add license keys from file.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.LicenseApi()
license_file = '/path/to/file.txt' # file | License key file content
x_iam_token = 'x_iam_token_example' # str | authentication header object (optional)

try:
    # Add license from file.
    api_response = api_instance.create_iceberg_add_license_from_file(license_file, x_iam_token=x_iam_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LicenseApi->create_iceberg_add_license_from_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **license_file** | **file**| License key file content | 
 **x_iam_token** | **str**| authentication header object | [optional] 

### Return type

[**InlineResponse2001**](InlineResponse2001.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_iceberg_delete_all_license**
> delete_iceberg_delete_all_license(x_iam_token=x_iam_token)

Delete all licenses.

Delete all the previously added license keys.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.LicenseApi()
x_iam_token = 'x_iam_token_example' # str | authentication header object (optional)

try:
    # Delete all licenses.
    api_instance.delete_iceberg_delete_all_license(x_iam_token=x_iam_token)
except ApiException as e:
    print("Exception when calling LicenseApi->delete_iceberg_delete_all_license: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_iam_token** | **str**| authentication header object | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_iceberg_delete_license_by_id**
> delete_iceberg_delete_license_by_id(license_id, x_iam_token=x_iam_token)

Delete a license.

Delete a license matching the license id.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.LicenseApi()
license_id = 'license_id_example' # str | License id
x_iam_token = 'x_iam_token_example' # str | authentication header object (optional)

try:
    # Delete a license.
    api_instance.delete_iceberg_delete_license_by_id(license_id, x_iam_token=x_iam_token)
except ApiException as e:
    print("Exception when calling LicenseApi->delete_iceberg_delete_license_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **license_id** | **str**| License id | 
 **x_iam_token** | **str**| authentication header object | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_iceberg_get_all_license_id**
> list[str] retrieve_iceberg_get_all_license_id(x_iam_token=x_iam_token)

List of available license id's.

Get the list of all available license id's.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.LicenseApi()
x_iam_token = 'x_iam_token_example' # str | authentication header object (optional)

try:
    # List of available license id's.
    api_response = api_instance.retrieve_iceberg_get_all_license_id(x_iam_token=x_iam_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LicenseApi->retrieve_iceberg_get_all_license_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_iam_token** | **str**| authentication header object | [optional] 

### Return type

**list[str]**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_iceberg_license_features_info**
> LicenseFeaturesSchema retrieve_iceberg_license_features_info(x_iam_token=x_iam_token)

Status of all the licensed features.

Get the status of all the licensed features. Also provides the compliance info per feature

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.LicenseApi()
x_iam_token = 'x_iam_token_example' # str | authentication header object (optional)

try:
    # Status of all the licensed features.
    api_response = api_instance.retrieve_iceberg_license_features_info(x_iam_token=x_iam_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LicenseApi->retrieve_iceberg_license_features_info: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_iam_token** | **str**| authentication header object | [optional] 

### Return type

[**LicenseFeaturesSchema**](LicenseFeaturesSchema.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_iceberg_license_file_by_license_id**
> file retrieve_iceberg_license_file_by_license_id(license_id, x_iam_token=x_iam_token)

Download license file.

Download the specified license file based on license id.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.LicenseApi()
license_id = 'license_id_example' # str | License id
x_iam_token = 'x_iam_token_example' # str | authentication header object (optional)

try:
    # Download license file.
    api_response = api_instance.retrieve_iceberg_license_file_by_license_id(license_id, x_iam_token=x_iam_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LicenseApi->retrieve_iceberg_license_file_by_license_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **license_id** | **str**| License id | 
 **x_iam_token** | **str**| authentication header object | [optional] 

### Return type

[**file**](file.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/octet-stream, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_iceberg_license_key_contents**
> LicenseKeysSchema retrieve_iceberg_license_key_contents(x_iam_token=x_iam_token)

Get the contents of all licenses.

Get the license key contents for all the available licenses.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.LicenseApi()
x_iam_token = 'x_iam_token_example' # str | authentication header object (optional)

try:
    # Get the contents of all licenses.
    api_response = api_instance.retrieve_iceberg_license_key_contents(x_iam_token=x_iam_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LicenseApi->retrieve_iceberg_license_key_contents: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_iam_token** | **str**| authentication header object | [optional] 

### Return type

[**LicenseKeysSchema**](LicenseKeysSchema.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_iceberg_license_key_contents_by_id**
> LicenseKeySchema retrieve_iceberg_license_key_contents_by_id(license_id, x_iam_token=x_iam_token)

Get the contents of a license.

Get the license key contents by the license id.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.LicenseApi()
license_id = 'license_id_example' # str | License id
x_iam_token = 'x_iam_token_example' # str | authentication header object (optional)

try:
    # Get the contents of a license.
    api_response = api_instance.retrieve_iceberg_license_key_contents_by_id(license_id, x_iam_token=x_iam_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LicenseApi->retrieve_iceberg_license_key_contents_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **license_id** | **str**| License id | 
 **x_iam_token** | **str**| authentication header object | [optional] 

### Return type

[**LicenseKeySchema**](LicenseKeySchema.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_iceberg_replace_license**
> InlineResponse2001 update_iceberg_replace_license(license_raw_keys, x_iam_token=x_iam_token)

Update the license.

Update existing license keys with the new one provided in this request.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.LicenseApi()
license_raw_keys = swagger_client.LicenseRawKeysSchema() # LicenseRawKeysSchema | License raw keys contents
x_iam_token = 'x_iam_token_example' # str | authentication header object (optional)

try:
    # Update the license.
    api_response = api_instance.update_iceberg_replace_license(license_raw_keys, x_iam_token=x_iam_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LicenseApi->update_iceberg_replace_license: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **license_raw_keys** | [**LicenseRawKeysSchema**](LicenseRawKeysSchema.md)| License raw keys contents | 
 **x_iam_token** | **str**| authentication header object | [optional] 

### Return type

[**InlineResponse2001**](InlineResponse2001.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

