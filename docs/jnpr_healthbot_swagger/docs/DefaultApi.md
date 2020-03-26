# swagger_client.DefaultApi

All URIs are relative to *http://api-server/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**backup_helper_files**](DefaultApi.md#backup_helper_files) | **GET** /files/helper-files/backup/ | Download the tar file containing all helper files.
[**create_files_certificates_by_file_name**](DefaultApi.md#create_files_certificates_by_file_name) | **POST** /files/certificates/{file_name}/ | Upload a certificate file.
[**create_files_helper_files_by_file_name**](DefaultApi.md#create_files_helper_files_by_file_name) | **POST** /files/helper-files/{file_name}/ | Upload a helper-file.
[**create_healthbot_ingest_settings_byoi_custom_plugin_by_id**](DefaultApi.md#create_healthbot_ingest_settings_byoi_custom_plugin_by_id) | **POST** /ingest-settings/byoi/custom-plugin/{name}/ | Create custom-plugin by ID
[**create_healthbot_ingest_settings_byoi_default_plugin_tlive_kafka_by_id**](DefaultApi.md#create_healthbot_ingest_settings_byoi_default_plugin_tlive_kafka_by_id) | **POST** /ingest-settings/byoi/default-plugin/tlive-kafka-oc/{name}/ | Create tlive-kafka-oc by ID
[**create_healthbot_ingest_settings_byoi_ingest_mapping_by_id**](DefaultApi.md#create_healthbot_ingest_settings_byoi_ingest_mapping_by_id) | **POST** /ingest-settings/byoi/ingest-mapping/{name}/ | Create ingest-mapping by ID
[**create_healthbot_ingest_settings_frequency_profile_by_id**](DefaultApi.md#create_healthbot_ingest_settings_frequency_profile_by_id) | **POST** /ingest-settings/frequency-profile/{name}/ | Create frequency-profile by ID
[**create_healthbot_system_time_series_database_time_series_database_by_id**](DefaultApi.md#create_healthbot_system_time_series_database_time_series_database_by_id) | **POST** /system/tsdb/ | Create time-series-database by ID
[**create_iceberg_ingest_settings**](DefaultApi.md#create_iceberg_ingest_settings) | **POST** /ingest-settings/ | Create ingest-settings by ID
[**create_iceberg_ingest_settings_flow**](DefaultApi.md#create_iceberg_ingest_settings_flow) | **POST** /ingest-settings/flow/ | Create flow by ID
[**create_iceberg_ingest_settings_flow_template_by_id**](DefaultApi.md#create_iceberg_ingest_settings_flow_template_by_id) | **POST** /ingest-settings/flow/template/{name}/ | Create template by ID
[**create_iceberg_ingest_settings_syslog**](DefaultApi.md#create_iceberg_ingest_settings_syslog) | **POST** /ingest-settings/syslog/ | Create syslog by ID
[**create_iceberg_ingest_settings_syslog_pattern_by_id**](DefaultApi.md#create_iceberg_ingest_settings_syslog_pattern_by_id) | **POST** /ingest-settings/syslog/pattern/{name}/ | Create pattern by ID
[**create_iceberg_ingest_settings_syslog_pattern_set_by_id**](DefaultApi.md#create_iceberg_ingest_settings_syslog_pattern_set_by_id) | **POST** /ingest-settings/syslog/pattern-set/{name}/ | Create pattern-set by ID
[**create_iceberg_profile_data_summarization_raw_by_id**](DefaultApi.md#create_iceberg_profile_data_summarization_raw_by_id) | **POST** /profile/data-summarization/raw/{name}/ | Create raw-data-summarization by ID
[**create_iceberg_profile_security_ca_profile_by_id**](DefaultApi.md#create_iceberg_profile_security_ca_profile_by_id) | **POST** /profile/security/ca-profile/{name}/ | Create ca-profile by ID
[**create_iceberg_profile_security_local_certificate_by_id**](DefaultApi.md#create_iceberg_profile_security_local_certificate_by_id) | **POST** /profile/security/local-certificate/{name}/ | Create local-certificate by ID
[**create_iceberg_profile_security_ssh_key_profile_by_id**](DefaultApi.md#create_iceberg_profile_security_ssh_key_profile_by_id) | **POST** /profile/security/ssh-key-profile/{name}/ | Create ssh-key-profile by ID
[**create_iceberg_profiles**](DefaultApi.md#create_iceberg_profiles) | **POST** /profiles/ | Create profile by ID
[**delete_files_certificates_by_file_name**](DefaultApi.md#delete_files_certificates_by_file_name) | **DELETE** /files/certificates/{file_name}/ | Delete a certificate-file.
[**delete_files_helper_files_by_file_name**](DefaultApi.md#delete_files_helper_files_by_file_name) | **DELETE** /files/helper-files/{file_name}/ | Delete a helper-file.
[**delete_healthbot_ingest_settings_byoi_custom_plugin_by_id**](DefaultApi.md#delete_healthbot_ingest_settings_byoi_custom_plugin_by_id) | **DELETE** /ingest-settings/byoi/custom-plugin/{name}/ | Delete custom-plugin by ID
[**delete_healthbot_ingest_settings_byoi_default_plugin_tlive_kafka_by_id**](DefaultApi.md#delete_healthbot_ingest_settings_byoi_default_plugin_tlive_kafka_by_id) | **DELETE** /ingest-settings/byoi/default-plugin/tlive-kafka-oc/{name}/ | Delete tlive-kafka-oc by ID
[**delete_healthbot_ingest_settings_byoi_ingest_mapping_by_id**](DefaultApi.md#delete_healthbot_ingest_settings_byoi_ingest_mapping_by_id) | **DELETE** /ingest-settings/byoi/ingest-mapping/{name}/ | Delete ingest-mapping by ID
[**delete_healthbot_ingest_settings_frequency_profile_by_id**](DefaultApi.md#delete_healthbot_ingest_settings_frequency_profile_by_id) | **DELETE** /ingest-settings/frequency-profile/{name}/ | Delete frequency-profile by ID
[**delete_healthbot_system_time_series_database_time_series_database_by_id**](DefaultApi.md#delete_healthbot_system_time_series_database_time_series_database_by_id) | **DELETE** /system/tsdb/ | Delete time-series-database
[**delete_iceberg_ingest_settings**](DefaultApi.md#delete_iceberg_ingest_settings) | **DELETE** /ingest-settings/ | Delete ingest-settings by ID
[**delete_iceberg_ingest_settings_flow**](DefaultApi.md#delete_iceberg_ingest_settings_flow) | **DELETE** /ingest-settings/flow/ | Delete flow by ID
[**delete_iceberg_ingest_settings_flow_template_by_id**](DefaultApi.md#delete_iceberg_ingest_settings_flow_template_by_id) | **DELETE** /ingest-settings/flow/template/{name}/ | Delete template by ID
[**delete_iceberg_ingest_settings_syslog**](DefaultApi.md#delete_iceberg_ingest_settings_syslog) | **DELETE** /ingest-settings/syslog/ | Delete syslog by ID
[**delete_iceberg_ingest_settings_syslog_pattern_by_id**](DefaultApi.md#delete_iceberg_ingest_settings_syslog_pattern_by_id) | **DELETE** /ingest-settings/syslog/pattern/{name}/ | Delete pattern by ID
[**delete_iceberg_ingest_settings_syslog_pattern_set_by_id**](DefaultApi.md#delete_iceberg_ingest_settings_syslog_pattern_set_by_id) | **DELETE** /ingest-settings/syslog/pattern-set/{name}/ | Delete pattern-set by ID
[**delete_iceberg_profile_data_summarization_raw_by_id**](DefaultApi.md#delete_iceberg_profile_data_summarization_raw_by_id) | **DELETE** /profile/data-summarization/raw/{name}/ | Delete raw-data-summarization by ID
[**delete_iceberg_profile_security_ca_profile_by_id**](DefaultApi.md#delete_iceberg_profile_security_ca_profile_by_id) | **DELETE** /profile/security/ca-profile/{name}/ | Delete ca-profile by ID
[**delete_iceberg_profile_security_local_certificate_by_id**](DefaultApi.md#delete_iceberg_profile_security_local_certificate_by_id) | **DELETE** /profile/security/local-certificate/{name}/ | Delete local-certificate by ID
[**delete_iceberg_profile_security_ssh_key_profile_by_id**](DefaultApi.md#delete_iceberg_profile_security_ssh_key_profile_by_id) | **DELETE** /profile/security/ssh-key-profile/{name}/ | Delete ssh-key-profile by ID
[**delete_iceberg_profiles**](DefaultApi.md#delete_iceberg_profiles) | **DELETE** /profiles/ | Delete profile by ID
[**inspect_command_rpc_table_on_device**](DefaultApi.md#inspect_command_rpc_table_on_device) | **POST** /inspect/command-rpc/table/ | Inspect the given iAgent table.
[**restore_helper_files**](DefaultApi.md#restore_helper_files) | **POST** /files/helper-files/backup/ | Upload a helper-file.
[**retrieve_configuration_jobs**](DefaultApi.md#retrieve_configuration_jobs) | **GET** /configuration/jobs/ | 
[**retrieve_data_database_table**](DefaultApi.md#retrieve_data_database_table) | **GET** /data/database/table/ | Get information about tables for a device of a device-group.
[**retrieve_data_database_table_column_by_table_name**](DefaultApi.md#retrieve_data_database_table_column_by_table_name) | **GET** /data/database/table/column/ | Get information about columns in a table.
[**retrieve_data_database_tags_by_table_name**](DefaultApi.md#retrieve_data_database_tags_by_table_name) | **GET** /data/database/table/tags/ | Get information about tags keys and values in a table.
[**retrieve_debug_jobs**](DefaultApi.md#retrieve_debug_jobs) | **GET** /debug/jobs/ | 
[**retrieve_event**](DefaultApi.md#retrieve_event) | **GET** /event/ | Get all events for a device.
[**retrieve_event_by_event_name**](DefaultApi.md#retrieve_event_by_event_name) | **GET** /event/{event_name}/ | Get instances of a device event.
[**retrieve_event_by_event_name_device_group**](DefaultApi.md#retrieve_event_by_event_name_device_group) | **GET** /event/device-group/{event_name}/ | Get instances of a device-group event.
[**retrieve_event_by_event_name_network_group**](DefaultApi.md#retrieve_event_by_event_name_network_group) | **GET** /event/network-group/{event_name}/ | Get instances of a network-group event.
[**retrieve_event_device_group**](DefaultApi.md#retrieve_event_device_group) | **GET** /event/device-group/ | Get all events for a device-group.
[**retrieve_event_network_group**](DefaultApi.md#retrieve_event_network_group) | **GET** /event/network-group/ | Get all events for a network-group.
[**retrieve_events**](DefaultApi.md#retrieve_events) | **GET** /events/ | Get all events.
[**retrieve_files_certificates_by_file_name**](DefaultApi.md#retrieve_files_certificates_by_file_name) | **GET** /files/certificates/{file_name}/ | Download a certificate-file.
[**retrieve_files_helper_files**](DefaultApi.md#retrieve_files_helper_files) | **GET** /files/helper-files/ | Get all helper-file names.
[**retrieve_files_helper_files_by_file_name**](DefaultApi.md#retrieve_files_helper_files_by_file_name) | **GET** /files/helper-files/{file_name}/ | Download a helper-file.
[**retrieve_health_all**](DefaultApi.md#retrieve_health_all) | **GET** /health/ | Return a dict with health of devices in device groups and network groups
[**retrieve_health_tree_by_device_group**](DefaultApi.md#retrieve_health_tree_by_device_group) | **GET** /health-tree/device-group/{device_group_name}/ | Get device-group health-tree.
[**retrieve_health_tree_by_id**](DefaultApi.md#retrieve_health_tree_by_id) | **GET** /health-tree/{device_id}/ | Return a device&#39;s health-tree.
[**retrieve_health_tree_by_network_group**](DefaultApi.md#retrieve_health_tree_by_network_group) | **GET** /health-tree/network-group/{network_group_name}/ | Get network-group health-tree.
[**retrieve_healthbot_ingest_settings_byoi_custom_plugin_by_id**](DefaultApi.md#retrieve_healthbot_ingest_settings_byoi_custom_plugin_by_id) | **GET** /ingest-settings/byoi/custom-plugin/{name}/ | Retrieve custom-plugin by ID
[**retrieve_healthbot_ingest_settings_byoi_custom_plugins**](DefaultApi.md#retrieve_healthbot_ingest_settings_byoi_custom_plugins) | **GET** /ingest-settings/byoi/custom-plugins/ | Retrieve custom-plugin by ID
[**retrieve_healthbot_ingest_settings_byoi_default_plugin_tlive_kafka_by_id**](DefaultApi.md#retrieve_healthbot_ingest_settings_byoi_default_plugin_tlive_kafka_by_id) | **GET** /ingest-settings/byoi/default-plugin/tlive-kafka-oc/{name}/ | Retrieve tlive-kafka-oc by ID
[**retrieve_healthbot_ingest_settings_byoi_default_plugin_tlive_kafkas**](DefaultApi.md#retrieve_healthbot_ingest_settings_byoi_default_plugin_tlive_kafkas) | **GET** /ingest-settings/byoi/default-plugin/tlive-kafka-ocs/ | Retrieve tlive-kafka-oc
[**retrieve_healthbot_ingest_settings_byoi_ingest_mapping_by_id**](DefaultApi.md#retrieve_healthbot_ingest_settings_byoi_ingest_mapping_by_id) | **GET** /ingest-settings/byoi/ingest-mapping/{name}/ | Retrieve ingest-mapping by ID
[**retrieve_healthbot_ingest_settings_byoi_ingest_mappings**](DefaultApi.md#retrieve_healthbot_ingest_settings_byoi_ingest_mappings) | **GET** /ingest-settings/byoi/ingest-mappings/ | Retrieve ingest-mapping
[**retrieve_healthbot_ingest_settings_frequency_profile**](DefaultApi.md#retrieve_healthbot_ingest_settings_frequency_profile) | **GET** /ingest-settings/frequency-profiles/ | Retrieve frequency-profile
[**retrieve_healthbot_ingest_settings_frequency_profile_by_id**](DefaultApi.md#retrieve_healthbot_ingest_settings_frequency_profile_by_id) | **GET** /ingest-settings/frequency-profile/{name}/ | Retrieve frequency-profile by ID
[**retrieve_healthbot_system_time_series_database_time_series_database**](DefaultApi.md#retrieve_healthbot_system_time_series_database_time_series_database) | **GET** /system/tsdb/ | Retrieve time-series-database
[**retrieve_iceberg_ingest_settings**](DefaultApi.md#retrieve_iceberg_ingest_settings) | **GET** /ingest-settings/ | Retrieve ingest-settings
[**retrieve_iceberg_ingest_settings_flow**](DefaultApi.md#retrieve_iceberg_ingest_settings_flow) | **GET** /ingest-settings/flow/ | Retrieve flow
[**retrieve_iceberg_ingest_settings_flow_template_by_id**](DefaultApi.md#retrieve_iceberg_ingest_settings_flow_template_by_id) | **GET** /ingest-settings/flow/template/{name}/ | Retrieve template by ID
[**retrieve_iceberg_ingest_settings_flow_template_ids**](DefaultApi.md#retrieve_iceberg_ingest_settings_flow_template_ids) | **GET** /ingest-settings/flow/template/ | Retrieve template
[**retrieve_iceberg_ingest_settings_syslog**](DefaultApi.md#retrieve_iceberg_ingest_settings_syslog) | **GET** /ingest-settings/syslog/ | Retrieve syslog
[**retrieve_iceberg_ingest_settings_syslog_pattern_by_id**](DefaultApi.md#retrieve_iceberg_ingest_settings_syslog_pattern_by_id) | **GET** /ingest-settings/syslog/pattern/{name}/ | Retrieve pattern by ID
[**retrieve_iceberg_ingest_settings_syslog_pattern_ids**](DefaultApi.md#retrieve_iceberg_ingest_settings_syslog_pattern_ids) | **GET** /ingest-settings/syslog/pattern/ | Retrieve pattern
[**retrieve_iceberg_ingest_settings_syslog_pattern_set_by_id**](DefaultApi.md#retrieve_iceberg_ingest_settings_syslog_pattern_set_by_id) | **GET** /ingest-settings/syslog/pattern-set/{name}/ | Retrieve pattern-set by ID
[**retrieve_iceberg_ingest_settings_syslog_pattern_set_ids**](DefaultApi.md#retrieve_iceberg_ingest_settings_syslog_pattern_set_ids) | **GET** /ingest-settings/syslog/pattern-set/ | Retrieve pattern-set
[**retrieve_iceberg_ingest_settings_syslog_pattern_sets**](DefaultApi.md#retrieve_iceberg_ingest_settings_syslog_pattern_sets) | **GET** /ingest-settings/syslog/pattern-sets/ | Retrieve pattern-set by ID
[**retrieve_iceberg_ingest_settings_syslog_patterns**](DefaultApi.md#retrieve_iceberg_ingest_settings_syslog_patterns) | **GET** /ingest-settings/syslog/patterns/ | Retrieve pattern by ID
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
[**update_healthbot_ingest_settings_byoi_custom_plugin_by_id**](DefaultApi.md#update_healthbot_ingest_settings_byoi_custom_plugin_by_id) | **PUT** /ingest-settings/byoi/custom-plugin/{name}/ | Update custom-plugin by ID
[**update_healthbot_ingest_settings_byoi_default_plugin_tlive_kafka_by_id**](DefaultApi.md#update_healthbot_ingest_settings_byoi_default_plugin_tlive_kafka_by_id) | **PUT** /ingest-settings/byoi/default-plugin/tlive-kafka-oc/{name}/ | Update tlive-kafka-oc by ID
[**update_healthbot_ingest_settings_byoi_ingest_mapping_by_id**](DefaultApi.md#update_healthbot_ingest_settings_byoi_ingest_mapping_by_id) | **PUT** /ingest-settings/byoi/ingest-mapping/{name}/ | Update ingest-mapping by ID
[**update_healthbot_ingest_settings_frequency_profile_by_id**](DefaultApi.md#update_healthbot_ingest_settings_frequency_profile_by_id) | **PUT** /ingest-settings/frequency-profile/{name}/ | Update frequency-profile by ID
[**update_healthbot_system_time_series_database_time_series_database_by_id**](DefaultApi.md#update_healthbot_system_time_series_database_time_series_database_by_id) | **PUT** /system/tsdb/ | Update time-series-database by ID
[**update_iceberg_ingest_settings**](DefaultApi.md#update_iceberg_ingest_settings) | **PUT** /ingest-settings/ | Update ingest-settings by ID
[**update_iceberg_ingest_settings_flow**](DefaultApi.md#update_iceberg_ingest_settings_flow) | **PUT** /ingest-settings/flow/ | Update flow by ID
[**update_iceberg_ingest_settings_flow_template_by_id**](DefaultApi.md#update_iceberg_ingest_settings_flow_template_by_id) | **PUT** /ingest-settings/flow/template/{name}/ | Update template by ID
[**update_iceberg_ingest_settings_syslog**](DefaultApi.md#update_iceberg_ingest_settings_syslog) | **PUT** /ingest-settings/syslog/ | Update syslog by ID
[**update_iceberg_ingest_settings_syslog_pattern_by_id**](DefaultApi.md#update_iceberg_ingest_settings_syslog_pattern_by_id) | **PUT** /ingest-settings/syslog/pattern/{name}/ | Update pattern by ID
[**update_iceberg_ingest_settings_syslog_pattern_set_by_id**](DefaultApi.md#update_iceberg_ingest_settings_syslog_pattern_set_by_id) | **PUT** /ingest-settings/syslog/pattern-set/{name}/ | Update pattern-set by ID
[**update_iceberg_profile_data_summarization_raw_by_id**](DefaultApi.md#update_iceberg_profile_data_summarization_raw_by_id) | **PUT** /profile/data-summarization/raw/{name}/ | Update raw-data-summarization by ID
[**update_iceberg_profile_security_ca_profile_by_id**](DefaultApi.md#update_iceberg_profile_security_ca_profile_by_id) | **PUT** /profile/security/ca-profile/{name}/ | Update ca-profile by ID
[**update_iceberg_profile_security_local_certificate_by_id**](DefaultApi.md#update_iceberg_profile_security_local_certificate_by_id) | **PUT** /profile/security/local-certificate/{name}/ | Update local-certificate by ID
[**update_iceberg_profile_security_ssh_key_profile_by_id**](DefaultApi.md#update_iceberg_profile_security_ssh_key_profile_by_id) | **PUT** /profile/security/ssh-key-profile/{name}/ | Update ssh-key-profile by ID
[**update_iceberg_profiles**](DefaultApi.md#update_iceberg_profiles) | **PUT** /profiles/ | Update profile by ID


# **backup_helper_files**
> file backup_helper_files(authorization=authorization)

Download the tar file containing all helper files.

Download helper files tar file, which will include the config and input directory.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
authorization = 'authorization_example' # str | authentication header object (optional)

try:
    # Download the tar file containing all helper files.
    api_response = api_instance.backup_helper_files(authorization=authorization)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->backup_helper_files: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| authentication header object | [optional] 

### Return type

[**file**](file.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, multipart/form-data
 - **Accept**: application/octet-stream

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_files_certificates_by_file_name**
> create_files_certificates_by_file_name(up_file, file_name, authorization=authorization, password=password, certificate_type=certificate_type)

Upload a certificate file.

Upload the specified certificate-file.

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
authorization = 'authorization_example' # str | authentication header object (optional)
password = 'password_example' # str | password (optional)
certificate_type = 'certificate_type_example' # str | Certificate type (optional)

try:
    # Upload a certificate file.
    api_instance.create_files_certificates_by_file_name(up_file, file_name, authorization=authorization, password=password, certificate_type=certificate_type)
except ApiException as e:
    print("Exception when calling DefaultApi->create_files_certificates_by_file_name: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **up_file** | **file**| File content | 
 **file_name** | **str**| File name | 
 **authorization** | **str**| authentication header object | [optional] 
 **password** | **str**| password | [optional] 
 **certificate_type** | **str**| Certificate type | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json, application/octet-stream

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_files_helper_files_by_file_name**
> create_files_helper_files_by_file_name(up_file, file_name, authorization=authorization)

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
authorization = 'authorization_example' # str | authentication header object (optional)

try:
    # Upload a helper-file.
    api_instance.create_files_helper_files_by_file_name(up_file, file_name, authorization=authorization)
except ApiException as e:
    print("Exception when calling DefaultApi->create_files_helper_files_by_file_name: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **up_file** | **file**| File content | 
 **file_name** | **str**| File name | 
 **authorization** | **str**| authentication header object | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json, application/octet-stream

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_healthbot_ingest_settings_byoi_custom_plugin_by_id**
> create_healthbot_ingest_settings_byoi_custom_plugin_by_id(name, custom_plugin, authorization=authorization)

Create custom-plugin by ID

Create operation of resource: custom-plugin

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
name = 'name_example' # str | Name of custom-plugin
custom_plugin = swagger_client.CustomPluginSchema() # CustomPluginSchema | custom_pluginbody object
authorization = 'authorization_example' # str | authentication header object (optional)

try:
    # Create custom-plugin by ID
    api_instance.create_healthbot_ingest_settings_byoi_custom_plugin_by_id(name, custom_plugin, authorization=authorization)
except ApiException as e:
    print("Exception when calling DefaultApi->create_healthbot_ingest_settings_byoi_custom_plugin_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of custom-plugin | 
 **custom_plugin** | [**CustomPluginSchema**](CustomPluginSchema.md)| custom_pluginbody object | 
 **authorization** | **str**| authentication header object | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_healthbot_ingest_settings_byoi_default_plugin_tlive_kafka_by_id**
> create_healthbot_ingest_settings_byoi_default_plugin_tlive_kafka_by_id(name, tlive_kafka, authorization=authorization)

Create tlive-kafka-oc by ID

Add/Merge a tlive-kafka-oc configuration.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
name = 'name_example' # str | Name of tlive-kafka-oc
tlive_kafka = swagger_client.TliveKafkaOcSchema() # TliveKafkaOcSchema | tlive_kafkabody object
authorization = 'authorization_example' # str | authentication header object (optional)

try:
    # Create tlive-kafka-oc by ID
    api_instance.create_healthbot_ingest_settings_byoi_default_plugin_tlive_kafka_by_id(name, tlive_kafka, authorization=authorization)
except ApiException as e:
    print("Exception when calling DefaultApi->create_healthbot_ingest_settings_byoi_default_plugin_tlive_kafka_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of tlive-kafka-oc | 
 **tlive_kafka** | [**TliveKafkaOcSchema**](TliveKafkaOcSchema.md)| tlive_kafkabody object | 
 **authorization** | **str**| authentication header object | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_healthbot_ingest_settings_byoi_ingest_mapping_by_id**
> create_healthbot_ingest_settings_byoi_ingest_mapping_by_id(name, ingest_mapping, authorization=authorization)

Create ingest-mapping by ID

Create ingest-mapping by name

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
name = 'name_example' # str | Name of ingest-mapping
ingest_mapping = swagger_client.IngestMappingSchema() # IngestMappingSchema | ingest_mappingbody object
authorization = 'authorization_example' # str | authentication header object (optional)

try:
    # Create ingest-mapping by ID
    api_instance.create_healthbot_ingest_settings_byoi_ingest_mapping_by_id(name, ingest_mapping, authorization=authorization)
except ApiException as e:
    print("Exception when calling DefaultApi->create_healthbot_ingest_settings_byoi_ingest_mapping_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of ingest-mapping | 
 **ingest_mapping** | [**IngestMappingSchema**](IngestMappingSchema.md)| ingest_mappingbody object | 
 **authorization** | **str**| authentication header object | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_healthbot_ingest_settings_frequency_profile_by_id**
> create_healthbot_ingest_settings_frequency_profile_by_id(name, frequency_profile, authorization=authorization)

Create frequency-profile by ID

Create operation of resource: frequency-profile

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
frequency_profile = swagger_client.FrequencyProfileSchema() # FrequencyProfileSchema | frequency_profilebody object
authorization = 'authorization_example' # str | authentication header object (optional)

try:
    # Create frequency-profile by ID
    api_instance.create_healthbot_ingest_settings_frequency_profile_by_id(name, frequency_profile, authorization=authorization)
except ApiException as e:
    print("Exception when calling DefaultApi->create_healthbot_ingest_settings_frequency_profile_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| ID of name | 
 **frequency_profile** | [**FrequencyProfileSchema**](FrequencyProfileSchema.md)| frequency_profilebody object | 
 **authorization** | **str**| authentication header object | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_healthbot_system_time_series_database_time_series_database_by_id**
> create_healthbot_system_time_series_database_time_series_database_by_id(time_series_database)

Create time-series-database by ID

Create operation of resource: time-series-database

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
time_series_database = swagger_client.TsdbSchema() # TsdbSchema | time_series_databasebody object

try:
    # Create time-series-database by ID
    api_instance.create_healthbot_system_time_series_database_time_series_database_by_id(time_series_database)
except ApiException as e:
    print("Exception when calling DefaultApi->create_healthbot_system_time_series_database_time_series_database_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **time_series_database** | [**TsdbSchema**](TsdbSchema.md)| time_series_databasebody object | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_iceberg_ingest_settings**
> create_iceberg_ingest_settings(ingest_settings, authorization=authorization)

Create ingest-settings by ID

Create operation of resource: ingest-settings

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
ingest_settings = swagger_client.IngestSettingsSchema() # IngestSettingsSchema | ingest_settingsbody object
authorization = 'authorization_example' # str | authentication header object (optional)

try:
    # Create ingest-settings by ID
    api_instance.create_iceberg_ingest_settings(ingest_settings, authorization=authorization)
except ApiException as e:
    print("Exception when calling DefaultApi->create_iceberg_ingest_settings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ingest_settings** | [**IngestSettingsSchema**](IngestSettingsSchema.md)| ingest_settingsbody object | 
 **authorization** | **str**| authentication header object | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_iceberg_ingest_settings_flow**
> create_iceberg_ingest_settings_flow(flow, authorization=authorization)

Create flow by ID

Create operation of resource: flow

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
flow = swagger_client.FlowSchema() # FlowSchema | flowbody object
authorization = 'authorization_example' # str | authentication header object (optional)

try:
    # Create flow by ID
    api_instance.create_iceberg_ingest_settings_flow(flow, authorization=authorization)
except ApiException as e:
    print("Exception when calling DefaultApi->create_iceberg_ingest_settings_flow: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **flow** | [**FlowSchema**](FlowSchema.md)| flowbody object | 
 **authorization** | **str**| authentication header object | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_iceberg_ingest_settings_flow_template_by_id**
> create_iceberg_ingest_settings_flow_template_by_id(name, template, authorization=authorization)

Create template by ID

Create operation of resource: template

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
name = 'name_example' # str | Name of template
template = swagger_client.TemplateSchema() # TemplateSchema | templatebody object
authorization = 'authorization_example' # str | authentication header object (optional)

try:
    # Create template by ID
    api_instance.create_iceberg_ingest_settings_flow_template_by_id(name, template, authorization=authorization)
except ApiException as e:
    print("Exception when calling DefaultApi->create_iceberg_ingest_settings_flow_template_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of template | 
 **template** | [**TemplateSchema**](TemplateSchema.md)| templatebody object | 
 **authorization** | **str**| authentication header object | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_iceberg_ingest_settings_syslog**
> create_iceberg_ingest_settings_syslog(syslog, authorization=authorization)

Create syslog by ID

Create operation of resource: syslog

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
syslog = swagger_client.SyslogSchema() # SyslogSchema | syslogbody object
authorization = 'authorization_example' # str | authentication header object (optional)

try:
    # Create syslog by ID
    api_instance.create_iceberg_ingest_settings_syslog(syslog, authorization=authorization)
except ApiException as e:
    print("Exception when calling DefaultApi->create_iceberg_ingest_settings_syslog: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **syslog** | [**SyslogSchema**](SyslogSchema.md)| syslogbody object | 
 **authorization** | **str**| authentication header object | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_iceberg_ingest_settings_syslog_pattern_by_id**
> create_iceberg_ingest_settings_syslog_pattern_by_id(name, pattern, authorization=authorization)

Create pattern by ID

Create operation of resource: pattern

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
name = 'name_example' # str | Name of pattern
pattern = swagger_client.PatternSchema() # PatternSchema | patternbody object
authorization = 'authorization_example' # str | authentication header object (optional)

try:
    # Create pattern by ID
    api_instance.create_iceberg_ingest_settings_syslog_pattern_by_id(name, pattern, authorization=authorization)
except ApiException as e:
    print("Exception when calling DefaultApi->create_iceberg_ingest_settings_syslog_pattern_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of pattern | 
 **pattern** | [**PatternSchema**](PatternSchema.md)| patternbody object | 
 **authorization** | **str**| authentication header object | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_iceberg_ingest_settings_syslog_pattern_set_by_id**
> create_iceberg_ingest_settings_syslog_pattern_set_by_id(name, pattern_set, authorization=authorization)

Create pattern-set by ID

Create operation of resource: pattern-set

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
name = 'name_example' # str | Name of pattern-set
pattern_set = swagger_client.PatternSetSchema() # PatternSetSchema | pattern_setbody object
authorization = 'authorization_example' # str | authentication header object (optional)

try:
    # Create pattern-set by ID
    api_instance.create_iceberg_ingest_settings_syslog_pattern_set_by_id(name, pattern_set, authorization=authorization)
except ApiException as e:
    print("Exception when calling DefaultApi->create_iceberg_ingest_settings_syslog_pattern_set_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of pattern-set | 
 **pattern_set** | [**PatternSetSchema**](PatternSetSchema.md)| pattern_setbody object | 
 **authorization** | **str**| authentication header object | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_iceberg_profile_data_summarization_raw_by_id**
> create_iceberg_profile_data_summarization_raw_by_id(name, raw_data_summarization, authorization=authorization)

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
name = 'name_example' # str | Name of raw-data-summarization
raw_data_summarization = swagger_client.RawSchema() # RawSchema | raw_data_summarizationbody object
authorization = 'authorization_example' # str | authentication header object (optional)

try:
    # Create raw-data-summarization by ID
    api_instance.create_iceberg_profile_data_summarization_raw_by_id(name, raw_data_summarization, authorization=authorization)
except ApiException as e:
    print("Exception when calling DefaultApi->create_iceberg_profile_data_summarization_raw_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of raw-data-summarization | 
 **raw_data_summarization** | [**RawSchema**](RawSchema.md)| raw_data_summarizationbody object | 
 **authorization** | **str**| authentication header object | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_iceberg_profile_security_ca_profile_by_id**
> create_iceberg_profile_security_ca_profile_by_id(name, ca_profile, authorization=authorization)

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
name = 'name_example' # str | Name of ca-profile
ca_profile = swagger_client.CaProfileSchema() # CaProfileSchema | ca_profilebody object
authorization = 'authorization_example' # str | authentication header object (optional)

try:
    # Create ca-profile by ID
    api_instance.create_iceberg_profile_security_ca_profile_by_id(name, ca_profile, authorization=authorization)
except ApiException as e:
    print("Exception when calling DefaultApi->create_iceberg_profile_security_ca_profile_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of ca-profile | 
 **ca_profile** | [**CaProfileSchema**](CaProfileSchema.md)| ca_profilebody object | 
 **authorization** | **str**| authentication header object | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_iceberg_profile_security_local_certificate_by_id**
> create_iceberg_profile_security_local_certificate_by_id(name, local_certificate, authorization=authorization)

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
name = 'name_example' # str | Name of local-certificate
local_certificate = swagger_client.LocalCertificateSchema() # LocalCertificateSchema | local_certificatebody object
authorization = 'authorization_example' # str | authentication header object (optional)

try:
    # Create local-certificate by ID
    api_instance.create_iceberg_profile_security_local_certificate_by_id(name, local_certificate, authorization=authorization)
except ApiException as e:
    print("Exception when calling DefaultApi->create_iceberg_profile_security_local_certificate_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of local-certificate | 
 **local_certificate** | [**LocalCertificateSchema**](LocalCertificateSchema.md)| local_certificatebody object | 
 **authorization** | **str**| authentication header object | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_iceberg_profile_security_ssh_key_profile_by_id**
> create_iceberg_profile_security_ssh_key_profile_by_id(name, ssh_key_profile, authorization=authorization)

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
name = 'name_example' # str | Name of ssh-key-profile
ssh_key_profile = swagger_client.SshKeyProfileSchema() # SshKeyProfileSchema | ssh_key_profilebody object
authorization = 'authorization_example' # str | authentication header object (optional)

try:
    # Create ssh-key-profile by ID
    api_instance.create_iceberg_profile_security_ssh_key_profile_by_id(name, ssh_key_profile, authorization=authorization)
except ApiException as e:
    print("Exception when calling DefaultApi->create_iceberg_profile_security_ssh_key_profile_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of ssh-key-profile | 
 **ssh_key_profile** | [**SshKeyProfileSchema**](SshKeyProfileSchema.md)| ssh_key_profilebody object | 
 **authorization** | **str**| authentication header object | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_iceberg_profiles**
> create_iceberg_profiles(profile, authorization=authorization)

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
authorization = 'authorization_example' # str | authentication header object (optional)

try:
    # Create profile by ID
    api_instance.create_iceberg_profiles(profile, authorization=authorization)
except ApiException as e:
    print("Exception when calling DefaultApi->create_iceberg_profiles: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **profile** | [**ProfilesSchema**](ProfilesSchema.md)| profilebody object | 
 **authorization** | **str**| authentication header object | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_files_certificates_by_file_name**
> delete_files_certificates_by_file_name(file_name, authorization=authorization, input_path=input_path, certificate_type=certificate_type)

Delete a certificate-file.

Delete the specified certificate-file. Delete will not fail if the certificate-file is being used by some service.

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
authorization = 'authorization_example' # str | authentication header object (optional)
input_path = 'input_path_example' # str | Input path (optional)
certificate_type = 'certificate_type_example' # str | Certificate type (optional)

try:
    # Delete a certificate-file.
    api_instance.delete_files_certificates_by_file_name(file_name, authorization=authorization, input_path=input_path, certificate_type=certificate_type)
except ApiException as e:
    print("Exception when calling DefaultApi->delete_files_certificates_by_file_name: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file_name** | **str**| File name | 
 **authorization** | **str**| authentication header object | [optional] 
 **input_path** | **str**| Input path | [optional] 
 **certificate_type** | **str**| Certificate type | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, multipart/form-data
 - **Accept**: application/json, application/octet-stream

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_files_helper_files_by_file_name**
> delete_files_helper_files_by_file_name(file_name, authorization=authorization, input_path=input_path)

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
authorization = 'authorization_example' # str | authentication header object (optional)
input_path = 'input_path_example' # str | Input path (optional)

try:
    # Delete a helper-file.
    api_instance.delete_files_helper_files_by_file_name(file_name, authorization=authorization, input_path=input_path)
except ApiException as e:
    print("Exception when calling DefaultApi->delete_files_helper_files_by_file_name: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file_name** | **str**| File name | 
 **authorization** | **str**| authentication header object | [optional] 
 **input_path** | **str**| Input path | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, multipart/form-data
 - **Accept**: application/json, application/octet-stream

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_healthbot_ingest_settings_byoi_custom_plugin_by_id**
> delete_healthbot_ingest_settings_byoi_custom_plugin_by_id(name, authorization=authorization)

Delete custom-plugin by ID

Delete operation of resource: custom-plugin

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
name = 'name_example' # str | Name of custom-plugin
authorization = 'authorization_example' # str | authentication header object (optional)

try:
    # Delete custom-plugin by ID
    api_instance.delete_healthbot_ingest_settings_byoi_custom_plugin_by_id(name, authorization=authorization)
except ApiException as e:
    print("Exception when calling DefaultApi->delete_healthbot_ingest_settings_byoi_custom_plugin_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of custom-plugin | 
 **authorization** | **str**| authentication header object | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_healthbot_ingest_settings_byoi_default_plugin_tlive_kafka_by_id**
> delete_healthbot_ingest_settings_byoi_default_plugin_tlive_kafka_by_id(name, authorization=authorization)

Delete tlive-kafka-oc by ID

Delete operation of resource: tlive-kafka-oc

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
name = 'name_example' # str | Name of tlive-kafka-oc
authorization = 'authorization_example' # str | authentication header object (optional)

try:
    # Delete tlive-kafka-oc by ID
    api_instance.delete_healthbot_ingest_settings_byoi_default_plugin_tlive_kafka_by_id(name, authorization=authorization)
except ApiException as e:
    print("Exception when calling DefaultApi->delete_healthbot_ingest_settings_byoi_default_plugin_tlive_kafka_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of tlive-kafka-oc | 
 **authorization** | **str**| authentication header object | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_healthbot_ingest_settings_byoi_ingest_mapping_by_id**
> delete_healthbot_ingest_settings_byoi_ingest_mapping_by_id(name, authorization=authorization)

Delete ingest-mapping by ID

Delete ingest-mapping by name

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
name = 'name_example' # str | Name of ingest-mapping
authorization = 'authorization_example' # str | authentication header object (optional)

try:
    # Delete ingest-mapping by ID
    api_instance.delete_healthbot_ingest_settings_byoi_ingest_mapping_by_id(name, authorization=authorization)
except ApiException as e:
    print("Exception when calling DefaultApi->delete_healthbot_ingest_settings_byoi_ingest_mapping_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of ingest-mapping | 
 **authorization** | **str**| authentication header object | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_healthbot_ingest_settings_frequency_profile_by_id**
> delete_healthbot_ingest_settings_frequency_profile_by_id(name, authorization=authorization)

Delete frequency-profile by ID

Delete operation of resource: frequency-profile

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
authorization = 'authorization_example' # str | authentication header object (optional)

try:
    # Delete frequency-profile by ID
    api_instance.delete_healthbot_ingest_settings_frequency_profile_by_id(name, authorization=authorization)
except ApiException as e:
    print("Exception when calling DefaultApi->delete_healthbot_ingest_settings_frequency_profile_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| ID of name | 
 **authorization** | **str**| authentication header object | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_healthbot_system_time_series_database_time_series_database_by_id**
> delete_healthbot_system_time_series_database_time_series_database_by_id()

Delete time-series-database

Delete operation of resource: time-series-database

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
    # Delete time-series-database
    api_instance.delete_healthbot_system_time_series_database_time_series_database_by_id()
except ApiException as e:
    print("Exception when calling DefaultApi->delete_healthbot_system_time_series_database_time_series_database_by_id: %s\n" % e)
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

# **delete_iceberg_ingest_settings**
> delete_iceberg_ingest_settings(authorization=authorization)

Delete ingest-settings by ID

Delete operation of resource: ingest-settings

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
authorization = 'authorization_example' # str | authentication header object (optional)

try:
    # Delete ingest-settings by ID
    api_instance.delete_iceberg_ingest_settings(authorization=authorization)
except ApiException as e:
    print("Exception when calling DefaultApi->delete_iceberg_ingest_settings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| authentication header object | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_iceberg_ingest_settings_flow**
> delete_iceberg_ingest_settings_flow(authorization=authorization)

Delete flow by ID

Delete operation of resource: flow

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
authorization = 'authorization_example' # str | authentication header object (optional)

try:
    # Delete flow by ID
    api_instance.delete_iceberg_ingest_settings_flow(authorization=authorization)
except ApiException as e:
    print("Exception when calling DefaultApi->delete_iceberg_ingest_settings_flow: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| authentication header object | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_iceberg_ingest_settings_flow_template_by_id**
> delete_iceberg_ingest_settings_flow_template_by_id(name, authorization=authorization)

Delete template by ID

Delete operation of resource: template

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
name = 'name_example' # str | Name of template
authorization = 'authorization_example' # str | authentication header object (optional)

try:
    # Delete template by ID
    api_instance.delete_iceberg_ingest_settings_flow_template_by_id(name, authorization=authorization)
except ApiException as e:
    print("Exception when calling DefaultApi->delete_iceberg_ingest_settings_flow_template_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of template | 
 **authorization** | **str**| authentication header object | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_iceberg_ingest_settings_syslog**
> delete_iceberg_ingest_settings_syslog(authorization=authorization)

Delete syslog by ID

Delete operation of resource: syslog

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
authorization = 'authorization_example' # str | authentication header object (optional)

try:
    # Delete syslog by ID
    api_instance.delete_iceberg_ingest_settings_syslog(authorization=authorization)
except ApiException as e:
    print("Exception when calling DefaultApi->delete_iceberg_ingest_settings_syslog: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| authentication header object | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_iceberg_ingest_settings_syslog_pattern_by_id**
> delete_iceberg_ingest_settings_syslog_pattern_by_id(name, authorization=authorization)

Delete pattern by ID

Delete operation of resource: pattern

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
name = 'name_example' # str | Name of pattern
authorization = 'authorization_example' # str | authentication header object (optional)

try:
    # Delete pattern by ID
    api_instance.delete_iceberg_ingest_settings_syslog_pattern_by_id(name, authorization=authorization)
except ApiException as e:
    print("Exception when calling DefaultApi->delete_iceberg_ingest_settings_syslog_pattern_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of pattern | 
 **authorization** | **str**| authentication header object | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_iceberg_ingest_settings_syslog_pattern_set_by_id**
> delete_iceberg_ingest_settings_syslog_pattern_set_by_id(name, authorization=authorization)

Delete pattern-set by ID

Delete operation of resource: pattern-set

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
name = 'name_example' # str | Name of pattern-set
authorization = 'authorization_example' # str | authentication header object (optional)

try:
    # Delete pattern-set by ID
    api_instance.delete_iceberg_ingest_settings_syslog_pattern_set_by_id(name, authorization=authorization)
except ApiException as e:
    print("Exception when calling DefaultApi->delete_iceberg_ingest_settings_syslog_pattern_set_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of pattern-set | 
 **authorization** | **str**| authentication header object | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_iceberg_profile_data_summarization_raw_by_id**
> delete_iceberg_profile_data_summarization_raw_by_id(name, authorization=authorization)

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
name = 'name_example' # str | Name of raw-data-summarization
authorization = 'authorization_example' # str | authentication header object (optional)

try:
    # Delete raw-data-summarization by ID
    api_instance.delete_iceberg_profile_data_summarization_raw_by_id(name, authorization=authorization)
except ApiException as e:
    print("Exception when calling DefaultApi->delete_iceberg_profile_data_summarization_raw_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of raw-data-summarization | 
 **authorization** | **str**| authentication header object | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_iceberg_profile_security_ca_profile_by_id**
> delete_iceberg_profile_security_ca_profile_by_id(name, authorization=authorization)

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
name = 'name_example' # str | Name of ca-profile
authorization = 'authorization_example' # str | authentication header object (optional)

try:
    # Delete ca-profile by ID
    api_instance.delete_iceberg_profile_security_ca_profile_by_id(name, authorization=authorization)
except ApiException as e:
    print("Exception when calling DefaultApi->delete_iceberg_profile_security_ca_profile_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of ca-profile | 
 **authorization** | **str**| authentication header object | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_iceberg_profile_security_local_certificate_by_id**
> delete_iceberg_profile_security_local_certificate_by_id(name, authorization=authorization)

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
name = 'name_example' # str | Name of local-certificate
authorization = 'authorization_example' # str | authentication header object (optional)

try:
    # Delete local-certificate by ID
    api_instance.delete_iceberg_profile_security_local_certificate_by_id(name, authorization=authorization)
except ApiException as e:
    print("Exception when calling DefaultApi->delete_iceberg_profile_security_local_certificate_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of local-certificate | 
 **authorization** | **str**| authentication header object | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_iceberg_profile_security_ssh_key_profile_by_id**
> delete_iceberg_profile_security_ssh_key_profile_by_id(name, authorization=authorization)

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
name = 'name_example' # str | Name of ssh-key-profile
authorization = 'authorization_example' # str | authentication header object (optional)

try:
    # Delete ssh-key-profile by ID
    api_instance.delete_iceberg_profile_security_ssh_key_profile_by_id(name, authorization=authorization)
except ApiException as e:
    print("Exception when calling DefaultApi->delete_iceberg_profile_security_ssh_key_profile_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of ssh-key-profile | 
 **authorization** | **str**| authentication header object | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_iceberg_profiles**
> delete_iceberg_profiles(authorization=authorization)

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
authorization = 'authorization_example' # str | authentication header object (optional)

try:
    # Delete profile by ID
    api_instance.delete_iceberg_profiles(authorization=authorization)
except ApiException as e:
    print("Exception when calling DefaultApi->delete_iceberg_profiles: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| authentication header object | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **inspect_command_rpc_table_on_device**
> inspect_command_rpc_table_on_device(command_rpc_detail, authorization=authorization)

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
authorization = 'authorization_example' # str | authentication header object (optional)

try:
    # Inspect the given iAgent table.
    api_instance.inspect_command_rpc_table_on_device(command_rpc_detail, authorization=authorization)
except ApiException as e:
    print("Exception when calling DefaultApi->inspect_command_rpc_table_on_device: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **command_rpc_detail** | [**CommandRpc**](CommandRpc.md)| command-rpc object | 
 **authorization** | **str**| authentication header object | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **restore_helper_files**
> restore_helper_files(restore_file, authorization=authorization)

Upload a helper-file.

Upload tar file of helper-files

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
restore_file = '/path/to/file.txt' # file | File content
authorization = 'authorization_example' # str | authentication header object (optional)

try:
    # Upload a helper-file.
    api_instance.restore_helper_files(restore_file, authorization=authorization)
except ApiException as e:
    print("Exception when calling DefaultApi->restore_helper_files: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **restore_file** | **file**| File content | 
 **authorization** | **str**| authentication header object | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json, application/octet-stream

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_configuration_jobs**
> list[InlineResponse200] retrieve_configuration_jobs(authorization=authorization, job_id=job_id, job_status=job_status)



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
authorization = 'authorization_example' # str | authentication header object (optional)
job_id = 'job_id_example' # str | Id of Job (optional)
job_status = 'job_status_example' # str | Type of job (optional)

try:
    api_response = api_instance.retrieve_configuration_jobs(authorization=authorization, job_id=job_id, job_status=job_status)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->retrieve_configuration_jobs: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| authentication header object | [optional] 
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
> list[TableSchema] retrieve_data_database_table(authorization=authorization, device_id=device_id, device_group_name=device_group_name, network_group_name=network_group_name)

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
authorization = 'authorization_example' # str | authentication header object (optional)
device_id = 'device_id_example' # str | Name of device (optional)
device_group_name = 'device_group_name_example' # str | Name of device-group (optional)
network_group_name = 'network_group_name_example' # str | Name of network-group (optional)

try:
    # Get information about tables for a device of a device-group.
    api_response = api_instance.retrieve_data_database_table(authorization=authorization, device_id=device_id, device_group_name=device_group_name, network_group_name=network_group_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->retrieve_data_database_table: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| authentication header object | [optional] 
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
> list[str] retrieve_data_database_table_column_by_table_name(table_name, authorization=authorization, device_id=device_id, device_group_name=device_group_name, network_group_name=network_group_name)

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
authorization = 'authorization_example' # str | authentication header object (optional)
device_id = 'device_id_example' # str | Name of device (optional)
device_group_name = 'device_group_name_example' # str | Name of device-group (optional)
network_group_name = 'network_group_name_example' # str | Name of network-group (optional)

try:
    # Get information about columns in a table.
    api_response = api_instance.retrieve_data_database_table_column_by_table_name(table_name, authorization=authorization, device_id=device_id, device_group_name=device_group_name, network_group_name=network_group_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->retrieve_data_database_table_column_by_table_name: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **table_name** | **str**| Name of table | 
 **authorization** | **str**| authentication header object | [optional] 
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
> list[str] retrieve_data_database_tags_by_table_name(table_name, authorization=authorization, device_id=device_id, device_group_name=device_group_name, network_group_name=network_group_name, tag=tag, where_clause=where_clause)

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
authorization = 'authorization_example' # str | authentication header object (optional)
device_id = 'device_id_example' # str | Name of device (optional)
device_group_name = 'device_group_name_example' # str | Name of device-group (optional)
network_group_name = 'network_group_name_example' # str | Name of network-group (optional)
tag = 'tag_example' # str | Tag key for which values are requested. (optional)
where_clause = 'where_clause_example' # str | Where condition to select values for the requested key. This would not be processed if there is no `tag` query parameter. eg: `tag_key1=val1 AND tag_key2=val2` (optional)

try:
    # Get information about tags keys and values in a table.
    api_response = api_instance.retrieve_data_database_tags_by_table_name(table_name, authorization=authorization, device_id=device_id, device_group_name=device_group_name, network_group_name=network_group_name, tag=tag, where_clause=where_clause)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->retrieve_data_database_tags_by_table_name: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **table_name** | **str**| Name of table | 
 **authorization** | **str**| authentication header object | [optional] 
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

# **retrieve_debug_jobs**
> retrieve_debug_jobs(authorization=authorization, job_id=job_id)



Return the status of the last \"/debug/\" job 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
authorization = 'authorization_example' # str | authentication header object (optional)
job_id = 'job_id_example' # str | Id of Job (optional)

try:
    api_instance.retrieve_debug_jobs(authorization=authorization, job_id=job_id)
except ApiException as e:
    print("Exception when calling DefaultApi->retrieve_debug_jobs: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| authentication header object | [optional] 
 **job_id** | [**str**](.md)| Id of Job | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, multipart/form-data
 - **Accept**: application/json, application/octet-stream

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_event**
> list[Event] retrieve_event(from_timestamp, device_id, authorization=authorization, to_timestamp=to_timestamp, device_group_name=device_group_name, granularity=granularity, color=color)

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
authorization = 'authorization_example' # str | authentication header object (optional)
to_timestamp = '2013-10-20T19:20:30+01:00' # datetime | Ending timestamp (optional)
device_group_name = 'device_group_name_example' # str | Device group's device-group-name of which the device is part (optional)
granularity = 'granularity_example' # str | Granularity of query (optional)
color = 'color_example' # str | Color of events. (optional)

try:
    # Get all events for a device.
    api_response = api_instance.retrieve_event(from_timestamp, device_id, authorization=authorization, to_timestamp=to_timestamp, device_group_name=device_group_name, granularity=granularity, color=color)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->retrieve_event: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **from_timestamp** | **datetime**| Starting timestamp | 
 **device_id** | **str**| device-id of the device for which events are requested | 
 **authorization** | **str**| authentication header object | [optional] 
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
> list[Event] retrieve_event_by_event_name(event_name, from_timestamp, device_id, authorization=authorization, to_timestamp=to_timestamp, device_group_name=device_group_name, granularity=granularity, color=color)

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
authorization = 'authorization_example' # str | authentication header object (optional)
to_timestamp = '2013-10-20T19:20:30+01:00' # datetime | Ending timestamp (optional)
device_group_name = 'device_group_name_example' # str | device-group-name of which the device is part (optional)
granularity = 'granularity_example' # str | Granularity of query (optional)
color = 'color_example' # str | Color of events. (optional)

try:
    # Get instances of a device event.
    api_response = api_instance.retrieve_event_by_event_name(event_name, from_timestamp, device_id, authorization=authorization, to_timestamp=to_timestamp, device_group_name=device_group_name, granularity=granularity, color=color)
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
 **authorization** | **str**| authentication header object | [optional] 
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
> list[Event] retrieve_event_by_event_name_device_group(event_name, from_timestamp, device_group_name, authorization=authorization, to_timestamp=to_timestamp, granularity=granularity, device_id=device_id, color=color)

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
authorization = 'authorization_example' # str | authentication header object (optional)
to_timestamp = '2013-10-20T19:20:30+01:00' # datetime | Ending timestamp (optional)
granularity = 'granularity_example' # str | Granularity of query (optional)
device_id = ['device_id_example'] # list[str] | list of devices under a device-group to be fetched (optional)
color = 'color_example' # str | Color of events. (optional)

try:
    # Get instances of a device-group event.
    api_response = api_instance.retrieve_event_by_event_name_device_group(event_name, from_timestamp, device_group_name, authorization=authorization, to_timestamp=to_timestamp, granularity=granularity, device_id=device_id, color=color)
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
 **authorization** | **str**| authentication header object | [optional] 
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
> list[Event] retrieve_event_by_event_name_network_group(event_name, from_timestamp, network_group_name, authorization=authorization, to_timestamp=to_timestamp, granularity=granularity, color=color)

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
authorization = 'authorization_example' # str | authentication header object (optional)
to_timestamp = '2013-10-20T19:20:30+01:00' # datetime | Ending timestamp (optional)
granularity = 'granularity_example' # str | Granularity of query (optional)
color = 'color_example' # str | Color of events. (optional)

try:
    # Get instances of a network-group event.
    api_response = api_instance.retrieve_event_by_event_name_network_group(event_name, from_timestamp, network_group_name, authorization=authorization, to_timestamp=to_timestamp, granularity=granularity, color=color)
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
 **authorization** | **str**| authentication header object | [optional] 
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
> list[Event] retrieve_event_device_group(from_timestamp, device_group_name, authorization=authorization, to_timestamp=to_timestamp, granularity=granularity, device_id=device_id, color=color)

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
authorization = 'authorization_example' # str | authentication header object (optional)
to_timestamp = '2013-10-20T19:20:30+01:00' # datetime | Ending timestamp (optional)
granularity = 'granularity_example' # str | Granularity of query (optional)
device_id = ['device_id_example'] # list[str] | list of devices under a device-group to be fetched (optional)
color = 'color_example' # str | Color of events. (optional)

try:
    # Get all events for a device-group.
    api_response = api_instance.retrieve_event_device_group(from_timestamp, device_group_name, authorization=authorization, to_timestamp=to_timestamp, granularity=granularity, device_id=device_id, color=color)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->retrieve_event_device_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **from_timestamp** | **datetime**| Starting timestamp | 
 **device_group_name** | **str**| device_group_name of the device-group for which events are requested | 
 **authorization** | **str**| authentication header object | [optional] 
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
> list[Event] retrieve_event_network_group(from_timestamp, network_group_name, authorization=authorization, to_timestamp=to_timestamp, granularity=granularity, color=color)

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
authorization = 'authorization_example' # str | authentication header object (optional)
to_timestamp = '2013-10-20T19:20:30+01:00' # datetime | Ending timestamp (optional)
granularity = 'granularity_example' # str | Granularity of query (optional)
color = 'color_example' # str | Color of events. (optional)

try:
    # Get all events for a network-group.
    api_response = api_instance.retrieve_event_network_group(from_timestamp, network_group_name, authorization=authorization, to_timestamp=to_timestamp, granularity=granularity, color=color)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->retrieve_event_network_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **from_timestamp** | **datetime**| Starting timestamp | 
 **network_group_name** | **str**| network_group_name of the network-group for which events are requested | 
 **authorization** | **str**| authentication header object | [optional] 
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

# **retrieve_events**
> list[Event] retrieve_events(from_timestamp, authorization=authorization, to_timestamp=to_timestamp, color=color)

Get all events.

Get the list of all events. Filtering is possible with the use of various query parameters.

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
authorization = 'authorization_example' # str | authentication header object (optional)
to_timestamp = '2013-10-20T19:20:30+01:00' # datetime | Ending timestamp (optional)
color = 'color_example' # str | Color of events. (optional)

try:
    # Get all events.
    api_response = api_instance.retrieve_events(from_timestamp, authorization=authorization, to_timestamp=to_timestamp, color=color)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->retrieve_events: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **from_timestamp** | **datetime**| Starting timestamp | 
 **authorization** | **str**| authentication header object | [optional] 
 **to_timestamp** | **datetime**| Ending timestamp | [optional] 
 **color** | **str**| Color of events. | [optional] 

### Return type

[**list[Event]**](Event.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, multipart/form-data
 - **Accept**: application/json, application/octet-stream

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_files_certificates_by_file_name**
> file retrieve_files_certificates_by_file_name(file_name, authorization=authorization, input_path=input_path, certificate_type=certificate_type)

Download a certificate-file.

Download the specified certificate-file.

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
authorization = 'authorization_example' # str | authentication header object (optional)
input_path = 'input_path_example' # str | Input path (optional)
certificate_type = 'certificate_type_example' # str | Certificate type (optional)

try:
    # Download a certificate-file.
    api_response = api_instance.retrieve_files_certificates_by_file_name(file_name, authorization=authorization, input_path=input_path, certificate_type=certificate_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->retrieve_files_certificates_by_file_name: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file_name** | **str**| File name | 
 **authorization** | **str**| authentication header object | [optional] 
 **input_path** | **str**| Input path | [optional] 
 **certificate_type** | **str**| Certificate type | [optional] 

### Return type

[**file**](file.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, multipart/form-data
 - **Accept**: application/octet-stream, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_files_helper_files**
> list[str] retrieve_files_helper_files(authorization=authorization, input_path=input_path)

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
authorization = 'authorization_example' # str | authentication header object (optional)
input_path = 'input_path_example' # str | Input path (optional)

try:
    # Get all helper-file names.
    api_response = api_instance.retrieve_files_helper_files(authorization=authorization, input_path=input_path)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->retrieve_files_helper_files: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| authentication header object | [optional] 
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
> file retrieve_files_helper_files_by_file_name(file_name, authorization=authorization, input_path=input_path)

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
authorization = 'authorization_example' # str | authentication header object (optional)
input_path = 'input_path_example' # str | Input path (optional)

try:
    # Download a helper-file.
    api_response = api_instance.retrieve_files_helper_files_by_file_name(file_name, authorization=authorization, input_path=input_path)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->retrieve_files_helper_files_by_file_name: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file_name** | **str**| File name | 
 **authorization** | **str**| authentication header object | [optional] 
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
> HealthSchema retrieve_health_all(authorization=authorization)

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
authorization = 'authorization_example' # str | authentication header object (optional)

try:
    # Return a dict with health of devices in device groups and network groups
    api_response = api_instance.retrieve_health_all(authorization=authorization)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->retrieve_health_all: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| authentication header object | [optional] 

### Return type

[**HealthSchema**](HealthSchema.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, multipart/form-data
 - **Accept**: application/json, application/octet-stream

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_health_tree_by_device_group**
> DeviceGroupHealthTree retrieve_health_tree_by_device_group(device_group_name, authorization=authorization, timestamp=timestamp, tolerance=tolerance, device=device)

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
authorization = 'authorization_example' # str | authentication header object (optional)
timestamp = '2013-10-20T19:20:30+01:00' # datetime | Timestamp at which health tree is requested. If not specified, current server timestamp is used. (optional)
tolerance = 789 # int | Timestamp tolerance in seconds. With this option, health-tree will contain latest data between `timestamp-2*tolerance` and `timestamp`. Default value is `2*frequency` where `frequency` is extracted from `trigger`. (optional)
device = ['device_example'] # list[str] | list of devices under a device-group to be fetched (optional)

try:
    # Get device-group health-tree.
    api_response = api_instance.retrieve_health_tree_by_device_group(device_group_name, authorization=authorization, timestamp=timestamp, tolerance=tolerance, device=device)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->retrieve_health_tree_by_device_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_group_name** | **str**| &#x60;device-group-name&#x60; of device-group | 
 **authorization** | **str**| authentication header object | [optional] 
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
> DeviceHealthTree retrieve_health_tree_by_id(device_id, authorization=authorization, timestamp=timestamp, tolerance=tolerance)

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
authorization = 'authorization_example' # str | authentication header object (optional)
timestamp = '2013-10-20T19:20:30+01:00' # datetime | Timestamp at which health tree is requested. If not specified, current server timestamp is used. (optional)
tolerance = 789 # int | Timestamp tolerance in seconds. With this option, health-tree will contain latest data between `timestamp-2*tolerance` and `timestamp`. Default value is `2*frequency` where `frequency` is extracted from `trigger`. (optional)

try:
    # Return a device's health-tree.
    api_response = api_instance.retrieve_health_tree_by_id(device_id, authorization=authorization, timestamp=timestamp, tolerance=tolerance)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->retrieve_health_tree_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **str**| &#x60;device-id&#x60; of device | 
 **authorization** | **str**| authentication header object | [optional] 
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
> NetworkHealthTree retrieve_health_tree_by_network_group(network_group_name, authorization=authorization, timestamp=timestamp, tolerance=tolerance)

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
authorization = 'authorization_example' # str | authentication header object (optional)
timestamp = '2013-10-20T19:20:30+01:00' # datetime | Timestamp at which health tree is requested. If not specified, current server timestamp is used. (optional)
tolerance = 789 # int | Timestamp tolerance in seconds. With this option, health-tree will contain latest data between `timestamp-2*tolerance` and `timestamp`. Default value is `2*frequency` where `frequency` is extracted from `trigger`. (optional)

try:
    # Get network-group health-tree.
    api_response = api_instance.retrieve_health_tree_by_network_group(network_group_name, authorization=authorization, timestamp=timestamp, tolerance=tolerance)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->retrieve_health_tree_by_network_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **network_group_name** | **str**| &#x60;network-group-name&#x60; of network-group | 
 **authorization** | **str**| authentication header object | [optional] 
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

# **retrieve_healthbot_ingest_settings_byoi_custom_plugin_by_id**
> CustomPluginSchema retrieve_healthbot_ingest_settings_byoi_custom_plugin_by_id(name, authorization=authorization, working=working)

Retrieve custom-plugin by ID

Retrieve operation of resource: custom-plugin

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
name = 'name_example' # str | Name of custom-plugin
authorization = 'authorization_example' # str | authentication header object (optional)
working = true # bool | true queries undeployed configuration (optional)

try:
    # Retrieve custom-plugin by ID
    api_response = api_instance.retrieve_healthbot_ingest_settings_byoi_custom_plugin_by_id(name, authorization=authorization, working=working)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->retrieve_healthbot_ingest_settings_byoi_custom_plugin_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of custom-plugin | 
 **authorization** | **str**| authentication header object | [optional] 
 **working** | **bool**| true queries undeployed configuration | [optional] 

### Return type

[**CustomPluginSchema**](CustomPluginSchema.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_healthbot_ingest_settings_byoi_custom_plugins**
> CustomPluginSchema retrieve_healthbot_ingest_settings_byoi_custom_plugins(authorization=authorization, working=working)

Retrieve custom-plugin by ID

Retrieve all the custom-plugins configured.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
authorization = 'authorization_example' # str | authentication header object (optional)
working = true # bool | true queries undeployed configuration (optional)

try:
    # Retrieve custom-plugin by ID
    api_response = api_instance.retrieve_healthbot_ingest_settings_byoi_custom_plugins(authorization=authorization, working=working)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->retrieve_healthbot_ingest_settings_byoi_custom_plugins: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| authentication header object | [optional] 
 **working** | **bool**| true queries undeployed configuration | [optional] 

### Return type

[**CustomPluginSchema**](CustomPluginSchema.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_healthbot_ingest_settings_byoi_default_plugin_tlive_kafka_by_id**
> TliveKafkaOcSchema retrieve_healthbot_ingest_settings_byoi_default_plugin_tlive_kafka_by_id(name, authorization=authorization, working=working)

Retrieve tlive-kafka-oc by ID

Retrieve operation of resource: tlive-kafka-oc

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
name = 'name_example' # str | Name of tlive-kafka-oc
authorization = 'authorization_example' # str | authentication header object (optional)
working = true # bool | true queries undeployed configuration (optional)

try:
    # Retrieve tlive-kafka-oc by ID
    api_response = api_instance.retrieve_healthbot_ingest_settings_byoi_default_plugin_tlive_kafka_by_id(name, authorization=authorization, working=working)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->retrieve_healthbot_ingest_settings_byoi_default_plugin_tlive_kafka_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of tlive-kafka-oc | 
 **authorization** | **str**| authentication header object | [optional] 
 **working** | **bool**| true queries undeployed configuration | [optional] 

### Return type

[**TliveKafkaOcSchema**](TliveKafkaOcSchema.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_healthbot_ingest_settings_byoi_default_plugin_tlive_kafkas**
> list[str] retrieve_healthbot_ingest_settings_byoi_default_plugin_tlive_kafkas(authorization=authorization, working=working)

Retrieve tlive-kafka-oc

Retrieve all the tlive-kafka-ocs configured.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
authorization = 'authorization_example' # str | authentication header object (optional)
working = true # bool | true queries undeployed configuration (optional)

try:
    # Retrieve tlive-kafka-oc
    api_response = api_instance.retrieve_healthbot_ingest_settings_byoi_default_plugin_tlive_kafkas(authorization=authorization, working=working)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->retrieve_healthbot_ingest_settings_byoi_default_plugin_tlive_kafkas: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| authentication header object | [optional] 
 **working** | **bool**| true queries undeployed configuration | [optional] 

### Return type

**list[str]**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_healthbot_ingest_settings_byoi_ingest_mapping_by_id**
> IngestMappingSchema retrieve_healthbot_ingest_settings_byoi_ingest_mapping_by_id(name, authorization=authorization, working=working)

Retrieve ingest-mapping by ID

Retrieve ingest-mapping by name

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
name = 'name_example' # str | Name of ingest-mapping
authorization = 'authorization_example' # str | authentication header object (optional)
working = true # bool | true queries undeployed configuration (optional)

try:
    # Retrieve ingest-mapping by ID
    api_response = api_instance.retrieve_healthbot_ingest_settings_byoi_ingest_mapping_by_id(name, authorization=authorization, working=working)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->retrieve_healthbot_ingest_settings_byoi_ingest_mapping_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of ingest-mapping | 
 **authorization** | **str**| authentication header object | [optional] 
 **working** | **bool**| true queries undeployed configuration | [optional] 

### Return type

[**IngestMappingSchema**](IngestMappingSchema.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_healthbot_ingest_settings_byoi_ingest_mappings**
> list[str] retrieve_healthbot_ingest_settings_byoi_ingest_mappings(authorization=authorization, working=working)

Retrieve ingest-mapping

Retrieve all the ingest mappings configured.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
authorization = 'authorization_example' # str | authentication header object (optional)
working = true # bool | true queries undeployed configuration (optional)

try:
    # Retrieve ingest-mapping
    api_response = api_instance.retrieve_healthbot_ingest_settings_byoi_ingest_mappings(authorization=authorization, working=working)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->retrieve_healthbot_ingest_settings_byoi_ingest_mappings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| authentication header object | [optional] 
 **working** | **bool**| true queries undeployed configuration | [optional] 

### Return type

**list[str]**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_healthbot_ingest_settings_frequency_profile**
> list[str] retrieve_healthbot_ingest_settings_frequency_profile(authorization=authorization, working=working)

Retrieve frequency-profile

Retrieve operation of resource: frequency-profile

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
authorization = 'authorization_example' # str | authentication header object (optional)
working = true # bool | true queries undeployed configuration (optional)

try:
    # Retrieve frequency-profile
    api_response = api_instance.retrieve_healthbot_ingest_settings_frequency_profile(authorization=authorization, working=working)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->retrieve_healthbot_ingest_settings_frequency_profile: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| authentication header object | [optional] 
 **working** | **bool**| true queries undeployed configuration | [optional] 

### Return type

**list[str]**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_healthbot_ingest_settings_frequency_profile_by_id**
> FrequencyProfileSchema retrieve_healthbot_ingest_settings_frequency_profile_by_id(name, authorization=authorization, working=working)

Retrieve frequency-profile by ID

Retrieve operation of resource: frequency-profile

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
authorization = 'authorization_example' # str | authentication header object (optional)
working = true # bool | true queries undeployed configuration (optional)

try:
    # Retrieve frequency-profile by ID
    api_response = api_instance.retrieve_healthbot_ingest_settings_frequency_profile_by_id(name, authorization=authorization, working=working)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->retrieve_healthbot_ingest_settings_frequency_profile_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| ID of name | 
 **authorization** | **str**| authentication header object | [optional] 
 **working** | **bool**| true queries undeployed configuration | [optional] 

### Return type

[**FrequencyProfileSchema**](FrequencyProfileSchema.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_healthbot_system_time_series_database_time_series_database**
> TsdbSchema retrieve_healthbot_system_time_series_database_time_series_database(working=working)

Retrieve time-series-database

Retrieve operation of resource: time-series-database

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
    # Retrieve time-series-database
    api_response = api_instance.retrieve_healthbot_system_time_series_database_time_series_database(working=working)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->retrieve_healthbot_system_time_series_database_time_series_database: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **working** | **bool**| true queries undeployed configuration | [optional] 

### Return type

[**TsdbSchema**](TsdbSchema.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_iceberg_ingest_settings**
> IngestSettingsSchema retrieve_iceberg_ingest_settings(authorization=authorization, working=working)

Retrieve ingest-settings

Retrieve operation of resource: ingest-settings

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
authorization = 'authorization_example' # str | authentication header object (optional)
working = true # bool | true queries undeployed configuration (optional)

try:
    # Retrieve ingest-settings
    api_response = api_instance.retrieve_iceberg_ingest_settings(authorization=authorization, working=working)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->retrieve_iceberg_ingest_settings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| authentication header object | [optional] 
 **working** | **bool**| true queries undeployed configuration | [optional] 

### Return type

[**IngestSettingsSchema**](IngestSettingsSchema.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_iceberg_ingest_settings_flow**
> FlowSchema retrieve_iceberg_ingest_settings_flow(authorization=authorization, working=working)

Retrieve flow

Retrieve operation of resource: flow

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
authorization = 'authorization_example' # str | authentication header object (optional)
working = true # bool | true queries undeployed configuration (optional)

try:
    # Retrieve flow
    api_response = api_instance.retrieve_iceberg_ingest_settings_flow(authorization=authorization, working=working)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->retrieve_iceberg_ingest_settings_flow: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| authentication header object | [optional] 
 **working** | **bool**| true queries undeployed configuration | [optional] 

### Return type

[**FlowSchema**](FlowSchema.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_iceberg_ingest_settings_flow_template_by_id**
> TemplateSchema retrieve_iceberg_ingest_settings_flow_template_by_id(name, authorization=authorization, working=working)

Retrieve template by ID

Retrieve operation of resource: template

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
name = 'name_example' # str | Name of template
authorization = 'authorization_example' # str | authentication header object (optional)
working = true # bool | true queries undeployed configuration (optional)

try:
    # Retrieve template by ID
    api_response = api_instance.retrieve_iceberg_ingest_settings_flow_template_by_id(name, authorization=authorization, working=working)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->retrieve_iceberg_ingest_settings_flow_template_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of template | 
 **authorization** | **str**| authentication header object | [optional] 
 **working** | **bool**| true queries undeployed configuration | [optional] 

### Return type

[**TemplateSchema**](TemplateSchema.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_iceberg_ingest_settings_flow_template_ids**
> list[str] retrieve_iceberg_ingest_settings_flow_template_ids(authorization=authorization, working=working)

Retrieve template

Retrieve operation of resource: template

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
authorization = 'authorization_example' # str | authentication header object (optional)
working = true # bool | true queries undeployed configuration (optional)

try:
    # Retrieve template
    api_response = api_instance.retrieve_iceberg_ingest_settings_flow_template_ids(authorization=authorization, working=working)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->retrieve_iceberg_ingest_settings_flow_template_ids: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| authentication header object | [optional] 
 **working** | **bool**| true queries undeployed configuration | [optional] 

### Return type

**list[str]**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_iceberg_ingest_settings_syslog**
> SyslogSchema retrieve_iceberg_ingest_settings_syslog(authorization=authorization, working=working)

Retrieve syslog

Retrieve operation of resource: syslog

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
authorization = 'authorization_example' # str | authentication header object (optional)
working = true # bool | true queries undeployed configuration (optional)

try:
    # Retrieve syslog
    api_response = api_instance.retrieve_iceberg_ingest_settings_syslog(authorization=authorization, working=working)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->retrieve_iceberg_ingest_settings_syslog: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| authentication header object | [optional] 
 **working** | **bool**| true queries undeployed configuration | [optional] 

### Return type

[**SyslogSchema**](SyslogSchema.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_iceberg_ingest_settings_syslog_pattern_by_id**
> PatternSchema retrieve_iceberg_ingest_settings_syslog_pattern_by_id(name, authorization=authorization, working=working)

Retrieve pattern by ID

Retrieve operation of resource: pattern

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
name = 'name_example' # str | Name of pattern
authorization = 'authorization_example' # str | authentication header object (optional)
working = true # bool | true queries undeployed configuration (optional)

try:
    # Retrieve pattern by ID
    api_response = api_instance.retrieve_iceberg_ingest_settings_syslog_pattern_by_id(name, authorization=authorization, working=working)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->retrieve_iceberg_ingest_settings_syslog_pattern_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of pattern | 
 **authorization** | **str**| authentication header object | [optional] 
 **working** | **bool**| true queries undeployed configuration | [optional] 

### Return type

[**PatternSchema**](PatternSchema.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_iceberg_ingest_settings_syslog_pattern_ids**
> list[str] retrieve_iceberg_ingest_settings_syslog_pattern_ids(authorization=authorization, working=working)

Retrieve pattern

Retrieve operation of resource: pattern

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
authorization = 'authorization_example' # str | authentication header object (optional)
working = true # bool | true queries undeployed configuration (optional)

try:
    # Retrieve pattern
    api_response = api_instance.retrieve_iceberg_ingest_settings_syslog_pattern_ids(authorization=authorization, working=working)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->retrieve_iceberg_ingest_settings_syslog_pattern_ids: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| authentication header object | [optional] 
 **working** | **bool**| true queries undeployed configuration | [optional] 

### Return type

**list[str]**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_iceberg_ingest_settings_syslog_pattern_set_by_id**
> PatternSetSchema retrieve_iceberg_ingest_settings_syslog_pattern_set_by_id(name, authorization=authorization, working=working)

Retrieve pattern-set by ID

Retrieve operation of resource: pattern-set

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
name = 'name_example' # str | Name of patter-set
authorization = 'authorization_example' # str | authentication header object (optional)
working = true # bool | true queries undeployed configuration (optional)

try:
    # Retrieve pattern-set by ID
    api_response = api_instance.retrieve_iceberg_ingest_settings_syslog_pattern_set_by_id(name, authorization=authorization, working=working)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->retrieve_iceberg_ingest_settings_syslog_pattern_set_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of patter-set | 
 **authorization** | **str**| authentication header object | [optional] 
 **working** | **bool**| true queries undeployed configuration | [optional] 

### Return type

[**PatternSetSchema**](PatternSetSchema.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_iceberg_ingest_settings_syslog_pattern_set_ids**
> list[str] retrieve_iceberg_ingest_settings_syslog_pattern_set_ids(authorization=authorization, working=working)

Retrieve pattern-set

Retrieve operation of resource: pattern-set

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
authorization = 'authorization_example' # str | authentication header object (optional)
working = true # bool | true queries undeployed configuration (optional)

try:
    # Retrieve pattern-set
    api_response = api_instance.retrieve_iceberg_ingest_settings_syslog_pattern_set_ids(authorization=authorization, working=working)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->retrieve_iceberg_ingest_settings_syslog_pattern_set_ids: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| authentication header object | [optional] 
 **working** | **bool**| true queries undeployed configuration | [optional] 

### Return type

**list[str]**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_iceberg_ingest_settings_syslog_pattern_sets**
> list[PatternSetSchema] retrieve_iceberg_ingest_settings_syslog_pattern_sets(authorization=authorization, working=working)

Retrieve pattern-set by ID

Retrieve operation of resource: pattern-set

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
authorization = 'authorization_example' # str | authentication header object (optional)
working = true # bool | true queries undeployed configuration (optional)

try:
    # Retrieve pattern-set by ID
    api_response = api_instance.retrieve_iceberg_ingest_settings_syslog_pattern_sets(authorization=authorization, working=working)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->retrieve_iceberg_ingest_settings_syslog_pattern_sets: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| authentication header object | [optional] 
 **working** | **bool**| true queries undeployed configuration | [optional] 

### Return type

[**list[PatternSetSchema]**](PatternSetSchema.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_iceberg_ingest_settings_syslog_patterns**
> list[PatternSchema] retrieve_iceberg_ingest_settings_syslog_patterns(authorization=authorization, working=working)

Retrieve pattern by ID

Retrieve operation of resource: pattern

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
authorization = 'authorization_example' # str | authentication header object (optional)
working = true # bool | true queries undeployed configuration (optional)

try:
    # Retrieve pattern by ID
    api_response = api_instance.retrieve_iceberg_ingest_settings_syslog_patterns(authorization=authorization, working=working)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->retrieve_iceberg_ingest_settings_syslog_patterns: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| authentication header object | [optional] 
 **working** | **bool**| true queries undeployed configuration | [optional] 

### Return type

[**list[PatternSchema]**](PatternSchema.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_iceberg_profile_data_summarization_raw_by_id**
> RawSchema retrieve_iceberg_profile_data_summarization_raw_by_id(name, authorization=authorization, working=working)

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
name = 'name_example' # str | Name of raw-data-summarization
authorization = 'authorization_example' # str | authentication header object (optional)
working = true # bool | true queries undeployed configuration (optional)

try:
    # Retrieve raw-data-summarization by ID
    api_response = api_instance.retrieve_iceberg_profile_data_summarization_raw_by_id(name, authorization=authorization, working=working)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->retrieve_iceberg_profile_data_summarization_raw_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of raw-data-summarization | 
 **authorization** | **str**| authentication header object | [optional] 
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
> RawSchema retrieve_iceberg_profile_data_summarizations_raw(authorization=authorization, working=working)

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
authorization = 'authorization_example' # str | authentication header object (optional)
working = true # bool | true queries undeployed configuration (optional)

try:
    # Retrieve raw-data-summarization
    api_response = api_instance.retrieve_iceberg_profile_data_summarizations_raw(authorization=authorization, working=working)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->retrieve_iceberg_profile_data_summarizations_raw: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| authentication header object | [optional] 
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
> CaProfileSchema retrieve_iceberg_profile_security_ca_profile_by_id(name, authorization=authorization, working=working)

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
name = 'name_example' # str | Name of ca-profile
authorization = 'authorization_example' # str | authentication header object (optional)
working = true # bool | true queries undeployed configuration (optional)

try:
    # Retrieve ca-profile by ID
    api_response = api_instance.retrieve_iceberg_profile_security_ca_profile_by_id(name, authorization=authorization, working=working)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->retrieve_iceberg_profile_security_ca_profile_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of ca-profile | 
 **authorization** | **str**| authentication header object | [optional] 
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
> list[str] retrieve_iceberg_profile_security_ca_profiles(authorization=authorization, working=working)

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
authorization = 'authorization_example' # str | authentication header object (optional)
working = true # bool | true queries undeployed configuration (optional)

try:
    # Retrieve ca-profile
    api_response = api_instance.retrieve_iceberg_profile_security_ca_profiles(authorization=authorization, working=working)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->retrieve_iceberg_profile_security_ca_profiles: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| authentication header object | [optional] 
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
> LocalCertificateSchema retrieve_iceberg_profile_security_local_certificate_by_id(name, authorization=authorization, working=working)

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
name = 'name_example' # str | Name of local-certificate
authorization = 'authorization_example' # str | authentication header object (optional)
working = true # bool | true queries undeployed configuration (optional)

try:
    # Retrieve local-certificate by ID
    api_response = api_instance.retrieve_iceberg_profile_security_local_certificate_by_id(name, authorization=authorization, working=working)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->retrieve_iceberg_profile_security_local_certificate_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of local-certificate | 
 **authorization** | **str**| authentication header object | [optional] 
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
> list[str] retrieve_iceberg_profile_security_local_certificates(authorization=authorization, working=working)

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
authorization = 'authorization_example' # str | authentication header object (optional)
working = true # bool | true queries undeployed configuration (optional)

try:
    # Retrieve local-certificate
    api_response = api_instance.retrieve_iceberg_profile_security_local_certificates(authorization=authorization, working=working)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->retrieve_iceberg_profile_security_local_certificates: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| authentication header object | [optional] 
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
> SshKeyProfileSchema retrieve_iceberg_profile_security_ssh_key_profile_by_id(name, authorization=authorization, working=working)

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
name = 'name_example' # str | Name of ssh-key-profile
authorization = 'authorization_example' # str | authentication header object (optional)
working = true # bool | true queries undeployed configuration (optional)

try:
    # Retrieve ssh-key-profile by ID
    api_response = api_instance.retrieve_iceberg_profile_security_ssh_key_profile_by_id(name, authorization=authorization, working=working)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->retrieve_iceberg_profile_security_ssh_key_profile_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of ssh-key-profile | 
 **authorization** | **str**| authentication header object | [optional] 
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
> list[str] retrieve_iceberg_profile_security_ssh_key_profiles(authorization=authorization, working=working)

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
authorization = 'authorization_example' # str | authentication header object (optional)
working = true # bool | true queries undeployed configuration (optional)

try:
    # Retrieve ssh-key-profile
    api_response = api_instance.retrieve_iceberg_profile_security_ssh_key_profiles(authorization=authorization, working=working)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->retrieve_iceberg_profile_security_ssh_key_profiles: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| authentication header object | [optional] 
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
> ProfilesSchema retrieve_iceberg_profiles(authorization=authorization, working=working)

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
authorization = 'authorization_example' # str | authentication header object (optional)
working = true # bool | true queries undeployed configuration (optional)

try:
    # Retrieve profile
    api_response = api_instance.retrieve_iceberg_profiles(authorization=authorization, working=working)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->retrieve_iceberg_profiles: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| authentication header object | [optional] 
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
> list[str] retrieve_sensors(sensor_type, authorization=authorization, sensor_name=sensor_name, depth=depth, append=append, snmp_table=snmp_table)

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
authorization = 'authorization_example' # str | authentication header object (optional)
sensor_name = 'sensor_name_example' # str | Sensor name prefix. (optional)
depth = 56 # int | Relative depth to the `sensor_name`. (optional)
append = true # bool | Returns full path of the sensor. (optional)
snmp_table = 'snmp_table_example' # str | Returns list of all the columns for the particular snmp_table (optional)

try:
    # List all OpenConfig sensors.
    api_response = api_instance.retrieve_sensors(sensor_type, authorization=authorization, sensor_name=sensor_name, depth=depth, append=append, snmp_table=snmp_table)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->retrieve_sensors: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sensor_type** | **str**| Sensor type | 
 **authorization** | **str**| authentication header object | [optional] 
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

# **update_healthbot_ingest_settings_byoi_custom_plugin_by_id**
> update_healthbot_ingest_settings_byoi_custom_plugin_by_id(name, custom_plugin, authorization=authorization)

Update custom-plugin by ID

Update operation of resource: custom-plugin

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
name = 'name_example' # str | Name of custom-plugin
custom_plugin = swagger_client.CustomPluginSchema() # CustomPluginSchema | custom_pluginbody object
authorization = 'authorization_example' # str | authentication header object (optional)

try:
    # Update custom-plugin by ID
    api_instance.update_healthbot_ingest_settings_byoi_custom_plugin_by_id(name, custom_plugin, authorization=authorization)
except ApiException as e:
    print("Exception when calling DefaultApi->update_healthbot_ingest_settings_byoi_custom_plugin_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of custom-plugin | 
 **custom_plugin** | [**CustomPluginSchema**](CustomPluginSchema.md)| custom_pluginbody object | 
 **authorization** | **str**| authentication header object | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_healthbot_ingest_settings_byoi_default_plugin_tlive_kafka_by_id**
> update_healthbot_ingest_settings_byoi_default_plugin_tlive_kafka_by_id(name, tlive_kafka, authorization=authorization)

Update tlive-kafka-oc by ID

Update operation of resource: tlive-kafka-oc

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
name = 'name_example' # str | Name of tlive-kafka-oc
tlive_kafka = swagger_client.TliveKafkaOcSchema() # TliveKafkaOcSchema | tlive_kafka body object
authorization = 'authorization_example' # str | authentication header object (optional)

try:
    # Update tlive-kafka-oc by ID
    api_instance.update_healthbot_ingest_settings_byoi_default_plugin_tlive_kafka_by_id(name, tlive_kafka, authorization=authorization)
except ApiException as e:
    print("Exception when calling DefaultApi->update_healthbot_ingest_settings_byoi_default_plugin_tlive_kafka_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of tlive-kafka-oc | 
 **tlive_kafka** | [**TliveKafkaOcSchema**](TliveKafkaOcSchema.md)| tlive_kafka body object | 
 **authorization** | **str**| authentication header object | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_healthbot_ingest_settings_byoi_ingest_mapping_by_id**
> update_healthbot_ingest_settings_byoi_ingest_mapping_by_id(name, ingest_mapping, authorization=authorization)

Update ingest-mapping by ID

Update ingest-mapping by name

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
name = 'name_example' # str | Name of ingest-mapping
ingest_mapping = swagger_client.IngestMappingSchema() # IngestMappingSchema | ingest_mappingbody object
authorization = 'authorization_example' # str | authentication header object (optional)

try:
    # Update ingest-mapping by ID
    api_instance.update_healthbot_ingest_settings_byoi_ingest_mapping_by_id(name, ingest_mapping, authorization=authorization)
except ApiException as e:
    print("Exception when calling DefaultApi->update_healthbot_ingest_settings_byoi_ingest_mapping_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of ingest-mapping | 
 **ingest_mapping** | [**IngestMappingSchema**](IngestMappingSchema.md)| ingest_mappingbody object | 
 **authorization** | **str**| authentication header object | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_healthbot_ingest_settings_frequency_profile_by_id**
> update_healthbot_ingest_settings_frequency_profile_by_id(name, frequency_profile, authorization=authorization)

Update frequency-profile by ID

Update operation of resource: frequency-profile

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
frequency_profile = swagger_client.FrequencyProfileSchema() # FrequencyProfileSchema | frequency_profilebody object
authorization = 'authorization_example' # str | authentication header object (optional)

try:
    # Update frequency-profile by ID
    api_instance.update_healthbot_ingest_settings_frequency_profile_by_id(name, frequency_profile, authorization=authorization)
except ApiException as e:
    print("Exception when calling DefaultApi->update_healthbot_ingest_settings_frequency_profile_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| ID of name | 
 **frequency_profile** | [**FrequencyProfileSchema**](FrequencyProfileSchema.md)| frequency_profilebody object | 
 **authorization** | **str**| authentication header object | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_healthbot_system_time_series_database_time_series_database_by_id**
> update_healthbot_system_time_series_database_time_series_database_by_id(time_series_database)

Update time-series-database by ID

Update operation of resource: time-series-database

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
time_series_database = swagger_client.TsdbSchema() # TsdbSchema | time_series_databasebody object

try:
    # Update time-series-database by ID
    api_instance.update_healthbot_system_time_series_database_time_series_database_by_id(time_series_database)
except ApiException as e:
    print("Exception when calling DefaultApi->update_healthbot_system_time_series_database_time_series_database_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **time_series_database** | [**TsdbSchema**](TsdbSchema.md)| time_series_databasebody object | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_iceberg_ingest_settings**
> update_iceberg_ingest_settings(ingest_settings, authorization=authorization)

Update ingest-settings by ID

Update operation of resource: ingest-settings

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
ingest_settings = swagger_client.IngestSettingsSchema() # IngestSettingsSchema | ingest_settingsbody object
authorization = 'authorization_example' # str | authentication header object (optional)

try:
    # Update ingest-settings by ID
    api_instance.update_iceberg_ingest_settings(ingest_settings, authorization=authorization)
except ApiException as e:
    print("Exception when calling DefaultApi->update_iceberg_ingest_settings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ingest_settings** | [**IngestSettingsSchema**](IngestSettingsSchema.md)| ingest_settingsbody object | 
 **authorization** | **str**| authentication header object | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_iceberg_ingest_settings_flow**
> update_iceberg_ingest_settings_flow(flow, authorization=authorization)

Update flow by ID

Update operation of resource: flow

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
flow = swagger_client.FlowSchema() # FlowSchema | flowbody object
authorization = 'authorization_example' # str | authentication header object (optional)

try:
    # Update flow by ID
    api_instance.update_iceberg_ingest_settings_flow(flow, authorization=authorization)
except ApiException as e:
    print("Exception when calling DefaultApi->update_iceberg_ingest_settings_flow: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **flow** | [**FlowSchema**](FlowSchema.md)| flowbody object | 
 **authorization** | **str**| authentication header object | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_iceberg_ingest_settings_flow_template_by_id**
> update_iceberg_ingest_settings_flow_template_by_id(name, template, authorization=authorization)

Update template by ID

Update operation of resource: template

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
name = 'name_example' # str | Name of template
template = swagger_client.TemplateSchema() # TemplateSchema | templatebody object
authorization = 'authorization_example' # str | authentication header object (optional)

try:
    # Update template by ID
    api_instance.update_iceberg_ingest_settings_flow_template_by_id(name, template, authorization=authorization)
except ApiException as e:
    print("Exception when calling DefaultApi->update_iceberg_ingest_settings_flow_template_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of template | 
 **template** | [**TemplateSchema**](TemplateSchema.md)| templatebody object | 
 **authorization** | **str**| authentication header object | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_iceberg_ingest_settings_syslog**
> update_iceberg_ingest_settings_syslog(syslog, authorization=authorization)

Update syslog by ID

Update operation of resource: syslog

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
syslog = swagger_client.SyslogSchema() # SyslogSchema | syslogbody object
authorization = 'authorization_example' # str | authentication header object (optional)

try:
    # Update syslog by ID
    api_instance.update_iceberg_ingest_settings_syslog(syslog, authorization=authorization)
except ApiException as e:
    print("Exception when calling DefaultApi->update_iceberg_ingest_settings_syslog: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **syslog** | [**SyslogSchema**](SyslogSchema.md)| syslogbody object | 
 **authorization** | **str**| authentication header object | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_iceberg_ingest_settings_syslog_pattern_by_id**
> update_iceberg_ingest_settings_syslog_pattern_by_id(name, pattern, authorization=authorization)

Update pattern by ID

Update operation of resource: pattern

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
name = 'name_example' # str | Name of pattern
pattern = swagger_client.PatternSchema() # PatternSchema | patternbody object
authorization = 'authorization_example' # str | authentication header object (optional)

try:
    # Update pattern by ID
    api_instance.update_iceberg_ingest_settings_syslog_pattern_by_id(name, pattern, authorization=authorization)
except ApiException as e:
    print("Exception when calling DefaultApi->update_iceberg_ingest_settings_syslog_pattern_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of pattern | 
 **pattern** | [**PatternSchema**](PatternSchema.md)| patternbody object | 
 **authorization** | **str**| authentication header object | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_iceberg_ingest_settings_syslog_pattern_set_by_id**
> update_iceberg_ingest_settings_syslog_pattern_set_by_id(name, pattern_set, authorization=authorization)

Update pattern-set by ID

Update operation of resource: pattern-set

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
name = 'name_example' # str | Name of pattern-set
pattern_set = swagger_client.PatternSetSchema() # PatternSetSchema | pattern_setbody object
authorization = 'authorization_example' # str | authentication header object (optional)

try:
    # Update pattern-set by ID
    api_instance.update_iceberg_ingest_settings_syslog_pattern_set_by_id(name, pattern_set, authorization=authorization)
except ApiException as e:
    print("Exception when calling DefaultApi->update_iceberg_ingest_settings_syslog_pattern_set_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of pattern-set | 
 **pattern_set** | [**PatternSetSchema**](PatternSetSchema.md)| pattern_setbody object | 
 **authorization** | **str**| authentication header object | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_iceberg_profile_data_summarization_raw_by_id**
> update_iceberg_profile_data_summarization_raw_by_id(name, raw_data_summarization, authorization=authorization)

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
name = 'name_example' # str | Name of raw-data-summarization
raw_data_summarization = swagger_client.RawSchema() # RawSchema | raw_data_summarizationbody object
authorization = 'authorization_example' # str | authentication header object (optional)

try:
    # Update raw-data-summarization by ID
    api_instance.update_iceberg_profile_data_summarization_raw_by_id(name, raw_data_summarization, authorization=authorization)
except ApiException as e:
    print("Exception when calling DefaultApi->update_iceberg_profile_data_summarization_raw_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of raw-data-summarization | 
 **raw_data_summarization** | [**RawSchema**](RawSchema.md)| raw_data_summarizationbody object | 
 **authorization** | **str**| authentication header object | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_iceberg_profile_security_ca_profile_by_id**
> update_iceberg_profile_security_ca_profile_by_id(name, ca_profile, authorization=authorization)

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
name = 'name_example' # str | Name of ca-profile
ca_profile = swagger_client.CaProfileSchema() # CaProfileSchema | ca_profilebody object
authorization = 'authorization_example' # str | authentication header object (optional)

try:
    # Update ca-profile by ID
    api_instance.update_iceberg_profile_security_ca_profile_by_id(name, ca_profile, authorization=authorization)
except ApiException as e:
    print("Exception when calling DefaultApi->update_iceberg_profile_security_ca_profile_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of ca-profile | 
 **ca_profile** | [**CaProfileSchema**](CaProfileSchema.md)| ca_profilebody object | 
 **authorization** | **str**| authentication header object | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_iceberg_profile_security_local_certificate_by_id**
> update_iceberg_profile_security_local_certificate_by_id(name, local_certificate, authorization=authorization)

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
name = 'name_example' # str | Name of local-certificate
local_certificate = swagger_client.LocalCertificateSchema() # LocalCertificateSchema | local_certificatebody object
authorization = 'authorization_example' # str | authentication header object (optional)

try:
    # Update local-certificate by ID
    api_instance.update_iceberg_profile_security_local_certificate_by_id(name, local_certificate, authorization=authorization)
except ApiException as e:
    print("Exception when calling DefaultApi->update_iceberg_profile_security_local_certificate_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of local-certificate | 
 **local_certificate** | [**LocalCertificateSchema**](LocalCertificateSchema.md)| local_certificatebody object | 
 **authorization** | **str**| authentication header object | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_iceberg_profile_security_ssh_key_profile_by_id**
> update_iceberg_profile_security_ssh_key_profile_by_id(name, ssh_key_profile, authorization=authorization)

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
name = 'name_example' # str | Name of ssh-key-profile
ssh_key_profile = swagger_client.SshKeyProfileSchema() # SshKeyProfileSchema | ssh_key_profilebody object
authorization = 'authorization_example' # str | authentication header object (optional)

try:
    # Update ssh-key-profile by ID
    api_instance.update_iceberg_profile_security_ssh_key_profile_by_id(name, ssh_key_profile, authorization=authorization)
except ApiException as e:
    print("Exception when calling DefaultApi->update_iceberg_profile_security_ssh_key_profile_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of ssh-key-profile | 
 **ssh_key_profile** | [**SshKeyProfileSchema**](SshKeyProfileSchema.md)| ssh_key_profilebody object | 
 **authorization** | **str**| authentication header object | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_iceberg_profiles**
> update_iceberg_profiles(profile, authorization=authorization)

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
authorization = 'authorization_example' # str | authentication header object (optional)

try:
    # Update profile by ID
    api_instance.update_iceberg_profiles(profile, authorization=authorization)
except ApiException as e:
    print("Exception when calling DefaultApi->update_iceberg_profiles: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **profile** | [**ProfilesSchema**](ProfilesSchema.md)| profilebody object | 
 **authorization** | **str**| authentication header object | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

