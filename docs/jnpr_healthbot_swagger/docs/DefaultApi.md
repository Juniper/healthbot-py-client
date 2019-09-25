# swagger_client.DefaultApi

All URIs are relative to *http://api-server/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_files_helper_files_by_file_name**](DefaultApi.md#create_files_helper_files_by_file_name) | **POST** /files/helper-files/{file_name}/ | Upload a helper-file.
[**create_iceberg_profile_data_summarization_raw_by_id**](DefaultApi.md#create_iceberg_profile_data_summarization_raw_by_id) | **POST** /profile/data-summarization/raw/{name}/ | Create raw-data-summarization by ID
[**create_iceberg_profile_security_ca_profile_by_id**](DefaultApi.md#create_iceberg_profile_security_ca_profile_by_id) | **POST** /profile/security/ca-profile/{name}/ | Create ca-profile by ID
[**create_iceberg_profile_security_local_certificate_by_id**](DefaultApi.md#create_iceberg_profile_security_local_certificate_by_id) | **POST** /profile/security/local-certificate/{name}/ | Create local-certificate by ID
[**create_iceberg_profile_security_ssh_key_profile_by_id**](DefaultApi.md#create_iceberg_profile_security_ssh_key_profile_by_id) | **POST** /profile/security/ssh-key-profile/{name}/ | Create ssh-key-profile by ID
[**create_iceberg_profiles**](DefaultApi.md#create_iceberg_profiles) | **POST** /profiles/ | Create profile by ID
[**delete_files_helper_files_by_file_name**](DefaultApi.md#delete_files_helper_files_by_file_name) | **DELETE** /files/helper-files/{file_name}/ | Delete a helper-file.
[**delete_iceberg_profile_data_summarization_raw_by_id**](DefaultApi.md#delete_iceberg_profile_data_summarization_raw_by_id) | **DELETE** /profile/data-summarization/raw/{name}/ | Delete raw-data-summarization by ID
[**delete_iceberg_profile_security_ca_profile_by_id**](DefaultApi.md#delete_iceberg_profile_security_ca_profile_by_id) | **DELETE** /profile/security/ca-profile/{name}/ | Delete ca-profile by ID
[**delete_iceberg_profile_security_local_certificate_by_id**](DefaultApi.md#delete_iceberg_profile_security_local_certificate_by_id) | **DELETE** /profile/security/local-certificate/{name}/ | Delete local-certificate by ID
[**delete_iceberg_profile_security_ssh_key_profile_by_id**](DefaultApi.md#delete_iceberg_profile_security_ssh_key_profile_by_id) | **DELETE** /profile/security/ssh-key-profile/{name}/ | Delete ssh-key-profile by ID
[**delete_iceberg_profiles**](DefaultApi.md#delete_iceberg_profiles) | **DELETE** /profiles/ | Delete profile by ID
[**inspect_command_rpc_table_on_device**](DefaultApi.md#inspect_command_rpc_table_on_device) | **POST** /inspect/command-rpc/table/ | Inspect the given iAgent table.
[**retrieve_configuration_jobs**](DefaultApi.md#retrieve_configuration_jobs) | **GET** /configuration/jobs/ | 
[**retrieve_data_database_table**](DefaultApi.md#retrieve_data_database_table) | **GET** /data/database/table/ | Get information about tables for a device of a device-group.
[**retrieve_data_database_table_column_by_table_name**](DefaultApi.md#retrieve_data_database_table_column_by_table_name) | **GET** /data/database/table/column/ | Get information about columns in a table.
[**retrieve_data_database_tags_by_table_name**](DefaultApi.md#retrieve_data_database_tags_by_table_name) | **GET** /data/database/table/tags/ | Get information about tags keys and values in a table.
[**retrieve_event**](DefaultApi.md#retrieve_event) | **GET** /event/ | Get all events for a device.
[**retrieve_event_by_event_name**](DefaultApi.md#retrieve_event_by_event_name) | **GET** /event/{event_name}/ | Get instances of a device event.
[**retrieve_event_by_event_name_device_group**](DefaultApi.md#retrieve_event_by_event_name_device_group) | **GET** /event/device-group/{event_name}/ | Get instances of a device-group event.
[**retrieve_event_by_event_name_network_group**](DefaultApi.md#retrieve_event_by_event_name_network_group) | **GET** /event/network-group/{event_name}/ | Get instances of a network-group event.
[**retrieve_event_device_group**](DefaultApi.md#retrieve_event_device_group) | **GET** /event/device-group/ | Get all events for a device-group.
[**retrieve_event_network_group**](DefaultApi.md#retrieve_event_network_group) | **GET** /event/network-group/ | Get all events for a network-group.
[**retrieve_files_helper_files**](DefaultApi.md#retrieve_files_helper_files) | **GET** /files/helper-files/ | Get all helper-file names.
[**retrieve_files_helper_files_by_file_name**](DefaultApi.md#retrieve_files_helper_files_by_file_name) | **GET** /files/helper-files/{file_name}/ | Download a helper-file.
[**retrieve_health_all**](DefaultApi.md#retrieve_health_all) | **GET** /health/ | Return a dict with health of devices in device groups and network groups
[**retrieve_health_tree_by_device_group**](DefaultApi.md#retrieve_health_tree_by_device_group) | **GET** /health-tree/device-group/{device_group_name}/ | Get device-group health-tree.
[**retrieve_health_tree_by_id**](DefaultApi.md#retrieve_health_tree_by_id) | **GET** /health-tree/{device_id}/ | Return a device&#39;s health-tree.
[**retrieve_health_tree_by_network_group**](DefaultApi.md#retrieve_health_tree_by_network_group) | **GET** /health-tree/network-group/{network_group_name}/ | Get network-group health-tree.
[**retrieve_iceberg_profile_data_summarization_raw_by_id**](DefaultApi.md#retrieve_iceberg_profile_data_summarization_raw_by_id) | **GET** /profile/data-summarization/raw/{name}/ | Retrieve raw-data-summarization by ID
[**retrieve_iceberg_profile_data_summarizations_raw**](DefaultApi.md#retrieve_iceberg_profile_data_summarizations_raw) | **GET** /profile/data-summarizations/raw/ | Retrieve raw-data-summarization
[**retrieve_iceberg_profile_security_ca_profile_by_id**](DefaultApi.md#retrieve_iceberg_profile_security_ca_profile_by_id) | **GET** /profile/security/ca-profile/{name}/ | Retrieve ca-profile by ID
[**retrieve_iceberg_profile_security_ca_profiles**](DefaultApi.md#retrieve_iceberg_profile_security_ca_profiles) | **GET** /profile/security/ca-profiles/ | Retrieve ca-profile
[**retrieve_iceberg_profile_security_local_certificate_by_id**](DefaultApi.md#retrieve_iceberg_profile_security_local_certificate_by_id) | **GET** /profile/security/local-certificate/{name}/ | Retrieve local-certificate by ID
[**retrieve_iceberg_profile_security_local_certificates**](DefaultApi.md#retrieve_iceberg_profile_security_local_certificates) | **GET** /profile/security/local-certificates/ | Retrieve local-certificate
[**retrieve_iceberg_profile_security_ssh_key_profile_by_id**](DefaultApi.md#retrieve_iceberg_profile_security_ssh_key_profile_by_id) | **GET** /profile/security/ssh-key-profile/{name}/ | Retrieve ssh-key-profile by ID
[**retrieve_iceberg_profile_security_ssh_key_profiles**](DefaultApi.md#retrieve_iceberg_profile_security_ssh_key_profiles) | **GET** /profile/security/ssh-key-profiles/ | Retrieve ssh-key-profile
[**retrieve_iceberg_profiles**](DefaultApi.md#retrieve_iceberg_profiles) | **GET** /profiles/ | Retrieve profile
[**retrieve_sensors**](DefaultApi.md#retrieve_sensors) | **GET** /sensors/ | List all OpenConfig sensors.
[**update_iceberg_profile_data_summarization_raw_by_id**](DefaultApi.md#update_iceberg_profile_data_summarization_raw_by_id) | **PUT** /profile/data-summarization/raw/{name}/ | Update raw-data-summarization by ID
[**update_iceberg_profile_security_ca_profile_by_id**](DefaultApi.md#update_iceberg_profile_security_ca_profile_by_id) | **PUT** /profile/security/ca-profile/{name}/ | Update ca-profile by ID
[**update_iceberg_profile_security_local_certificate_by_id**](DefaultApi.md#update_iceberg_profile_security_local_certificate_by_id) | **PUT** /profile/security/local-certificate/{name}/ | Update local-certificate by ID
[**update_iceberg_profile_security_ssh_key_profile_by_id**](DefaultApi.md#update_iceberg_profile_security_ssh_key_profile_by_id) | **PUT** /profile/security/ssh-key-profile/{name}/ | Update ssh-key-profile by ID
[**update_iceberg_profiles**](DefaultApi.md#update_iceberg_profiles) | **PUT** /profiles/ | Update profile by ID


# **create_files_helper_files_by_file_name**
> create_files_helper_files_by_file_name(up_file, file_name, input_path=input_path)

Upload a helper-file.

Upload the specified helper-file.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
up_file = '/path/to/file.txt' # file | File content
file_name = 'file_name_example' # str | File name
input_path = 'input_path_example' # str | Input path (optional)

try:
    # Upload a helper-file.
    api_instance.create_files_helper_files_by_file_name(up_file, file_name, input_path=input_path)
except ApiException as e:
    print("Exception when calling DefaultApi->create_files_helper_files_by_file_name: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **up_file** | **file**| File content | 
 **file_name** | **str**| File name | 
 **input_path** | **str**| Input path | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json, application/octet-stream

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_iceberg_profile_data_summarization_raw_by_id**
> create_iceberg_profile_data_summarization_raw_by_id(name, raw_data_summarization)

Create raw-data-summarization by ID

Create operation of resource: raw-data-summarization

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
name = 'name_example' # str | ID of name
raw_data_summarization = swagger_client.RawSchema() # RawSchema | raw_data_summarizationbody object

try:
    # Create raw-data-summarization by ID
    api_instance.create_iceberg_profile_data_summarization_raw_by_id(name, raw_data_summarization)
except ApiException as e:
    print("Exception when calling DefaultApi->create_iceberg_profile_data_summarization_raw_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| ID of name | 
 **raw_data_summarization** | [**RawSchema**](RawSchema.md)| raw_data_summarizationbody object | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_iceberg_profile_security_ca_profile_by_id**
> create_iceberg_profile_security_ca_profile_by_id(name, ca_profile)

Create ca-profile by ID

Create operation of resource: ca-profile

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
name = 'name_example' # str | ID of name
ca_profile = swagger_client.CaProfileSchema() # CaProfileSchema | ca_profilebody object

try:
    # Create ca-profile by ID
    api_instance.create_iceberg_profile_security_ca_profile_by_id(name, ca_profile)
except ApiException as e:
    print("Exception when calling DefaultApi->create_iceberg_profile_security_ca_profile_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| ID of name | 
 **ca_profile** | [**CaProfileSchema**](CaProfileSchema.md)| ca_profilebody object | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_iceberg_profile_security_local_certificate_by_id**
> create_iceberg_profile_security_local_certificate_by_id(name, local_certificate)

Create local-certificate by ID

Create operation of resource: local-certificate

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
name = 'name_example' # str | ID of name
local_certificate = swagger_client.LocalCertificateSchema() # LocalCertificateSchema | local_certificatebody object

try:
    # Create local-certificate by ID
    api_instance.create_iceberg_profile_security_local_certificate_by_id(name, local_certificate)
except ApiException as e:
    print("Exception when calling DefaultApi->create_iceberg_profile_security_local_certificate_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| ID of name | 
 **local_certificate** | [**LocalCertificateSchema**](LocalCertificateSchema.md)| local_certificatebody object | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_iceberg_profile_security_ssh_key_profile_by_id**
> create_iceberg_profile_security_ssh_key_profile_by_id(name, ssh_key_profile)

Create ssh-key-profile by ID

Create operation of resource: ssh-key-profile

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
name = 'name_example' # str | ID of name
ssh_key_profile = swagger_client.SshKeyProfileSchema() # SshKeyProfileSchema | ssh_key_profilebody object

try:
    # Create ssh-key-profile by ID
    api_instance.create_iceberg_profile_security_ssh_key_profile_by_id(name, ssh_key_profile)
except ApiException as e:
    print("Exception when calling DefaultApi->create_iceberg_profile_security_ssh_key_profile_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| ID of name | 
 **ssh_key_profile** | [**SshKeyProfileSchema**](SshKeyProfileSchema.md)| ssh_key_profilebody object | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_iceberg_profiles**
> create_iceberg_profiles(profile)

Create profile by ID

Create entire profile configuration.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
profile = swagger_client.ProfilesSchema() # ProfilesSchema | profilebody object

try:
    # Create profile by ID
    api_instance.create_iceberg_profiles(profile)
except ApiException as e:
    print("Exception when calling DefaultApi->create_iceberg_profiles: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **profile** | [**ProfilesSchema**](ProfilesSchema.md)| profilebody object | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_files_helper_files_by_file_name**
> delete_files_helper_files_by_file_name(file_name, input_path=input_path)

Delete a helper-file.

Delete the specified helper-file. Delete will not fail if the helper-file is being used by some service.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
file_name = 'file_name_example' # str | File name
input_path = 'input_path_example' # str | Input path (optional)

try:
    # Delete a helper-file.
    api_instance.delete_files_helper_files_by_file_name(file_name, input_path=input_path)
except ApiException as e:
    print("Exception when calling DefaultApi->delete_files_helper_files_by_file_name: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file_name** | **str**| File name | 
 **input_path** | **str**| Input path | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, multipart/form-data
 - **Accept**: application/json, application/octet-stream

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_iceberg_profile_data_summarization_raw_by_id**
> delete_iceberg_profile_data_summarization_raw_by_id(name)

Delete raw-data-summarization by ID

Delete operation of resource: raw data-summarization

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
name = 'name_example' # str | ID of name

try:
    # Delete raw-data-summarization by ID
    api_instance.delete_iceberg_profile_data_summarization_raw_by_id(name)
except ApiException as e:
    print("Exception when calling DefaultApi->delete_iceberg_profile_data_summarization_raw_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| ID of name | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_iceberg_profile_security_ca_profile_by_id**
> delete_iceberg_profile_security_ca_profile_by_id(name)

Delete ca-profile by ID

Delete operation of resource: ca-profile

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
name = 'name_example' # str | ID of name

try:
    # Delete ca-profile by ID
    api_instance.delete_iceberg_profile_security_ca_profile_by_id(name)
except ApiException as e:
    print("Exception when calling DefaultApi->delete_iceberg_profile_security_ca_profile_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| ID of name | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_iceberg_profile_security_local_certificate_by_id**
> delete_iceberg_profile_security_local_certificate_by_id(name)

Delete local-certificate by ID

Delete operation of resource: local-certificate

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
name = 'name_example' # str | ID of name

try:
    # Delete local-certificate by ID
    api_instance.delete_iceberg_profile_security_local_certificate_by_id(name)
except ApiException as e:
    print("Exception when calling DefaultApi->delete_iceberg_profile_security_local_certificate_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| ID of name | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_iceberg_profile_security_ssh_key_profile_by_id**
> delete_iceberg_profile_security_ssh_key_profile_by_id(name)

Delete ssh-key-profile by ID

Delete operation of resource: ssh-key-profile

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
name = 'name_example' # str | ID of name

try:
    # Delete ssh-key-profile by ID
    api_instance.delete_iceberg_profile_security_ssh_key_profile_by_id(name)
except ApiException as e:
    print("Exception when calling DefaultApi->delete_iceberg_profile_security_ssh_key_profile_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| ID of name | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_iceberg_profiles**
> delete_iceberg_profiles()

Delete profile by ID

Delete entire profile configuration.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()

try:
    # Delete profile by ID
    api_instance.delete_iceberg_profiles()
except ApiException as e:
    print("Exception when calling DefaultApi->delete_iceberg_profiles: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **inspect_command_rpc_table_on_device**
> inspect_command_rpc_table_on_device(command_rpc_detail)

Inspect the given iAgent table.

Inspect the given iAgent table on a device and return the results.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
command_rpc_detail = swagger_client.CommandRpc() # CommandRpc | command-rpc object

try:
    # Inspect the given iAgent table.
    api_instance.inspect_command_rpc_table_on_device(command_rpc_detail)
except ApiException as e:
    print("Exception when calling DefaultApi->inspect_command_rpc_table_on_device: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **command_rpc_detail** | [**CommandRpc**](CommandRpc.md)| command-rpc object | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_configuration_jobs**
> list[InlineResponse200] retrieve_configuration_jobs(job_id=job_id, job_status=job_status)



Return list of all the Commit Job ID's

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
job_id = 'job_id_example' # str | Id of Job (optional)
job_status = 'job_status_example' # str | Type of job (optional)

try:
    api_response = api_instance.retrieve_configuration_jobs(job_id=job_id, job_status=job_status)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->retrieve_configuration_jobs: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_id** | [**str**](.md)| Id of Job | [optional] 
 **job_status** | **str**| Type of job | [optional] 

### Return type

[**list[InlineResponse200]**](InlineResponse200.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, multipart/form-data
 - **Accept**: application/json, application/octet-stream

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_data_database_table**
> list[TableSchema] retrieve_data_database_table(device_id=device_id, device_group_name=device_group_name, network_group_name=network_group_name)

Get information about tables for a device of a device-group.

Get information about different types of tables stored for a device of a device-group.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
device_id = 'device_id_example' # str | Name of device (optional)
device_group_name = 'device_group_name_example' # str | Name of device-group (optional)
network_group_name = 'network_group_name_example' # str | Name of network-group (optional)

try:
    # Get information about tables for a device of a device-group.
    api_response = api_instance.retrieve_data_database_table(device_id=device_id, device_group_name=device_group_name, network_group_name=network_group_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->retrieve_data_database_table: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **str**| Name of device | [optional] 
 **device_group_name** | **str**| Name of device-group | [optional] 
 **network_group_name** | **str**| Name of network-group | [optional] 

### Return type

[**list[TableSchema]**](TableSchema.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, multipart/form-data
 - **Accept**: application/json, application/octet-stream

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_data_database_table_column_by_table_name**
> list[str] retrieve_data_database_table_column_by_table_name(table_name, device_id=device_id, device_group_name=device_group_name, network_group_name=network_group_name)

Get information about columns in a table.

Get information about columns in a table.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
table_name = 'table_name_example' # str | Name of table
device_id = 'device_id_example' # str | Name of device (optional)
device_group_name = 'device_group_name_example' # str | Name of device-group (optional)
network_group_name = 'network_group_name_example' # str | Name of network-group (optional)

try:
    # Get information about columns in a table.
    api_response = api_instance.retrieve_data_database_table_column_by_table_name(table_name, device_id=device_id, device_group_name=device_group_name, network_group_name=network_group_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->retrieve_data_database_table_column_by_table_name: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **table_name** | **str**| Name of table | 
 **device_id** | **str**| Name of device | [optional] 
 **device_group_name** | **str**| Name of device-group | [optional] 
 **network_group_name** | **str**| Name of network-group | [optional] 

### Return type

**list[str]**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, multipart/form-data
 - **Accept**: application/json, application/octet-stream

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_data_database_tags_by_table_name**
> list[str] retrieve_data_database_tags_by_table_name(table_name, device_id=device_id, device_group_name=device_group_name, network_group_name=network_group_name, tag=tag, where_clause=where_clause)

Get information about tags keys and values in a table.

Get information about tags keys and values in a table.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
table_name = 'table_name_example' # str | Name of table
device_id = 'device_id_example' # str | Name of device (optional)
device_group_name = 'device_group_name_example' # str | Name of device-group (optional)
network_group_name = 'network_group_name_example' # str | Name of network-group (optional)
tag = 'tag_example' # str | Tag key for which values are requested. (optional)
where_clause = 'where_clause_example' # str | Where condition to select values for the requested key. This would not be processed if there is no `tag` query parameter. eg: `tag_key1=val1 AND tag_key2=val2` (optional)

try:
    # Get information about tags keys and values in a table.
    api_response = api_instance.retrieve_data_database_tags_by_table_name(table_name, device_id=device_id, device_group_name=device_group_name, network_group_name=network_group_name, tag=tag, where_clause=where_clause)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->retrieve_data_database_tags_by_table_name: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **table_name** | **str**| Name of table | 
 **device_id** | **str**| Name of device | [optional] 
 **device_group_name** | **str**| Name of device-group | [optional] 
 **network_group_name** | **str**| Name of network-group | [optional] 
 **tag** | **str**| Tag key for which values are requested. | [optional] 
 **where_clause** | **str**| Where condition to select values for the requested key. This would not be processed if there is no &#x60;tag&#x60; query parameter. eg: &#x60;tag_key1&#x3D;val1 AND tag_key2&#x3D;val2&#x60; | [optional] 

### Return type

**list[str]**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, multipart/form-data
 - **Accept**: application/json, application/octet-stream

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_event**
> list[Event] retrieve_event(from_timestamp, device_id, to_timestamp=to_timestamp, device_group_name=device_group_name, granularity=granularity, color=color)

Get all events for a device.

Get the list of events for a device. Filtering is possible with the use of various query parameters.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
from_timestamp = '2013-10-20T19:20:30+01:00' # datetime | Starting timestamp
device_id = 'device_id_example' # str | device-id of the device for which events are requested
to_timestamp = '2013-10-20T19:20:30+01:00' # datetime | Ending timestamp (optional)
device_group_name = 'device_group_name_example' # str | Device group's device-group-name of which the device is part (optional)
granularity = 'granularity_example' # str | Granularity of query (optional)
color = 'color_example' # str | Color of events. (optional)

try:
    # Get all events for a device.
    api_response = api_instance.retrieve_event(from_timestamp, device_id, to_timestamp=to_timestamp, device_group_name=device_group_name, granularity=granularity, color=color)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->retrieve_event: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **from_timestamp** | **datetime**| Starting timestamp | 
 **device_id** | **str**| device-id of the device for which events are requested | 
 **to_timestamp** | **datetime**| Ending timestamp | [optional] 
 **device_group_name** | **str**| Device group&#39;s device-group-name of which the device is part | [optional] 
 **granularity** | **str**| Granularity of query | [optional] 
 **color** | **str**| Color of events. | [optional] 

### Return type

[**list[Event]**](Event.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, multipart/form-data
 - **Accept**: application/json, application/octet-stream

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_event_by_event_name**
> list[Event] retrieve_event_by_event_name(event_name, from_timestamp, device_id, to_timestamp=to_timestamp, device_group_name=device_group_name, granularity=granularity, color=color)

Get instances of a device event.

Get instances of a specified device event. Filtering is possible with the use of various query parameters.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
event_name = 'event_name_example' # str | Name of event
from_timestamp = '2013-10-20T19:20:30+01:00' # datetime | Starting timestamp
device_id = 'device_id_example' # str | device-id of the device for which events are requested
to_timestamp = '2013-10-20T19:20:30+01:00' # datetime | Ending timestamp (optional)
device_group_name = 'device_group_name_example' # str | device-group-name of which the device is part (optional)
granularity = 'granularity_example' # str | Granularity of query (optional)
color = 'color_example' # str | Color of events. (optional)

try:
    # Get instances of a device event.
    api_response = api_instance.retrieve_event_by_event_name(event_name, from_timestamp, device_id, to_timestamp=to_timestamp, device_group_name=device_group_name, granularity=granularity, color=color)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->retrieve_event_by_event_name: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **event_name** | **str**| Name of event | 
 **from_timestamp** | **datetime**| Starting timestamp | 
 **device_id** | **str**| device-id of the device for which events are requested | 
 **to_timestamp** | **datetime**| Ending timestamp | [optional] 
 **device_group_name** | **str**| device-group-name of which the device is part | [optional] 
 **granularity** | **str**| Granularity of query | [optional] 
 **color** | **str**| Color of events. | [optional] 

### Return type

[**list[Event]**](Event.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, multipart/form-data
 - **Accept**: application/json, application/octet-stream

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_event_by_event_name_device_group**
> list[Event] retrieve_event_by_event_name_device_group(event_name, from_timestamp, device_group_name, to_timestamp=to_timestamp, granularity=granularity, device_id=device_id, color=color)

Get instances of a device-group event.

Get instances of a specified device-group event. Filtering is possible with the use of various query parameters.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
event_name = 'event_name_example' # str | Name of event
from_timestamp = '2013-10-20T19:20:30+01:00' # datetime | Starting timestamp
device_group_name = 'device_group_name_example' # str | device_group_name of the device-group for which events are requested
to_timestamp = '2013-10-20T19:20:30+01:00' # datetime | Ending timestamp (optional)
granularity = 'granularity_example' # str | Granularity of query (optional)
device_id = ['device_id_example'] # list[str] | list of devices under a device-group to be fetched (optional)
color = 'color_example' # str | Color of events. (optional)

try:
    # Get instances of a device-group event.
    api_response = api_instance.retrieve_event_by_event_name_device_group(event_name, from_timestamp, device_group_name, to_timestamp=to_timestamp, granularity=granularity, device_id=device_id, color=color)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->retrieve_event_by_event_name_device_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **event_name** | **str**| Name of event | 
 **from_timestamp** | **datetime**| Starting timestamp | 
 **device_group_name** | **str**| device_group_name of the device-group for which events are requested | 
 **to_timestamp** | **datetime**| Ending timestamp | [optional] 
 **granularity** | **str**| Granularity of query | [optional] 
 **device_id** | [**list[str]**](str.md)| list of devices under a device-group to be fetched | [optional] 
 **color** | **str**| Color of events. | [optional] 

### Return type

[**list[Event]**](Event.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, multipart/form-data
 - **Accept**: application/json, application/octet-stream

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_event_by_event_name_network_group**
> list[Event] retrieve_event_by_event_name_network_group(event_name, from_timestamp, network_group_name, to_timestamp=to_timestamp, granularity=granularity, color=color)

Get instances of a network-group event.

Get instances of a specified network-group event. Filtering is possible with the use of various query parameters.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
event_name = 'event_name_example' # str | Name of event
from_timestamp = '2013-10-20T19:20:30+01:00' # datetime | Starting timestamp
network_group_name = 'network_group_name_example' # str | network_group_name of the network-group for which events are requested
to_timestamp = '2013-10-20T19:20:30+01:00' # datetime | Ending timestamp (optional)
granularity = 'granularity_example' # str | Granularity of query (optional)
color = 'color_example' # str | Color of events. (optional)

try:
    # Get instances of a network-group event.
    api_response = api_instance.retrieve_event_by_event_name_network_group(event_name, from_timestamp, network_group_name, to_timestamp=to_timestamp, granularity=granularity, color=color)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->retrieve_event_by_event_name_network_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **event_name** | **str**| Name of event | 
 **from_timestamp** | **datetime**| Starting timestamp | 
 **network_group_name** | **str**| network_group_name of the network-group for which events are requested | 
 **to_timestamp** | **datetime**| Ending timestamp | [optional] 
 **granularity** | **str**| Granularity of query | [optional] 
 **color** | **str**| Color of events. | [optional] 

### Return type

[**list[Event]**](Event.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, multipart/form-data
 - **Accept**: application/json, application/octet-stream

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_event_device_group**
> list[Event] retrieve_event_device_group(from_timestamp, device_group_name, to_timestamp=to_timestamp, granularity=granularity, device_id=device_id, color=color)

Get all events for a device-group.

Get the list of events for a device-group. Filtering is possible with the use of various query parameters.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
from_timestamp = '2013-10-20T19:20:30+01:00' # datetime | Starting timestamp
device_group_name = 'device_group_name_example' # str | device_group_name of the device-group for which events are requested
to_timestamp = '2013-10-20T19:20:30+01:00' # datetime | Ending timestamp (optional)
granularity = 'granularity_example' # str | Granularity of query (optional)
device_id = ['device_id_example'] # list[str] | list of devices under a device-group to be fetched (optional)
color = 'color_example' # str | Color of events. (optional)

try:
    # Get all events for a device-group.
    api_response = api_instance.retrieve_event_device_group(from_timestamp, device_group_name, to_timestamp=to_timestamp, granularity=granularity, device_id=device_id, color=color)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->retrieve_event_device_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **from_timestamp** | **datetime**| Starting timestamp | 
 **device_group_name** | **str**| device_group_name of the device-group for which events are requested | 
 **to_timestamp** | **datetime**| Ending timestamp | [optional] 
 **granularity** | **str**| Granularity of query | [optional] 
 **device_id** | [**list[str]**](str.md)| list of devices under a device-group to be fetched | [optional] 
 **color** | **str**| Color of events. | [optional] 

### Return type

[**list[Event]**](Event.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, multipart/form-data
 - **Accept**: application/json, application/octet-stream

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_event_network_group**
> list[Event] retrieve_event_network_group(from_timestamp, network_group_name, to_timestamp=to_timestamp, granularity=granularity, color=color)

Get all events for a network-group.

Get the list of events for a network-group. Filtering is possible with the use of various query parameters.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
from_timestamp = '2013-10-20T19:20:30+01:00' # datetime | Starting timestamp
network_group_name = 'network_group_name_example' # str | network_group_name of the network-group for which events are requested
to_timestamp = '2013-10-20T19:20:30+01:00' # datetime | Ending timestamp (optional)
granularity = 'granularity_example' # str | Granularity of query (optional)
color = 'color_example' # str | Color of events. (optional)

try:
    # Get all events for a network-group.
    api_response = api_instance.retrieve_event_network_group(from_timestamp, network_group_name, to_timestamp=to_timestamp, granularity=granularity, color=color)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->retrieve_event_network_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **from_timestamp** | **datetime**| Starting timestamp | 
 **network_group_name** | **str**| network_group_name of the network-group for which events are requested | 
 **to_timestamp** | **datetime**| Ending timestamp | [optional] 
 **granularity** | **str**| Granularity of query | [optional] 
 **color** | **str**| Color of events. | [optional] 

### Return type

[**list[Event]**](Event.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, multipart/form-data
 - **Accept**: application/json, application/octet-stream

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_files_helper_files**
> list[str] retrieve_files_helper_files(input_path=input_path)

Get all helper-file names.

Get a list of all the helper-file file-names.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
input_path = 'input_path_example' # str | Input path (optional)

try:
    # Get all helper-file names.
    api_response = api_instance.retrieve_files_helper_files(input_path=input_path)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->retrieve_files_helper_files: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **input_path** | **str**| Input path | [optional] 

### Return type

**list[str]**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, multipart/form-data
 - **Accept**: application/json, application/octet-stream

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_files_helper_files_by_file_name**
> file retrieve_files_helper_files_by_file_name(file_name, input_path=input_path)

Download a helper-file.

Download the specified helper-file.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
file_name = 'file_name_example' # str | File name
input_path = 'input_path_example' # str | Input path (optional)

try:
    # Download a helper-file.
    api_response = api_instance.retrieve_files_helper_files_by_file_name(file_name, input_path=input_path)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->retrieve_files_helper_files_by_file_name: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file_name** | **str**| File name | 
 **input_path** | **str**| Input path | [optional] 

### Return type

[**file**](file.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, multipart/form-data
 - **Accept**: application/octet-stream, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_health_all**
> HealthSchema retrieve_health_all()

Return a dict with health of devices in device groups and network groups

Returns health of network-groups and devices in device-groups

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()

try:
    # Return a dict with health of devices in device groups and network groups
    api_response = api_instance.retrieve_health_all()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->retrieve_health_all: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**HealthSchema**](HealthSchema.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, multipart/form-data
 - **Accept**: application/json, application/octet-stream

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_health_tree_by_device_group**
> DeviceGroupHealthTree retrieve_health_tree_by_device_group(device_group_name, timestamp=timestamp, tolerance=tolerance, device=device)

Get device-group health-tree.

Get health-tree of a specified device-group.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
device_group_name = 'device_group_name_example' # str | `device-group-name` of device-group
timestamp = '2013-10-20T19:20:30+01:00' # datetime | Timestamp at which health tree is requested. If not specified, current server timestamp is used. (optional)
tolerance = 789 # int | Timestamp tolerance in seconds. With this option, health-tree will contain latest data between `timestamp-2*tolerance` and `timestamp`. Default value is `2*frequency` where `frequency` is extracted from `trigger`. (optional)
device = ['device_example'] # list[str] | list of devices under a device-group to be fetched (optional)

try:
    # Get device-group health-tree.
    api_response = api_instance.retrieve_health_tree_by_device_group(device_group_name, timestamp=timestamp, tolerance=tolerance, device=device)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->retrieve_health_tree_by_device_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_group_name** | **str**| &#x60;device-group-name&#x60; of device-group | 
 **timestamp** | **datetime**| Timestamp at which health tree is requested. If not specified, current server timestamp is used. | [optional] 
 **tolerance** | **int**| Timestamp tolerance in seconds. With this option, health-tree will contain latest data between &#x60;timestamp-2*tolerance&#x60; and &#x60;timestamp&#x60;. Default value is &#x60;2*frequency&#x60; where &#x60;frequency&#x60; is extracted from &#x60;trigger&#x60;. | [optional] 
 **device** | [**list[str]**](str.md)| list of devices under a device-group to be fetched | [optional] 

### Return type

[**DeviceGroupHealthTree**](DeviceGroupHealthTree.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, multipart/form-data
 - **Accept**: application/json, application/octet-stream

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_health_tree_by_id**
> DeviceHealthTree retrieve_health_tree_by_id(device_id, timestamp=timestamp, tolerance=tolerance)

Return a device's health-tree.

Return health-tree of a specified device identified by `device-id`.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
device_id = 'device_id_example' # str | `device-id` of device
timestamp = '2013-10-20T19:20:30+01:00' # datetime | Timestamp at which health tree is requested. If not specified, current server timestamp is used. (optional)
tolerance = 789 # int | Timestamp tolerance in seconds. With this option, health-tree will contain latest data between `timestamp-2*tolerance` and `timestamp`. Default value is `2*frequency` where `frequency` is extracted from `trigger`. (optional)

try:
    # Return a device's health-tree.
    api_response = api_instance.retrieve_health_tree_by_id(device_id, timestamp=timestamp, tolerance=tolerance)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->retrieve_health_tree_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **str**| &#x60;device-id&#x60; of device | 
 **timestamp** | **datetime**| Timestamp at which health tree is requested. If not specified, current server timestamp is used. | [optional] 
 **tolerance** | **int**| Timestamp tolerance in seconds. With this option, health-tree will contain latest data between &#x60;timestamp-2*tolerance&#x60; and &#x60;timestamp&#x60;. Default value is &#x60;2*frequency&#x60; where &#x60;frequency&#x60; is extracted from &#x60;trigger&#x60;. | [optional] 

### Return type

[**DeviceHealthTree**](DeviceHealthTree.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, multipart/form-data
 - **Accept**: application/json, application/octet-stream

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_health_tree_by_network_group**
> NetworkHealthTree retrieve_health_tree_by_network_group(network_group_name, timestamp=timestamp, tolerance=tolerance)

Get network-group health-tree.

Get health-tree of a specified network-group.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
network_group_name = 'network_group_name_example' # str | `network-group-name` of network-group
timestamp = '2013-10-20T19:20:30+01:00' # datetime | Timestamp at which health tree is requested. If not specified, current server timestamp is used. (optional)
tolerance = 789 # int | Timestamp tolerance in seconds. With this option, health-tree will contain latest data between `timestamp-2*tolerance` and `timestamp`. Default value is `2*frequency` where `frequency` is extracted from `trigger`. (optional)

try:
    # Get network-group health-tree.
    api_response = api_instance.retrieve_health_tree_by_network_group(network_group_name, timestamp=timestamp, tolerance=tolerance)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->retrieve_health_tree_by_network_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **network_group_name** | **str**| &#x60;network-group-name&#x60; of network-group | 
 **timestamp** | **datetime**| Timestamp at which health tree is requested. If not specified, current server timestamp is used. | [optional] 
 **tolerance** | **int**| Timestamp tolerance in seconds. With this option, health-tree will contain latest data between &#x60;timestamp-2*tolerance&#x60; and &#x60;timestamp&#x60;. Default value is &#x60;2*frequency&#x60; where &#x60;frequency&#x60; is extracted from &#x60;trigger&#x60;. | [optional] 

### Return type

[**NetworkHealthTree**](NetworkHealthTree.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, multipart/form-data
 - **Accept**: application/json, application/octet-stream

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_iceberg_profile_data_summarization_raw_by_id**
> RawSchema retrieve_iceberg_profile_data_summarization_raw_by_id(name, working=working)

Retrieve raw-data-summarization by ID

Retrieve operation of resource: raw-data-summarization

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
name = 'name_example' # str | ID of name
working = true # bool | true queries undeployed configuration (optional)

try:
    # Retrieve raw-data-summarization by ID
    api_response = api_instance.retrieve_iceberg_profile_data_summarization_raw_by_id(name, working=working)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->retrieve_iceberg_profile_data_summarization_raw_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| ID of name | 
 **working** | **bool**| true queries undeployed configuration | [optional] 

### Return type

[**RawSchema**](RawSchema.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_iceberg_profile_data_summarizations_raw**
> RawSchema retrieve_iceberg_profile_data_summarizations_raw(working=working)

Retrieve raw-data-summarization

Retrieve operation of resource: raw-data-summarization

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
working = true # bool | true queries undeployed configuration (optional)

try:
    # Retrieve raw-data-summarization
    api_response = api_instance.retrieve_iceberg_profile_data_summarizations_raw(working=working)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->retrieve_iceberg_profile_data_summarizations_raw: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **working** | **bool**| true queries undeployed configuration | [optional] 

### Return type

[**RawSchema**](RawSchema.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_iceberg_profile_security_ca_profile_by_id**
> CaProfileSchema retrieve_iceberg_profile_security_ca_profile_by_id(name, working=working)

Retrieve ca-profile by ID

Retrieve operation of resource: ca-profile

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
name = 'name_example' # str | ID of name
working = true # bool | true queries undeployed configuration (optional)

try:
    # Retrieve ca-profile by ID
    api_response = api_instance.retrieve_iceberg_profile_security_ca_profile_by_id(name, working=working)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->retrieve_iceberg_profile_security_ca_profile_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| ID of name | 
 **working** | **bool**| true queries undeployed configuration | [optional] 

### Return type

[**CaProfileSchema**](CaProfileSchema.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_iceberg_profile_security_ca_profiles**
> list[str] retrieve_iceberg_profile_security_ca_profiles(working=working)

Retrieve ca-profile

Retrieve entire ca-profiles configuration.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
working = true # bool | true queries undeployed configuration (optional)

try:
    # Retrieve ca-profile
    api_response = api_instance.retrieve_iceberg_profile_security_ca_profiles(working=working)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->retrieve_iceberg_profile_security_ca_profiles: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **working** | **bool**| true queries undeployed configuration | [optional] 

### Return type

**list[str]**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_iceberg_profile_security_local_certificate_by_id**
> LocalCertificateSchema retrieve_iceberg_profile_security_local_certificate_by_id(name, working=working)

Retrieve local-certificate by ID

Retrieve operation of resource: local-certificate

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
name = 'name_example' # str | ID of name
working = true # bool | true queries undeployed configuration (optional)

try:
    # Retrieve local-certificate by ID
    api_response = api_instance.retrieve_iceberg_profile_security_local_certificate_by_id(name, working=working)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->retrieve_iceberg_profile_security_local_certificate_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| ID of name | 
 **working** | **bool**| true queries undeployed configuration | [optional] 

### Return type

[**LocalCertificateSchema**](LocalCertificateSchema.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_iceberg_profile_security_local_certificates**
> list[str] retrieve_iceberg_profile_security_local_certificates(working=working)

Retrieve local-certificate

Retrieve entire local-certificates configuration.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
working = true # bool | true queries undeployed configuration (optional)

try:
    # Retrieve local-certificate
    api_response = api_instance.retrieve_iceberg_profile_security_local_certificates(working=working)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->retrieve_iceberg_profile_security_local_certificates: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **working** | **bool**| true queries undeployed configuration | [optional] 

### Return type

**list[str]**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_iceberg_profile_security_ssh_key_profile_by_id**
> SshKeyProfileSchema retrieve_iceberg_profile_security_ssh_key_profile_by_id(name, working=working)

Retrieve ssh-key-profile by ID

Retrieve operation of resource: ssh-key-profile

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
name = 'name_example' # str | ID of name
working = true # bool | true queries undeployed configuration (optional)

try:
    # Retrieve ssh-key-profile by ID
    api_response = api_instance.retrieve_iceberg_profile_security_ssh_key_profile_by_id(name, working=working)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->retrieve_iceberg_profile_security_ssh_key_profile_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| ID of name | 
 **working** | **bool**| true queries undeployed configuration | [optional] 

### Return type

[**SshKeyProfileSchema**](SshKeyProfileSchema.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_iceberg_profile_security_ssh_key_profiles**
> list[str] retrieve_iceberg_profile_security_ssh_key_profiles(working=working)

Retrieve ssh-key-profile

Retrieve entire ssh-key-profiles configuration.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
working = true # bool | true queries undeployed configuration (optional)

try:
    # Retrieve ssh-key-profile
    api_response = api_instance.retrieve_iceberg_profile_security_ssh_key_profiles(working=working)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->retrieve_iceberg_profile_security_ssh_key_profiles: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **working** | **bool**| true queries undeployed configuration | [optional] 

### Return type

**list[str]**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_iceberg_profiles**
> ProfilesSchema retrieve_iceberg_profiles(working=working)

Retrieve profile

Retrieve entire profile configuration.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
working = true # bool | true queries undeployed configuration (optional)

try:
    # Retrieve profile
    api_response = api_instance.retrieve_iceberg_profiles(working=working)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->retrieve_iceberg_profiles: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **working** | **bool**| true queries undeployed configuration | [optional] 

### Return type

[**ProfilesSchema**](ProfilesSchema.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_sensors**
> list[str] retrieve_sensors(sensor_type, sensor_name=sensor_name, depth=depth, append=append, snmp_table=snmp_table)

List all OpenConfig sensors.

Get a list of all the sensors for the filters provided. Filtering is possible with the use of query parameters. If you have a sensor `/1/2/3/4/5/6/` and `sensor_name=/1`and `depth=3`, the result would be `/2/3/4`. If you use `append=true`, then the result would be `/1/2/3/4`.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
sensor_type = 'sensor_type_example' # str | Sensor type
sensor_name = 'sensor_name_example' # str | Sensor name prefix. (optional)
depth = 56 # int | Relative depth to the `sensor_name`. (optional)
append = true # bool | Returns full path of the sensor. (optional)
snmp_table = 'snmp_table_example' # str | Returns list of all the columns for the particular snmp_table (optional)

try:
    # List all OpenConfig sensors.
    api_response = api_instance.retrieve_sensors(sensor_type, sensor_name=sensor_name, depth=depth, append=append, snmp_table=snmp_table)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->retrieve_sensors: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sensor_type** | **str**| Sensor type | 
 **sensor_name** | **str**| Sensor name prefix. | [optional] 
 **depth** | **int**| Relative depth to the &#x60;sensor_name&#x60;. | [optional] 
 **append** | **bool**| Returns full path of the sensor. | [optional] 
 **snmp_table** | **str**| Returns list of all the columns for the particular snmp_table | [optional] 

### Return type

**list[str]**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, multipart/form-data
 - **Accept**: application/json, application/octet-stream

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_iceberg_profile_data_summarization_raw_by_id**
> update_iceberg_profile_data_summarization_raw_by_id(name, raw_data_summarization)

Update raw-data-summarization by ID

Update operation of resource: raw-data-summarization

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
name = 'name_example' # str | ID of name
raw_data_summarization = swagger_client.RawSchema() # RawSchema | raw_data_summarizationbody object

try:
    # Update raw-data-summarization by ID
    api_instance.update_iceberg_profile_data_summarization_raw_by_id(name, raw_data_summarization)
except ApiException as e:
    print("Exception when calling DefaultApi->update_iceberg_profile_data_summarization_raw_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| ID of name | 
 **raw_data_summarization** | [**RawSchema**](RawSchema.md)| raw_data_summarizationbody object | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_iceberg_profile_security_ca_profile_by_id**
> update_iceberg_profile_security_ca_profile_by_id(name, ca_profile)

Update ca-profile by ID

Update operation of resource: ca-profile

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
name = 'name_example' # str | ID of name
ca_profile = swagger_client.CaProfileSchema() # CaProfileSchema | ca_profilebody object

try:
    # Update ca-profile by ID
    api_instance.update_iceberg_profile_security_ca_profile_by_id(name, ca_profile)
except ApiException as e:
    print("Exception when calling DefaultApi->update_iceberg_profile_security_ca_profile_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| ID of name | 
 **ca_profile** | [**CaProfileSchema**](CaProfileSchema.md)| ca_profilebody object | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_iceberg_profile_security_local_certificate_by_id**
> update_iceberg_profile_security_local_certificate_by_id(name, local_certificate)

Update local-certificate by ID

Update operation of resource: local-certificate

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
name = 'name_example' # str | ID of name
local_certificate = swagger_client.LocalCertificateSchema() # LocalCertificateSchema | local_certificatebody object

try:
    # Update local-certificate by ID
    api_instance.update_iceberg_profile_security_local_certificate_by_id(name, local_certificate)
except ApiException as e:
    print("Exception when calling DefaultApi->update_iceberg_profile_security_local_certificate_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| ID of name | 
 **local_certificate** | [**LocalCertificateSchema**](LocalCertificateSchema.md)| local_certificatebody object | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_iceberg_profile_security_ssh_key_profile_by_id**
> update_iceberg_profile_security_ssh_key_profile_by_id(name, ssh_key_profile)

Update ssh-key-profile by ID

Update operation of resource: ssh-key-profile

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
name = 'name_example' # str | ID of name
ssh_key_profile = swagger_client.SshKeyProfileSchema() # SshKeyProfileSchema | ssh_key_profilebody object

try:
    # Update ssh-key-profile by ID
    api_instance.update_iceberg_profile_security_ssh_key_profile_by_id(name, ssh_key_profile)
except ApiException as e:
    print("Exception when calling DefaultApi->update_iceberg_profile_security_ssh_key_profile_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| ID of name | 
 **ssh_key_profile** | [**SshKeyProfileSchema**](SshKeyProfileSchema.md)| ssh_key_profilebody object | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_iceberg_profiles**
> update_iceberg_profiles(profile)

Update profile by ID

Update entire profile configuration.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
profile = swagger_client.ProfilesSchema() # ProfilesSchema | profilebody object

try:
    # Update profile by ID
    api_instance.update_iceberg_profiles(profile)
except ApiException as e:
    print("Exception when calling DefaultApi->update_iceberg_profiles: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **profile** | [**ProfilesSchema**](ProfilesSchema.md)| profilebody object | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

