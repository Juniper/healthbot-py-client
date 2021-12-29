# swagger_client.DefaultApi

All URIs are relative to *http://api-server/api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**backup_grafana**](DefaultApi.md#backup_grafana) | **GET** /grafana/backup/ | Take backup of Grafana configuration
[**backup_helper_files**](DefaultApi.md#backup_helper_files) | **GET** /config/files/helper-files/backup/ | Download the tar file containing all helper files.
[**create_dynamic_tagging_by_key**](DefaultApi.md#create_dynamic_tagging_by_key) | **POST** /config/dynamic-tagging/key/ | Creates Dynamic-tagging key-value
[**create_files_certificates_by_file_name**](DefaultApi.md#create_files_certificates_by_file_name) | **POST** /config/files/certificates/{file_name}/ | Upload a certificate file.
[**create_files_helper_files_by_file_name**](DefaultApi.md#create_files_helper_files_by_file_name) | **POST** /config/files/helper-files/{file_name}/ | Upload a helper-file.
[**create_healthbot_deployment_deployment_by_id**](DefaultApi.md#create_healthbot_deployment_deployment_by_id) | **POST** /config/deployment/ | Create deployment by ID
[**create_healthbot_dynamic_tagging**](DefaultApi.md#create_healthbot_dynamic_tagging) | **POST** /config/dynamic-tagging/keys/ | Create dynamic-tagging by ID
[**create_healthbot_ingest_byoi_custom_plugin_by_id**](DefaultApi.md#create_healthbot_ingest_byoi_custom_plugin_by_id) | **POST** /config/ingest/byoi/custom-plugin/{name}/ | Create custom-plugin by ID
[**create_healthbot_ingest_byoi_default_plugin_tlive_kafka_by_id**](DefaultApi.md#create_healthbot_ingest_byoi_default_plugin_tlive_kafka_by_id) | **POST** /config/ingest/byoi/default-plugin/tlive-kafka-oc/{name}/ | Create tlive-kafka-oc by ID
[**create_healthbot_ingest_byoi_ingest_mapping_by_id**](DefaultApi.md#create_healthbot_ingest_byoi_ingest_mapping_by_id) | **POST** /config/ingest/byoi/ingest-mapping/{name}/ | Create ingest-mapping by ID
[**create_healthbot_ingest_frequency_profile_by_id**](DefaultApi.md#create_healthbot_ingest_frequency_profile_by_id) | **POST** /config/ingest/frequency-profile/{name}/ | Create frequency-profile by ID
[**create_healthbot_ingest_outbound_ssh**](DefaultApi.md#create_healthbot_ingest_outbound_ssh) | **POST** /config/ingest/outbound-ssh/ | Create outbound-ssh by ID
[**create_healthbot_ingest_settings_byoi_custom_plugin_by_id**](DefaultApi.md#create_healthbot_ingest_settings_byoi_custom_plugin_by_id) | **POST** /config/ingest-settings/byoi/custom-plugin/{name}/ | Create custom-plugin by ID
[**create_healthbot_ingest_settings_byoi_default_plugin_tlive_kafka_by_id**](DefaultApi.md#create_healthbot_ingest_settings_byoi_default_plugin_tlive_kafka_by_id) | **POST** /config/ingest-settings/byoi/default-plugin/tlive-kafka-oc/{name}/ | Create tlive-kafka-oc by ID
[**create_healthbot_ingest_settings_byoi_ingest_mapping_by_id**](DefaultApi.md#create_healthbot_ingest_settings_byoi_ingest_mapping_by_id) | **POST** /config/ingest-settings/byoi/ingest-mapping/{name}/ | Create ingest-mapping by ID
[**create_healthbot_ingest_settings_frequency_profile_by_id**](DefaultApi.md#create_healthbot_ingest_settings_frequency_profile_by_id) | **POST** /config/ingest-settings/frequency-profile/{name}/ | Create frequency-profile by ID
[**create_healthbot_ingest_settings_tagging_profile_by_id**](DefaultApi.md#create_healthbot_ingest_settings_tagging_profile_by_id) | **POST** /config/ingest-settings/data-enrichment/tagging-profile/{name}/ | Create tagging-profile by ID
[**create_healthbot_ingest_settings_tagging_profiles**](DefaultApi.md#create_healthbot_ingest_settings_tagging_profiles) | **POST** /config/ingest-settings/data-enrichment/tagging-profiles/ | Create tagging-profile by ID
[**create_healthbot_ingest_sflow**](DefaultApi.md#create_healthbot_ingest_sflow) | **POST** /config/ingest/sflow/ | Create sflow by ID
[**create_healthbot_ingest_sflow_counter_record_by_id**](DefaultApi.md#create_healthbot_ingest_sflow_counter_record_by_id) | **POST** /config/ingest/sflow/counter-record/{record_name}/ | Create counter-record by ID
[**create_healthbot_ingest_sflow_flow_record_by_id**](DefaultApi.md#create_healthbot_ingest_sflow_flow_record_by_id) | **POST** /config/ingest/sflow/flow-record/{record_name}/ | Create flow-record by ID
[**create_healthbot_ingest_sflow_protocol_by_id**](DefaultApi.md#create_healthbot_ingest_sflow_protocol_by_id) | **POST** /config/ingest/sflow/protocol/{protocol_name}/ | Create protocol by ID
[**create_healthbot_ingest_sflow_sample_by_id**](DefaultApi.md#create_healthbot_ingest_sflow_sample_by_id) | **POST** /config/ingest/sflow/sample/{sample_name}/ | Create sample by ID
[**create_healthbot_ingest_snmp_notification**](DefaultApi.md#create_healthbot_ingest_snmp_notification) | **POST** /config/ingest/snmp-notification/ | Create snmp-notification by ID
[**create_healthbot_ingest_snmp_notification_v3_usm_user_by_id**](DefaultApi.md#create_healthbot_ingest_snmp_notification_v3_usm_user_by_id) | **POST** /config/ingest/snmp-notification/v3/usm/user/{name}/ | Create SNMPv3 user by UserName(ID)
[**create_healthbot_ingest_syslog_header_pattern_by_id**](DefaultApi.md#create_healthbot_ingest_syslog_header_pattern_by_id) | **POST** /config/ingest/syslog/header-pattern/{name}/ | Create pattern by ID
[**create_healthbot_ingest_tagging_profile_by_id**](DefaultApi.md#create_healthbot_ingest_tagging_profile_by_id) | **POST** /config/ingest/data-enrichment/tagging-profile/{name}/ | Create tagging-profile by ID
[**create_healthbot_ingest_tagging_profiles**](DefaultApi.md#create_healthbot_ingest_tagging_profiles) | **POST** /config/ingest/data-enrichment/tagging-profiles/ | Create tagging-profile by ID
[**create_healthbot_organization_organization_by_id**](DefaultApi.md#create_healthbot_organization_organization_by_id) | **POST** /config/organization/{organization_name}/ | Create organization by ID
[**create_healthbot_profile_rollup_summarization_field_profile_field_profile_by_id**](DefaultApi.md#create_healthbot_profile_rollup_summarization_field_profile_field_profile_by_id) | **POST** /config/profile/rollup-summarization/field-profile/{profile_id}/ | Create field-profile by ID
[**create_healthbot_system_time_series_database_time_series_database_by_id**](DefaultApi.md#create_healthbot_system_time_series_database_time_series_database_by_id) | **POST** /config/system/tsdb/ | Create time-series-database by ID
[**create_healthbot_system_trigger_action**](DefaultApi.md#create_healthbot_system_trigger_action) | **POST** /config/system/trigger_action/ | Create trigger-action
[**create_iceberg_ingest**](DefaultApi.md#create_iceberg_ingest) | **POST** /config/ingest/ | Create ingest by ID
[**create_iceberg_ingest_flow**](DefaultApi.md#create_iceberg_ingest_flow) | **POST** /config/ingest/flow/ | Create flow by ID
[**create_iceberg_ingest_flow_template_by_id**](DefaultApi.md#create_iceberg_ingest_flow_template_by_id) | **POST** /config/ingest/flow/template/{name}/ | Create template by ID
[**create_iceberg_ingest_native_gpb**](DefaultApi.md#create_iceberg_ingest_native_gpb) | **POST** /config/ingest/native-gpb/ | Create native-gpb by ID
[**create_iceberg_ingest_settings**](DefaultApi.md#create_iceberg_ingest_settings) | **POST** /config/ingest-settings/ | Create ingest-settings by ID
[**create_iceberg_ingest_settings_flow**](DefaultApi.md#create_iceberg_ingest_settings_flow) | **POST** /config/ingest-settings/flow/ | Create flow by ID
[**create_iceberg_ingest_settings_flow_template_by_id**](DefaultApi.md#create_iceberg_ingest_settings_flow_template_by_id) | **POST** /config/ingest-settings/flow/template/{name}/ | Create template by ID
[**create_iceberg_ingest_settings_syslog**](DefaultApi.md#create_iceberg_ingest_settings_syslog) | **POST** /config/ingest-settings/syslog/ | Create syslog by ID
[**create_iceberg_ingest_settings_syslog_pattern_by_id**](DefaultApi.md#create_iceberg_ingest_settings_syslog_pattern_by_id) | **POST** /config/ingest-settings/syslog/pattern/{name}/ | Create pattern by ID
[**create_iceberg_ingest_settings_syslog_pattern_set_by_id**](DefaultApi.md#create_iceberg_ingest_settings_syslog_pattern_set_by_id) | **POST** /config/ingest-settings/syslog/pattern-set/{name}/ | Create pattern-set by ID
[**create_iceberg_ingest_syslog**](DefaultApi.md#create_iceberg_ingest_syslog) | **POST** /config/ingest/syslog/ | Create syslog by ID
[**create_iceberg_ingest_syslog_pattern_by_id**](DefaultApi.md#create_iceberg_ingest_syslog_pattern_by_id) | **POST** /config/ingest/syslog/pattern/{name}/ | Create pattern by ID
[**create_iceberg_ingest_syslog_pattern_set_by_id**](DefaultApi.md#create_iceberg_ingest_syslog_pattern_set_by_id) | **POST** /config/ingest/syslog/pattern-set/{name}/ | Create pattern-set by ID
[**create_iceberg_profile_data_summarization_raw_by_id**](DefaultApi.md#create_iceberg_profile_data_summarization_raw_by_id) | **POST** /config/profile/data-summarization/raw/{name}/ | Create raw-data-summarization by ID
[**create_iceberg_profile_security_ca_profile_by_id**](DefaultApi.md#create_iceberg_profile_security_ca_profile_by_id) | **POST** /config/profile/security/ca-profile/{name}/ | Create ca-profile by ID
[**create_iceberg_profile_security_local_certificate_by_id**](DefaultApi.md#create_iceberg_profile_security_local_certificate_by_id) | **POST** /config/profile/security/local-certificate/{name}/ | Create local-certificate by ID
[**create_iceberg_profile_security_ssh_key_profile_by_id**](DefaultApi.md#create_iceberg_profile_security_ssh_key_profile_by_id) | **POST** /config/profile/security/ssh-key-profile/{name}/ | Create ssh-key-profile by ID
[**create_iceberg_profiles**](DefaultApi.md#create_iceberg_profiles) | **POST** /config/profiles/ | Create profile by ID
[**delete_dynamic_tagging_by_key**](DefaultApi.md#delete_dynamic_tagging_by_key) | **DELETE** /config/dynamic-tagging/key/ | Delete Dynamic-tagging key-value
[**delete_files_certificates_by_file_name**](DefaultApi.md#delete_files_certificates_by_file_name) | **DELETE** /config/files/certificates/{file_name}/ | Delete a certificate-file.
[**delete_files_helper_files_by_file_name**](DefaultApi.md#delete_files_helper_files_by_file_name) | **DELETE** /config/files/helper-files/{file_name}/ | Delete a helper-file.
[**delete_healthbot_deployment_deployment_by_id**](DefaultApi.md#delete_healthbot_deployment_deployment_by_id) | **DELETE** /config/deployment/ | Delete deployment by ID
[**delete_healthbot_dynamic_tagging**](DefaultApi.md#delete_healthbot_dynamic_tagging) | **DELETE** /config/dynamic-tagging/keys/ | Delete dynamic-tagging by ID
[**delete_healthbot_ingest_byoi_custom_plugin_by_id**](DefaultApi.md#delete_healthbot_ingest_byoi_custom_plugin_by_id) | **DELETE** /config/ingest/byoi/custom-plugin/{name}/ | Delete custom-plugin by ID
[**delete_healthbot_ingest_byoi_default_plugin_tlive_kafka_by_id**](DefaultApi.md#delete_healthbot_ingest_byoi_default_plugin_tlive_kafka_by_id) | **DELETE** /config/ingest/byoi/default-plugin/tlive-kafka-oc/{name}/ | Delete tlive-kafka-oc by ID
[**delete_healthbot_ingest_byoi_ingest_mapping_by_id**](DefaultApi.md#delete_healthbot_ingest_byoi_ingest_mapping_by_id) | **DELETE** /config/ingest/byoi/ingest-mapping/{name}/ | Delete ingest-mapping by ID
[**delete_healthbot_ingest_frequency_profile_by_id**](DefaultApi.md#delete_healthbot_ingest_frequency_profile_by_id) | **DELETE** /config/ingest/frequency-profile/{name}/ | Delete frequency-profile by ID
[**delete_healthbot_ingest_outbound_ssh**](DefaultApi.md#delete_healthbot_ingest_outbound_ssh) | **DELETE** /config/ingest/outbound-ssh/ | Delete outbound-ssh by ID
[**delete_healthbot_ingest_settings_byoi_custom_plugin_by_id**](DefaultApi.md#delete_healthbot_ingest_settings_byoi_custom_plugin_by_id) | **DELETE** /config/ingest-settings/byoi/custom-plugin/{name}/ | Delete custom-plugin by ID
[**delete_healthbot_ingest_settings_byoi_default_plugin_tlive_kafka_by_id**](DefaultApi.md#delete_healthbot_ingest_settings_byoi_default_plugin_tlive_kafka_by_id) | **DELETE** /config/ingest-settings/byoi/default-plugin/tlive-kafka-oc/{name}/ | Delete tlive-kafka-oc by ID
[**delete_healthbot_ingest_settings_byoi_ingest_mapping_by_id**](DefaultApi.md#delete_healthbot_ingest_settings_byoi_ingest_mapping_by_id) | **DELETE** /config/ingest-settings/byoi/ingest-mapping/{name}/ | Delete ingest-mapping by ID
[**delete_healthbot_ingest_settings_frequency_profile_by_id**](DefaultApi.md#delete_healthbot_ingest_settings_frequency_profile_by_id) | **DELETE** /config/ingest-settings/frequency-profile/{name}/ | Delete frequency-profile by ID
[**delete_healthbot_ingest_settings_tagging_profile_by_id**](DefaultApi.md#delete_healthbot_ingest_settings_tagging_profile_by_id) | **DELETE** /config/ingest-settings/data-enrichment/tagging-profile/{name}/ | Delete tagging-profile by ID
[**delete_healthbot_ingest_settings_tagging_profiles**](DefaultApi.md#delete_healthbot_ingest_settings_tagging_profiles) | **DELETE** /config/ingest-settings/data-enrichment/tagging-profiles/ | Delete tagging-profile by ID
[**delete_healthbot_ingest_sflow**](DefaultApi.md#delete_healthbot_ingest_sflow) | **DELETE** /config/ingest/sflow/ | Delete sflow by ID
[**delete_healthbot_ingest_sflow_counter_record_by_id**](DefaultApi.md#delete_healthbot_ingest_sflow_counter_record_by_id) | **DELETE** /config/ingest/sflow/counter-record/{record_name}/ | Delete counter-record by ID
[**delete_healthbot_ingest_sflow_flow_record_by_id**](DefaultApi.md#delete_healthbot_ingest_sflow_flow_record_by_id) | **DELETE** /config/ingest/sflow/flow-record/{record_name}/ | Delete flow-record by ID
[**delete_healthbot_ingest_sflow_protocol_by_id**](DefaultApi.md#delete_healthbot_ingest_sflow_protocol_by_id) | **DELETE** /config/ingest/sflow/protocol/{protocol_name}/ | Delete protocol by ID
[**delete_healthbot_ingest_sflow_sample_by_id**](DefaultApi.md#delete_healthbot_ingest_sflow_sample_by_id) | **DELETE** /config/ingest/sflow/sample/{sample_name}/ | Delete sample by ID
[**delete_healthbot_ingest_snmp_notification**](DefaultApi.md#delete_healthbot_ingest_snmp_notification) | **DELETE** /config/ingest/snmp-notification/ | Delete snmp-notification
[**delete_healthbot_ingest_snmp_notification_v3_usm_user_by_id**](DefaultApi.md#delete_healthbot_ingest_snmp_notification_v3_usm_user_by_id) | **DELETE** /config/ingest/snmp-notification/v3/usm/user/{name}/ | Delete SNMPv3 user by UserName(ID)
[**delete_healthbot_ingest_syslog_header_pattern_by_id**](DefaultApi.md#delete_healthbot_ingest_syslog_header_pattern_by_id) | **DELETE** /config/ingest/syslog/header-pattern/{name}/ | Delete pattern by ID
[**delete_healthbot_ingest_tagging_profile_by_id**](DefaultApi.md#delete_healthbot_ingest_tagging_profile_by_id) | **DELETE** /config/ingest/data-enrichment/tagging-profile/{name}/ | Delete tagging-profile by ID
[**delete_healthbot_ingest_tagging_profiles**](DefaultApi.md#delete_healthbot_ingest_tagging_profiles) | **DELETE** /config/ingest/data-enrichment/tagging-profiles/ | Delete tagging-profile by ID
[**delete_healthbot_organization_organization_by_id**](DefaultApi.md#delete_healthbot_organization_organization_by_id) | **DELETE** /config/organization/{organization_name}/ | Delete organization by ID
[**delete_healthbot_profile_rollup_summarization_field_profile_field_profile_by_id**](DefaultApi.md#delete_healthbot_profile_rollup_summarization_field_profile_field_profile_by_id) | **DELETE** /config/profile/rollup-summarization/field-profile/{profile_id}/ | Delete field-profile by ID
[**delete_healthbot_system_time_series_database_time_series_database_by_id**](DefaultApi.md#delete_healthbot_system_time_series_database_time_series_database_by_id) | **DELETE** /config/system/tsdb/ | Delete time-series-database
[**delete_healthbot_system_trigger_action**](DefaultApi.md#delete_healthbot_system_trigger_action) | **DELETE** /config/system/trigger_action/ | Delete trigger-action schedulers
[**delete_iceberg_ingest**](DefaultApi.md#delete_iceberg_ingest) | **DELETE** /config/ingest/ | Delete ingest by ID
[**delete_iceberg_ingest_flow**](DefaultApi.md#delete_iceberg_ingest_flow) | **DELETE** /config/ingest/flow/ | Delete flow by ID
[**delete_iceberg_ingest_flow_template_by_id**](DefaultApi.md#delete_iceberg_ingest_flow_template_by_id) | **DELETE** /config/ingest/flow/template/{name}/ | Delete template by ID
[**delete_iceberg_ingest_native_gpb**](DefaultApi.md#delete_iceberg_ingest_native_gpb) | **DELETE** /config/ingest/native-gpb/ | Delete native-gpb by ID
[**delete_iceberg_ingest_settings**](DefaultApi.md#delete_iceberg_ingest_settings) | **DELETE** /config/ingest-settings/ | Delete ingest-settings by ID
[**delete_iceberg_ingest_settings_flow**](DefaultApi.md#delete_iceberg_ingest_settings_flow) | **DELETE** /config/ingest-settings/flow/ | Delete flow by ID
[**delete_iceberg_ingest_settings_flow_template_by_id**](DefaultApi.md#delete_iceberg_ingest_settings_flow_template_by_id) | **DELETE** /config/ingest-settings/flow/template/{name}/ | Delete template by ID
[**delete_iceberg_ingest_settings_syslog**](DefaultApi.md#delete_iceberg_ingest_settings_syslog) | **DELETE** /config/ingest-settings/syslog/ | Delete syslog by ID
[**delete_iceberg_ingest_settings_syslog_pattern_by_id**](DefaultApi.md#delete_iceberg_ingest_settings_syslog_pattern_by_id) | **DELETE** /config/ingest-settings/syslog/pattern/{name}/ | Delete pattern by ID
[**delete_iceberg_ingest_settings_syslog_pattern_set_by_id**](DefaultApi.md#delete_iceberg_ingest_settings_syslog_pattern_set_by_id) | **DELETE** /config/ingest-settings/syslog/pattern-set/{name}/ | Delete pattern-set by ID
[**delete_iceberg_ingest_syslog**](DefaultApi.md#delete_iceberg_ingest_syslog) | **DELETE** /config/ingest/syslog/ | Delete syslog by ID
[**delete_iceberg_ingest_syslog_pattern_by_id**](DefaultApi.md#delete_iceberg_ingest_syslog_pattern_by_id) | **DELETE** /config/ingest/syslog/pattern/{name}/ | Delete pattern by ID
[**delete_iceberg_ingest_syslog_pattern_set_by_id**](DefaultApi.md#delete_iceberg_ingest_syslog_pattern_set_by_id) | **DELETE** /config/ingest/syslog/pattern-set/{name}/ | Delete pattern-set by ID
[**delete_iceberg_profile_data_summarization_raw_by_id**](DefaultApi.md#delete_iceberg_profile_data_summarization_raw_by_id) | **DELETE** /config/profile/data-summarization/raw/{name}/ | Delete raw-data-summarization by ID
[**delete_iceberg_profile_security_ca_profile_by_id**](DefaultApi.md#delete_iceberg_profile_security_ca_profile_by_id) | **DELETE** /config/profile/security/ca-profile/{name}/ | Delete ca-profile by ID
[**delete_iceberg_profile_security_local_certificate_by_id**](DefaultApi.md#delete_iceberg_profile_security_local_certificate_by_id) | **DELETE** /config/profile/security/local-certificate/{name}/ | Delete local-certificate by ID
[**delete_iceberg_profile_security_ssh_key_profile_by_id**](DefaultApi.md#delete_iceberg_profile_security_ssh_key_profile_by_id) | **DELETE** /config/profile/security/ssh-key-profile/{name}/ | Delete ssh-key-profile by ID
[**delete_iceberg_profiles**](DefaultApi.md#delete_iceberg_profiles) | **DELETE** /config/profiles/ | Delete profile by ID
[**get_dynamic_tagging_by_key**](DefaultApi.md#get_dynamic_tagging_by_key) | **GET** /config/dynamic-tagging/key/ | Get value of corresponding Dynamic-tagging key
[**get_fields_from_xpath**](DefaultApi.md#get_fields_from_xpath) | **GET** /field-capture/ | Get last value of all fields before a given timestamp.
[**grafana_login**](DefaultApi.md#grafana_login) | **GET** /grafana/login/ | Login to grafana
[**inspect_command_rpc_table_on_device**](DefaultApi.md#inspect_command_rpc_table_on_device) | **POST** /inspect/command-rpc/table/ | Inspect the given iAgent table.
[**restore_grafana**](DefaultApi.md#restore_grafana) | **POST** /grafana/restore/ | Restore Grafana configuration
[**restore_helper_files**](DefaultApi.md#restore_helper_files) | **POST** /config/files/helper-files/backup/ | Upload a helper-file.
[**retrieve_configuration_jobs**](DefaultApi.md#retrieve_configuration_jobs) | **GET** /config/configuration/jobs/ | 
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
[**retrieve_files_certificates_by_file_name**](DefaultApi.md#retrieve_files_certificates_by_file_name) | **GET** /config/files/certificates/{file_name}/ | Download a certificate-file.
[**retrieve_files_helper_files**](DefaultApi.md#retrieve_files_helper_files) | **GET** /config/files/helper-files/ | Get all helper-file names.
[**retrieve_files_helper_files_by_file_name**](DefaultApi.md#retrieve_files_helper_files_by_file_name) | **GET** /config/files/helper-files/{file_name}/ | Download a helper-file.
[**retrieve_health_all**](DefaultApi.md#retrieve_health_all) | **GET** /health/ | Return a dict with health of devices in device groups and network groups
[**retrieve_health_tree_by_device_group**](DefaultApi.md#retrieve_health_tree_by_device_group) | **GET** /health-tree/device-group/{device_group_name}/ | Get device-group health-tree.
[**retrieve_health_tree_by_id**](DefaultApi.md#retrieve_health_tree_by_id) | **GET** /health-tree/{device_id}/ | Return a device&#39;s health-tree.
[**retrieve_health_tree_by_network_group**](DefaultApi.md#retrieve_health_tree_by_network_group) | **GET** /health-tree/network-group/{network_group_name}/ | Get network-group health-tree.
[**retrieve_healthbot_deployment_deployment**](DefaultApi.md#retrieve_healthbot_deployment_deployment) | **GET** /config/deployment/ | Retrieve deployment
[**retrieve_healthbot_device_details_by_uuids**](DefaultApi.md#retrieve_healthbot_device_details_by_uuids) | **POST** /deployed-device-details/ | Get device-identifying details by for specified UUIDs.
[**retrieve_healthbot_dynamic_tagging**](DefaultApi.md#retrieve_healthbot_dynamic_tagging) | **GET** /config/dynamic-tagging/keys/ | Retrieve dynamic-tagging by ID
[**retrieve_healthbot_ingest_byoi_custom_plugin_by_id**](DefaultApi.md#retrieve_healthbot_ingest_byoi_custom_plugin_by_id) | **GET** /config/ingest/byoi/custom-plugin/{name}/ | Retrieve custom-plugin by ID
[**retrieve_healthbot_ingest_byoi_custom_plugins**](DefaultApi.md#retrieve_healthbot_ingest_byoi_custom_plugins) | **GET** /config/ingest/byoi/custom-plugins/ | Retrieve custom-plugin by ID
[**retrieve_healthbot_ingest_byoi_default_plugin_tlive_kafka_by_id**](DefaultApi.md#retrieve_healthbot_ingest_byoi_default_plugin_tlive_kafka_by_id) | **GET** /config/ingest/byoi/default-plugin/tlive-kafka-oc/{name}/ | Retrieve tlive-kafka-oc by ID
[**retrieve_healthbot_ingest_byoi_default_plugin_tlive_kafkas**](DefaultApi.md#retrieve_healthbot_ingest_byoi_default_plugin_tlive_kafkas) | **GET** /config/ingest/byoi/default-plugin/tlive-kafka-ocs/ | Retrieve tlive-kafka-oc
[**retrieve_healthbot_ingest_byoi_ingest_mapping_by_id**](DefaultApi.md#retrieve_healthbot_ingest_byoi_ingest_mapping_by_id) | **GET** /config/ingest/byoi/ingest-mapping/{name}/ | Retrieve ingest-mapping by ID
[**retrieve_healthbot_ingest_byoi_ingest_mappings**](DefaultApi.md#retrieve_healthbot_ingest_byoi_ingest_mappings) | **GET** /config/ingest/byoi/ingest-mappings/ | Retrieve ingest-mapping
[**retrieve_healthbot_ingest_frequency_profile**](DefaultApi.md#retrieve_healthbot_ingest_frequency_profile) | **GET** /config/ingest/frequency-profiles/ | Retrieve frequency-profile
[**retrieve_healthbot_ingest_frequency_profile_by_id**](DefaultApi.md#retrieve_healthbot_ingest_frequency_profile_by_id) | **GET** /config/ingest/frequency-profile/{name}/ | Retrieve frequency-profile by ID
[**retrieve_healthbot_ingest_outbound_ssh**](DefaultApi.md#retrieve_healthbot_ingest_outbound_ssh) | **GET** /config/ingest/outbound-ssh/ | Retrieve outbound-ssh
[**retrieve_healthbot_ingest_settings_byoi_custom_plugin_by_id**](DefaultApi.md#retrieve_healthbot_ingest_settings_byoi_custom_plugin_by_id) | **GET** /config/ingest-settings/byoi/custom-plugin/{name}/ | Retrieve custom-plugin by ID
[**retrieve_healthbot_ingest_settings_byoi_custom_plugins**](DefaultApi.md#retrieve_healthbot_ingest_settings_byoi_custom_plugins) | **GET** /config/ingest-settings/byoi/custom-plugins/ | Retrieve custom-plugin by ID
[**retrieve_healthbot_ingest_settings_byoi_default_plugin_tlive_kafka_by_id**](DefaultApi.md#retrieve_healthbot_ingest_settings_byoi_default_plugin_tlive_kafka_by_id) | **GET** /config/ingest-settings/byoi/default-plugin/tlive-kafka-oc/{name}/ | Retrieve tlive-kafka-oc by ID
[**retrieve_healthbot_ingest_settings_byoi_default_plugin_tlive_kafkas**](DefaultApi.md#retrieve_healthbot_ingest_settings_byoi_default_plugin_tlive_kafkas) | **GET** /config/ingest-settings/byoi/default-plugin/tlive-kafka-ocs/ | Retrieve tlive-kafka-oc
[**retrieve_healthbot_ingest_settings_byoi_ingest_mapping_by_id**](DefaultApi.md#retrieve_healthbot_ingest_settings_byoi_ingest_mapping_by_id) | **GET** /config/ingest-settings/byoi/ingest-mapping/{name}/ | Retrieve ingest-mapping by ID
[**retrieve_healthbot_ingest_settings_byoi_ingest_mappings**](DefaultApi.md#retrieve_healthbot_ingest_settings_byoi_ingest_mappings) | **GET** /config/ingest-settings/byoi/ingest-mappings/ | Retrieve ingest-mapping
[**retrieve_healthbot_ingest_settings_frequency_profile**](DefaultApi.md#retrieve_healthbot_ingest_settings_frequency_profile) | **GET** /config/ingest-settings/frequency-profiles/ | Retrieve frequency-profile
[**retrieve_healthbot_ingest_settings_frequency_profile_by_id**](DefaultApi.md#retrieve_healthbot_ingest_settings_frequency_profile_by_id) | **GET** /config/ingest-settings/frequency-profile/{name}/ | Retrieve frequency-profile by ID
[**retrieve_healthbot_ingest_settings_tagging_profile_by_id**](DefaultApi.md#retrieve_healthbot_ingest_settings_tagging_profile_by_id) | **GET** /config/ingest-settings/data-enrichment/tagging-profile/{name}/ | Retrieve tagging-profile by ID
[**retrieve_healthbot_ingest_settings_tagging_profiles**](DefaultApi.md#retrieve_healthbot_ingest_settings_tagging_profiles) | **GET** /config/ingest-settings/data-enrichment/tagging-profiles/ | Retrieve tagging-profile by ID
[**retrieve_healthbot_ingest_sflow**](DefaultApi.md#retrieve_healthbot_ingest_sflow) | **GET** /config/ingest/sflow/ | Retrieve sflow
[**retrieve_healthbot_ingest_sflow_counter_record_by_id**](DefaultApi.md#retrieve_healthbot_ingest_sflow_counter_record_by_id) | **GET** /config/ingest/sflow/counter-record/{record_name}/ | Retrieve counter-record by ID
[**retrieve_healthbot_ingest_sflow_flow_record_by_id**](DefaultApi.md#retrieve_healthbot_ingest_sflow_flow_record_by_id) | **GET** /config/ingest/sflow/flow-record/{record_name}/ | Retrieve flow-record by ID
[**retrieve_healthbot_ingest_sflow_protocol_by_id**](DefaultApi.md#retrieve_healthbot_ingest_sflow_protocol_by_id) | **GET** /config/ingest/sflow/protocol/{protocol_name}/ | Retrieve protocol by ID
[**retrieve_healthbot_ingest_sflow_sample_by_id**](DefaultApi.md#retrieve_healthbot_ingest_sflow_sample_by_id) | **GET** /config/ingest/sflow/sample/{sample_name}/ | Retrieve sample by ID
[**retrieve_healthbot_ingest_snmp_notification**](DefaultApi.md#retrieve_healthbot_ingest_snmp_notification) | **GET** /config/ingest/snmp-notification/ | Retrieve snmp-notification
[**retrieve_healthbot_ingest_snmp_notification_v3_usm_user_by_id**](DefaultApi.md#retrieve_healthbot_ingest_snmp_notification_v3_usm_user_by_id) | **GET** /config/ingest/snmp-notification/v3/usm/user/{name}/ | Retrieve SNMPv3 user by UserName(ID)
[**retrieve_healthbot_ingest_snmp_notification_v3_usm_usernames**](DefaultApi.md#retrieve_healthbot_ingest_snmp_notification_v3_usm_usernames) | **GET** /config/ingest/snmp-notification/v3/usm/user/ | Retrieve snmp v3 usm user names
[**retrieve_healthbot_ingest_snmp_notification_v3_usm_users**](DefaultApi.md#retrieve_healthbot_ingest_snmp_notification_v3_usm_users) | **GET** /config/ingest/snmp-notification/v3/usm/users/ | Retrieve SNMP v3 USM users
[**retrieve_healthbot_ingest_syslog_header_pattern_by_id**](DefaultApi.md#retrieve_healthbot_ingest_syslog_header_pattern_by_id) | **GET** /config/ingest/syslog/header-pattern/{name}/ | Retrieve pattern by ID
[**retrieve_healthbot_ingest_syslog_header_pattern_ids**](DefaultApi.md#retrieve_healthbot_ingest_syslog_header_pattern_ids) | **GET** /config/ingest/syslog/header-pattern/ | Retrieve header pattern names
[**retrieve_healthbot_ingest_syslog_header_patterns**](DefaultApi.md#retrieve_healthbot_ingest_syslog_header_patterns) | **GET** /config/ingest/syslog/header-patterns/ | Retrieve header patterns
[**retrieve_healthbot_ingest_tagging_profile_by_id**](DefaultApi.md#retrieve_healthbot_ingest_tagging_profile_by_id) | **GET** /config/ingest/data-enrichment/tagging-profile/{name}/ | Retrieve tagging-profile by ID
[**retrieve_healthbot_ingest_tagging_profiles**](DefaultApi.md#retrieve_healthbot_ingest_tagging_profiles) | **GET** /config/ingest/data-enrichment/tagging-profiles/ | Retrieve tagging-profile by ID
[**retrieve_healthbot_organization_organization**](DefaultApi.md#retrieve_healthbot_organization_organization) | **GET** /config/organization/ | Retrieve organization
[**retrieve_healthbot_organization_organization_by_id**](DefaultApi.md#retrieve_healthbot_organization_organization_by_id) | **GET** /config/organization/{organization_name}/ | Retrieve organization by ID
[**retrieve_healthbot_profile_rollup_summarization_field_profile_field_profile_by_id**](DefaultApi.md#retrieve_healthbot_profile_rollup_summarization_field_profile_field_profile_by_id) | **GET** /config/profile/rollup-summarization/field-profile/{profile_id}/ | Retrieve field-profile by ID
[**retrieve_healthbot_profile_rollup_summarization_field_profile_profile**](DefaultApi.md#retrieve_healthbot_profile_rollup_summarization_field_profile_profile) | **GET** /config/profile/rollup-summarization/field-profile/ | Retrieve field-profile
[**retrieve_healthbot_system_time_series_database_time_series_database**](DefaultApi.md#retrieve_healthbot_system_time_series_database_time_series_database) | **GET** /config/system/tsdb/ | Retrieve time-series-database
[**retrieve_healthbot_system_trigger_action**](DefaultApi.md#retrieve_healthbot_system_trigger_action) | **GET** /config/system/trigger_action/ | Retrieve trigger-action
[**retrieve_healthbot_topic_resource_resource**](DefaultApi.md#retrieve_healthbot_topic_resource_resource) | **GET** /config/topic/{topic_name}/resource/ | List all resource-names in a topic
[**retrieve_healthbot_topic_resource_resource_by_id**](DefaultApi.md#retrieve_healthbot_topic_resource_resource_by_id) | **GET** /config/topic/{topic_name}/resource/{resource_name}/ | Get a resource&#39;s configuration
[**retrieve_iceberg_ingest**](DefaultApi.md#retrieve_iceberg_ingest) | **GET** /config/ingest/ | Retrieve ingest
[**retrieve_iceberg_ingest_flow**](DefaultApi.md#retrieve_iceberg_ingest_flow) | **GET** /config/ingest/flow/ | Retrieve flow
[**retrieve_iceberg_ingest_flow_template_by_id**](DefaultApi.md#retrieve_iceberg_ingest_flow_template_by_id) | **GET** /config/ingest/flow/template/{name}/ | Retrieve template by ID
[**retrieve_iceberg_ingest_flow_template_ids**](DefaultApi.md#retrieve_iceberg_ingest_flow_template_ids) | **GET** /config/ingest/flow/template/ | Retrieve template
[**retrieve_iceberg_ingest_native_gpb**](DefaultApi.md#retrieve_iceberg_ingest_native_gpb) | **GET** /config/ingest/native-gpb/ | Retrieve native-gpb
[**retrieve_iceberg_ingest_settings**](DefaultApi.md#retrieve_iceberg_ingest_settings) | **GET** /config/ingest-settings/ | Retrieve ingest-settings
[**retrieve_iceberg_ingest_settings_flow**](DefaultApi.md#retrieve_iceberg_ingest_settings_flow) | **GET** /config/ingest-settings/flow/ | Retrieve flow
[**retrieve_iceberg_ingest_settings_flow_template_by_id**](DefaultApi.md#retrieve_iceberg_ingest_settings_flow_template_by_id) | **GET** /config/ingest-settings/flow/template/{name}/ | Retrieve template by ID
[**retrieve_iceberg_ingest_settings_flow_template_ids**](DefaultApi.md#retrieve_iceberg_ingest_settings_flow_template_ids) | **GET** /config/ingest-settings/flow/template/ | Retrieve template
[**retrieve_iceberg_ingest_settings_syslog**](DefaultApi.md#retrieve_iceberg_ingest_settings_syslog) | **GET** /config/ingest-settings/syslog/ | Retrieve syslog
[**retrieve_iceberg_ingest_settings_syslog_pattern_by_id**](DefaultApi.md#retrieve_iceberg_ingest_settings_syslog_pattern_by_id) | **GET** /config/ingest-settings/syslog/pattern/{name}/ | Retrieve pattern by ID
[**retrieve_iceberg_ingest_settings_syslog_pattern_ids**](DefaultApi.md#retrieve_iceberg_ingest_settings_syslog_pattern_ids) | **GET** /config/ingest-settings/syslog/pattern/ | Retrieve pattern
[**retrieve_iceberg_ingest_settings_syslog_pattern_set_by_id**](DefaultApi.md#retrieve_iceberg_ingest_settings_syslog_pattern_set_by_id) | **GET** /config/ingest-settings/syslog/pattern-set/{name}/ | Retrieve pattern-set by ID
[**retrieve_iceberg_ingest_settings_syslog_pattern_set_ids**](DefaultApi.md#retrieve_iceberg_ingest_settings_syslog_pattern_set_ids) | **GET** /config/ingest-settings/syslog/pattern-set/ | Retrieve pattern-set
[**retrieve_iceberg_ingest_settings_syslog_pattern_sets**](DefaultApi.md#retrieve_iceberg_ingest_settings_syslog_pattern_sets) | **GET** /config/ingest-settings/syslog/pattern-sets/ | Retrieve pattern-set by ID
[**retrieve_iceberg_ingest_settings_syslog_patterns**](DefaultApi.md#retrieve_iceberg_ingest_settings_syslog_patterns) | **GET** /config/ingest-settings/syslog/patterns/ | Retrieve pattern by ID
[**retrieve_iceberg_ingest_syslog**](DefaultApi.md#retrieve_iceberg_ingest_syslog) | **GET** /config/ingest/syslog/ | Retrieve syslog
[**retrieve_iceberg_ingest_syslog_pattern_by_id**](DefaultApi.md#retrieve_iceberg_ingest_syslog_pattern_by_id) | **GET** /config/ingest/syslog/pattern/{name}/ | Retrieve pattern by ID
[**retrieve_iceberg_ingest_syslog_pattern_ids**](DefaultApi.md#retrieve_iceberg_ingest_syslog_pattern_ids) | **GET** /config/ingest/syslog/pattern/ | Retrieve pattern
[**retrieve_iceberg_ingest_syslog_pattern_set_by_id**](DefaultApi.md#retrieve_iceberg_ingest_syslog_pattern_set_by_id) | **GET** /config/ingest/syslog/pattern-set/{name}/ | Retrieve pattern-set by ID
[**retrieve_iceberg_ingest_syslog_pattern_set_ids**](DefaultApi.md#retrieve_iceberg_ingest_syslog_pattern_set_ids) | **GET** /config/ingest/syslog/pattern-set/ | Retrieve pattern-set
[**retrieve_iceberg_ingest_syslog_pattern_sets**](DefaultApi.md#retrieve_iceberg_ingest_syslog_pattern_sets) | **GET** /config/ingest/syslog/pattern-sets/ | Retrieve pattern-set by ID
[**retrieve_iceberg_ingest_syslog_patterns**](DefaultApi.md#retrieve_iceberg_ingest_syslog_patterns) | **GET** /config/ingest/syslog/patterns/ | Retrieve pattern by ID
[**retrieve_iceberg_profile_data_summarization_raw_by_id**](DefaultApi.md#retrieve_iceberg_profile_data_summarization_raw_by_id) | **GET** /config/profile/data-summarization/raw/{name}/ | Retrieve raw-data-summarization by ID
[**retrieve_iceberg_profile_data_summarizations_raw**](DefaultApi.md#retrieve_iceberg_profile_data_summarizations_raw) | **GET** /config/profile/data-summarizations/raw/ | Retrieve raw-data-summarization
[**retrieve_iceberg_profile_security_ca_profile_by_id**](DefaultApi.md#retrieve_iceberg_profile_security_ca_profile_by_id) | **GET** /config/profile/security/ca-profile/{name}/ | Retrieve ca-profile by ID
[**retrieve_iceberg_profile_security_ca_profiles**](DefaultApi.md#retrieve_iceberg_profile_security_ca_profiles) | **GET** /config/profile/security/ca-profiles/ | Retrieve ca-profile
[**retrieve_iceberg_profile_security_local_certificate_by_id**](DefaultApi.md#retrieve_iceberg_profile_security_local_certificate_by_id) | **GET** /config/profile/security/local-certificate/{name}/ | Retrieve local-certificate by ID
[**retrieve_iceberg_profile_security_local_certificates**](DefaultApi.md#retrieve_iceberg_profile_security_local_certificates) | **GET** /config/profile/security/local-certificates/ | Retrieve local-certificate
[**retrieve_iceberg_profile_security_ssh_key_profile_by_id**](DefaultApi.md#retrieve_iceberg_profile_security_ssh_key_profile_by_id) | **GET** /config/profile/security/ssh-key-profile/{name}/ | Retrieve ssh-key-profile by ID
[**retrieve_iceberg_profile_security_ssh_key_profiles**](DefaultApi.md#retrieve_iceberg_profile_security_ssh_key_profiles) | **GET** /config/profile/security/ssh-key-profiles/ | Retrieve ssh-key-profile
[**retrieve_iceberg_profiles**](DefaultApi.md#retrieve_iceberg_profiles) | **GET** /config/profiles/ | Retrieve profile
[**retrieve_sensors**](DefaultApi.md#retrieve_sensors) | **GET** /config/sensors/ | List all OpenConfig sensors.
[**update_dynamic_tagging_by_key**](DefaultApi.md#update_dynamic_tagging_by_key) | **PUT** /config/dynamic-tagging/key/ | Updates Dynamic-tagging key-value
[**update_healthbot_deployment_deployment_by_id**](DefaultApi.md#update_healthbot_deployment_deployment_by_id) | **PUT** /config/deployment/ | Update deployment by ID
[**update_healthbot_dynamic_tagging**](DefaultApi.md#update_healthbot_dynamic_tagging) | **PUT** /config/dynamic-tagging/keys/ | Update dynamic-tagging by ID
[**update_healthbot_ingest_byoi_custom_plugin_by_id**](DefaultApi.md#update_healthbot_ingest_byoi_custom_plugin_by_id) | **PUT** /config/ingest/byoi/custom-plugin/{name}/ | Update custom-plugin by ID
[**update_healthbot_ingest_byoi_default_plugin_tlive_kafka_by_id**](DefaultApi.md#update_healthbot_ingest_byoi_default_plugin_tlive_kafka_by_id) | **PUT** /config/ingest/byoi/default-plugin/tlive-kafka-oc/{name}/ | Update tlive-kafka-oc by ID
[**update_healthbot_ingest_byoi_ingest_mapping_by_id**](DefaultApi.md#update_healthbot_ingest_byoi_ingest_mapping_by_id) | **PUT** /config/ingest/byoi/ingest-mapping/{name}/ | Update ingest-mapping by ID
[**update_healthbot_ingest_frequency_profile_by_id**](DefaultApi.md#update_healthbot_ingest_frequency_profile_by_id) | **PUT** /config/ingest/frequency-profile/{name}/ | Update frequency-profile by ID
[**update_healthbot_ingest_outbound_ssh**](DefaultApi.md#update_healthbot_ingest_outbound_ssh) | **PUT** /config/ingest/outbound-ssh/ | Update outbound-ssh by ID
[**update_healthbot_ingest_settings_byoi_custom_plugin_by_id**](DefaultApi.md#update_healthbot_ingest_settings_byoi_custom_plugin_by_id) | **PUT** /config/ingest-settings/byoi/custom-plugin/{name}/ | Update custom-plugin by ID
[**update_healthbot_ingest_settings_byoi_default_plugin_tlive_kafka_by_id**](DefaultApi.md#update_healthbot_ingest_settings_byoi_default_plugin_tlive_kafka_by_id) | **PUT** /config/ingest-settings/byoi/default-plugin/tlive-kafka-oc/{name}/ | Update tlive-kafka-oc by ID
[**update_healthbot_ingest_settings_byoi_ingest_mapping_by_id**](DefaultApi.md#update_healthbot_ingest_settings_byoi_ingest_mapping_by_id) | **PUT** /config/ingest-settings/byoi/ingest-mapping/{name}/ | Update ingest-mapping by ID
[**update_healthbot_ingest_settings_frequency_profile_by_id**](DefaultApi.md#update_healthbot_ingest_settings_frequency_profile_by_id) | **PUT** /config/ingest-settings/frequency-profile/{name}/ | Update frequency-profile by ID
[**update_healthbot_ingest_settings_tagging_profile_by_id**](DefaultApi.md#update_healthbot_ingest_settings_tagging_profile_by_id) | **PUT** /config/ingest-settings/data-enrichment/tagging-profile/{name}/ | Update tagging-profile by ID
[**update_healthbot_ingest_settings_tagging_profiles**](DefaultApi.md#update_healthbot_ingest_settings_tagging_profiles) | **PUT** /config/ingest-settings/data-enrichment/tagging-profiles/ | Update tagging-profile by ID
[**update_healthbot_ingest_sflow**](DefaultApi.md#update_healthbot_ingest_sflow) | **PUT** /config/ingest/sflow/ | Update sflow by ID
[**update_healthbot_ingest_sflow_counter_record_by_id**](DefaultApi.md#update_healthbot_ingest_sflow_counter_record_by_id) | **PUT** /config/ingest/sflow/counter-record/{record_name}/ | Update counter-record by ID
[**update_healthbot_ingest_sflow_flow_record_by_id**](DefaultApi.md#update_healthbot_ingest_sflow_flow_record_by_id) | **PUT** /config/ingest/sflow/flow-record/{record_name}/ | Update flow-record by ID
[**update_healthbot_ingest_sflow_protocol_by_id**](DefaultApi.md#update_healthbot_ingest_sflow_protocol_by_id) | **PUT** /config/ingest/sflow/protocol/{protocol_name}/ | Update protocol by ID
[**update_healthbot_ingest_sflow_sample_by_id**](DefaultApi.md#update_healthbot_ingest_sflow_sample_by_id) | **PUT** /config/ingest/sflow/sample/{sample_name}/ | Update sample by ID
[**update_healthbot_ingest_snmp_notification**](DefaultApi.md#update_healthbot_ingest_snmp_notification) | **PUT** /config/ingest/snmp-notification/ | Update snmp-notification by ID
[**update_healthbot_ingest_snmp_notification_v3_usm_user_by_id**](DefaultApi.md#update_healthbot_ingest_snmp_notification_v3_usm_user_by_id) | **PUT** /config/ingest/snmp-notification/v3/usm/user/{name}/ | Update SNMPv3 user by UserName(ID)
[**update_healthbot_ingest_syslog_header_pattern_by_id**](DefaultApi.md#update_healthbot_ingest_syslog_header_pattern_by_id) | **PUT** /config/ingest/syslog/header-pattern/{name}/ | Update pattern by ID
[**update_healthbot_ingest_tagging_profile_by_id**](DefaultApi.md#update_healthbot_ingest_tagging_profile_by_id) | **PUT** /config/ingest/data-enrichment/tagging-profile/{name}/ | Update tagging-profile by ID
[**update_healthbot_ingest_tagging_profiles**](DefaultApi.md#update_healthbot_ingest_tagging_profiles) | **PUT** /config/ingest/data-enrichment/tagging-profiles/ | Update tagging-profile by ID
[**update_healthbot_organization_organization_by_id**](DefaultApi.md#update_healthbot_organization_organization_by_id) | **PUT** /config/organization/{organization_name}/ | Update organization by ID
[**update_healthbot_profile_rollup_summarization_field_profile_field_profile_by_id**](DefaultApi.md#update_healthbot_profile_rollup_summarization_field_profile_field_profile_by_id) | **PUT** /config/profile/rollup-summarization/field-profile/{profile_id}/ | Update field-profile by ID
[**update_healthbot_system_time_series_database_time_series_database_by_id**](DefaultApi.md#update_healthbot_system_time_series_database_time_series_database_by_id) | **PUT** /config/system/tsdb/ | Update time-series-database by ID
[**update_healthbot_system_trigger_action**](DefaultApi.md#update_healthbot_system_trigger_action) | **PUT** /config/system/trigger_action/ | Update trigger-action
[**update_iceberg_ingest**](DefaultApi.md#update_iceberg_ingest) | **PUT** /config/ingest/ | Update ingest by ID
[**update_iceberg_ingest_flow**](DefaultApi.md#update_iceberg_ingest_flow) | **PUT** /config/ingest/flow/ | Update flow by ID
[**update_iceberg_ingest_flow_template_by_id**](DefaultApi.md#update_iceberg_ingest_flow_template_by_id) | **PUT** /config/ingest/flow/template/{name}/ | Update template by ID
[**update_iceberg_ingest_native_gpb**](DefaultApi.md#update_iceberg_ingest_native_gpb) | **PUT** /config/ingest/native-gpb/ | Update native-gpb by ID
[**update_iceberg_ingest_settings**](DefaultApi.md#update_iceberg_ingest_settings) | **PUT** /config/ingest-settings/ | Update ingest-settings by ID
[**update_iceberg_ingest_settings_flow**](DefaultApi.md#update_iceberg_ingest_settings_flow) | **PUT** /config/ingest-settings/flow/ | Update flow by ID
[**update_iceberg_ingest_settings_flow_template_by_id**](DefaultApi.md#update_iceberg_ingest_settings_flow_template_by_id) | **PUT** /config/ingest-settings/flow/template/{name}/ | Update template by ID
[**update_iceberg_ingest_settings_syslog**](DefaultApi.md#update_iceberg_ingest_settings_syslog) | **PUT** /config/ingest-settings/syslog/ | Update syslog by ID
[**update_iceberg_ingest_settings_syslog_pattern_by_id**](DefaultApi.md#update_iceberg_ingest_settings_syslog_pattern_by_id) | **PUT** /config/ingest-settings/syslog/pattern/{name}/ | Update pattern by ID
[**update_iceberg_ingest_settings_syslog_pattern_set_by_id**](DefaultApi.md#update_iceberg_ingest_settings_syslog_pattern_set_by_id) | **PUT** /config/ingest-settings/syslog/pattern-set/{name}/ | Update pattern-set by ID
[**update_iceberg_ingest_syslog**](DefaultApi.md#update_iceberg_ingest_syslog) | **PUT** /config/ingest/syslog/ | Update syslog by ID
[**update_iceberg_ingest_syslog_pattern_by_id**](DefaultApi.md#update_iceberg_ingest_syslog_pattern_by_id) | **PUT** /config/ingest/syslog/pattern/{name}/ | Update pattern by ID
[**update_iceberg_ingest_syslog_pattern_set_by_id**](DefaultApi.md#update_iceberg_ingest_syslog_pattern_set_by_id) | **PUT** /config/ingest/syslog/pattern-set/{name}/ | Update pattern-set by ID
[**update_iceberg_profile_data_summarization_raw_by_id**](DefaultApi.md#update_iceberg_profile_data_summarization_raw_by_id) | **PUT** /config/profile/data-summarization/raw/{name}/ | Update raw-data-summarization by ID
[**update_iceberg_profile_security_ca_profile_by_id**](DefaultApi.md#update_iceberg_profile_security_ca_profile_by_id) | **PUT** /config/profile/security/ca-profile/{name}/ | Update ca-profile by ID
[**update_iceberg_profile_security_local_certificate_by_id**](DefaultApi.md#update_iceberg_profile_security_local_certificate_by_id) | **PUT** /config/profile/security/local-certificate/{name}/ | Update local-certificate by ID
[**update_iceberg_profile_security_ssh_key_profile_by_id**](DefaultApi.md#update_iceberg_profile_security_ssh_key_profile_by_id) | **PUT** /config/profile/security/ssh-key-profile/{name}/ | Update ssh-key-profile by ID
[**update_iceberg_profiles**](DefaultApi.md#update_iceberg_profiles) | **PUT** /config/profiles/ | Update profile by ID


# **backup_grafana**
> file backup_grafana(x_iam_token=x_iam_token)

Take backup of Grafana configuration

Take backup of Grafana configuration

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
x_iam_token = 'x_iam_token_example' # str | authentication header object (optional)

try:
    # Take backup of Grafana configuration
    api_response = api_instance.backup_grafana(x_iam_token=x_iam_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->backup_grafana: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_iam_token** | **str**| authentication header object | [optional] 

### Return type

[**file**](file.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, multipart/form-data
 - **Accept**: application/octet-stream

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **backup_helper_files**
> file backup_helper_files(x_iam_token=x_iam_token)

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
x_iam_token = 'x_iam_token_example' # str | authentication header object (optional)

try:
    # Download the tar file containing all helper files.
    api_response = api_instance.backup_helper_files(x_iam_token=x_iam_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->backup_helper_files: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_iam_token** | **str**| authentication header object | [optional] 

### Return type

[**file**](file.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, multipart/form-data
 - **Accept**: application/octet-stream

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_dynamic_tagging_by_key**
> create_dynamic_tagging_by_key(key_name, dynamic_tagging_obj, x_iam_token=x_iam_token)

Creates Dynamic-tagging key-value

Creates a key in Dynamic-tagging

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
key_name = 'key_name_example' # str | Dynamic-tagging Key
dynamic_tagging_obj = swagger_client.DynamicTaggingSchemaObject() # DynamicTaggingSchemaObject | Dynamic-tagging object containing key-value pair
x_iam_token = 'x_iam_token_example' # str | authentication header object (optional)

try:
    # Creates Dynamic-tagging key-value
    api_instance.create_dynamic_tagging_by_key(key_name, dynamic_tagging_obj, x_iam_token=x_iam_token)
except ApiException as e:
    print("Exception when calling DefaultApi->create_dynamic_tagging_by_key: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key_name** | **str**| Dynamic-tagging Key | 
 **dynamic_tagging_obj** | [**DynamicTaggingSchemaObject**](DynamicTaggingSchemaObject.md)| Dynamic-tagging object containing key-value pair | 
 **x_iam_token** | **str**| authentication header object | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_files_certificates_by_file_name**
> create_files_certificates_by_file_name(up_file, file_name, x_iam_token=x_iam_token, password=password, certificate_type=certificate_type)

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
x_iam_token = 'x_iam_token_example' # str | authentication header object (optional)
password = 'password_example' # str | password (optional)
certificate_type = 'certificate_type_example' # str | Certificate type (optional)

try:
    # Upload a certificate file.
    api_instance.create_files_certificates_by_file_name(up_file, file_name, x_iam_token=x_iam_token, password=password, certificate_type=certificate_type)
except ApiException as e:
    print("Exception when calling DefaultApi->create_files_certificates_by_file_name: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **up_file** | **file**| File content | 
 **file_name** | **str**| File name | 
 **x_iam_token** | **str**| authentication header object | [optional] 
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
> create_files_helper_files_by_file_name(up_file, file_name, x_iam_token=x_iam_token)

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
x_iam_token = 'x_iam_token_example' # str | authentication header object (optional)

try:
    # Upload a helper-file.
    api_instance.create_files_helper_files_by_file_name(up_file, file_name, x_iam_token=x_iam_token)
except ApiException as e:
    print("Exception when calling DefaultApi->create_files_helper_files_by_file_name: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **up_file** | **file**| File content | 
 **file_name** | **str**| File name | 
 **x_iam_token** | **str**| authentication header object | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json, application/octet-stream

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_healthbot_deployment_deployment_by_id**
> create_healthbot_deployment_deployment_by_id(deployment, x_iam_token=x_iam_token)

Create deployment by ID

Create operation of resource: deployment

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
deployment = swagger_client.DeploymentSchema() # DeploymentSchema | deployment body object
x_iam_token = 'x_iam_token_example' # str | authentication header object (optional)

try:
    # Create deployment by ID
    api_instance.create_healthbot_deployment_deployment_by_id(deployment, x_iam_token=x_iam_token)
except ApiException as e:
    print("Exception when calling DefaultApi->create_healthbot_deployment_deployment_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **deployment** | [**DeploymentSchema**](DeploymentSchema.md)| deployment body object | 
 **x_iam_token** | **str**| authentication header object | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_healthbot_dynamic_tagging**
> list[str] create_healthbot_dynamic_tagging(dynamic_tagging, x_iam_token=x_iam_token)

Create dynamic-tagging by ID

Create operation of resource: dynamic-tagging

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
dynamic_tagging = swagger_client.DynamicTaggingsSchemaObject() # DynamicTaggingsSchemaObject | dynamic_taggingbody object
x_iam_token = 'x_iam_token_example' # str | authentication header object (optional)

try:
    # Create dynamic-tagging by ID
    api_response = api_instance.create_healthbot_dynamic_tagging(dynamic_tagging, x_iam_token=x_iam_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->create_healthbot_dynamic_tagging: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dynamic_tagging** | [**DynamicTaggingsSchemaObject**](DynamicTaggingsSchemaObject.md)| dynamic_taggingbody object | 
 **x_iam_token** | **str**| authentication header object | [optional] 

### Return type

**list[str]**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_healthbot_ingest_byoi_custom_plugin_by_id**
> create_healthbot_ingest_byoi_custom_plugin_by_id(name, custom_plugin, x_iam_token=x_iam_token)

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
x_iam_token = 'x_iam_token_example' # str | authentication header object (optional)

try:
    # Create custom-plugin by ID
    api_instance.create_healthbot_ingest_byoi_custom_plugin_by_id(name, custom_plugin, x_iam_token=x_iam_token)
except ApiException as e:
    print("Exception when calling DefaultApi->create_healthbot_ingest_byoi_custom_plugin_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of custom-plugin | 
 **custom_plugin** | [**CustomPluginSchema**](CustomPluginSchema.md)| custom_pluginbody object | 
 **x_iam_token** | **str**| authentication header object | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_healthbot_ingest_byoi_default_plugin_tlive_kafka_by_id**
> create_healthbot_ingest_byoi_default_plugin_tlive_kafka_by_id(name, tlive_kafka, x_iam_token=x_iam_token)

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
x_iam_token = 'x_iam_token_example' # str | authentication header object (optional)

try:
    # Create tlive-kafka-oc by ID
    api_instance.create_healthbot_ingest_byoi_default_plugin_tlive_kafka_by_id(name, tlive_kafka, x_iam_token=x_iam_token)
except ApiException as e:
    print("Exception when calling DefaultApi->create_healthbot_ingest_byoi_default_plugin_tlive_kafka_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of tlive-kafka-oc | 
 **tlive_kafka** | [**TliveKafkaOcSchema**](TliveKafkaOcSchema.md)| tlive_kafkabody object | 
 **x_iam_token** | **str**| authentication header object | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_healthbot_ingest_byoi_ingest_mapping_by_id**
> create_healthbot_ingest_byoi_ingest_mapping_by_id(name, ingest_mapping, x_iam_token=x_iam_token)

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
x_iam_token = 'x_iam_token_example' # str | authentication header object (optional)

try:
    # Create ingest-mapping by ID
    api_instance.create_healthbot_ingest_byoi_ingest_mapping_by_id(name, ingest_mapping, x_iam_token=x_iam_token)
except ApiException as e:
    print("Exception when calling DefaultApi->create_healthbot_ingest_byoi_ingest_mapping_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of ingest-mapping | 
 **ingest_mapping** | [**IngestMappingSchema**](IngestMappingSchema.md)| ingest_mappingbody object | 
 **x_iam_token** | **str**| authentication header object | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_healthbot_ingest_frequency_profile_by_id**
> create_healthbot_ingest_frequency_profile_by_id(name, frequency_profile, x_iam_token=x_iam_token)

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
x_iam_token = 'x_iam_token_example' # str | authentication header object (optional)

try:
    # Create frequency-profile by ID
    api_instance.create_healthbot_ingest_frequency_profile_by_id(name, frequency_profile, x_iam_token=x_iam_token)
except ApiException as e:
    print("Exception when calling DefaultApi->create_healthbot_ingest_frequency_profile_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| ID of name | 
 **frequency_profile** | [**FrequencyProfileSchema**](FrequencyProfileSchema.md)| frequency_profilebody object | 
 **x_iam_token** | **str**| authentication header object | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_healthbot_ingest_outbound_ssh**
> create_healthbot_ingest_outbound_ssh(outbound_ssh, x_iam_token=x_iam_token)

Create outbound-ssh by ID

Create operation of resource: outbound-ssh

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
outbound_ssh = swagger_client.OutboundSshSchema() # OutboundSshSchema | outbound_ssh body object
x_iam_token = 'x_iam_token_example' # str | authentication header object (optional)

try:
    # Create outbound-ssh by ID
    api_instance.create_healthbot_ingest_outbound_ssh(outbound_ssh, x_iam_token=x_iam_token)
except ApiException as e:
    print("Exception when calling DefaultApi->create_healthbot_ingest_outbound_ssh: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **outbound_ssh** | [**OutboundSshSchema**](OutboundSshSchema.md)| outbound_ssh body object | 
 **x_iam_token** | **str**| authentication header object | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_healthbot_ingest_settings_byoi_custom_plugin_by_id**
> create_healthbot_ingest_settings_byoi_custom_plugin_by_id(name, custom_plugin, x_iam_token=x_iam_token)

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
x_iam_token = 'x_iam_token_example' # str | authentication header object (optional)

try:
    # Create custom-plugin by ID
    api_instance.create_healthbot_ingest_settings_byoi_custom_plugin_by_id(name, custom_plugin, x_iam_token=x_iam_token)
except ApiException as e:
    print("Exception when calling DefaultApi->create_healthbot_ingest_settings_byoi_custom_plugin_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of custom-plugin | 
 **custom_plugin** | [**CustomPluginSchema**](CustomPluginSchema.md)| custom_pluginbody object | 
 **x_iam_token** | **str**| authentication header object | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_healthbot_ingest_settings_byoi_default_plugin_tlive_kafka_by_id**
> create_healthbot_ingest_settings_byoi_default_plugin_tlive_kafka_by_id(name, tlive_kafka, x_iam_token=x_iam_token)

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
x_iam_token = 'x_iam_token_example' # str | authentication header object (optional)

try:
    # Create tlive-kafka-oc by ID
    api_instance.create_healthbot_ingest_settings_byoi_default_plugin_tlive_kafka_by_id(name, tlive_kafka, x_iam_token=x_iam_token)
except ApiException as e:
    print("Exception when calling DefaultApi->create_healthbot_ingest_settings_byoi_default_plugin_tlive_kafka_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of tlive-kafka-oc | 
 **tlive_kafka** | [**TliveKafkaOcSchema**](TliveKafkaOcSchema.md)| tlive_kafkabody object | 
 **x_iam_token** | **str**| authentication header object | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_healthbot_ingest_settings_byoi_ingest_mapping_by_id**
> create_healthbot_ingest_settings_byoi_ingest_mapping_by_id(name, ingest_mapping, x_iam_token=x_iam_token)

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
x_iam_token = 'x_iam_token_example' # str | authentication header object (optional)

try:
    # Create ingest-mapping by ID
    api_instance.create_healthbot_ingest_settings_byoi_ingest_mapping_by_id(name, ingest_mapping, x_iam_token=x_iam_token)
except ApiException as e:
    print("Exception when calling DefaultApi->create_healthbot_ingest_settings_byoi_ingest_mapping_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of ingest-mapping | 
 **ingest_mapping** | [**IngestMappingSchema**](IngestMappingSchema.md)| ingest_mappingbody object | 
 **x_iam_token** | **str**| authentication header object | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_healthbot_ingest_settings_frequency_profile_by_id**
> create_healthbot_ingest_settings_frequency_profile_by_id(name, frequency_profile, x_iam_token=x_iam_token)

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
x_iam_token = 'x_iam_token_example' # str | authentication header object (optional)

try:
    # Create frequency-profile by ID
    api_instance.create_healthbot_ingest_settings_frequency_profile_by_id(name, frequency_profile, x_iam_token=x_iam_token)
except ApiException as e:
    print("Exception when calling DefaultApi->create_healthbot_ingest_settings_frequency_profile_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| ID of name | 
 **frequency_profile** | [**FrequencyProfileSchema**](FrequencyProfileSchema.md)| frequency_profilebody object | 
 **x_iam_token** | **str**| authentication header object | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_healthbot_ingest_settings_tagging_profile_by_id**
> create_healthbot_ingest_settings_tagging_profile_by_id(name, tagging_profile, x_iam_token=x_iam_token)

Create tagging-profile by ID

Create operation of resource: tagging-profile

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
tagging_profile = swagger_client.TaggingProfileSchema() # TaggingProfileSchema | tagging_profilebody object
x_iam_token = 'x_iam_token_example' # str | authentication header object (optional)

try:
    # Create tagging-profile by ID
    api_instance.create_healthbot_ingest_settings_tagging_profile_by_id(name, tagging_profile, x_iam_token=x_iam_token)
except ApiException as e:
    print("Exception when calling DefaultApi->create_healthbot_ingest_settings_tagging_profile_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| ID of name | 
 **tagging_profile** | [**TaggingProfileSchema**](TaggingProfileSchema.md)| tagging_profilebody object | 
 **x_iam_token** | **str**| authentication header object | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_healthbot_ingest_settings_tagging_profiles**
> list[str] create_healthbot_ingest_settings_tagging_profiles(tagging_profile, x_iam_token=x_iam_token)

Create tagging-profile by ID

Create operation of resource: tagging-profile

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
tagging_profile = swagger_client.TaggingProfilesSchema() # TaggingProfilesSchema | tagging_profilebody object
x_iam_token = 'x_iam_token_example' # str | authentication header object (optional)

try:
    # Create tagging-profile by ID
    api_response = api_instance.create_healthbot_ingest_settings_tagging_profiles(tagging_profile, x_iam_token=x_iam_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->create_healthbot_ingest_settings_tagging_profiles: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tagging_profile** | [**TaggingProfilesSchema**](TaggingProfilesSchema.md)| tagging_profilebody object | 
 **x_iam_token** | **str**| authentication header object | [optional] 

### Return type

**list[str]**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_healthbot_ingest_sflow**
> create_healthbot_ingest_sflow(sflow, x_iam_token=x_iam_token)

Create sflow by ID

Create operation of resource: sflow

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
sflow = swagger_client.SflowSchema() # SflowSchema | sflowbody object
x_iam_token = 'x_iam_token_example' # str | authentication header object (optional)

try:
    # Create sflow by ID
    api_instance.create_healthbot_ingest_sflow(sflow, x_iam_token=x_iam_token)
except ApiException as e:
    print("Exception when calling DefaultApi->create_healthbot_ingest_sflow: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sflow** | [**SflowSchema**](SflowSchema.md)| sflowbody object | 
 **x_iam_token** | **str**| authentication header object | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_healthbot_ingest_sflow_counter_record_by_id**
> create_healthbot_ingest_sflow_counter_record_by_id(record_name, counter_record, x_iam_token=x_iam_token)

Create counter-record by ID

Create operation of resource: counter-record

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
record_name = 'record_name_example' # str | ID of record-name
counter_record = swagger_client.CounterRecordSchema() # CounterRecordSchema | counter_recordbody object
x_iam_token = 'x_iam_token_example' # str | authentication header object (optional)

try:
    # Create counter-record by ID
    api_instance.create_healthbot_ingest_sflow_counter_record_by_id(record_name, counter_record, x_iam_token=x_iam_token)
except ApiException as e:
    print("Exception when calling DefaultApi->create_healthbot_ingest_sflow_counter_record_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **record_name** | **str**| ID of record-name | 
 **counter_record** | [**CounterRecordSchema**](CounterRecordSchema.md)| counter_recordbody object | 
 **x_iam_token** | **str**| authentication header object | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_healthbot_ingest_sflow_flow_record_by_id**
> create_healthbot_ingest_sflow_flow_record_by_id(record_name, flow_record, x_iam_token=x_iam_token)

Create flow-record by ID

Create operation of resource: flow-record

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
record_name = 'record_name_example' # str | ID of record-name
flow_record = swagger_client.FlowRecordSchema() # FlowRecordSchema | flow_recordbody object
x_iam_token = 'x_iam_token_example' # str | authentication header object (optional)

try:
    # Create flow-record by ID
    api_instance.create_healthbot_ingest_sflow_flow_record_by_id(record_name, flow_record, x_iam_token=x_iam_token)
except ApiException as e:
    print("Exception when calling DefaultApi->create_healthbot_ingest_sflow_flow_record_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **record_name** | **str**| ID of record-name | 
 **flow_record** | [**FlowRecordSchema**](FlowRecordSchema.md)| flow_recordbody object | 
 **x_iam_token** | **str**| authentication header object | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_healthbot_ingest_sflow_protocol_by_id**
> create_healthbot_ingest_sflow_protocol_by_id(protocol_name, protocol, x_iam_token=x_iam_token)

Create protocol by ID

Create operation of resource: protocol

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
protocol_name = 'protocol_name_example' # str | ID of protocol-name
protocol = swagger_client.ProtocolSchema() # ProtocolSchema | protocolbody object
x_iam_token = 'x_iam_token_example' # str | authentication header object (optional)

try:
    # Create protocol by ID
    api_instance.create_healthbot_ingest_sflow_protocol_by_id(protocol_name, protocol, x_iam_token=x_iam_token)
except ApiException as e:
    print("Exception when calling DefaultApi->create_healthbot_ingest_sflow_protocol_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **protocol_name** | **str**| ID of protocol-name | 
 **protocol** | [**ProtocolSchema**](ProtocolSchema.md)| protocolbody object | 
 **x_iam_token** | **str**| authentication header object | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_healthbot_ingest_sflow_sample_by_id**
> create_healthbot_ingest_sflow_sample_by_id(sample_name, sample, x_iam_token=x_iam_token)

Create sample by ID

Create operation of resource: sample

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
sample_name = 'sample_name_example' # str | ID of sample-name
sample = swagger_client.SampleSchema() # SampleSchema | samplebody object
x_iam_token = 'x_iam_token_example' # str | authentication header object (optional)

try:
    # Create sample by ID
    api_instance.create_healthbot_ingest_sflow_sample_by_id(sample_name, sample, x_iam_token=x_iam_token)
except ApiException as e:
    print("Exception when calling DefaultApi->create_healthbot_ingest_sflow_sample_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sample_name** | **str**| ID of sample-name | 
 **sample** | [**SampleSchema**](SampleSchema.md)| samplebody object | 
 **x_iam_token** | **str**| authentication header object | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_healthbot_ingest_snmp_notification**
> create_healthbot_ingest_snmp_notification(snmp_notification, x_iam_token=x_iam_token)

Create snmp-notification by ID

Create operation of resource: snmp-notification

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
snmp_notification = swagger_client.SnmpNotificationSchema() # SnmpNotificationSchema | snmp_notification body object
x_iam_token = 'x_iam_token_example' # str | authentication header object (optional)

try:
    # Create snmp-notification by ID
    api_instance.create_healthbot_ingest_snmp_notification(snmp_notification, x_iam_token=x_iam_token)
except ApiException as e:
    print("Exception when calling DefaultApi->create_healthbot_ingest_snmp_notification: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **snmp_notification** | [**SnmpNotificationSchema**](SnmpNotificationSchema.md)| snmp_notification body object | 
 **x_iam_token** | **str**| authentication header object | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_healthbot_ingest_snmp_notification_v3_usm_user_by_id**
> create_healthbot_ingest_snmp_notification_v3_usm_user_by_id(name, usm_user, x_iam_token=x_iam_token)

Create SNMPv3 user by UserName(ID)

Create operation of resource: snmp v3 usm user

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
name = 'name_example' # str | User Name
usm_user = swagger_client.Snmpv3UsmUserSchema() # Snmpv3UsmUserSchema | snmp_v3_usm user object
x_iam_token = 'x_iam_token_example' # str | authentication header object (optional)

try:
    # Create SNMPv3 user by UserName(ID)
    api_instance.create_healthbot_ingest_snmp_notification_v3_usm_user_by_id(name, usm_user, x_iam_token=x_iam_token)
except ApiException as e:
    print("Exception when calling DefaultApi->create_healthbot_ingest_snmp_notification_v3_usm_user_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| User Name | 
 **usm_user** | [**Snmpv3UsmUserSchema**](Snmpv3UsmUserSchema.md)| snmp_v3_usm user object | 
 **x_iam_token** | **str**| authentication header object | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_healthbot_ingest_syslog_header_pattern_by_id**
> create_healthbot_ingest_syslog_header_pattern_by_id(name, pattern, x_iam_token=x_iam_token)

Create pattern by ID

Create operation of resource: header-pattern

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
pattern = swagger_client.HeaderPatternSchema() # HeaderPatternSchema | header_patternbody object
x_iam_token = 'x_iam_token_example' # str | authentication header object (optional)

try:
    # Create pattern by ID
    api_instance.create_healthbot_ingest_syslog_header_pattern_by_id(name, pattern, x_iam_token=x_iam_token)
except ApiException as e:
    print("Exception when calling DefaultApi->create_healthbot_ingest_syslog_header_pattern_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| ID of name | 
 **pattern** | [**HeaderPatternSchema**](HeaderPatternSchema.md)| header_patternbody object | 
 **x_iam_token** | **str**| authentication header object | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_healthbot_ingest_tagging_profile_by_id**
> create_healthbot_ingest_tagging_profile_by_id(name, tagging_profile, x_iam_token=x_iam_token)

Create tagging-profile by ID

Create operation of resource: tagging-profile

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
tagging_profile = swagger_client.TaggingProfileSchema() # TaggingProfileSchema | tagging_profilebody object
x_iam_token = 'x_iam_token_example' # str | authentication header object (optional)

try:
    # Create tagging-profile by ID
    api_instance.create_healthbot_ingest_tagging_profile_by_id(name, tagging_profile, x_iam_token=x_iam_token)
except ApiException as e:
    print("Exception when calling DefaultApi->create_healthbot_ingest_tagging_profile_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| ID of name | 
 **tagging_profile** | [**TaggingProfileSchema**](TaggingProfileSchema.md)| tagging_profilebody object | 
 **x_iam_token** | **str**| authentication header object | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_healthbot_ingest_tagging_profiles**
> list[str] create_healthbot_ingest_tagging_profiles(tagging_profile, x_iam_token=x_iam_token)

Create tagging-profile by ID

Create operation of resource: tagging-profile

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
tagging_profile = swagger_client.TaggingProfilesSchema() # TaggingProfilesSchema | tagging_profilebody object
x_iam_token = 'x_iam_token_example' # str | authentication header object (optional)

try:
    # Create tagging-profile by ID
    api_response = api_instance.create_healthbot_ingest_tagging_profiles(tagging_profile, x_iam_token=x_iam_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->create_healthbot_ingest_tagging_profiles: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tagging_profile** | [**TaggingProfilesSchema**](TaggingProfilesSchema.md)| tagging_profilebody object | 
 **x_iam_token** | **str**| authentication header object | [optional] 

### Return type

**list[str]**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_healthbot_organization_organization_by_id**
> create_healthbot_organization_organization_by_id(organization_name, organization, x_iam_token=x_iam_token)

Create organization by ID

Create operation of resource: organization

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
organization_name = 'organization_name_example' # str | ID of organization-name
organization = swagger_client.OrganizationSchema() # OrganizationSchema | organizationbody object
x_iam_token = 'x_iam_token_example' # str | authentication header object (optional)

try:
    # Create organization by ID
    api_instance.create_healthbot_organization_organization_by_id(organization_name, organization, x_iam_token=x_iam_token)
except ApiException as e:
    print("Exception when calling DefaultApi->create_healthbot_organization_organization_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_name** | **str**| ID of organization-name | 
 **organization** | [**OrganizationSchema**](OrganizationSchema.md)| organizationbody object | 
 **x_iam_token** | **str**| authentication header object | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_healthbot_profile_rollup_summarization_field_profile_field_profile_by_id**
> create_healthbot_profile_rollup_summarization_field_profile_field_profile_by_id(profile_id, field_profile, x_iam_token=x_iam_token)

Create field-profile by ID

Create operation of resource: field-profile

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
profile_id = 'profile_id_example' # str | ID of profile-id
field_profile = swagger_client.RollupSummarizationSchema() # RollupSummarizationSchema | field_profilebody object
x_iam_token = 'x_iam_token_example' # str | authentication header object (optional)

try:
    # Create field-profile by ID
    api_instance.create_healthbot_profile_rollup_summarization_field_profile_field_profile_by_id(profile_id, field_profile, x_iam_token=x_iam_token)
except ApiException as e:
    print("Exception when calling DefaultApi->create_healthbot_profile_rollup_summarization_field_profile_field_profile_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **profile_id** | **str**| ID of profile-id | 
 **field_profile** | [**RollupSummarizationSchema**](RollupSummarizationSchema.md)| field_profilebody object | 
 **x_iam_token** | **str**| authentication header object | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_healthbot_system_time_series_database_time_series_database_by_id**
> create_healthbot_system_time_series_database_time_series_database_by_id(time_series_database, force_tsdb=force_tsdb)

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
force_tsdb = false # bool | force update tsdb when force is set to True (optional) (default to false)

try:
    # Create time-series-database by ID
    api_instance.create_healthbot_system_time_series_database_time_series_database_by_id(time_series_database, force_tsdb=force_tsdb)
except ApiException as e:
    print("Exception when calling DefaultApi->create_healthbot_system_time_series_database_time_series_database_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **time_series_database** | [**TsdbSchema**](TsdbSchema.md)| time_series_databasebody object | 
 **force_tsdb** | **bool**| force update tsdb when force is set to True | [optional] [default to false]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_healthbot_system_trigger_action**
> create_healthbot_system_trigger_action(trigger_action)

Create trigger-action

Create operation of resource: trigger-action

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
trigger_action = swagger_client.TriggerActionSchema() # TriggerActionSchema | trigger_action object

try:
    # Create trigger-action
    api_instance.create_healthbot_system_trigger_action(trigger_action)
except ApiException as e:
    print("Exception when calling DefaultApi->create_healthbot_system_trigger_action: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **trigger_action** | [**TriggerActionSchema**](TriggerActionSchema.md)| trigger_action object | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_iceberg_ingest**
> create_iceberg_ingest(ingest_settings, x_iam_token=x_iam_token)

Create ingest by ID

Create operation of resource: ingest

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
x_iam_token = 'x_iam_token_example' # str | authentication header object (optional)

try:
    # Create ingest by ID
    api_instance.create_iceberg_ingest(ingest_settings, x_iam_token=x_iam_token)
except ApiException as e:
    print("Exception when calling DefaultApi->create_iceberg_ingest: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ingest_settings** | [**IngestSettingsSchema**](IngestSettingsSchema.md)| ingest_settingsbody object | 
 **x_iam_token** | **str**| authentication header object | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_iceberg_ingest_flow**
> create_iceberg_ingest_flow(flow, x_iam_token=x_iam_token)

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
x_iam_token = 'x_iam_token_example' # str | authentication header object (optional)

try:
    # Create flow by ID
    api_instance.create_iceberg_ingest_flow(flow, x_iam_token=x_iam_token)
except ApiException as e:
    print("Exception when calling DefaultApi->create_iceberg_ingest_flow: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **flow** | [**FlowSchema**](FlowSchema.md)| flowbody object | 
 **x_iam_token** | **str**| authentication header object | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_iceberg_ingest_flow_template_by_id**
> create_iceberg_ingest_flow_template_by_id(name, template, x_iam_token=x_iam_token)

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
x_iam_token = 'x_iam_token_example' # str | authentication header object (optional)

try:
    # Create template by ID
    api_instance.create_iceberg_ingest_flow_template_by_id(name, template, x_iam_token=x_iam_token)
except ApiException as e:
    print("Exception when calling DefaultApi->create_iceberg_ingest_flow_template_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of template | 
 **template** | [**TemplateSchema**](TemplateSchema.md)| templatebody object | 
 **x_iam_token** | **str**| authentication header object | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_iceberg_ingest_native_gpb**
> create_iceberg_ingest_native_gpb(native_gpb, x_iam_token=x_iam_token)

Create native-gpb by ID

Create operation of resource: native-gpb

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
native_gpb = swagger_client.NativeGpbSchema() # NativeGpbSchema | native_gpbbody object
x_iam_token = 'x_iam_token_example' # str | authentication header object (optional)

try:
    # Create native-gpb by ID
    api_instance.create_iceberg_ingest_native_gpb(native_gpb, x_iam_token=x_iam_token)
except ApiException as e:
    print("Exception when calling DefaultApi->create_iceberg_ingest_native_gpb: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **native_gpb** | [**NativeGpbSchema**](NativeGpbSchema.md)| native_gpbbody object | 
 **x_iam_token** | **str**| authentication header object | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_iceberg_ingest_settings**
> create_iceberg_ingest_settings(ingest_settings, x_iam_token=x_iam_token)

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
x_iam_token = 'x_iam_token_example' # str | authentication header object (optional)

try:
    # Create ingest-settings by ID
    api_instance.create_iceberg_ingest_settings(ingest_settings, x_iam_token=x_iam_token)
except ApiException as e:
    print("Exception when calling DefaultApi->create_iceberg_ingest_settings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ingest_settings** | [**IngestSettingsSchema**](IngestSettingsSchema.md)| ingest_settingsbody object | 
 **x_iam_token** | **str**| authentication header object | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_iceberg_ingest_settings_flow**
> create_iceberg_ingest_settings_flow(flow, x_iam_token=x_iam_token)

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
x_iam_token = 'x_iam_token_example' # str | authentication header object (optional)

try:
    # Create flow by ID
    api_instance.create_iceberg_ingest_settings_flow(flow, x_iam_token=x_iam_token)
except ApiException as e:
    print("Exception when calling DefaultApi->create_iceberg_ingest_settings_flow: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **flow** | [**FlowSchema**](FlowSchema.md)| flowbody object | 
 **x_iam_token** | **str**| authentication header object | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_iceberg_ingest_settings_flow_template_by_id**
> create_iceberg_ingest_settings_flow_template_by_id(name, template, x_iam_token=x_iam_token)

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
x_iam_token = 'x_iam_token_example' # str | authentication header object (optional)

try:
    # Create template by ID
    api_instance.create_iceberg_ingest_settings_flow_template_by_id(name, template, x_iam_token=x_iam_token)
except ApiException as e:
    print("Exception when calling DefaultApi->create_iceberg_ingest_settings_flow_template_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of template | 
 **template** | [**TemplateSchema**](TemplateSchema.md)| templatebody object | 
 **x_iam_token** | **str**| authentication header object | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_iceberg_ingest_settings_syslog**
> create_iceberg_ingest_settings_syslog(syslog, x_iam_token=x_iam_token)

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
x_iam_token = 'x_iam_token_example' # str | authentication header object (optional)

try:
    # Create syslog by ID
    api_instance.create_iceberg_ingest_settings_syslog(syslog, x_iam_token=x_iam_token)
except ApiException as e:
    print("Exception when calling DefaultApi->create_iceberg_ingest_settings_syslog: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **syslog** | [**SyslogSchema**](SyslogSchema.md)| syslogbody object | 
 **x_iam_token** | **str**| authentication header object | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_iceberg_ingest_settings_syslog_pattern_by_id**
> create_iceberg_ingest_settings_syslog_pattern_by_id(name, pattern, x_iam_token=x_iam_token)

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
x_iam_token = 'x_iam_token_example' # str | authentication header object (optional)

try:
    # Create pattern by ID
    api_instance.create_iceberg_ingest_settings_syslog_pattern_by_id(name, pattern, x_iam_token=x_iam_token)
except ApiException as e:
    print("Exception when calling DefaultApi->create_iceberg_ingest_settings_syslog_pattern_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of pattern | 
 **pattern** | [**PatternSchema**](PatternSchema.md)| patternbody object | 
 **x_iam_token** | **str**| authentication header object | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_iceberg_ingest_settings_syslog_pattern_set_by_id**
> create_iceberg_ingest_settings_syslog_pattern_set_by_id(name, pattern_set, x_iam_token=x_iam_token)

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
x_iam_token = 'x_iam_token_example' # str | authentication header object (optional)

try:
    # Create pattern-set by ID
    api_instance.create_iceberg_ingest_settings_syslog_pattern_set_by_id(name, pattern_set, x_iam_token=x_iam_token)
except ApiException as e:
    print("Exception when calling DefaultApi->create_iceberg_ingest_settings_syslog_pattern_set_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of pattern-set | 
 **pattern_set** | [**PatternSetSchema**](PatternSetSchema.md)| pattern_setbody object | 
 **x_iam_token** | **str**| authentication header object | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_iceberg_ingest_syslog**
> create_iceberg_ingest_syslog(syslog, x_iam_token=x_iam_token)

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
x_iam_token = 'x_iam_token_example' # str | authentication header object (optional)

try:
    # Create syslog by ID
    api_instance.create_iceberg_ingest_syslog(syslog, x_iam_token=x_iam_token)
except ApiException as e:
    print("Exception when calling DefaultApi->create_iceberg_ingest_syslog: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **syslog** | [**SyslogSchema**](SyslogSchema.md)| syslogbody object | 
 **x_iam_token** | **str**| authentication header object | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_iceberg_ingest_syslog_pattern_by_id**
> create_iceberg_ingest_syslog_pattern_by_id(name, pattern, x_iam_token=x_iam_token)

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
x_iam_token = 'x_iam_token_example' # str | authentication header object (optional)

try:
    # Create pattern by ID
    api_instance.create_iceberg_ingest_syslog_pattern_by_id(name, pattern, x_iam_token=x_iam_token)
except ApiException as e:
    print("Exception when calling DefaultApi->create_iceberg_ingest_syslog_pattern_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of pattern | 
 **pattern** | [**PatternSchema**](PatternSchema.md)| patternbody object | 
 **x_iam_token** | **str**| authentication header object | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_iceberg_ingest_syslog_pattern_set_by_id**
> create_iceberg_ingest_syslog_pattern_set_by_id(name, pattern_set, x_iam_token=x_iam_token)

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
x_iam_token = 'x_iam_token_example' # str | authentication header object (optional)

try:
    # Create pattern-set by ID
    api_instance.create_iceberg_ingest_syslog_pattern_set_by_id(name, pattern_set, x_iam_token=x_iam_token)
except ApiException as e:
    print("Exception when calling DefaultApi->create_iceberg_ingest_syslog_pattern_set_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of pattern-set | 
 **pattern_set** | [**PatternSetSchema**](PatternSetSchema.md)| pattern_setbody object | 
 **x_iam_token** | **str**| authentication header object | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_iceberg_profile_data_summarization_raw_by_id**
> create_iceberg_profile_data_summarization_raw_by_id(name, raw_data_summarization, x_iam_token=x_iam_token)

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
x_iam_token = 'x_iam_token_example' # str | authentication header object (optional)

try:
    # Create raw-data-summarization by ID
    api_instance.create_iceberg_profile_data_summarization_raw_by_id(name, raw_data_summarization, x_iam_token=x_iam_token)
except ApiException as e:
    print("Exception when calling DefaultApi->create_iceberg_profile_data_summarization_raw_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of raw-data-summarization | 
 **raw_data_summarization** | [**RawSchema**](RawSchema.md)| raw_data_summarizationbody object | 
 **x_iam_token** | **str**| authentication header object | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_iceberg_profile_security_ca_profile_by_id**
> create_iceberg_profile_security_ca_profile_by_id(name, ca_profile, x_iam_token=x_iam_token)

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
x_iam_token = 'x_iam_token_example' # str | authentication header object (optional)

try:
    # Create ca-profile by ID
    api_instance.create_iceberg_profile_security_ca_profile_by_id(name, ca_profile, x_iam_token=x_iam_token)
except ApiException as e:
    print("Exception when calling DefaultApi->create_iceberg_profile_security_ca_profile_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of ca-profile | 
 **ca_profile** | [**CaProfileSchema**](CaProfileSchema.md)| ca_profilebody object | 
 **x_iam_token** | **str**| authentication header object | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_iceberg_profile_security_local_certificate_by_id**
> create_iceberg_profile_security_local_certificate_by_id(name, local_certificate, x_iam_token=x_iam_token)

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
x_iam_token = 'x_iam_token_example' # str | authentication header object (optional)

try:
    # Create local-certificate by ID
    api_instance.create_iceberg_profile_security_local_certificate_by_id(name, local_certificate, x_iam_token=x_iam_token)
except ApiException as e:
    print("Exception when calling DefaultApi->create_iceberg_profile_security_local_certificate_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of local-certificate | 
 **local_certificate** | [**LocalCertificateSchema**](LocalCertificateSchema.md)| local_certificatebody object | 
 **x_iam_token** | **str**| authentication header object | [optional] 

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
> create_iceberg_profiles(profile, x_iam_token=x_iam_token)

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
x_iam_token = 'x_iam_token_example' # str | authentication header object (optional)

try:
    # Create profile by ID
    api_instance.create_iceberg_profiles(profile, x_iam_token=x_iam_token)
except ApiException as e:
    print("Exception when calling DefaultApi->create_iceberg_profiles: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **profile** | [**ProfilesSchema**](ProfilesSchema.md)| profilebody object | 
 **x_iam_token** | **str**| authentication header object | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_dynamic_tagging_by_key**
> delete_dynamic_tagging_by_key(key_name, x_iam_token=x_iam_token)

Delete Dynamic-tagging key-value

Update a key in Dynamic-tagging

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
key_name = 'key_name_example' # str | Dynamic-tagging Key
x_iam_token = 'x_iam_token_example' # str | authentication header object (optional)

try:
    # Delete Dynamic-tagging key-value
    api_instance.delete_dynamic_tagging_by_key(key_name, x_iam_token=x_iam_token)
except ApiException as e:
    print("Exception when calling DefaultApi->delete_dynamic_tagging_by_key: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key_name** | **str**| Dynamic-tagging Key | 
 **x_iam_token** | **str**| authentication header object | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_files_certificates_by_file_name**
> delete_files_certificates_by_file_name(file_name, x_iam_token=x_iam_token, input_path=input_path, certificate_type=certificate_type)

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
x_iam_token = 'x_iam_token_example' # str | authentication header object (optional)
input_path = 'input_path_example' # str | Input path (optional)
certificate_type = 'certificate_type_example' # str | Certificate type (optional)

try:
    # Delete a certificate-file.
    api_instance.delete_files_certificates_by_file_name(file_name, x_iam_token=x_iam_token, input_path=input_path, certificate_type=certificate_type)
except ApiException as e:
    print("Exception when calling DefaultApi->delete_files_certificates_by_file_name: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file_name** | **str**| File name | 
 **x_iam_token** | **str**| authentication header object | [optional] 
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
> delete_files_helper_files_by_file_name(file_name, x_iam_token=x_iam_token, input_path=input_path)

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
x_iam_token = 'x_iam_token_example' # str | authentication header object (optional)
input_path = 'input_path_example' # str | Input path (optional)

try:
    # Delete a helper-file.
    api_instance.delete_files_helper_files_by_file_name(file_name, x_iam_token=x_iam_token, input_path=input_path)
except ApiException as e:
    print("Exception when calling DefaultApi->delete_files_helper_files_by_file_name: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file_name** | **str**| File name | 
 **x_iam_token** | **str**| authentication header object | [optional] 
 **input_path** | **str**| Input path | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, multipart/form-data
 - **Accept**: application/json, application/octet-stream

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_healthbot_deployment_deployment_by_id**
> delete_healthbot_deployment_deployment_by_id(x_iam_token=x_iam_token)

Delete deployment by ID

Delete operation of resource: deployment

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
x_iam_token = 'x_iam_token_example' # str | authentication header object (optional)

try:
    # Delete deployment by ID
    api_instance.delete_healthbot_deployment_deployment_by_id(x_iam_token=x_iam_token)
except ApiException as e:
    print("Exception when calling DefaultApi->delete_healthbot_deployment_deployment_by_id: %s\n" % e)
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

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_healthbot_dynamic_tagging**
> delete_healthbot_dynamic_tagging(x_iam_token=x_iam_token)

Delete dynamic-tagging by ID

Delete operation of resource: dynamic-tagging

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
x_iam_token = 'x_iam_token_example' # str | authentication header object (optional)

try:
    # Delete dynamic-tagging by ID
    api_instance.delete_healthbot_dynamic_tagging(x_iam_token=x_iam_token)
except ApiException as e:
    print("Exception when calling DefaultApi->delete_healthbot_dynamic_tagging: %s\n" % e)
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

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_healthbot_ingest_byoi_custom_plugin_by_id**
> delete_healthbot_ingest_byoi_custom_plugin_by_id(name, x_iam_token=x_iam_token)

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
x_iam_token = 'x_iam_token_example' # str | authentication header object (optional)

try:
    # Delete custom-plugin by ID
    api_instance.delete_healthbot_ingest_byoi_custom_plugin_by_id(name, x_iam_token=x_iam_token)
except ApiException as e:
    print("Exception when calling DefaultApi->delete_healthbot_ingest_byoi_custom_plugin_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of custom-plugin | 
 **x_iam_token** | **str**| authentication header object | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_healthbot_ingest_byoi_default_plugin_tlive_kafka_by_id**
> delete_healthbot_ingest_byoi_default_plugin_tlive_kafka_by_id(name, x_iam_token=x_iam_token)

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
x_iam_token = 'x_iam_token_example' # str | authentication header object (optional)

try:
    # Delete tlive-kafka-oc by ID
    api_instance.delete_healthbot_ingest_byoi_default_plugin_tlive_kafka_by_id(name, x_iam_token=x_iam_token)
except ApiException as e:
    print("Exception when calling DefaultApi->delete_healthbot_ingest_byoi_default_plugin_tlive_kafka_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of tlive-kafka-oc | 
 **x_iam_token** | **str**| authentication header object | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_healthbot_ingest_byoi_ingest_mapping_by_id**
> delete_healthbot_ingest_byoi_ingest_mapping_by_id(name, x_iam_token=x_iam_token)

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
x_iam_token = 'x_iam_token_example' # str | authentication header object (optional)

try:
    # Delete ingest-mapping by ID
    api_instance.delete_healthbot_ingest_byoi_ingest_mapping_by_id(name, x_iam_token=x_iam_token)
except ApiException as e:
    print("Exception when calling DefaultApi->delete_healthbot_ingest_byoi_ingest_mapping_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of ingest-mapping | 
 **x_iam_token** | **str**| authentication header object | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_healthbot_ingest_frequency_profile_by_id**
> delete_healthbot_ingest_frequency_profile_by_id(name, x_iam_token=x_iam_token)

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
x_iam_token = 'x_iam_token_example' # str | authentication header object (optional)

try:
    # Delete frequency-profile by ID
    api_instance.delete_healthbot_ingest_frequency_profile_by_id(name, x_iam_token=x_iam_token)
except ApiException as e:
    print("Exception when calling DefaultApi->delete_healthbot_ingest_frequency_profile_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| ID of name | 
 **x_iam_token** | **str**| authentication header object | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_healthbot_ingest_outbound_ssh**
> delete_healthbot_ingest_outbound_ssh(x_iam_token=x_iam_token)

Delete outbound-ssh by ID

Delete operation of resource: outbound-ssh

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
x_iam_token = 'x_iam_token_example' # str | authentication header object (optional)

try:
    # Delete outbound-ssh by ID
    api_instance.delete_healthbot_ingest_outbound_ssh(x_iam_token=x_iam_token)
except ApiException as e:
    print("Exception when calling DefaultApi->delete_healthbot_ingest_outbound_ssh: %s\n" % e)
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

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_healthbot_ingest_settings_byoi_custom_plugin_by_id**
> delete_healthbot_ingest_settings_byoi_custom_plugin_by_id(name, x_iam_token=x_iam_token)

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
x_iam_token = 'x_iam_token_example' # str | authentication header object (optional)

try:
    # Delete custom-plugin by ID
    api_instance.delete_healthbot_ingest_settings_byoi_custom_plugin_by_id(name, x_iam_token=x_iam_token)
except ApiException as e:
    print("Exception when calling DefaultApi->delete_healthbot_ingest_settings_byoi_custom_plugin_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of custom-plugin | 
 **x_iam_token** | **str**| authentication header object | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_healthbot_ingest_settings_byoi_default_plugin_tlive_kafka_by_id**
> delete_healthbot_ingest_settings_byoi_default_plugin_tlive_kafka_by_id(name, x_iam_token=x_iam_token)

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
x_iam_token = 'x_iam_token_example' # str | authentication header object (optional)

try:
    # Delete tlive-kafka-oc by ID
    api_instance.delete_healthbot_ingest_settings_byoi_default_plugin_tlive_kafka_by_id(name, x_iam_token=x_iam_token)
except ApiException as e:
    print("Exception when calling DefaultApi->delete_healthbot_ingest_settings_byoi_default_plugin_tlive_kafka_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of tlive-kafka-oc | 
 **x_iam_token** | **str**| authentication header object | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_healthbot_ingest_settings_byoi_ingest_mapping_by_id**
> delete_healthbot_ingest_settings_byoi_ingest_mapping_by_id(name, x_iam_token=x_iam_token)

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
x_iam_token = 'x_iam_token_example' # str | authentication header object (optional)

try:
    # Delete ingest-mapping by ID
    api_instance.delete_healthbot_ingest_settings_byoi_ingest_mapping_by_id(name, x_iam_token=x_iam_token)
except ApiException as e:
    print("Exception when calling DefaultApi->delete_healthbot_ingest_settings_byoi_ingest_mapping_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of ingest-mapping | 
 **x_iam_token** | **str**| authentication header object | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_healthbot_ingest_settings_frequency_profile_by_id**
> delete_healthbot_ingest_settings_frequency_profile_by_id(name, x_iam_token=x_iam_token)

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
x_iam_token = 'x_iam_token_example' # str | authentication header object (optional)

try:
    # Delete frequency-profile by ID
    api_instance.delete_healthbot_ingest_settings_frequency_profile_by_id(name, x_iam_token=x_iam_token)
except ApiException as e:
    print("Exception when calling DefaultApi->delete_healthbot_ingest_settings_frequency_profile_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| ID of name | 
 **x_iam_token** | **str**| authentication header object | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_healthbot_ingest_settings_tagging_profile_by_id**
> delete_healthbot_ingest_settings_tagging_profile_by_id(name, x_iam_token=x_iam_token)

Delete tagging-profile by ID

Delete operation of resource: tagging-profile

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
x_iam_token = 'x_iam_token_example' # str | authentication header object (optional)

try:
    # Delete tagging-profile by ID
    api_instance.delete_healthbot_ingest_settings_tagging_profile_by_id(name, x_iam_token=x_iam_token)
except ApiException as e:
    print("Exception when calling DefaultApi->delete_healthbot_ingest_settings_tagging_profile_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| ID of name | 
 **x_iam_token** | **str**| authentication header object | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_healthbot_ingest_settings_tagging_profiles**
> delete_healthbot_ingest_settings_tagging_profiles(x_iam_token=x_iam_token)

Delete tagging-profile by ID

Delete operation of resource: tagging-profile

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
x_iam_token = 'x_iam_token_example' # str | authentication header object (optional)

try:
    # Delete tagging-profile by ID
    api_instance.delete_healthbot_ingest_settings_tagging_profiles(x_iam_token=x_iam_token)
except ApiException as e:
    print("Exception when calling DefaultApi->delete_healthbot_ingest_settings_tagging_profiles: %s\n" % e)
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

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_healthbot_ingest_sflow**
> delete_healthbot_ingest_sflow(x_iam_token=x_iam_token)

Delete sflow by ID

Delete operation of resource: sflow

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
x_iam_token = 'x_iam_token_example' # str | authentication header object (optional)

try:
    # Delete sflow by ID
    api_instance.delete_healthbot_ingest_sflow(x_iam_token=x_iam_token)
except ApiException as e:
    print("Exception when calling DefaultApi->delete_healthbot_ingest_sflow: %s\n" % e)
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

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_healthbot_ingest_sflow_counter_record_by_id**
> delete_healthbot_ingest_sflow_counter_record_by_id(record_name, x_iam_token=x_iam_token)

Delete counter-record by ID

Delete operation of resource: counter-record

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
record_name = 'record_name_example' # str | ID of record-name
x_iam_token = 'x_iam_token_example' # str | authentication header object (optional)

try:
    # Delete counter-record by ID
    api_instance.delete_healthbot_ingest_sflow_counter_record_by_id(record_name, x_iam_token=x_iam_token)
except ApiException as e:
    print("Exception when calling DefaultApi->delete_healthbot_ingest_sflow_counter_record_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **record_name** | **str**| ID of record-name | 
 **x_iam_token** | **str**| authentication header object | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_healthbot_ingest_sflow_flow_record_by_id**
> delete_healthbot_ingest_sflow_flow_record_by_id(record_name, x_iam_token=x_iam_token)

Delete flow-record by ID

Delete operation of resource: flow-record

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
record_name = 'record_name_example' # str | ID of record-name
x_iam_token = 'x_iam_token_example' # str | authentication header object (optional)

try:
    # Delete flow-record by ID
    api_instance.delete_healthbot_ingest_sflow_flow_record_by_id(record_name, x_iam_token=x_iam_token)
except ApiException as e:
    print("Exception when calling DefaultApi->delete_healthbot_ingest_sflow_flow_record_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **record_name** | **str**| ID of record-name | 
 **x_iam_token** | **str**| authentication header object | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_healthbot_ingest_sflow_protocol_by_id**
> delete_healthbot_ingest_sflow_protocol_by_id(protocol_name, x_iam_token=x_iam_token)

Delete protocol by ID

Delete operation of resource: protocol

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
protocol_name = 'protocol_name_example' # str | ID of protocol-name
x_iam_token = 'x_iam_token_example' # str | authentication header object (optional)

try:
    # Delete protocol by ID
    api_instance.delete_healthbot_ingest_sflow_protocol_by_id(protocol_name, x_iam_token=x_iam_token)
except ApiException as e:
    print("Exception when calling DefaultApi->delete_healthbot_ingest_sflow_protocol_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **protocol_name** | **str**| ID of protocol-name | 
 **x_iam_token** | **str**| authentication header object | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_healthbot_ingest_sflow_sample_by_id**
> delete_healthbot_ingest_sflow_sample_by_id(sample_name, x_iam_token=x_iam_token)

Delete sample by ID

Delete operation of resource: sample

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
sample_name = 'sample_name_example' # str | ID of sample-name
x_iam_token = 'x_iam_token_example' # str | authentication header object (optional)

try:
    # Delete sample by ID
    api_instance.delete_healthbot_ingest_sflow_sample_by_id(sample_name, x_iam_token=x_iam_token)
except ApiException as e:
    print("Exception when calling DefaultApi->delete_healthbot_ingest_sflow_sample_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sample_name** | **str**| ID of sample-name | 
 **x_iam_token** | **str**| authentication header object | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_healthbot_ingest_snmp_notification**
> delete_healthbot_ingest_snmp_notification(x_iam_token=x_iam_token)

Delete snmp-notification

Delete operation of resource: snmp-notification

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
x_iam_token = 'x_iam_token_example' # str | authentication header object (optional)

try:
    # Delete snmp-notification
    api_instance.delete_healthbot_ingest_snmp_notification(x_iam_token=x_iam_token)
except ApiException as e:
    print("Exception when calling DefaultApi->delete_healthbot_ingest_snmp_notification: %s\n" % e)
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

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_healthbot_ingest_snmp_notification_v3_usm_user_by_id**
> delete_healthbot_ingest_snmp_notification_v3_usm_user_by_id(name, x_iam_token=x_iam_token)

Delete SNMPv3 user by UserName(ID)

Delete operation of resource: snmp v3 usm user

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
name = 'name_example' # str | User Name
x_iam_token = 'x_iam_token_example' # str | authentication header object (optional)

try:
    # Delete SNMPv3 user by UserName(ID)
    api_instance.delete_healthbot_ingest_snmp_notification_v3_usm_user_by_id(name, x_iam_token=x_iam_token)
except ApiException as e:
    print("Exception when calling DefaultApi->delete_healthbot_ingest_snmp_notification_v3_usm_user_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| User Name | 
 **x_iam_token** | **str**| authentication header object | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_healthbot_ingest_syslog_header_pattern_by_id**
> delete_healthbot_ingest_syslog_header_pattern_by_id(name, x_iam_token=x_iam_token)

Delete pattern by ID

Delete operation of resource: header-pattern

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
x_iam_token = 'x_iam_token_example' # str | authentication header object (optional)

try:
    # Delete pattern by ID
    api_instance.delete_healthbot_ingest_syslog_header_pattern_by_id(name, x_iam_token=x_iam_token)
except ApiException as e:
    print("Exception when calling DefaultApi->delete_healthbot_ingest_syslog_header_pattern_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| ID of name | 
 **x_iam_token** | **str**| authentication header object | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_healthbot_ingest_tagging_profile_by_id**
> delete_healthbot_ingest_tagging_profile_by_id(name, x_iam_token=x_iam_token)

Delete tagging-profile by ID

Delete operation of resource: tagging-profile

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
x_iam_token = 'x_iam_token_example' # str | authentication header object (optional)

try:
    # Delete tagging-profile by ID
    api_instance.delete_healthbot_ingest_tagging_profile_by_id(name, x_iam_token=x_iam_token)
except ApiException as e:
    print("Exception when calling DefaultApi->delete_healthbot_ingest_tagging_profile_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| ID of name | 
 **x_iam_token** | **str**| authentication header object | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_healthbot_ingest_tagging_profiles**
> delete_healthbot_ingest_tagging_profiles(x_iam_token=x_iam_token)

Delete tagging-profile by ID

Delete operation of resource: tagging-profile

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
x_iam_token = 'x_iam_token_example' # str | authentication header object (optional)

try:
    # Delete tagging-profile by ID
    api_instance.delete_healthbot_ingest_tagging_profiles(x_iam_token=x_iam_token)
except ApiException as e:
    print("Exception when calling DefaultApi->delete_healthbot_ingest_tagging_profiles: %s\n" % e)
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

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_healthbot_organization_organization_by_id**
> delete_healthbot_organization_organization_by_id(organization_name, x_iam_token=x_iam_token)

Delete organization by ID

Delete operation of resource: organization

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
organization_name = 'organization_name_example' # str | ID of organization-name
x_iam_token = 'x_iam_token_example' # str | authentication header object (optional)

try:
    # Delete organization by ID
    api_instance.delete_healthbot_organization_organization_by_id(organization_name, x_iam_token=x_iam_token)
except ApiException as e:
    print("Exception when calling DefaultApi->delete_healthbot_organization_organization_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_name** | **str**| ID of organization-name | 
 **x_iam_token** | **str**| authentication header object | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_healthbot_profile_rollup_summarization_field_profile_field_profile_by_id**
> delete_healthbot_profile_rollup_summarization_field_profile_field_profile_by_id(profile_id, x_iam_token=x_iam_token)

Delete field-profile by ID

Delete operation of resource: field-profile

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
profile_id = 'profile_id_example' # str | ID of profile-id
x_iam_token = 'x_iam_token_example' # str | authentication header object (optional)

try:
    # Delete field-profile by ID
    api_instance.delete_healthbot_profile_rollup_summarization_field_profile_field_profile_by_id(profile_id, x_iam_token=x_iam_token)
except ApiException as e:
    print("Exception when calling DefaultApi->delete_healthbot_profile_rollup_summarization_field_profile_field_profile_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **profile_id** | **str**| ID of profile-id | 
 **x_iam_token** | **str**| authentication header object | [optional] 

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

# **delete_healthbot_system_trigger_action**
> delete_healthbot_system_trigger_action()

Delete trigger-action schedulers

Delete operation of resource: trigger-action

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
    # Delete trigger-action schedulers
    api_instance.delete_healthbot_system_trigger_action()
except ApiException as e:
    print("Exception when calling DefaultApi->delete_healthbot_system_trigger_action: %s\n" % e)
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

# **delete_iceberg_ingest**
> delete_iceberg_ingest(x_iam_token=x_iam_token)

Delete ingest by ID

Delete operation of resource: ingest

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
x_iam_token = 'x_iam_token_example' # str | authentication header object (optional)

try:
    # Delete ingest by ID
    api_instance.delete_iceberg_ingest(x_iam_token=x_iam_token)
except ApiException as e:
    print("Exception when calling DefaultApi->delete_iceberg_ingest: %s\n" % e)
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

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_iceberg_ingest_flow**
> delete_iceberg_ingest_flow(x_iam_token=x_iam_token)

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
x_iam_token = 'x_iam_token_example' # str | authentication header object (optional)

try:
    # Delete flow by ID
    api_instance.delete_iceberg_ingest_flow(x_iam_token=x_iam_token)
except ApiException as e:
    print("Exception when calling DefaultApi->delete_iceberg_ingest_flow: %s\n" % e)
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

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_iceberg_ingest_flow_template_by_id**
> delete_iceberg_ingest_flow_template_by_id(name, x_iam_token=x_iam_token)

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
x_iam_token = 'x_iam_token_example' # str | authentication header object (optional)

try:
    # Delete template by ID
    api_instance.delete_iceberg_ingest_flow_template_by_id(name, x_iam_token=x_iam_token)
except ApiException as e:
    print("Exception when calling DefaultApi->delete_iceberg_ingest_flow_template_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of template | 
 **x_iam_token** | **str**| authentication header object | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_iceberg_ingest_native_gpb**
> delete_iceberg_ingest_native_gpb(x_iam_token=x_iam_token)

Delete native-gpb by ID

Delete operation of resource: native-gpb

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
x_iam_token = 'x_iam_token_example' # str | authentication header object (optional)

try:
    # Delete native-gpb by ID
    api_instance.delete_iceberg_ingest_native_gpb(x_iam_token=x_iam_token)
except ApiException as e:
    print("Exception when calling DefaultApi->delete_iceberg_ingest_native_gpb: %s\n" % e)
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

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_iceberg_ingest_settings**
> delete_iceberg_ingest_settings(x_iam_token=x_iam_token)

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
x_iam_token = 'x_iam_token_example' # str | authentication header object (optional)

try:
    # Delete ingest-settings by ID
    api_instance.delete_iceberg_ingest_settings(x_iam_token=x_iam_token)
except ApiException as e:
    print("Exception when calling DefaultApi->delete_iceberg_ingest_settings: %s\n" % e)
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

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_iceberg_ingest_settings_flow**
> delete_iceberg_ingest_settings_flow(x_iam_token=x_iam_token)

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
x_iam_token = 'x_iam_token_example' # str | authentication header object (optional)

try:
    # Delete flow by ID
    api_instance.delete_iceberg_ingest_settings_flow(x_iam_token=x_iam_token)
except ApiException as e:
    print("Exception when calling DefaultApi->delete_iceberg_ingest_settings_flow: %s\n" % e)
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

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_iceberg_ingest_settings_flow_template_by_id**
> delete_iceberg_ingest_settings_flow_template_by_id(name, x_iam_token=x_iam_token)

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
x_iam_token = 'x_iam_token_example' # str | authentication header object (optional)

try:
    # Delete template by ID
    api_instance.delete_iceberg_ingest_settings_flow_template_by_id(name, x_iam_token=x_iam_token)
except ApiException as e:
    print("Exception when calling DefaultApi->delete_iceberg_ingest_settings_flow_template_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of template | 
 **x_iam_token** | **str**| authentication header object | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_iceberg_ingest_settings_syslog**
> delete_iceberg_ingest_settings_syslog(x_iam_token=x_iam_token)

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
x_iam_token = 'x_iam_token_example' # str | authentication header object (optional)

try:
    # Delete syslog by ID
    api_instance.delete_iceberg_ingest_settings_syslog(x_iam_token=x_iam_token)
except ApiException as e:
    print("Exception when calling DefaultApi->delete_iceberg_ingest_settings_syslog: %s\n" % e)
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

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_iceberg_ingest_settings_syslog_pattern_by_id**
> delete_iceberg_ingest_settings_syslog_pattern_by_id(name, x_iam_token=x_iam_token)

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
x_iam_token = 'x_iam_token_example' # str | authentication header object (optional)

try:
    # Delete pattern by ID
    api_instance.delete_iceberg_ingest_settings_syslog_pattern_by_id(name, x_iam_token=x_iam_token)
except ApiException as e:
    print("Exception when calling DefaultApi->delete_iceberg_ingest_settings_syslog_pattern_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of pattern | 
 **x_iam_token** | **str**| authentication header object | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_iceberg_ingest_settings_syslog_pattern_set_by_id**
> delete_iceberg_ingest_settings_syslog_pattern_set_by_id(name, x_iam_token=x_iam_token)

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
x_iam_token = 'x_iam_token_example' # str | authentication header object (optional)

try:
    # Delete pattern-set by ID
    api_instance.delete_iceberg_ingest_settings_syslog_pattern_set_by_id(name, x_iam_token=x_iam_token)
except ApiException as e:
    print("Exception when calling DefaultApi->delete_iceberg_ingest_settings_syslog_pattern_set_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of pattern-set | 
 **x_iam_token** | **str**| authentication header object | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_iceberg_ingest_syslog**
> delete_iceberg_ingest_syslog(x_iam_token=x_iam_token)

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
x_iam_token = 'x_iam_token_example' # str | authentication header object (optional)

try:
    # Delete syslog by ID
    api_instance.delete_iceberg_ingest_syslog(x_iam_token=x_iam_token)
except ApiException as e:
    print("Exception when calling DefaultApi->delete_iceberg_ingest_syslog: %s\n" % e)
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

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_iceberg_ingest_syslog_pattern_by_id**
> delete_iceberg_ingest_syslog_pattern_by_id(name, x_iam_token=x_iam_token)

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
x_iam_token = 'x_iam_token_example' # str | authentication header object (optional)

try:
    # Delete pattern by ID
    api_instance.delete_iceberg_ingest_syslog_pattern_by_id(name, x_iam_token=x_iam_token)
except ApiException as e:
    print("Exception when calling DefaultApi->delete_iceberg_ingest_syslog_pattern_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of pattern | 
 **x_iam_token** | **str**| authentication header object | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_iceberg_ingest_syslog_pattern_set_by_id**
> delete_iceberg_ingest_syslog_pattern_set_by_id(name, x_iam_token=x_iam_token)

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
x_iam_token = 'x_iam_token_example' # str | authentication header object (optional)

try:
    # Delete pattern-set by ID
    api_instance.delete_iceberg_ingest_syslog_pattern_set_by_id(name, x_iam_token=x_iam_token)
except ApiException as e:
    print("Exception when calling DefaultApi->delete_iceberg_ingest_syslog_pattern_set_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of pattern-set | 
 **x_iam_token** | **str**| authentication header object | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_iceberg_profile_data_summarization_raw_by_id**
> delete_iceberg_profile_data_summarization_raw_by_id(name, x_iam_token=x_iam_token)

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
x_iam_token = 'x_iam_token_example' # str | authentication header object (optional)

try:
    # Delete raw-data-summarization by ID
    api_instance.delete_iceberg_profile_data_summarization_raw_by_id(name, x_iam_token=x_iam_token)
except ApiException as e:
    print("Exception when calling DefaultApi->delete_iceberg_profile_data_summarization_raw_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of raw-data-summarization | 
 **x_iam_token** | **str**| authentication header object | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_iceberg_profile_security_ca_profile_by_id**
> delete_iceberg_profile_security_ca_profile_by_id(name, x_iam_token=x_iam_token)

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
x_iam_token = 'x_iam_token_example' # str | authentication header object (optional)

try:
    # Delete ca-profile by ID
    api_instance.delete_iceberg_profile_security_ca_profile_by_id(name, x_iam_token=x_iam_token)
except ApiException as e:
    print("Exception when calling DefaultApi->delete_iceberg_profile_security_ca_profile_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of ca-profile | 
 **x_iam_token** | **str**| authentication header object | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_iceberg_profile_security_local_certificate_by_id**
> delete_iceberg_profile_security_local_certificate_by_id(name, x_iam_token=x_iam_token)

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
x_iam_token = 'x_iam_token_example' # str | authentication header object (optional)

try:
    # Delete local-certificate by ID
    api_instance.delete_iceberg_profile_security_local_certificate_by_id(name, x_iam_token=x_iam_token)
except ApiException as e:
    print("Exception when calling DefaultApi->delete_iceberg_profile_security_local_certificate_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of local-certificate | 
 **x_iam_token** | **str**| authentication header object | [optional] 

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
> delete_iceberg_profiles(x_iam_token=x_iam_token)

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
x_iam_token = 'x_iam_token_example' # str | authentication header object (optional)

try:
    # Delete profile by ID
    api_instance.delete_iceberg_profiles(x_iam_token=x_iam_token)
except ApiException as e:
    print("Exception when calling DefaultApi->delete_iceberg_profiles: %s\n" % e)
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

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_dynamic_tagging_by_key**
> str get_dynamic_tagging_by_key(key_name, x_iam_token=x_iam_token)

Get value of corresponding Dynamic-tagging key

Get Value of corresponding key from dynamic-tagging

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
key_name = 'key_name_example' # str | Dynamic-tagging Key
x_iam_token = 'x_iam_token_example' # str | authentication header object (optional)

try:
    # Get value of corresponding Dynamic-tagging key
    api_response = api_instance.get_dynamic_tagging_by_key(key_name, x_iam_token=x_iam_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_dynamic_tagging_by_key: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key_name** | **str**| Dynamic-tagging Key | 
 **x_iam_token** | **str**| authentication header object | [optional] 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_fields_from_xpath**
> FieldCaptureSchema get_fields_from_xpath(xpath, timestamp=timestamp)

Get last value of all fields before a given timestamp.

Get the values of all fields

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
xpath = 'xpath_example' # str | XPATH
timestamp = 'timestamp_example' # str | Timestamp (optional)

try:
    # Get last value of all fields before a given timestamp.
    api_response = api_instance.get_fields_from_xpath(xpath, timestamp=timestamp)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_fields_from_xpath: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xpath** | **str**| XPATH | 
 **timestamp** | **str**| Timestamp | [optional] 

### Return type

[**FieldCaptureSchema**](FieldCaptureSchema.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, multipart/form-data
 - **Accept**: application/json, application/octet-stream

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **grafana_login**
> grafana_login(x_iam_token=x_iam_token)

Login to grafana

Login to Grafana

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
x_iam_token = 'x_iam_token_example' # str | authentication header object (optional)

try:
    # Login to grafana
    api_instance.grafana_login(x_iam_token=x_iam_token)
except ApiException as e:
    print("Exception when calling DefaultApi->grafana_login: %s\n" % e)
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

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **inspect_command_rpc_table_on_device**
> inspect_command_rpc_table_on_device(command_rpc_detail, x_iam_token=x_iam_token)

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
x_iam_token = 'x_iam_token_example' # str | authentication header object (optional)

try:
    # Inspect the given iAgent table.
    api_instance.inspect_command_rpc_table_on_device(command_rpc_detail, x_iam_token=x_iam_token)
except ApiException as e:
    print("Exception when calling DefaultApi->inspect_command_rpc_table_on_device: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **command_rpc_detail** | [**CommandRpc**](CommandRpc.md)| command-rpc object | 
 **x_iam_token** | **str**| authentication header object | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **restore_grafana**
> restore_grafana(restore_file, x_iam_token=x_iam_token)

Restore Grafana configuration

Restore Grafana configuration

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
x_iam_token = 'x_iam_token_example' # str | authentication header object (optional)

try:
    # Restore Grafana configuration
    api_instance.restore_grafana(restore_file, x_iam_token=x_iam_token)
except ApiException as e:
    print("Exception when calling DefaultApi->restore_grafana: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **restore_file** | **file**| File content | 
 **x_iam_token** | **str**| authentication header object | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json, application/octet-stream

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **restore_helper_files**
> restore_helper_files(restore_file, x_iam_token=x_iam_token)

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
x_iam_token = 'x_iam_token_example' # str | authentication header object (optional)

try:
    # Upload a helper-file.
    api_instance.restore_helper_files(restore_file, x_iam_token=x_iam_token)
except ApiException as e:
    print("Exception when calling DefaultApi->restore_helper_files: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **restore_file** | **file**| File content | 
 **x_iam_token** | **str**| authentication header object | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json, application/octet-stream

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_configuration_jobs**
> list[InlineResponse200] retrieve_configuration_jobs(x_iam_token=x_iam_token, job_id=job_id, job_status=job_status)



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
x_iam_token = 'x_iam_token_example' # str | authentication header object (optional)
job_id = 'job_id_example' # str | Id of Job (optional)
job_status = 'job_status_example' # str | Type of job (optional)

try:
    api_response = api_instance.retrieve_configuration_jobs(x_iam_token=x_iam_token, job_id=job_id, job_status=job_status)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->retrieve_configuration_jobs: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_iam_token** | **str**| authentication header object | [optional] 
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
> list[TableSchema] retrieve_data_database_table(x_iam_token=x_iam_token, device_id=device_id, device_group_name=device_group_name, network_group_name=network_group_name)

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
x_iam_token = 'x_iam_token_example' # str | authentication header object (optional)
device_id = 'device_id_example' # str | Name of device (optional)
device_group_name = 'device_group_name_example' # str | Name of device-group (optional)
network_group_name = 'network_group_name_example' # str | Name of network-group (optional)

try:
    # Get information about tables for a device of a device-group.
    api_response = api_instance.retrieve_data_database_table(x_iam_token=x_iam_token, device_id=device_id, device_group_name=device_group_name, network_group_name=network_group_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->retrieve_data_database_table: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_iam_token** | **str**| authentication header object | [optional] 
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
> list[str] retrieve_data_database_table_column_by_table_name(table_name, x_iam_token=x_iam_token, device_id=device_id, device_group_name=device_group_name, network_group_name=network_group_name)

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
x_iam_token = 'x_iam_token_example' # str | authentication header object (optional)
device_id = 'device_id_example' # str | Name of device (optional)
device_group_name = 'device_group_name_example' # str | Name of device-group (optional)
network_group_name = 'network_group_name_example' # str | Name of network-group (optional)

try:
    # Get information about columns in a table.
    api_response = api_instance.retrieve_data_database_table_column_by_table_name(table_name, x_iam_token=x_iam_token, device_id=device_id, device_group_name=device_group_name, network_group_name=network_group_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->retrieve_data_database_table_column_by_table_name: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **table_name** | **str**| Name of table | 
 **x_iam_token** | **str**| authentication header object | [optional] 
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
> list[str] retrieve_data_database_tags_by_table_name(table_name, x_iam_token=x_iam_token, device_id=device_id, device_group_name=device_group_name, network_group_name=network_group_name, tag=tag, where_clause=where_clause)

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
x_iam_token = 'x_iam_token_example' # str | authentication header object (optional)
device_id = 'device_id_example' # str | Name of device (optional)
device_group_name = 'device_group_name_example' # str | Name of device-group (optional)
network_group_name = 'network_group_name_example' # str | Name of network-group (optional)
tag = 'tag_example' # str | Tag key for which values are requested. (optional)
where_clause = 'where_clause_example' # str | Where condition to select values for the requested key. This would not be processed if there is no `tag` query parameter. eg: `tag_key1=val1 AND tag_key2=val2` (optional)

try:
    # Get information about tags keys and values in a table.
    api_response = api_instance.retrieve_data_database_tags_by_table_name(table_name, x_iam_token=x_iam_token, device_id=device_id, device_group_name=device_group_name, network_group_name=network_group_name, tag=tag, where_clause=where_clause)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->retrieve_data_database_tags_by_table_name: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **table_name** | **str**| Name of table | 
 **x_iam_token** | **str**| authentication header object | [optional] 
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
> object retrieve_debug_jobs(x_iam_token=x_iam_token, job_id=job_id)



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
x_iam_token = 'x_iam_token_example' # str | authentication header object (optional)
job_id = 'job_id_example' # str | Id of Job (optional)

try:
    api_response = api_instance.retrieve_debug_jobs(x_iam_token=x_iam_token, job_id=job_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->retrieve_debug_jobs: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_iam_token** | **str**| authentication header object | [optional] 
 **job_id** | [**str**](.md)| Id of Job | [optional] 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, multipart/form-data
 - **Accept**: application/json, application/octet-stream

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_event**
> list[Event] retrieve_event(from_timestamp, device_id, x_iam_token=x_iam_token, to_timestamp=to_timestamp, device_group_name=device_group_name, granularity=granularity, color=color)

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
x_iam_token = 'x_iam_token_example' # str | authentication header object (optional)
to_timestamp = '2013-10-20T19:20:30+01:00' # datetime | Ending timestamp (optional)
device_group_name = 'device_group_name_example' # str | Device group's device-group-name of which the device is part (optional)
granularity = 'granularity_example' # str | Granularity of query (optional)
color = 'color_example' # str | Color of events. (optional)

try:
    # Get all events for a device.
    api_response = api_instance.retrieve_event(from_timestamp, device_id, x_iam_token=x_iam_token, to_timestamp=to_timestamp, device_group_name=device_group_name, granularity=granularity, color=color)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->retrieve_event: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **from_timestamp** | **datetime**| Starting timestamp | 
 **device_id** | **str**| device-id of the device for which events are requested | 
 **x_iam_token** | **str**| authentication header object | [optional] 
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
> list[Event] retrieve_event_by_event_name(event_name, from_timestamp, device_id, x_iam_token=x_iam_token, to_timestamp=to_timestamp, device_group_name=device_group_name, granularity=granularity, color=color)

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
x_iam_token = 'x_iam_token_example' # str | authentication header object (optional)
to_timestamp = '2013-10-20T19:20:30+01:00' # datetime | Ending timestamp (optional)
device_group_name = 'device_group_name_example' # str | device-group-name of which the device is part (optional)
granularity = 'granularity_example' # str | Granularity of query (optional)
color = 'color_example' # str | Color of events. (optional)

try:
    # Get instances of a device event.
    api_response = api_instance.retrieve_event_by_event_name(event_name, from_timestamp, device_id, x_iam_token=x_iam_token, to_timestamp=to_timestamp, device_group_name=device_group_name, granularity=granularity, color=color)
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
 **x_iam_token** | **str**| authentication header object | [optional] 
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
> list[Event] retrieve_event_by_event_name_device_group(event_name, from_timestamp, device_group_name, x_iam_token=x_iam_token, to_timestamp=to_timestamp, granularity=granularity, device_id=device_id, color=color)

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
x_iam_token = 'x_iam_token_example' # str | authentication header object (optional)
to_timestamp = '2013-10-20T19:20:30+01:00' # datetime | Ending timestamp (optional)
granularity = 'granularity_example' # str | Granularity of query (optional)
device_id = ['device_id_example'] # list[str] | list of devices under a device-group to be fetched (optional)
color = 'color_example' # str | Color of events. (optional)

try:
    # Get instances of a device-group event.
    api_response = api_instance.retrieve_event_by_event_name_device_group(event_name, from_timestamp, device_group_name, x_iam_token=x_iam_token, to_timestamp=to_timestamp, granularity=granularity, device_id=device_id, color=color)
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
 **x_iam_token** | **str**| authentication header object | [optional] 
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
> list[Event] retrieve_event_by_event_name_network_group(event_name, from_timestamp, network_group_name, x_iam_token=x_iam_token, to_timestamp=to_timestamp, granularity=granularity, color=color)

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
x_iam_token = 'x_iam_token_example' # str | authentication header object (optional)
to_timestamp = '2013-10-20T19:20:30+01:00' # datetime | Ending timestamp (optional)
granularity = 'granularity_example' # str | Granularity of query (optional)
color = 'color_example' # str | Color of events. (optional)

try:
    # Get instances of a network-group event.
    api_response = api_instance.retrieve_event_by_event_name_network_group(event_name, from_timestamp, network_group_name, x_iam_token=x_iam_token, to_timestamp=to_timestamp, granularity=granularity, color=color)
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
 **x_iam_token** | **str**| authentication header object | [optional] 
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
> list[Event] retrieve_event_device_group(from_timestamp, device_group_name, x_iam_token=x_iam_token, to_timestamp=to_timestamp, granularity=granularity, device_id=device_id, color=color)

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
x_iam_token = 'x_iam_token_example' # str | authentication header object (optional)
to_timestamp = '2013-10-20T19:20:30+01:00' # datetime | Ending timestamp (optional)
granularity = 'granularity_example' # str | Granularity of query (optional)
device_id = ['device_id_example'] # list[str] | list of devices under a device-group to be fetched (optional)
color = 'color_example' # str | Color of events. (optional)

try:
    # Get all events for a device-group.
    api_response = api_instance.retrieve_event_device_group(from_timestamp, device_group_name, x_iam_token=x_iam_token, to_timestamp=to_timestamp, granularity=granularity, device_id=device_id, color=color)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->retrieve_event_device_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **from_timestamp** | **datetime**| Starting timestamp | 
 **device_group_name** | **str**| device_group_name of the device-group for which events are requested | 
 **x_iam_token** | **str**| authentication header object | [optional] 
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
> list[Event] retrieve_event_network_group(from_timestamp, network_group_name, x_iam_token=x_iam_token, to_timestamp=to_timestamp, granularity=granularity, color=color)

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
x_iam_token = 'x_iam_token_example' # str | authentication header object (optional)
to_timestamp = '2013-10-20T19:20:30+01:00' # datetime | Ending timestamp (optional)
granularity = 'granularity_example' # str | Granularity of query (optional)
color = 'color_example' # str | Color of events. (optional)

try:
    # Get all events for a network-group.
    api_response = api_instance.retrieve_event_network_group(from_timestamp, network_group_name, x_iam_token=x_iam_token, to_timestamp=to_timestamp, granularity=granularity, color=color)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->retrieve_event_network_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **from_timestamp** | **datetime**| Starting timestamp | 
 **network_group_name** | **str**| network_group_name of the network-group for which events are requested | 
 **x_iam_token** | **str**| authentication header object | [optional] 
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
> list[Event] retrieve_events(from_timestamp, x_iam_token=x_iam_token, to_timestamp=to_timestamp, color=color)

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
x_iam_token = 'x_iam_token_example' # str | authentication header object (optional)
to_timestamp = '2013-10-20T19:20:30+01:00' # datetime | Ending timestamp (optional)
color = 'color_example' # str | Color of events. (optional)

try:
    # Get all events.
    api_response = api_instance.retrieve_events(from_timestamp, x_iam_token=x_iam_token, to_timestamp=to_timestamp, color=color)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->retrieve_events: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **from_timestamp** | **datetime**| Starting timestamp | 
 **x_iam_token** | **str**| authentication header object | [optional] 
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
> file retrieve_files_certificates_by_file_name(file_name, x_iam_token=x_iam_token, input_path=input_path, certificate_type=certificate_type)

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
x_iam_token = 'x_iam_token_example' # str | authentication header object (optional)
input_path = 'input_path_example' # str | Input path (optional)
certificate_type = 'certificate_type_example' # str | Certificate type (optional)

try:
    # Download a certificate-file.
    api_response = api_instance.retrieve_files_certificates_by_file_name(file_name, x_iam_token=x_iam_token, input_path=input_path, certificate_type=certificate_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->retrieve_files_certificates_by_file_name: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file_name** | **str**| File name | 
 **x_iam_token** | **str**| authentication header object | [optional] 
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
> list[str] retrieve_files_helper_files(x_iam_token=x_iam_token, input_path=input_path)

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
x_iam_token = 'x_iam_token_example' # str | authentication header object (optional)
input_path = 'input_path_example' # str | Input path (optional)

try:
    # Get all helper-file names.
    api_response = api_instance.retrieve_files_helper_files(x_iam_token=x_iam_token, input_path=input_path)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->retrieve_files_helper_files: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_iam_token** | **str**| authentication header object | [optional] 
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
> file retrieve_files_helper_files_by_file_name(file_name, x_iam_token=x_iam_token, input_path=input_path)

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
x_iam_token = 'x_iam_token_example' # str | authentication header object (optional)
input_path = 'input_path_example' # str | Input path (optional)

try:
    # Download a helper-file.
    api_response = api_instance.retrieve_files_helper_files_by_file_name(file_name, x_iam_token=x_iam_token, input_path=input_path)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->retrieve_files_helper_files_by_file_name: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file_name** | **str**| File name | 
 **x_iam_token** | **str**| authentication header object | [optional] 
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
> HealthSchema retrieve_health_all(x_iam_token=x_iam_token)

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
x_iam_token = 'x_iam_token_example' # str | authentication header object (optional)

try:
    # Return a dict with health of devices in device groups and network groups
    api_response = api_instance.retrieve_health_all(x_iam_token=x_iam_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->retrieve_health_all: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_iam_token** | **str**| authentication header object | [optional] 

### Return type

[**HealthSchema**](HealthSchema.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, multipart/form-data
 - **Accept**: application/json, application/octet-stream

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_health_tree_by_device_group**
> DeviceGroupHealthTree retrieve_health_tree_by_device_group(device_group_name, x_iam_token=x_iam_token, timestamp=timestamp, tolerance=tolerance, device=device)

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
x_iam_token = 'x_iam_token_example' # str | authentication header object (optional)
timestamp = '2013-10-20T19:20:30+01:00' # datetime | Timestamp at which health tree is requested. If not specified, current server timestamp is used. (optional)
tolerance = 789 # int | Timestamp tolerance in seconds. With this option, health-tree will contain latest data between `timestamp-2*tolerance` and `timestamp`. Default value is `2*frequency` where `frequency` is extracted from `trigger`. (optional)
device = ['device_example'] # list[str] | list of devices under a device-group to be fetched (optional)

try:
    # Get device-group health-tree.
    api_response = api_instance.retrieve_health_tree_by_device_group(device_group_name, x_iam_token=x_iam_token, timestamp=timestamp, tolerance=tolerance, device=device)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->retrieve_health_tree_by_device_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_group_name** | **str**| &#x60;device-group-name&#x60; of device-group | 
 **x_iam_token** | **str**| authentication header object | [optional] 
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
> DeviceHealthTree retrieve_health_tree_by_id(device_id, x_iam_token=x_iam_token, timestamp=timestamp, tolerance=tolerance)

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
x_iam_token = 'x_iam_token_example' # str | authentication header object (optional)
timestamp = '2013-10-20T19:20:30+01:00' # datetime | Timestamp at which health tree is requested. If not specified, current server timestamp is used. (optional)
tolerance = 789 # int | Timestamp tolerance in seconds. With this option, health-tree will contain latest data between `timestamp-2*tolerance` and `timestamp`. Default value is `2*frequency` where `frequency` is extracted from `trigger`. (optional)

try:
    # Return a device's health-tree.
    api_response = api_instance.retrieve_health_tree_by_id(device_id, x_iam_token=x_iam_token, timestamp=timestamp, tolerance=tolerance)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->retrieve_health_tree_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **str**| &#x60;device-id&#x60; of device | 
 **x_iam_token** | **str**| authentication header object | [optional] 
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
> NetworkHealthTree retrieve_health_tree_by_network_group(network_group_name, x_iam_token=x_iam_token, timestamp=timestamp, tolerance=tolerance)

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
x_iam_token = 'x_iam_token_example' # str | authentication header object (optional)
timestamp = '2013-10-20T19:20:30+01:00' # datetime | Timestamp at which health tree is requested. If not specified, current server timestamp is used. (optional)
tolerance = 789 # int | Timestamp tolerance in seconds. With this option, health-tree will contain latest data between `timestamp-2*tolerance` and `timestamp`. Default value is `2*frequency` where `frequency` is extracted from `trigger`. (optional)

try:
    # Get network-group health-tree.
    api_response = api_instance.retrieve_health_tree_by_network_group(network_group_name, x_iam_token=x_iam_token, timestamp=timestamp, tolerance=tolerance)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->retrieve_health_tree_by_network_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **network_group_name** | **str**| &#x60;network-group-name&#x60; of network-group | 
 **x_iam_token** | **str**| authentication header object | [optional] 
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

# **retrieve_healthbot_deployment_deployment**
> DeploymentSchema retrieve_healthbot_deployment_deployment(x_iam_token=x_iam_token, working=working)

Retrieve deployment

Retrieve operation of resource: deployment

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
x_iam_token = 'x_iam_token_example' # str | authentication header object (optional)
working = true # bool | true queries undeployed configuration (optional)

try:
    # Retrieve deployment
    api_response = api_instance.retrieve_healthbot_deployment_deployment(x_iam_token=x_iam_token, working=working)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->retrieve_healthbot_deployment_deployment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_iam_token** | **str**| authentication header object | [optional] 
 **working** | **bool**| true queries undeployed configuration | [optional] 

### Return type

[**DeploymentSchema**](DeploymentSchema.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_healthbot_device_details_by_uuids**
> DeviceDetailsSchema retrieve_healthbot_device_details_by_uuids(uuid_object, x_iam_token=x_iam_token)

Get device-identifying details by for specified UUIDs.

Get device-identifying details (device-id and TSDB databases if playbooks are deployed on it) for all the UUIDs present in the request body.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
uuid_object = swagger_client.UuidObject() # UuidObject | device_uuids object
x_iam_token = 'x_iam_token_example' # str | authentication header object (optional)

try:
    # Get device-identifying details by for specified UUIDs.
    api_response = api_instance.retrieve_healthbot_device_details_by_uuids(uuid_object, x_iam_token=x_iam_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->retrieve_healthbot_device_details_by_uuids: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid_object** | [**UuidObject**](UuidObject.md)| device_uuids object | 
 **x_iam_token** | **str**| authentication header object | [optional] 

### Return type

[**DeviceDetailsSchema**](DeviceDetailsSchema.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_healthbot_dynamic_tagging**
> list[str] retrieve_healthbot_dynamic_tagging(x_iam_token=x_iam_token)

Retrieve dynamic-tagging by ID

Retrieve operation of resource: dynamic-tagging

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
x_iam_token = 'x_iam_token_example' # str | authentication header object (optional)

try:
    # Retrieve dynamic-tagging by ID
    api_response = api_instance.retrieve_healthbot_dynamic_tagging(x_iam_token=x_iam_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->retrieve_healthbot_dynamic_tagging: %s\n" % e)
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

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_healthbot_ingest_byoi_custom_plugin_by_id**
> CustomPluginSchema retrieve_healthbot_ingest_byoi_custom_plugin_by_id(name, x_iam_token=x_iam_token, working=working)

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
x_iam_token = 'x_iam_token_example' # str | authentication header object (optional)
working = true # bool | true queries undeployed configuration (optional)

try:
    # Retrieve custom-plugin by ID
    api_response = api_instance.retrieve_healthbot_ingest_byoi_custom_plugin_by_id(name, x_iam_token=x_iam_token, working=working)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->retrieve_healthbot_ingest_byoi_custom_plugin_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of custom-plugin | 
 **x_iam_token** | **str**| authentication header object | [optional] 
 **working** | **bool**| true queries undeployed configuration | [optional] 

### Return type

[**CustomPluginSchema**](CustomPluginSchema.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_healthbot_ingest_byoi_custom_plugins**
> CustomPluginSchema retrieve_healthbot_ingest_byoi_custom_plugins(x_iam_token=x_iam_token, working=working)

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
x_iam_token = 'x_iam_token_example' # str | authentication header object (optional)
working = true # bool | true queries undeployed configuration (optional)

try:
    # Retrieve custom-plugin by ID
    api_response = api_instance.retrieve_healthbot_ingest_byoi_custom_plugins(x_iam_token=x_iam_token, working=working)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->retrieve_healthbot_ingest_byoi_custom_plugins: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_iam_token** | **str**| authentication header object | [optional] 
 **working** | **bool**| true queries undeployed configuration | [optional] 

### Return type

[**CustomPluginSchema**](CustomPluginSchema.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_healthbot_ingest_byoi_default_plugin_tlive_kafka_by_id**
> TliveKafkaOcSchema retrieve_healthbot_ingest_byoi_default_plugin_tlive_kafka_by_id(name, x_iam_token=x_iam_token, working=working)

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
x_iam_token = 'x_iam_token_example' # str | authentication header object (optional)
working = true # bool | true queries undeployed configuration (optional)

try:
    # Retrieve tlive-kafka-oc by ID
    api_response = api_instance.retrieve_healthbot_ingest_byoi_default_plugin_tlive_kafka_by_id(name, x_iam_token=x_iam_token, working=working)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->retrieve_healthbot_ingest_byoi_default_plugin_tlive_kafka_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of tlive-kafka-oc | 
 **x_iam_token** | **str**| authentication header object | [optional] 
 **working** | **bool**| true queries undeployed configuration | [optional] 

### Return type

[**TliveKafkaOcSchema**](TliveKafkaOcSchema.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_healthbot_ingest_byoi_default_plugin_tlive_kafkas**
> list[str] retrieve_healthbot_ingest_byoi_default_plugin_tlive_kafkas(x_iam_token=x_iam_token, working=working)

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
x_iam_token = 'x_iam_token_example' # str | authentication header object (optional)
working = true # bool | true queries undeployed configuration (optional)

try:
    # Retrieve tlive-kafka-oc
    api_response = api_instance.retrieve_healthbot_ingest_byoi_default_plugin_tlive_kafkas(x_iam_token=x_iam_token, working=working)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->retrieve_healthbot_ingest_byoi_default_plugin_tlive_kafkas: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_iam_token** | **str**| authentication header object | [optional] 
 **working** | **bool**| true queries undeployed configuration | [optional] 

### Return type

**list[str]**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_healthbot_ingest_byoi_ingest_mapping_by_id**
> IngestMappingSchema retrieve_healthbot_ingest_byoi_ingest_mapping_by_id(name, x_iam_token=x_iam_token, working=working)

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
x_iam_token = 'x_iam_token_example' # str | authentication header object (optional)
working = true # bool | true queries undeployed configuration (optional)

try:
    # Retrieve ingest-mapping by ID
    api_response = api_instance.retrieve_healthbot_ingest_byoi_ingest_mapping_by_id(name, x_iam_token=x_iam_token, working=working)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->retrieve_healthbot_ingest_byoi_ingest_mapping_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of ingest-mapping | 
 **x_iam_token** | **str**| authentication header object | [optional] 
 **working** | **bool**| true queries undeployed configuration | [optional] 

### Return type

[**IngestMappingSchema**](IngestMappingSchema.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_healthbot_ingest_byoi_ingest_mappings**
> list[str] retrieve_healthbot_ingest_byoi_ingest_mappings(x_iam_token=x_iam_token, working=working)

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
x_iam_token = 'x_iam_token_example' # str | authentication header object (optional)
working = true # bool | true queries undeployed configuration (optional)

try:
    # Retrieve ingest-mapping
    api_response = api_instance.retrieve_healthbot_ingest_byoi_ingest_mappings(x_iam_token=x_iam_token, working=working)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->retrieve_healthbot_ingest_byoi_ingest_mappings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_iam_token** | **str**| authentication header object | [optional] 
 **working** | **bool**| true queries undeployed configuration | [optional] 

### Return type

**list[str]**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_healthbot_ingest_frequency_profile**
> list[str] retrieve_healthbot_ingest_frequency_profile(x_iam_token=x_iam_token, working=working)

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
x_iam_token = 'x_iam_token_example' # str | authentication header object (optional)
working = true # bool | true queries undeployed configuration (optional)

try:
    # Retrieve frequency-profile
    api_response = api_instance.retrieve_healthbot_ingest_frequency_profile(x_iam_token=x_iam_token, working=working)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->retrieve_healthbot_ingest_frequency_profile: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_iam_token** | **str**| authentication header object | [optional] 
 **working** | **bool**| true queries undeployed configuration | [optional] 

### Return type

**list[str]**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_healthbot_ingest_frequency_profile_by_id**
> FrequencyProfileSchema retrieve_healthbot_ingest_frequency_profile_by_id(name, x_iam_token=x_iam_token, working=working)

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
x_iam_token = 'x_iam_token_example' # str | authentication header object (optional)
working = true # bool | true queries undeployed configuration (optional)

try:
    # Retrieve frequency-profile by ID
    api_response = api_instance.retrieve_healthbot_ingest_frequency_profile_by_id(name, x_iam_token=x_iam_token, working=working)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->retrieve_healthbot_ingest_frequency_profile_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| ID of name | 
 **x_iam_token** | **str**| authentication header object | [optional] 
 **working** | **bool**| true queries undeployed configuration | [optional] 

### Return type

[**FrequencyProfileSchema**](FrequencyProfileSchema.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_healthbot_ingest_outbound_ssh**
> OutboundSshSchema retrieve_healthbot_ingest_outbound_ssh(working=working, x_iam_token=x_iam_token)

Retrieve outbound-ssh

Retrieve operation of resource: outbound-ssh

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
x_iam_token = 'x_iam_token_example' # str | authentication header object (optional)

try:
    # Retrieve outbound-ssh
    api_response = api_instance.retrieve_healthbot_ingest_outbound_ssh(working=working, x_iam_token=x_iam_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->retrieve_healthbot_ingest_outbound_ssh: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **working** | **bool**| true queries undeployed configuration | [optional] 
 **x_iam_token** | **str**| authentication header object | [optional] 

### Return type

[**OutboundSshSchema**](OutboundSshSchema.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_healthbot_ingest_settings_byoi_custom_plugin_by_id**
> CustomPluginSchema retrieve_healthbot_ingest_settings_byoi_custom_plugin_by_id(name, x_iam_token=x_iam_token, working=working)

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
x_iam_token = 'x_iam_token_example' # str | authentication header object (optional)
working = true # bool | true queries undeployed configuration (optional)

try:
    # Retrieve custom-plugin by ID
    api_response = api_instance.retrieve_healthbot_ingest_settings_byoi_custom_plugin_by_id(name, x_iam_token=x_iam_token, working=working)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->retrieve_healthbot_ingest_settings_byoi_custom_plugin_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of custom-plugin | 
 **x_iam_token** | **str**| authentication header object | [optional] 
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
> CustomPluginSchema retrieve_healthbot_ingest_settings_byoi_custom_plugins(x_iam_token=x_iam_token, working=working)

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
x_iam_token = 'x_iam_token_example' # str | authentication header object (optional)
working = true # bool | true queries undeployed configuration (optional)

try:
    # Retrieve custom-plugin by ID
    api_response = api_instance.retrieve_healthbot_ingest_settings_byoi_custom_plugins(x_iam_token=x_iam_token, working=working)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->retrieve_healthbot_ingest_settings_byoi_custom_plugins: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_iam_token** | **str**| authentication header object | [optional] 
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
> TliveKafkaOcSchema retrieve_healthbot_ingest_settings_byoi_default_plugin_tlive_kafka_by_id(name, x_iam_token=x_iam_token, working=working)

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
x_iam_token = 'x_iam_token_example' # str | authentication header object (optional)
working = true # bool | true queries undeployed configuration (optional)

try:
    # Retrieve tlive-kafka-oc by ID
    api_response = api_instance.retrieve_healthbot_ingest_settings_byoi_default_plugin_tlive_kafka_by_id(name, x_iam_token=x_iam_token, working=working)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->retrieve_healthbot_ingest_settings_byoi_default_plugin_tlive_kafka_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of tlive-kafka-oc | 
 **x_iam_token** | **str**| authentication header object | [optional] 
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
> list[str] retrieve_healthbot_ingest_settings_byoi_default_plugin_tlive_kafkas(x_iam_token=x_iam_token, working=working)

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
x_iam_token = 'x_iam_token_example' # str | authentication header object (optional)
working = true # bool | true queries undeployed configuration (optional)

try:
    # Retrieve tlive-kafka-oc
    api_response = api_instance.retrieve_healthbot_ingest_settings_byoi_default_plugin_tlive_kafkas(x_iam_token=x_iam_token, working=working)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->retrieve_healthbot_ingest_settings_byoi_default_plugin_tlive_kafkas: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_iam_token** | **str**| authentication header object | [optional] 
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
> IngestMappingSchema retrieve_healthbot_ingest_settings_byoi_ingest_mapping_by_id(name, x_iam_token=x_iam_token, working=working)

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
x_iam_token = 'x_iam_token_example' # str | authentication header object (optional)
working = true # bool | true queries undeployed configuration (optional)

try:
    # Retrieve ingest-mapping by ID
    api_response = api_instance.retrieve_healthbot_ingest_settings_byoi_ingest_mapping_by_id(name, x_iam_token=x_iam_token, working=working)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->retrieve_healthbot_ingest_settings_byoi_ingest_mapping_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of ingest-mapping | 
 **x_iam_token** | **str**| authentication header object | [optional] 
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
> list[str] retrieve_healthbot_ingest_settings_byoi_ingest_mappings(x_iam_token=x_iam_token, working=working)

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
x_iam_token = 'x_iam_token_example' # str | authentication header object (optional)
working = true # bool | true queries undeployed configuration (optional)

try:
    # Retrieve ingest-mapping
    api_response = api_instance.retrieve_healthbot_ingest_settings_byoi_ingest_mappings(x_iam_token=x_iam_token, working=working)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->retrieve_healthbot_ingest_settings_byoi_ingest_mappings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_iam_token** | **str**| authentication header object | [optional] 
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
> list[str] retrieve_healthbot_ingest_settings_frequency_profile(x_iam_token=x_iam_token, working=working)

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
x_iam_token = 'x_iam_token_example' # str | authentication header object (optional)
working = true # bool | true queries undeployed configuration (optional)

try:
    # Retrieve frequency-profile
    api_response = api_instance.retrieve_healthbot_ingest_settings_frequency_profile(x_iam_token=x_iam_token, working=working)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->retrieve_healthbot_ingest_settings_frequency_profile: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_iam_token** | **str**| authentication header object | [optional] 
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
> FrequencyProfileSchema retrieve_healthbot_ingest_settings_frequency_profile_by_id(name, x_iam_token=x_iam_token, working=working)

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
x_iam_token = 'x_iam_token_example' # str | authentication header object (optional)
working = true # bool | true queries undeployed configuration (optional)

try:
    # Retrieve frequency-profile by ID
    api_response = api_instance.retrieve_healthbot_ingest_settings_frequency_profile_by_id(name, x_iam_token=x_iam_token, working=working)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->retrieve_healthbot_ingest_settings_frequency_profile_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| ID of name | 
 **x_iam_token** | **str**| authentication header object | [optional] 
 **working** | **bool**| true queries undeployed configuration | [optional] 

### Return type

[**FrequencyProfileSchema**](FrequencyProfileSchema.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_healthbot_ingest_settings_tagging_profile_by_id**
> TaggingProfileSchema retrieve_healthbot_ingest_settings_tagging_profile_by_id(name, x_iam_token=x_iam_token, working=working)

Retrieve tagging-profile by ID

Retrieve operation of resource: tagging-profile

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
x_iam_token = 'x_iam_token_example' # str | authentication header object (optional)
working = true # bool | true queries undeployed configuration (optional)

try:
    # Retrieve tagging-profile by ID
    api_response = api_instance.retrieve_healthbot_ingest_settings_tagging_profile_by_id(name, x_iam_token=x_iam_token, working=working)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->retrieve_healthbot_ingest_settings_tagging_profile_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| ID of name | 
 **x_iam_token** | **str**| authentication header object | [optional] 
 **working** | **bool**| true queries undeployed configuration | [optional] 

### Return type

[**TaggingProfileSchema**](TaggingProfileSchema.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_healthbot_ingest_settings_tagging_profiles**
> list[str] retrieve_healthbot_ingest_settings_tagging_profiles(x_iam_token=x_iam_token, working=working)

Retrieve tagging-profile by ID

Retrieve operation of resource: tagging-profile

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
x_iam_token = 'x_iam_token_example' # str | authentication header object (optional)
working = true # bool | true queries undeployed configuration (optional)

try:
    # Retrieve tagging-profile by ID
    api_response = api_instance.retrieve_healthbot_ingest_settings_tagging_profiles(x_iam_token=x_iam_token, working=working)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->retrieve_healthbot_ingest_settings_tagging_profiles: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_iam_token** | **str**| authentication header object | [optional] 
 **working** | **bool**| true queries undeployed configuration | [optional] 

### Return type

**list[str]**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_healthbot_ingest_sflow**
> SflowSchema retrieve_healthbot_ingest_sflow(x_iam_token=x_iam_token, working=working)

Retrieve sflow

Retrieve operation of resource: sflow

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
x_iam_token = 'x_iam_token_example' # str | authentication header object (optional)
working = true # bool | true queries undeployed configuration (optional)

try:
    # Retrieve sflow
    api_response = api_instance.retrieve_healthbot_ingest_sflow(x_iam_token=x_iam_token, working=working)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->retrieve_healthbot_ingest_sflow: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_iam_token** | **str**| authentication header object | [optional] 
 **working** | **bool**| true queries undeployed configuration | [optional] 

### Return type

[**SflowSchema**](SflowSchema.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_healthbot_ingest_sflow_counter_record_by_id**
> CounterRecordSchema retrieve_healthbot_ingest_sflow_counter_record_by_id(record_name, x_iam_token=x_iam_token, working=working)

Retrieve counter-record by ID

Retrieve operation of resource: counter-record

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
record_name = 'record_name_example' # str | ID of record-name
x_iam_token = 'x_iam_token_example' # str | authentication header object (optional)
working = true # bool | true queries undeployed configuration (optional)

try:
    # Retrieve counter-record by ID
    api_response = api_instance.retrieve_healthbot_ingest_sflow_counter_record_by_id(record_name, x_iam_token=x_iam_token, working=working)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->retrieve_healthbot_ingest_sflow_counter_record_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **record_name** | **str**| ID of record-name | 
 **x_iam_token** | **str**| authentication header object | [optional] 
 **working** | **bool**| true queries undeployed configuration | [optional] 

### Return type

[**CounterRecordSchema**](CounterRecordSchema.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_healthbot_ingest_sflow_flow_record_by_id**
> FlowRecordSchema retrieve_healthbot_ingest_sflow_flow_record_by_id(record_name, x_iam_token=x_iam_token, working=working)

Retrieve flow-record by ID

Retrieve operation of resource: flow-record

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
record_name = 'record_name_example' # str | ID of record-name
x_iam_token = 'x_iam_token_example' # str | authentication header object (optional)
working = true # bool | true queries undeployed configuration (optional)

try:
    # Retrieve flow-record by ID
    api_response = api_instance.retrieve_healthbot_ingest_sflow_flow_record_by_id(record_name, x_iam_token=x_iam_token, working=working)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->retrieve_healthbot_ingest_sflow_flow_record_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **record_name** | **str**| ID of record-name | 
 **x_iam_token** | **str**| authentication header object | [optional] 
 **working** | **bool**| true queries undeployed configuration | [optional] 

### Return type

[**FlowRecordSchema**](FlowRecordSchema.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_healthbot_ingest_sflow_protocol_by_id**
> ProtocolSchema retrieve_healthbot_ingest_sflow_protocol_by_id(protocol_name, x_iam_token=x_iam_token, working=working)

Retrieve protocol by ID

Retrieve operation of resource: protocol

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
protocol_name = 'protocol_name_example' # str | ID of protocol-name
x_iam_token = 'x_iam_token_example' # str | authentication header object (optional)
working = true # bool | true queries undeployed configuration (optional)

try:
    # Retrieve protocol by ID
    api_response = api_instance.retrieve_healthbot_ingest_sflow_protocol_by_id(protocol_name, x_iam_token=x_iam_token, working=working)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->retrieve_healthbot_ingest_sflow_protocol_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **protocol_name** | **str**| ID of protocol-name | 
 **x_iam_token** | **str**| authentication header object | [optional] 
 **working** | **bool**| true queries undeployed configuration | [optional] 

### Return type

[**ProtocolSchema**](ProtocolSchema.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_healthbot_ingest_sflow_sample_by_id**
> SampleSchema retrieve_healthbot_ingest_sflow_sample_by_id(sample_name, x_iam_token=x_iam_token, working=working)

Retrieve sample by ID

Retrieve operation of resource: sample

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
sample_name = 'sample_name_example' # str | ID of sample-name
x_iam_token = 'x_iam_token_example' # str | authentication header object (optional)
working = true # bool | true queries undeployed configuration (optional)

try:
    # Retrieve sample by ID
    api_response = api_instance.retrieve_healthbot_ingest_sflow_sample_by_id(sample_name, x_iam_token=x_iam_token, working=working)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->retrieve_healthbot_ingest_sflow_sample_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sample_name** | **str**| ID of sample-name | 
 **x_iam_token** | **str**| authentication header object | [optional] 
 **working** | **bool**| true queries undeployed configuration | [optional] 

### Return type

[**SampleSchema**](SampleSchema.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_healthbot_ingest_snmp_notification**
> SnmpNotificationSchema retrieve_healthbot_ingest_snmp_notification(x_iam_token=x_iam_token, working=working)

Retrieve snmp-notification

Retrieve operation of resource: snmp-notification

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
x_iam_token = 'x_iam_token_example' # str | authentication header object (optional)
working = true # bool | true queries undeployed configuration (optional)

try:
    # Retrieve snmp-notification
    api_response = api_instance.retrieve_healthbot_ingest_snmp_notification(x_iam_token=x_iam_token, working=working)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->retrieve_healthbot_ingest_snmp_notification: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_iam_token** | **str**| authentication header object | [optional] 
 **working** | **bool**| true queries undeployed configuration | [optional] 

### Return type

[**SnmpNotificationSchema**](SnmpNotificationSchema.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_healthbot_ingest_snmp_notification_v3_usm_user_by_id**
> Snmpv3UsmUserSchema retrieve_healthbot_ingest_snmp_notification_v3_usm_user_by_id(name, x_iam_token=x_iam_token, working=working)

Retrieve SNMPv3 user by UserName(ID)

Retrieve operation of resource: snmp v3 usm user

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
name = 'name_example' # str | User Name
x_iam_token = 'x_iam_token_example' # str | authentication header object (optional)
working = true # bool | true queries undeployed configuration (optional)

try:
    # Retrieve SNMPv3 user by UserName(ID)
    api_response = api_instance.retrieve_healthbot_ingest_snmp_notification_v3_usm_user_by_id(name, x_iam_token=x_iam_token, working=working)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->retrieve_healthbot_ingest_snmp_notification_v3_usm_user_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| User Name | 
 **x_iam_token** | **str**| authentication header object | [optional] 
 **working** | **bool**| true queries undeployed configuration | [optional] 

### Return type

[**Snmpv3UsmUserSchema**](Snmpv3UsmUserSchema.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_healthbot_ingest_snmp_notification_v3_usm_usernames**
> list[str] retrieve_healthbot_ingest_snmp_notification_v3_usm_usernames(x_iam_token=x_iam_token, working=working)

Retrieve snmp v3 usm user names

Retrieve operation of resource: snmp v3 usm user names

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
x_iam_token = 'x_iam_token_example' # str | authentication header object (optional)
working = true # bool | true queries undeployed configuration (optional)

try:
    # Retrieve snmp v3 usm user names
    api_response = api_instance.retrieve_healthbot_ingest_snmp_notification_v3_usm_usernames(x_iam_token=x_iam_token, working=working)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->retrieve_healthbot_ingest_snmp_notification_v3_usm_usernames: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_iam_token** | **str**| authentication header object | [optional] 
 **working** | **bool**| true queries undeployed configuration | [optional] 

### Return type

**list[str]**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_healthbot_ingest_snmp_notification_v3_usm_users**
> list[Snmpv3UsmUsersSchema] retrieve_healthbot_ingest_snmp_notification_v3_usm_users(x_iam_token=x_iam_token, working=working)

Retrieve SNMP v3 USM users

Retrieve operation of resource: SNMP v3 USM users

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
x_iam_token = 'x_iam_token_example' # str | authentication header object (optional)
working = true # bool | true queries undeployed configuration (optional)

try:
    # Retrieve SNMP v3 USM users
    api_response = api_instance.retrieve_healthbot_ingest_snmp_notification_v3_usm_users(x_iam_token=x_iam_token, working=working)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->retrieve_healthbot_ingest_snmp_notification_v3_usm_users: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_iam_token** | **str**| authentication header object | [optional] 
 **working** | **bool**| true queries undeployed configuration | [optional] 

### Return type

[**list[Snmpv3UsmUsersSchema]**](Snmpv3UsmUsersSchema.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_healthbot_ingest_syslog_header_pattern_by_id**
> HeaderPatternSchema retrieve_healthbot_ingest_syslog_header_pattern_by_id(name, x_iam_token=x_iam_token, working=working)

Retrieve pattern by ID

Retrieve operation of resource: header-pattern

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
x_iam_token = 'x_iam_token_example' # str | authentication header object (optional)
working = true # bool | true queries undeployed configuration (optional)

try:
    # Retrieve pattern by ID
    api_response = api_instance.retrieve_healthbot_ingest_syslog_header_pattern_by_id(name, x_iam_token=x_iam_token, working=working)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->retrieve_healthbot_ingest_syslog_header_pattern_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| ID of name | 
 **x_iam_token** | **str**| authentication header object | [optional] 
 **working** | **bool**| true queries undeployed configuration | [optional] 

### Return type

[**HeaderPatternSchema**](HeaderPatternSchema.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_healthbot_ingest_syslog_header_pattern_ids**
> list[str] retrieve_healthbot_ingest_syslog_header_pattern_ids(x_iam_token=x_iam_token, working=working)

Retrieve header pattern names

Retrieve operation of resource: header-pattern

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
x_iam_token = 'x_iam_token_example' # str | authentication header object (optional)
working = true # bool | true queries undeployed configuration (optional)

try:
    # Retrieve header pattern names
    api_response = api_instance.retrieve_healthbot_ingest_syslog_header_pattern_ids(x_iam_token=x_iam_token, working=working)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->retrieve_healthbot_ingest_syslog_header_pattern_ids: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_iam_token** | **str**| authentication header object | [optional] 
 **working** | **bool**| true queries undeployed configuration | [optional] 

### Return type

**list[str]**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_healthbot_ingest_syslog_header_patterns**
> list[HeaderPatternSchema] retrieve_healthbot_ingest_syslog_header_patterns(x_iam_token=x_iam_token, working=working)

Retrieve header patterns

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
x_iam_token = 'x_iam_token_example' # str | authentication header object (optional)
working = true # bool | true queries undeployed configuration (optional)

try:
    # Retrieve header patterns
    api_response = api_instance.retrieve_healthbot_ingest_syslog_header_patterns(x_iam_token=x_iam_token, working=working)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->retrieve_healthbot_ingest_syslog_header_patterns: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_iam_token** | **str**| authentication header object | [optional] 
 **working** | **bool**| true queries undeployed configuration | [optional] 

### Return type

[**list[HeaderPatternSchema]**](HeaderPatternSchema.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_healthbot_ingest_tagging_profile_by_id**
> TaggingProfileSchema retrieve_healthbot_ingest_tagging_profile_by_id(name, x_iam_token=x_iam_token, working=working)

Retrieve tagging-profile by ID

Retrieve operation of resource: tagging-profile

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
x_iam_token = 'x_iam_token_example' # str | authentication header object (optional)
working = true # bool | true queries undeployed configuration (optional)

try:
    # Retrieve tagging-profile by ID
    api_response = api_instance.retrieve_healthbot_ingest_tagging_profile_by_id(name, x_iam_token=x_iam_token, working=working)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->retrieve_healthbot_ingest_tagging_profile_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| ID of name | 
 **x_iam_token** | **str**| authentication header object | [optional] 
 **working** | **bool**| true queries undeployed configuration | [optional] 

### Return type

[**TaggingProfileSchema**](TaggingProfileSchema.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_healthbot_ingest_tagging_profiles**
> list[str] retrieve_healthbot_ingest_tagging_profiles(x_iam_token=x_iam_token, working=working)

Retrieve tagging-profile by ID

Retrieve operation of resource: tagging-profile

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
x_iam_token = 'x_iam_token_example' # str | authentication header object (optional)
working = true # bool | true queries undeployed configuration (optional)

try:
    # Retrieve tagging-profile by ID
    api_response = api_instance.retrieve_healthbot_ingest_tagging_profiles(x_iam_token=x_iam_token, working=working)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->retrieve_healthbot_ingest_tagging_profiles: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_iam_token** | **str**| authentication header object | [optional] 
 **working** | **bool**| true queries undeployed configuration | [optional] 

### Return type

**list[str]**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_healthbot_organization_organization**
> list[str] retrieve_healthbot_organization_organization(working=working)

Retrieve organization

Retrieve operation of resource: organization

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
    # Retrieve organization
    api_response = api_instance.retrieve_healthbot_organization_organization(working=working)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->retrieve_healthbot_organization_organization: %s\n" % e)
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

# **retrieve_healthbot_organization_organization_by_id**
> OrganizationSchema retrieve_healthbot_organization_organization_by_id(organization_name, x_iam_token=x_iam_token, working=working)

Retrieve organization by ID

Retrieve operation of resource: organization

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
organization_name = 'organization_name_example' # str | ID of organization-name
x_iam_token = 'x_iam_token_example' # str | authentication header object (optional)
working = true # bool | true queries undeployed configuration (optional)

try:
    # Retrieve organization by ID
    api_response = api_instance.retrieve_healthbot_organization_organization_by_id(organization_name, x_iam_token=x_iam_token, working=working)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->retrieve_healthbot_organization_organization_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_name** | **str**| ID of organization-name | 
 **x_iam_token** | **str**| authentication header object | [optional] 
 **working** | **bool**| true queries undeployed configuration | [optional] 

### Return type

[**OrganizationSchema**](OrganizationSchema.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_healthbot_profile_rollup_summarization_field_profile_field_profile_by_id**
> RollupSummarizationSchema retrieve_healthbot_profile_rollup_summarization_field_profile_field_profile_by_id(profile_id, working=working, x_iam_token=x_iam_token)

Retrieve field-profile by ID

Retrieve operation of resource: field-profile

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
profile_id = 'profile_id_example' # str | ID of profile-id
working = true # bool | true queries undeployed configuration (optional)
x_iam_token = 'x_iam_token_example' # str | authentication header object (optional)

try:
    # Retrieve field-profile by ID
    api_response = api_instance.retrieve_healthbot_profile_rollup_summarization_field_profile_field_profile_by_id(profile_id, working=working, x_iam_token=x_iam_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->retrieve_healthbot_profile_rollup_summarization_field_profile_field_profile_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **profile_id** | **str**| ID of profile-id | 
 **working** | **bool**| true queries undeployed configuration | [optional] 
 **x_iam_token** | **str**| authentication header object | [optional] 

### Return type

[**RollupSummarizationSchema**](RollupSummarizationSchema.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_healthbot_profile_rollup_summarization_field_profile_profile**
> RollupSummarizationsSchema retrieve_healthbot_profile_rollup_summarization_field_profile_profile(working=working, x_iam_token=x_iam_token)

Retrieve field-profile

Retrieve operation of resource: field-profile

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
x_iam_token = 'x_iam_token_example' # str | authentication header object (optional)

try:
    # Retrieve field-profile
    api_response = api_instance.retrieve_healthbot_profile_rollup_summarization_field_profile_profile(working=working, x_iam_token=x_iam_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->retrieve_healthbot_profile_rollup_summarization_field_profile_profile: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **working** | **bool**| true queries undeployed configuration | [optional] 
 **x_iam_token** | **str**| authentication header object | [optional] 

### Return type

[**RollupSummarizationsSchema**](RollupSummarizationsSchema.md)

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

# **retrieve_healthbot_system_trigger_action**
> TriggerActionSchema retrieve_healthbot_system_trigger_action(working=working)

Retrieve trigger-action

Retrieve operation of resource: trigger-action

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
    # Retrieve trigger-action
    api_response = api_instance.retrieve_healthbot_system_trigger_action(working=working)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->retrieve_healthbot_system_trigger_action: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **working** | **bool**| true queries undeployed configuration | [optional] 

### Return type

[**TriggerActionSchema**](TriggerActionSchema.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_healthbot_topic_resource_resource**
> list[str] retrieve_healthbot_topic_resource_resource(topic_name, authorization=authorization, working=working)

List all resource-names in a topic

Get a list of all the resource-name`s in a topic

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
topic_name = 'topic_name_example' # str | ID of topic-name
authorization = 'authorization_example' # str | authentication header object (optional)
working = true # bool | true queries un-committed configuration (optional)

try:
    # List all resource-names in a topic
    api_response = api_instance.retrieve_healthbot_topic_resource_resource(topic_name, authorization=authorization, working=working)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->retrieve_healthbot_topic_resource_resource: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **topic_name** | **str**| ID of topic-name | 
 **authorization** | **str**| authentication header object | [optional] 
 **working** | **bool**| true queries un-committed configuration | [optional] 

### Return type

**list[str]**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_healthbot_topic_resource_resource_by_id**
> ResourceSchema retrieve_healthbot_topic_resource_resource_by_id(topic_name, resource_name, authorization=authorization, working=working, download=download)

Get a resource's configuration

Get the configuration details of a resource by `resource-name`

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
topic_name = 'topic_name_example' # str | ID of topic-name
resource_name = 'resource_name_example' # str | ID of resource-name
authorization = 'authorization_example' # str | authentication header object (optional)
working = true # bool | true queries un-committed configuration (optional)
download = true # bool | Download a compressed .resource file (optional)

try:
    # Get a resource's configuration
    api_response = api_instance.retrieve_healthbot_topic_resource_resource_by_id(topic_name, resource_name, authorization=authorization, working=working, download=download)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->retrieve_healthbot_topic_resource_resource_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **topic_name** | **str**| ID of topic-name | 
 **resource_name** | **str**| ID of resource-name | 
 **authorization** | **str**| authentication header object | [optional] 
 **working** | **bool**| true queries un-committed configuration | [optional] 
 **download** | **bool**| Download a compressed .resource file | [optional] 

### Return type

[**ResourceSchema**](ResourceSchema.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_iceberg_ingest**
> IngestSettingsSchema retrieve_iceberg_ingest(x_iam_token=x_iam_token, working=working)

Retrieve ingest

Retrieve operation of resource: ingest

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
x_iam_token = 'x_iam_token_example' # str | authentication header object (optional)
working = true # bool | true queries undeployed configuration (optional)

try:
    # Retrieve ingest
    api_response = api_instance.retrieve_iceberg_ingest(x_iam_token=x_iam_token, working=working)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->retrieve_iceberg_ingest: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_iam_token** | **str**| authentication header object | [optional] 
 **working** | **bool**| true queries undeployed configuration | [optional] 

### Return type

[**IngestSettingsSchema**](IngestSettingsSchema.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_iceberg_ingest_flow**
> FlowSchema retrieve_iceberg_ingest_flow(x_iam_token=x_iam_token, working=working)

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
x_iam_token = 'x_iam_token_example' # str | authentication header object (optional)
working = true # bool | true queries undeployed configuration (optional)

try:
    # Retrieve flow
    api_response = api_instance.retrieve_iceberg_ingest_flow(x_iam_token=x_iam_token, working=working)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->retrieve_iceberg_ingest_flow: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_iam_token** | **str**| authentication header object | [optional] 
 **working** | **bool**| true queries undeployed configuration | [optional] 

### Return type

[**FlowSchema**](FlowSchema.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_iceberg_ingest_flow_template_by_id**
> TemplateSchema retrieve_iceberg_ingest_flow_template_by_id(name, x_iam_token=x_iam_token, working=working)

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
x_iam_token = 'x_iam_token_example' # str | authentication header object (optional)
working = true # bool | true queries undeployed configuration (optional)

try:
    # Retrieve template by ID
    api_response = api_instance.retrieve_iceberg_ingest_flow_template_by_id(name, x_iam_token=x_iam_token, working=working)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->retrieve_iceberg_ingest_flow_template_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of template | 
 **x_iam_token** | **str**| authentication header object | [optional] 
 **working** | **bool**| true queries undeployed configuration | [optional] 

### Return type

[**TemplateSchema**](TemplateSchema.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_iceberg_ingest_flow_template_ids**
> list[str] retrieve_iceberg_ingest_flow_template_ids(x_iam_token=x_iam_token, working=working)

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
x_iam_token = 'x_iam_token_example' # str | authentication header object (optional)
working = true # bool | true queries undeployed configuration (optional)

try:
    # Retrieve template
    api_response = api_instance.retrieve_iceberg_ingest_flow_template_ids(x_iam_token=x_iam_token, working=working)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->retrieve_iceberg_ingest_flow_template_ids: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_iam_token** | **str**| authentication header object | [optional] 
 **working** | **bool**| true queries undeployed configuration | [optional] 

### Return type

**list[str]**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_iceberg_ingest_native_gpb**
> NativeGpbSchema retrieve_iceberg_ingest_native_gpb(x_iam_token=x_iam_token, working=working)

Retrieve native-gpb

Retrieve operation of resource: native-gpb

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
x_iam_token = 'x_iam_token_example' # str | authentication header object (optional)
working = true # bool | true queries undeployed configuration (optional)

try:
    # Retrieve native-gpb
    api_response = api_instance.retrieve_iceberg_ingest_native_gpb(x_iam_token=x_iam_token, working=working)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->retrieve_iceberg_ingest_native_gpb: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_iam_token** | **str**| authentication header object | [optional] 
 **working** | **bool**| true queries undeployed configuration | [optional] 

### Return type

[**NativeGpbSchema**](NativeGpbSchema.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_iceberg_ingest_settings**
> IngestSettingsSchema retrieve_iceberg_ingest_settings(x_iam_token=x_iam_token, working=working)

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
x_iam_token = 'x_iam_token_example' # str | authentication header object (optional)
working = true # bool | true queries undeployed configuration (optional)

try:
    # Retrieve ingest-settings
    api_response = api_instance.retrieve_iceberg_ingest_settings(x_iam_token=x_iam_token, working=working)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->retrieve_iceberg_ingest_settings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_iam_token** | **str**| authentication header object | [optional] 
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
> FlowSchema retrieve_iceberg_ingest_settings_flow(x_iam_token=x_iam_token, working=working)

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
x_iam_token = 'x_iam_token_example' # str | authentication header object (optional)
working = true # bool | true queries undeployed configuration (optional)

try:
    # Retrieve flow
    api_response = api_instance.retrieve_iceberg_ingest_settings_flow(x_iam_token=x_iam_token, working=working)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->retrieve_iceberg_ingest_settings_flow: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_iam_token** | **str**| authentication header object | [optional] 
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
> TemplateSchema retrieve_iceberg_ingest_settings_flow_template_by_id(name, x_iam_token=x_iam_token, working=working)

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
x_iam_token = 'x_iam_token_example' # str | authentication header object (optional)
working = true # bool | true queries undeployed configuration (optional)

try:
    # Retrieve template by ID
    api_response = api_instance.retrieve_iceberg_ingest_settings_flow_template_by_id(name, x_iam_token=x_iam_token, working=working)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->retrieve_iceberg_ingest_settings_flow_template_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of template | 
 **x_iam_token** | **str**| authentication header object | [optional] 
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
> list[str] retrieve_iceberg_ingest_settings_flow_template_ids(x_iam_token=x_iam_token, working=working)

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
x_iam_token = 'x_iam_token_example' # str | authentication header object (optional)
working = true # bool | true queries undeployed configuration (optional)

try:
    # Retrieve template
    api_response = api_instance.retrieve_iceberg_ingest_settings_flow_template_ids(x_iam_token=x_iam_token, working=working)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->retrieve_iceberg_ingest_settings_flow_template_ids: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_iam_token** | **str**| authentication header object | [optional] 
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
> SyslogSchema retrieve_iceberg_ingest_settings_syslog(x_iam_token=x_iam_token, working=working)

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
x_iam_token = 'x_iam_token_example' # str | authentication header object (optional)
working = true # bool | true queries undeployed configuration (optional)

try:
    # Retrieve syslog
    api_response = api_instance.retrieve_iceberg_ingest_settings_syslog(x_iam_token=x_iam_token, working=working)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->retrieve_iceberg_ingest_settings_syslog: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_iam_token** | **str**| authentication header object | [optional] 
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
> PatternSchema retrieve_iceberg_ingest_settings_syslog_pattern_by_id(name, x_iam_token=x_iam_token, working=working)

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
x_iam_token = 'x_iam_token_example' # str | authentication header object (optional)
working = true # bool | true queries undeployed configuration (optional)

try:
    # Retrieve pattern by ID
    api_response = api_instance.retrieve_iceberg_ingest_settings_syslog_pattern_by_id(name, x_iam_token=x_iam_token, working=working)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->retrieve_iceberg_ingest_settings_syslog_pattern_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of pattern | 
 **x_iam_token** | **str**| authentication header object | [optional] 
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
> list[str] retrieve_iceberg_ingest_settings_syslog_pattern_ids(x_iam_token=x_iam_token, working=working)

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
x_iam_token = 'x_iam_token_example' # str | authentication header object (optional)
working = true # bool | true queries undeployed configuration (optional)

try:
    # Retrieve pattern
    api_response = api_instance.retrieve_iceberg_ingest_settings_syslog_pattern_ids(x_iam_token=x_iam_token, working=working)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->retrieve_iceberg_ingest_settings_syslog_pattern_ids: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_iam_token** | **str**| authentication header object | [optional] 
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
> PatternSetSchema retrieve_iceberg_ingest_settings_syslog_pattern_set_by_id(name, x_iam_token=x_iam_token, working=working)

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
x_iam_token = 'x_iam_token_example' # str | authentication header object (optional)
working = true # bool | true queries undeployed configuration (optional)

try:
    # Retrieve pattern-set by ID
    api_response = api_instance.retrieve_iceberg_ingest_settings_syslog_pattern_set_by_id(name, x_iam_token=x_iam_token, working=working)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->retrieve_iceberg_ingest_settings_syslog_pattern_set_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of patter-set | 
 **x_iam_token** | **str**| authentication header object | [optional] 
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
> list[str] retrieve_iceberg_ingest_settings_syslog_pattern_set_ids(x_iam_token=x_iam_token, working=working)

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
x_iam_token = 'x_iam_token_example' # str | authentication header object (optional)
working = true # bool | true queries undeployed configuration (optional)

try:
    # Retrieve pattern-set
    api_response = api_instance.retrieve_iceberg_ingest_settings_syslog_pattern_set_ids(x_iam_token=x_iam_token, working=working)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->retrieve_iceberg_ingest_settings_syslog_pattern_set_ids: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_iam_token** | **str**| authentication header object | [optional] 
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
> list[PatternSetSchema] retrieve_iceberg_ingest_settings_syslog_pattern_sets(x_iam_token=x_iam_token, working=working)

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
x_iam_token = 'x_iam_token_example' # str | authentication header object (optional)
working = true # bool | true queries undeployed configuration (optional)

try:
    # Retrieve pattern-set by ID
    api_response = api_instance.retrieve_iceberg_ingest_settings_syslog_pattern_sets(x_iam_token=x_iam_token, working=working)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->retrieve_iceberg_ingest_settings_syslog_pattern_sets: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_iam_token** | **str**| authentication header object | [optional] 
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
> list[PatternSchema] retrieve_iceberg_ingest_settings_syslog_patterns(x_iam_token=x_iam_token, working=working)

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
x_iam_token = 'x_iam_token_example' # str | authentication header object (optional)
working = true # bool | true queries undeployed configuration (optional)

try:
    # Retrieve pattern by ID
    api_response = api_instance.retrieve_iceberg_ingest_settings_syslog_patterns(x_iam_token=x_iam_token, working=working)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->retrieve_iceberg_ingest_settings_syslog_patterns: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_iam_token** | **str**| authentication header object | [optional] 
 **working** | **bool**| true queries undeployed configuration | [optional] 

### Return type

[**list[PatternSchema]**](PatternSchema.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_iceberg_ingest_syslog**
> SyslogSchema retrieve_iceberg_ingest_syslog(x_iam_token=x_iam_token, working=working)

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
x_iam_token = 'x_iam_token_example' # str | authentication header object (optional)
working = true # bool | true queries undeployed configuration (optional)

try:
    # Retrieve syslog
    api_response = api_instance.retrieve_iceberg_ingest_syslog(x_iam_token=x_iam_token, working=working)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->retrieve_iceberg_ingest_syslog: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_iam_token** | **str**| authentication header object | [optional] 
 **working** | **bool**| true queries undeployed configuration | [optional] 

### Return type

[**SyslogSchema**](SyslogSchema.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_iceberg_ingest_syslog_pattern_by_id**
> PatternSchema retrieve_iceberg_ingest_syslog_pattern_by_id(name, x_iam_token=x_iam_token, working=working)

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
x_iam_token = 'x_iam_token_example' # str | authentication header object (optional)
working = true # bool | true queries undeployed configuration (optional)

try:
    # Retrieve pattern by ID
    api_response = api_instance.retrieve_iceberg_ingest_syslog_pattern_by_id(name, x_iam_token=x_iam_token, working=working)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->retrieve_iceberg_ingest_syslog_pattern_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of pattern | 
 **x_iam_token** | **str**| authentication header object | [optional] 
 **working** | **bool**| true queries undeployed configuration | [optional] 

### Return type

[**PatternSchema**](PatternSchema.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_iceberg_ingest_syslog_pattern_ids**
> list[str] retrieve_iceberg_ingest_syslog_pattern_ids(x_iam_token=x_iam_token, working=working)

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
x_iam_token = 'x_iam_token_example' # str | authentication header object (optional)
working = true # bool | true queries undeployed configuration (optional)

try:
    # Retrieve pattern
    api_response = api_instance.retrieve_iceberg_ingest_syslog_pattern_ids(x_iam_token=x_iam_token, working=working)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->retrieve_iceberg_ingest_syslog_pattern_ids: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_iam_token** | **str**| authentication header object | [optional] 
 **working** | **bool**| true queries undeployed configuration | [optional] 

### Return type

**list[str]**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_iceberg_ingest_syslog_pattern_set_by_id**
> PatternSetSchema retrieve_iceberg_ingest_syslog_pattern_set_by_id(name, x_iam_token=x_iam_token, working=working)

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
name = 'name_example' # str | Name of pattern-set
x_iam_token = 'x_iam_token_example' # str | authentication header object (optional)
working = true # bool | true queries undeployed configuration (optional)

try:
    # Retrieve pattern-set by ID
    api_response = api_instance.retrieve_iceberg_ingest_syslog_pattern_set_by_id(name, x_iam_token=x_iam_token, working=working)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->retrieve_iceberg_ingest_syslog_pattern_set_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of pattern-set | 
 **x_iam_token** | **str**| authentication header object | [optional] 
 **working** | **bool**| true queries undeployed configuration | [optional] 

### Return type

[**PatternSetSchema**](PatternSetSchema.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_iceberg_ingest_syslog_pattern_set_ids**
> list[str] retrieve_iceberg_ingest_syslog_pattern_set_ids(x_iam_token=x_iam_token, working=working)

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
x_iam_token = 'x_iam_token_example' # str | authentication header object (optional)
working = true # bool | true queries undeployed configuration (optional)

try:
    # Retrieve pattern-set
    api_response = api_instance.retrieve_iceberg_ingest_syslog_pattern_set_ids(x_iam_token=x_iam_token, working=working)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->retrieve_iceberg_ingest_syslog_pattern_set_ids: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_iam_token** | **str**| authentication header object | [optional] 
 **working** | **bool**| true queries undeployed configuration | [optional] 

### Return type

**list[str]**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_iceberg_ingest_syslog_pattern_sets**
> list[PatternSetSchema] retrieve_iceberg_ingest_syslog_pattern_sets(x_iam_token=x_iam_token, working=working)

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
x_iam_token = 'x_iam_token_example' # str | authentication header object (optional)
working = true # bool | true queries undeployed configuration (optional)

try:
    # Retrieve pattern-set by ID
    api_response = api_instance.retrieve_iceberg_ingest_syslog_pattern_sets(x_iam_token=x_iam_token, working=working)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->retrieve_iceberg_ingest_syslog_pattern_sets: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_iam_token** | **str**| authentication header object | [optional] 
 **working** | **bool**| true queries undeployed configuration | [optional] 

### Return type

[**list[PatternSetSchema]**](PatternSetSchema.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_iceberg_ingest_syslog_patterns**
> list[PatternSchema] retrieve_iceberg_ingest_syslog_patterns(x_iam_token=x_iam_token, working=working)

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
x_iam_token = 'x_iam_token_example' # str | authentication header object (optional)
working = true # bool | true queries undeployed configuration (optional)

try:
    # Retrieve pattern by ID
    api_response = api_instance.retrieve_iceberg_ingest_syslog_patterns(x_iam_token=x_iam_token, working=working)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->retrieve_iceberg_ingest_syslog_patterns: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_iam_token** | **str**| authentication header object | [optional] 
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
> RawSchema retrieve_iceberg_profile_data_summarization_raw_by_id(name, x_iam_token=x_iam_token, working=working)

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
x_iam_token = 'x_iam_token_example' # str | authentication header object (optional)
working = true # bool | true queries undeployed configuration (optional)

try:
    # Retrieve raw-data-summarization by ID
    api_response = api_instance.retrieve_iceberg_profile_data_summarization_raw_by_id(name, x_iam_token=x_iam_token, working=working)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->retrieve_iceberg_profile_data_summarization_raw_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of raw-data-summarization | 
 **x_iam_token** | **str**| authentication header object | [optional] 
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
> RawSchema retrieve_iceberg_profile_data_summarizations_raw(x_iam_token=x_iam_token, working=working)

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
x_iam_token = 'x_iam_token_example' # str | authentication header object (optional)
working = true # bool | true queries undeployed configuration (optional)

try:
    # Retrieve raw-data-summarization
    api_response = api_instance.retrieve_iceberg_profile_data_summarizations_raw(x_iam_token=x_iam_token, working=working)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->retrieve_iceberg_profile_data_summarizations_raw: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_iam_token** | **str**| authentication header object | [optional] 
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
> CaProfileSchema retrieve_iceberg_profile_security_ca_profile_by_id(name, x_iam_token=x_iam_token, working=working)

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
x_iam_token = 'x_iam_token_example' # str | authentication header object (optional)
working = true # bool | true queries undeployed configuration (optional)

try:
    # Retrieve ca-profile by ID
    api_response = api_instance.retrieve_iceberg_profile_security_ca_profile_by_id(name, x_iam_token=x_iam_token, working=working)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->retrieve_iceberg_profile_security_ca_profile_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of ca-profile | 
 **x_iam_token** | **str**| authentication header object | [optional] 
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
> list[str] retrieve_iceberg_profile_security_ca_profiles(x_iam_token=x_iam_token, working=working)

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
x_iam_token = 'x_iam_token_example' # str | authentication header object (optional)
working = true # bool | true queries undeployed configuration (optional)

try:
    # Retrieve ca-profile
    api_response = api_instance.retrieve_iceberg_profile_security_ca_profiles(x_iam_token=x_iam_token, working=working)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->retrieve_iceberg_profile_security_ca_profiles: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_iam_token** | **str**| authentication header object | [optional] 
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
> LocalCertificateSchema retrieve_iceberg_profile_security_local_certificate_by_id(name, x_iam_token=x_iam_token, working=working)

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
x_iam_token = 'x_iam_token_example' # str | authentication header object (optional)
working = true # bool | true queries undeployed configuration (optional)

try:
    # Retrieve local-certificate by ID
    api_response = api_instance.retrieve_iceberg_profile_security_local_certificate_by_id(name, x_iam_token=x_iam_token, working=working)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->retrieve_iceberg_profile_security_local_certificate_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of local-certificate | 
 **x_iam_token** | **str**| authentication header object | [optional] 
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
> list[str] retrieve_iceberg_profile_security_local_certificates(x_iam_token=x_iam_token, working=working)

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
x_iam_token = 'x_iam_token_example' # str | authentication header object (optional)
working = true # bool | true queries undeployed configuration (optional)

try:
    # Retrieve local-certificate
    api_response = api_instance.retrieve_iceberg_profile_security_local_certificates(x_iam_token=x_iam_token, working=working)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->retrieve_iceberg_profile_security_local_certificates: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_iam_token** | **str**| authentication header object | [optional] 
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
> ProfilesSchema retrieve_iceberg_profiles(x_iam_token=x_iam_token, working=working)

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
x_iam_token = 'x_iam_token_example' # str | authentication header object (optional)
working = true # bool | true queries undeployed configuration (optional)

try:
    # Retrieve profile
    api_response = api_instance.retrieve_iceberg_profiles(x_iam_token=x_iam_token, working=working)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->retrieve_iceberg_profiles: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_iam_token** | **str**| authentication header object | [optional] 
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
> list[str] retrieve_sensors(sensor_type, x_iam_token=x_iam_token, sensor_name=sensor_name, depth=depth, append=append, snmp_table=snmp_table)

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
x_iam_token = 'x_iam_token_example' # str | authentication header object (optional)
sensor_name = 'sensor_name_example' # str | Sensor name prefix. (optional)
depth = 56 # int | Relative depth to the `sensor_name`. (optional)
append = true # bool | Returns full path of the sensor. (optional)
snmp_table = 'snmp_table_example' # str | Returns list of all the columns for the particular snmp_table (optional)

try:
    # List all OpenConfig sensors.
    api_response = api_instance.retrieve_sensors(sensor_type, x_iam_token=x_iam_token, sensor_name=sensor_name, depth=depth, append=append, snmp_table=snmp_table)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->retrieve_sensors: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sensor_type** | **str**| Sensor type | 
 **x_iam_token** | **str**| authentication header object | [optional] 
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

# **update_dynamic_tagging_by_key**
> update_dynamic_tagging_by_key(key_name, dynamic_tagging_obj, x_iam_token=x_iam_token)

Updates Dynamic-tagging key-value

Update operation of Dynamic-tagging key

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
key_name = 'key_name_example' # str | Dynamic-tagging Key
dynamic_tagging_obj = swagger_client.DynamicTaggingSchemaObject() # DynamicTaggingSchemaObject | Dynamic-tagging object containing key-value pair
x_iam_token = 'x_iam_token_example' # str | authentication header object (optional)

try:
    # Updates Dynamic-tagging key-value
    api_instance.update_dynamic_tagging_by_key(key_name, dynamic_tagging_obj, x_iam_token=x_iam_token)
except ApiException as e:
    print("Exception when calling DefaultApi->update_dynamic_tagging_by_key: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key_name** | **str**| Dynamic-tagging Key | 
 **dynamic_tagging_obj** | [**DynamicTaggingSchemaObject**](DynamicTaggingSchemaObject.md)| Dynamic-tagging object containing key-value pair | 
 **x_iam_token** | **str**| authentication header object | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_healthbot_deployment_deployment_by_id**
> update_healthbot_deployment_deployment_by_id(deployment, x_iam_token=x_iam_token)

Update deployment by ID

Update operation of resource: deployment

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
deployment = swagger_client.DeploymentSchema() # DeploymentSchema | deploymentbody object
x_iam_token = 'x_iam_token_example' # str | authentication header object (optional)

try:
    # Update deployment by ID
    api_instance.update_healthbot_deployment_deployment_by_id(deployment, x_iam_token=x_iam_token)
except ApiException as e:
    print("Exception when calling DefaultApi->update_healthbot_deployment_deployment_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **deployment** | [**DeploymentSchema**](DeploymentSchema.md)| deploymentbody object | 
 **x_iam_token** | **str**| authentication header object | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_healthbot_dynamic_tagging**
> list[str] update_healthbot_dynamic_tagging(dynamic_tagging, x_iam_token=x_iam_token)

Update dynamic-tagging by ID

Update operation of resource: dynamic-tagging

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
dynamic_tagging = swagger_client.DynamicTaggingsSchemaObject() # DynamicTaggingsSchemaObject | dynamic_taggingbody object
x_iam_token = 'x_iam_token_example' # str | authentication header object (optional)

try:
    # Update dynamic-tagging by ID
    api_response = api_instance.update_healthbot_dynamic_tagging(dynamic_tagging, x_iam_token=x_iam_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->update_healthbot_dynamic_tagging: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dynamic_tagging** | [**DynamicTaggingsSchemaObject**](DynamicTaggingsSchemaObject.md)| dynamic_taggingbody object | 
 **x_iam_token** | **str**| authentication header object | [optional] 

### Return type

**list[str]**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_healthbot_ingest_byoi_custom_plugin_by_id**
> update_healthbot_ingest_byoi_custom_plugin_by_id(name, custom_plugin, x_iam_token=x_iam_token)

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
x_iam_token = 'x_iam_token_example' # str | authentication header object (optional)

try:
    # Update custom-plugin by ID
    api_instance.update_healthbot_ingest_byoi_custom_plugin_by_id(name, custom_plugin, x_iam_token=x_iam_token)
except ApiException as e:
    print("Exception when calling DefaultApi->update_healthbot_ingest_byoi_custom_plugin_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of custom-plugin | 
 **custom_plugin** | [**CustomPluginSchema**](CustomPluginSchema.md)| custom_pluginbody object | 
 **x_iam_token** | **str**| authentication header object | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_healthbot_ingest_byoi_default_plugin_tlive_kafka_by_id**
> update_healthbot_ingest_byoi_default_plugin_tlive_kafka_by_id(name, tlive_kafka, x_iam_token=x_iam_token)

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
x_iam_token = 'x_iam_token_example' # str | authentication header object (optional)

try:
    # Update tlive-kafka-oc by ID
    api_instance.update_healthbot_ingest_byoi_default_plugin_tlive_kafka_by_id(name, tlive_kafka, x_iam_token=x_iam_token)
except ApiException as e:
    print("Exception when calling DefaultApi->update_healthbot_ingest_byoi_default_plugin_tlive_kafka_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of tlive-kafka-oc | 
 **tlive_kafka** | [**TliveKafkaOcSchema**](TliveKafkaOcSchema.md)| tlive_kafka body object | 
 **x_iam_token** | **str**| authentication header object | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_healthbot_ingest_byoi_ingest_mapping_by_id**
> update_healthbot_ingest_byoi_ingest_mapping_by_id(name, ingest_mapping, x_iam_token=x_iam_token)

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
x_iam_token = 'x_iam_token_example' # str | authentication header object (optional)

try:
    # Update ingest-mapping by ID
    api_instance.update_healthbot_ingest_byoi_ingest_mapping_by_id(name, ingest_mapping, x_iam_token=x_iam_token)
except ApiException as e:
    print("Exception when calling DefaultApi->update_healthbot_ingest_byoi_ingest_mapping_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of ingest-mapping | 
 **ingest_mapping** | [**IngestMappingSchema**](IngestMappingSchema.md)| ingest_mappingbody object | 
 **x_iam_token** | **str**| authentication header object | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_healthbot_ingest_frequency_profile_by_id**
> update_healthbot_ingest_frequency_profile_by_id(name, frequency_profile, x_iam_token=x_iam_token)

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
x_iam_token = 'x_iam_token_example' # str | authentication header object (optional)

try:
    # Update frequency-profile by ID
    api_instance.update_healthbot_ingest_frequency_profile_by_id(name, frequency_profile, x_iam_token=x_iam_token)
except ApiException as e:
    print("Exception when calling DefaultApi->update_healthbot_ingest_frequency_profile_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| ID of name | 
 **frequency_profile** | [**FrequencyProfileSchema**](FrequencyProfileSchema.md)| frequency_profilebody object | 
 **x_iam_token** | **str**| authentication header object | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_healthbot_ingest_outbound_ssh**
> update_healthbot_ingest_outbound_ssh(outbound_ssh, x_iam_token=x_iam_token)

Update outbound-ssh by ID

Update operation of resource: outbound-ssh

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
outbound_ssh = swagger_client.OutboundSshSchema() # OutboundSshSchema | outbound_sshbody object
x_iam_token = 'x_iam_token_example' # str | authentication header object (optional)

try:
    # Update outbound-ssh by ID
    api_instance.update_healthbot_ingest_outbound_ssh(outbound_ssh, x_iam_token=x_iam_token)
except ApiException as e:
    print("Exception when calling DefaultApi->update_healthbot_ingest_outbound_ssh: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **outbound_ssh** | [**OutboundSshSchema**](OutboundSshSchema.md)| outbound_sshbody object | 
 **x_iam_token** | **str**| authentication header object | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_healthbot_ingest_settings_byoi_custom_plugin_by_id**
> update_healthbot_ingest_settings_byoi_custom_plugin_by_id(name, custom_plugin, x_iam_token=x_iam_token)

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
x_iam_token = 'x_iam_token_example' # str | authentication header object (optional)

try:
    # Update custom-plugin by ID
    api_instance.update_healthbot_ingest_settings_byoi_custom_plugin_by_id(name, custom_plugin, x_iam_token=x_iam_token)
except ApiException as e:
    print("Exception when calling DefaultApi->update_healthbot_ingest_settings_byoi_custom_plugin_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of custom-plugin | 
 **custom_plugin** | [**CustomPluginSchema**](CustomPluginSchema.md)| custom_pluginbody object | 
 **x_iam_token** | **str**| authentication header object | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_healthbot_ingest_settings_byoi_default_plugin_tlive_kafka_by_id**
> update_healthbot_ingest_settings_byoi_default_plugin_tlive_kafka_by_id(name, tlive_kafka, x_iam_token=x_iam_token)

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
x_iam_token = 'x_iam_token_example' # str | authentication header object (optional)

try:
    # Update tlive-kafka-oc by ID
    api_instance.update_healthbot_ingest_settings_byoi_default_plugin_tlive_kafka_by_id(name, tlive_kafka, x_iam_token=x_iam_token)
except ApiException as e:
    print("Exception when calling DefaultApi->update_healthbot_ingest_settings_byoi_default_plugin_tlive_kafka_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of tlive-kafka-oc | 
 **tlive_kafka** | [**TliveKafkaOcSchema**](TliveKafkaOcSchema.md)| tlive_kafka body object | 
 **x_iam_token** | **str**| authentication header object | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_healthbot_ingest_settings_byoi_ingest_mapping_by_id**
> update_healthbot_ingest_settings_byoi_ingest_mapping_by_id(name, ingest_mapping, x_iam_token=x_iam_token)

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
x_iam_token = 'x_iam_token_example' # str | authentication header object (optional)

try:
    # Update ingest-mapping by ID
    api_instance.update_healthbot_ingest_settings_byoi_ingest_mapping_by_id(name, ingest_mapping, x_iam_token=x_iam_token)
except ApiException as e:
    print("Exception when calling DefaultApi->update_healthbot_ingest_settings_byoi_ingest_mapping_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of ingest-mapping | 
 **ingest_mapping** | [**IngestMappingSchema**](IngestMappingSchema.md)| ingest_mappingbody object | 
 **x_iam_token** | **str**| authentication header object | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_healthbot_ingest_settings_frequency_profile_by_id**
> update_healthbot_ingest_settings_frequency_profile_by_id(name, frequency_profile, x_iam_token=x_iam_token)

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
x_iam_token = 'x_iam_token_example' # str | authentication header object (optional)

try:
    # Update frequency-profile by ID
    api_instance.update_healthbot_ingest_settings_frequency_profile_by_id(name, frequency_profile, x_iam_token=x_iam_token)
except ApiException as e:
    print("Exception when calling DefaultApi->update_healthbot_ingest_settings_frequency_profile_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| ID of name | 
 **frequency_profile** | [**FrequencyProfileSchema**](FrequencyProfileSchema.md)| frequency_profilebody object | 
 **x_iam_token** | **str**| authentication header object | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_healthbot_ingest_settings_tagging_profile_by_id**
> update_healthbot_ingest_settings_tagging_profile_by_id(name, tagging_profile, x_iam_token=x_iam_token)

Update tagging-profile by ID

Update operation of resource: tagging-profile

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
tagging_profile = swagger_client.TaggingProfileSchema() # TaggingProfileSchema | tagging_profilebody object
x_iam_token = 'x_iam_token_example' # str | authentication header object (optional)

try:
    # Update tagging-profile by ID
    api_instance.update_healthbot_ingest_settings_tagging_profile_by_id(name, tagging_profile, x_iam_token=x_iam_token)
except ApiException as e:
    print("Exception when calling DefaultApi->update_healthbot_ingest_settings_tagging_profile_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| ID of name | 
 **tagging_profile** | [**TaggingProfileSchema**](TaggingProfileSchema.md)| tagging_profilebody object | 
 **x_iam_token** | **str**| authentication header object | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_healthbot_ingest_settings_tagging_profiles**
> list[str] update_healthbot_ingest_settings_tagging_profiles(tagging_profiles, x_iam_token=x_iam_token)

Update tagging-profile by ID

Update operation of resource: tagging-profile

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
tagging_profiles = swagger_client.TaggingProfilesSchema() # TaggingProfilesSchema | tagging_profilebody object
x_iam_token = 'x_iam_token_example' # str | authentication header object (optional)

try:
    # Update tagging-profile by ID
    api_response = api_instance.update_healthbot_ingest_settings_tagging_profiles(tagging_profiles, x_iam_token=x_iam_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->update_healthbot_ingest_settings_tagging_profiles: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tagging_profiles** | [**TaggingProfilesSchema**](TaggingProfilesSchema.md)| tagging_profilebody object | 
 **x_iam_token** | **str**| authentication header object | [optional] 

### Return type

**list[str]**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_healthbot_ingest_sflow**
> update_healthbot_ingest_sflow(sflow, x_iam_token=x_iam_token)

Update sflow by ID

Update operation of resource: sflow

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
sflow = swagger_client.SflowSchema() # SflowSchema | sflowbody object
x_iam_token = 'x_iam_token_example' # str | authentication header object (optional)

try:
    # Update sflow by ID
    api_instance.update_healthbot_ingest_sflow(sflow, x_iam_token=x_iam_token)
except ApiException as e:
    print("Exception when calling DefaultApi->update_healthbot_ingest_sflow: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sflow** | [**SflowSchema**](SflowSchema.md)| sflowbody object | 
 **x_iam_token** | **str**| authentication header object | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_healthbot_ingest_sflow_counter_record_by_id**
> update_healthbot_ingest_sflow_counter_record_by_id(record_name, counter_record, x_iam_token=x_iam_token)

Update counter-record by ID

Update operation of resource: counter-record

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
record_name = 'record_name_example' # str | ID of record-name
counter_record = swagger_client.CounterRecordSchema() # CounterRecordSchema | counter_recordbody object
x_iam_token = 'x_iam_token_example' # str | authentication header object (optional)

try:
    # Update counter-record by ID
    api_instance.update_healthbot_ingest_sflow_counter_record_by_id(record_name, counter_record, x_iam_token=x_iam_token)
except ApiException as e:
    print("Exception when calling DefaultApi->update_healthbot_ingest_sflow_counter_record_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **record_name** | **str**| ID of record-name | 
 **counter_record** | [**CounterRecordSchema**](CounterRecordSchema.md)| counter_recordbody object | 
 **x_iam_token** | **str**| authentication header object | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_healthbot_ingest_sflow_flow_record_by_id**
> update_healthbot_ingest_sflow_flow_record_by_id(record_name, flow_record, x_iam_token=x_iam_token)

Update flow-record by ID

Update operation of resource: flow-record

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
record_name = 'record_name_example' # str | ID of record-name
flow_record = swagger_client.FlowRecordSchema() # FlowRecordSchema | flow_recordbody object
x_iam_token = 'x_iam_token_example' # str | authentication header object (optional)

try:
    # Update flow-record by ID
    api_instance.update_healthbot_ingest_sflow_flow_record_by_id(record_name, flow_record, x_iam_token=x_iam_token)
except ApiException as e:
    print("Exception when calling DefaultApi->update_healthbot_ingest_sflow_flow_record_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **record_name** | **str**| ID of record-name | 
 **flow_record** | [**FlowRecordSchema**](FlowRecordSchema.md)| flow_recordbody object | 
 **x_iam_token** | **str**| authentication header object | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_healthbot_ingest_sflow_protocol_by_id**
> update_healthbot_ingest_sflow_protocol_by_id(protocol_name, protocol, x_iam_token=x_iam_token)

Update protocol by ID

Update operation of resource: protocol

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
protocol_name = 'protocol_name_example' # str | ID of protocol-name
protocol = swagger_client.ProtocolSchema() # ProtocolSchema | protocolbody object
x_iam_token = 'x_iam_token_example' # str | authentication header object (optional)

try:
    # Update protocol by ID
    api_instance.update_healthbot_ingest_sflow_protocol_by_id(protocol_name, protocol, x_iam_token=x_iam_token)
except ApiException as e:
    print("Exception when calling DefaultApi->update_healthbot_ingest_sflow_protocol_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **protocol_name** | **str**| ID of protocol-name | 
 **protocol** | [**ProtocolSchema**](ProtocolSchema.md)| protocolbody object | 
 **x_iam_token** | **str**| authentication header object | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_healthbot_ingest_sflow_sample_by_id**
> update_healthbot_ingest_sflow_sample_by_id(sample_name, sample, x_iam_token=x_iam_token)

Update sample by ID

Update operation of resource: sample

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
sample_name = 'sample_name_example' # str | ID of sample-name
sample = swagger_client.SampleSchema() # SampleSchema | samplebody object
x_iam_token = 'x_iam_token_example' # str | authentication header object (optional)

try:
    # Update sample by ID
    api_instance.update_healthbot_ingest_sflow_sample_by_id(sample_name, sample, x_iam_token=x_iam_token)
except ApiException as e:
    print("Exception when calling DefaultApi->update_healthbot_ingest_sflow_sample_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sample_name** | **str**| ID of sample-name | 
 **sample** | [**SampleSchema**](SampleSchema.md)| samplebody object | 
 **x_iam_token** | **str**| authentication header object | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_healthbot_ingest_snmp_notification**
> update_healthbot_ingest_snmp_notification(snmp_notification, x_iam_token=x_iam_token)

Update snmp-notification by ID

Update operation of resource: snmp-notification

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
snmp_notification = swagger_client.SnmpNotificationSchema() # SnmpNotificationSchema | snmp_notification body object
x_iam_token = 'x_iam_token_example' # str | authentication header object (optional)

try:
    # Update snmp-notification by ID
    api_instance.update_healthbot_ingest_snmp_notification(snmp_notification, x_iam_token=x_iam_token)
except ApiException as e:
    print("Exception when calling DefaultApi->update_healthbot_ingest_snmp_notification: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **snmp_notification** | [**SnmpNotificationSchema**](SnmpNotificationSchema.md)| snmp_notification body object | 
 **x_iam_token** | **str**| authentication header object | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_healthbot_ingest_snmp_notification_v3_usm_user_by_id**
> update_healthbot_ingest_snmp_notification_v3_usm_user_by_id(name, usm_user, x_iam_token=x_iam_token)

Update SNMPv3 user by UserName(ID)

Update operation of resource: snmp v3 usm user

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
name = 'name_example' # str | User Name
usm_user = swagger_client.Snmpv3UsmUserSchema() # Snmpv3UsmUserSchema | snmp_v3_usm user object
x_iam_token = 'x_iam_token_example' # str | authentication header object (optional)

try:
    # Update SNMPv3 user by UserName(ID)
    api_instance.update_healthbot_ingest_snmp_notification_v3_usm_user_by_id(name, usm_user, x_iam_token=x_iam_token)
except ApiException as e:
    print("Exception when calling DefaultApi->update_healthbot_ingest_snmp_notification_v3_usm_user_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| User Name | 
 **usm_user** | [**Snmpv3UsmUserSchema**](Snmpv3UsmUserSchema.md)| snmp_v3_usm user object | 
 **x_iam_token** | **str**| authentication header object | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_healthbot_ingest_syslog_header_pattern_by_id**
> update_healthbot_ingest_syslog_header_pattern_by_id(name, pattern, x_iam_token=x_iam_token)

Update pattern by ID

Update operation of resource: header-pattern

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
pattern = swagger_client.HeaderPatternSchema() # HeaderPatternSchema | header_patternbody object
x_iam_token = 'x_iam_token_example' # str | authentication header object (optional)

try:
    # Update pattern by ID
    api_instance.update_healthbot_ingest_syslog_header_pattern_by_id(name, pattern, x_iam_token=x_iam_token)
except ApiException as e:
    print("Exception when calling DefaultApi->update_healthbot_ingest_syslog_header_pattern_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| ID of name | 
 **pattern** | [**HeaderPatternSchema**](HeaderPatternSchema.md)| header_patternbody object | 
 **x_iam_token** | **str**| authentication header object | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_healthbot_ingest_tagging_profile_by_id**
> update_healthbot_ingest_tagging_profile_by_id(name, tagging_profile, x_iam_token=x_iam_token)

Update tagging-profile by ID

Update operation of resource: tagging-profile

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
tagging_profile = swagger_client.TaggingProfileSchema() # TaggingProfileSchema | tagging_profilebody object
x_iam_token = 'x_iam_token_example' # str | authentication header object (optional)

try:
    # Update tagging-profile by ID
    api_instance.update_healthbot_ingest_tagging_profile_by_id(name, tagging_profile, x_iam_token=x_iam_token)
except ApiException as e:
    print("Exception when calling DefaultApi->update_healthbot_ingest_tagging_profile_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| ID of name | 
 **tagging_profile** | [**TaggingProfileSchema**](TaggingProfileSchema.md)| tagging_profilebody object | 
 **x_iam_token** | **str**| authentication header object | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_healthbot_ingest_tagging_profiles**
> list[str] update_healthbot_ingest_tagging_profiles(tagging_profiles, x_iam_token=x_iam_token)

Update tagging-profile by ID

Update operation of resource: tagging-profile

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
tagging_profiles = swagger_client.TaggingProfilesSchema() # TaggingProfilesSchema | tagging_profilebody object
x_iam_token = 'x_iam_token_example' # str | authentication header object (optional)

try:
    # Update tagging-profile by ID
    api_response = api_instance.update_healthbot_ingest_tagging_profiles(tagging_profiles, x_iam_token=x_iam_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->update_healthbot_ingest_tagging_profiles: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tagging_profiles** | [**TaggingProfilesSchema**](TaggingProfilesSchema.md)| tagging_profilebody object | 
 **x_iam_token** | **str**| authentication header object | [optional] 

### Return type

**list[str]**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_healthbot_organization_organization_by_id**
> update_healthbot_organization_organization_by_id(organization_name, organization, x_iam_token=x_iam_token)

Update organization by ID

Update operation of resource: organization

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
organization_name = 'organization_name_example' # str | ID of organization-name
organization = swagger_client.OrganizationSchema() # OrganizationSchema | organizationbody object
x_iam_token = 'x_iam_token_example' # str | authentication header object (optional)

try:
    # Update organization by ID
    api_instance.update_healthbot_organization_organization_by_id(organization_name, organization, x_iam_token=x_iam_token)
except ApiException as e:
    print("Exception when calling DefaultApi->update_healthbot_organization_organization_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_name** | **str**| ID of organization-name | 
 **organization** | [**OrganizationSchema**](OrganizationSchema.md)| organizationbody object | 
 **x_iam_token** | **str**| authentication header object | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_healthbot_profile_rollup_summarization_field_profile_field_profile_by_id**
> update_healthbot_profile_rollup_summarization_field_profile_field_profile_by_id(profile_id, field_profile, x_iam_token=x_iam_token)

Update field-profile by ID

Update operation of resource: field-profile

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
profile_id = 'profile_id_example' # str | ID of profile-id
field_profile = swagger_client.RollupSummarizationSchema() # RollupSummarizationSchema | field_profilebody object
x_iam_token = 'x_iam_token_example' # str | authentication header object (optional)

try:
    # Update field-profile by ID
    api_instance.update_healthbot_profile_rollup_summarization_field_profile_field_profile_by_id(profile_id, field_profile, x_iam_token=x_iam_token)
except ApiException as e:
    print("Exception when calling DefaultApi->update_healthbot_profile_rollup_summarization_field_profile_field_profile_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **profile_id** | **str**| ID of profile-id | 
 **field_profile** | [**RollupSummarizationSchema**](RollupSummarizationSchema.md)| field_profilebody object | 
 **x_iam_token** | **str**| authentication header object | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_healthbot_system_time_series_database_time_series_database_by_id**
> update_healthbot_system_time_series_database_time_series_database_by_id(time_series_database, force_tsdb=force_tsdb)

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
force_tsdb = false # bool | force update tsdb when force is set to True (optional) (default to false)

try:
    # Update time-series-database by ID
    api_instance.update_healthbot_system_time_series_database_time_series_database_by_id(time_series_database, force_tsdb=force_tsdb)
except ApiException as e:
    print("Exception when calling DefaultApi->update_healthbot_system_time_series_database_time_series_database_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **time_series_database** | [**TsdbSchema**](TsdbSchema.md)| time_series_databasebody object | 
 **force_tsdb** | **bool**| force update tsdb when force is set to True | [optional] [default to false]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_healthbot_system_trigger_action**
> update_healthbot_system_trigger_action(trigger_action)

Update trigger-action

Update operation of resource: trigger-action

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
trigger_action = swagger_client.TriggerActionSchema() # TriggerActionSchema | trigger_action object

try:
    # Update trigger-action
    api_instance.update_healthbot_system_trigger_action(trigger_action)
except ApiException as e:
    print("Exception when calling DefaultApi->update_healthbot_system_trigger_action: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **trigger_action** | [**TriggerActionSchema**](TriggerActionSchema.md)| trigger_action object | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_iceberg_ingest**
> update_iceberg_ingest(ingest_settings, x_iam_token=x_iam_token)

Update ingest by ID

Update operation of resource: ingest

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
x_iam_token = 'x_iam_token_example' # str | authentication header object (optional)

try:
    # Update ingest by ID
    api_instance.update_iceberg_ingest(ingest_settings, x_iam_token=x_iam_token)
except ApiException as e:
    print("Exception when calling DefaultApi->update_iceberg_ingest: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ingest_settings** | [**IngestSettingsSchema**](IngestSettingsSchema.md)| ingest_settingsbody object | 
 **x_iam_token** | **str**| authentication header object | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_iceberg_ingest_flow**
> update_iceberg_ingest_flow(flow, x_iam_token=x_iam_token)

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
x_iam_token = 'x_iam_token_example' # str | authentication header object (optional)

try:
    # Update flow by ID
    api_instance.update_iceberg_ingest_flow(flow, x_iam_token=x_iam_token)
except ApiException as e:
    print("Exception when calling DefaultApi->update_iceberg_ingest_flow: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **flow** | [**FlowSchema**](FlowSchema.md)| flowbody object | 
 **x_iam_token** | **str**| authentication header object | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_iceberg_ingest_flow_template_by_id**
> update_iceberg_ingest_flow_template_by_id(name, template, x_iam_token=x_iam_token)

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
x_iam_token = 'x_iam_token_example' # str | authentication header object (optional)

try:
    # Update template by ID
    api_instance.update_iceberg_ingest_flow_template_by_id(name, template, x_iam_token=x_iam_token)
except ApiException as e:
    print("Exception when calling DefaultApi->update_iceberg_ingest_flow_template_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of template | 
 **template** | [**TemplateSchema**](TemplateSchema.md)| templatebody object | 
 **x_iam_token** | **str**| authentication header object | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_iceberg_ingest_native_gpb**
> update_iceberg_ingest_native_gpb(native_gpb, x_iam_token=x_iam_token)

Update native-gpb by ID

Update operation of resource: native-gpb

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
native_gpb = swagger_client.NativeGpbSchema() # NativeGpbSchema | native_gpbbody object
x_iam_token = 'x_iam_token_example' # str | authentication header object (optional)

try:
    # Update native-gpb by ID
    api_instance.update_iceberg_ingest_native_gpb(native_gpb, x_iam_token=x_iam_token)
except ApiException as e:
    print("Exception when calling DefaultApi->update_iceberg_ingest_native_gpb: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **native_gpb** | [**NativeGpbSchema**](NativeGpbSchema.md)| native_gpbbody object | 
 **x_iam_token** | **str**| authentication header object | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_iceberg_ingest_settings**
> update_iceberg_ingest_settings(ingest_settings, x_iam_token=x_iam_token)

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
x_iam_token = 'x_iam_token_example' # str | authentication header object (optional)

try:
    # Update ingest-settings by ID
    api_instance.update_iceberg_ingest_settings(ingest_settings, x_iam_token=x_iam_token)
except ApiException as e:
    print("Exception when calling DefaultApi->update_iceberg_ingest_settings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ingest_settings** | [**IngestSettingsSchema**](IngestSettingsSchema.md)| ingest_settingsbody object | 
 **x_iam_token** | **str**| authentication header object | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_iceberg_ingest_settings_flow**
> update_iceberg_ingest_settings_flow(flow, x_iam_token=x_iam_token)

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
x_iam_token = 'x_iam_token_example' # str | authentication header object (optional)

try:
    # Update flow by ID
    api_instance.update_iceberg_ingest_settings_flow(flow, x_iam_token=x_iam_token)
except ApiException as e:
    print("Exception when calling DefaultApi->update_iceberg_ingest_settings_flow: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **flow** | [**FlowSchema**](FlowSchema.md)| flowbody object | 
 **x_iam_token** | **str**| authentication header object | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_iceberg_ingest_settings_flow_template_by_id**
> update_iceberg_ingest_settings_flow_template_by_id(name, template, x_iam_token=x_iam_token)

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
x_iam_token = 'x_iam_token_example' # str | authentication header object (optional)

try:
    # Update template by ID
    api_instance.update_iceberg_ingest_settings_flow_template_by_id(name, template, x_iam_token=x_iam_token)
except ApiException as e:
    print("Exception when calling DefaultApi->update_iceberg_ingest_settings_flow_template_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of template | 
 **template** | [**TemplateSchema**](TemplateSchema.md)| templatebody object | 
 **x_iam_token** | **str**| authentication header object | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_iceberg_ingest_settings_syslog**
> update_iceberg_ingest_settings_syslog(syslog, x_iam_token=x_iam_token)

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
x_iam_token = 'x_iam_token_example' # str | authentication header object (optional)

try:
    # Update syslog by ID
    api_instance.update_iceberg_ingest_settings_syslog(syslog, x_iam_token=x_iam_token)
except ApiException as e:
    print("Exception when calling DefaultApi->update_iceberg_ingest_settings_syslog: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **syslog** | [**SyslogSchema**](SyslogSchema.md)| syslogbody object | 
 **x_iam_token** | **str**| authentication header object | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_iceberg_ingest_settings_syslog_pattern_by_id**
> update_iceberg_ingest_settings_syslog_pattern_by_id(name, pattern, x_iam_token=x_iam_token)

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
x_iam_token = 'x_iam_token_example' # str | authentication header object (optional)

try:
    # Update pattern by ID
    api_instance.update_iceberg_ingest_settings_syslog_pattern_by_id(name, pattern, x_iam_token=x_iam_token)
except ApiException as e:
    print("Exception when calling DefaultApi->update_iceberg_ingest_settings_syslog_pattern_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of pattern | 
 **pattern** | [**PatternSchema**](PatternSchema.md)| patternbody object | 
 **x_iam_token** | **str**| authentication header object | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_iceberg_ingest_settings_syslog_pattern_set_by_id**
> update_iceberg_ingest_settings_syslog_pattern_set_by_id(name, pattern_set, x_iam_token=x_iam_token)

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
x_iam_token = 'x_iam_token_example' # str | authentication header object (optional)

try:
    # Update pattern-set by ID
    api_instance.update_iceberg_ingest_settings_syslog_pattern_set_by_id(name, pattern_set, x_iam_token=x_iam_token)
except ApiException as e:
    print("Exception when calling DefaultApi->update_iceberg_ingest_settings_syslog_pattern_set_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of pattern-set | 
 **pattern_set** | [**PatternSetSchema**](PatternSetSchema.md)| pattern_setbody object | 
 **x_iam_token** | **str**| authentication header object | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_iceberg_ingest_syslog**
> update_iceberg_ingest_syslog(syslog, x_iam_token=x_iam_token)

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
x_iam_token = 'x_iam_token_example' # str | authentication header object (optional)

try:
    # Update syslog by ID
    api_instance.update_iceberg_ingest_syslog(syslog, x_iam_token=x_iam_token)
except ApiException as e:
    print("Exception when calling DefaultApi->update_iceberg_ingest_syslog: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **syslog** | [**SyslogSchema**](SyslogSchema.md)| syslogbody object | 
 **x_iam_token** | **str**| authentication header object | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_iceberg_ingest_syslog_pattern_by_id**
> update_iceberg_ingest_syslog_pattern_by_id(name, pattern, x_iam_token=x_iam_token)

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
x_iam_token = 'x_iam_token_example' # str | authentication header object (optional)

try:
    # Update pattern by ID
    api_instance.update_iceberg_ingest_syslog_pattern_by_id(name, pattern, x_iam_token=x_iam_token)
except ApiException as e:
    print("Exception when calling DefaultApi->update_iceberg_ingest_syslog_pattern_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of pattern | 
 **pattern** | [**PatternSchema**](PatternSchema.md)| patternbody object | 
 **x_iam_token** | **str**| authentication header object | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_iceberg_ingest_syslog_pattern_set_by_id**
> update_iceberg_ingest_syslog_pattern_set_by_id(name, pattern_set, x_iam_token=x_iam_token)

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
x_iam_token = 'x_iam_token_example' # str | authentication header object (optional)

try:
    # Update pattern-set by ID
    api_instance.update_iceberg_ingest_syslog_pattern_set_by_id(name, pattern_set, x_iam_token=x_iam_token)
except ApiException as e:
    print("Exception when calling DefaultApi->update_iceberg_ingest_syslog_pattern_set_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of pattern-set | 
 **pattern_set** | [**PatternSetSchema**](PatternSetSchema.md)| pattern_setbody object | 
 **x_iam_token** | **str**| authentication header object | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_iceberg_profile_data_summarization_raw_by_id**
> update_iceberg_profile_data_summarization_raw_by_id(name, raw_data_summarization, x_iam_token=x_iam_token)

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
x_iam_token = 'x_iam_token_example' # str | authentication header object (optional)

try:
    # Update raw-data-summarization by ID
    api_instance.update_iceberg_profile_data_summarization_raw_by_id(name, raw_data_summarization, x_iam_token=x_iam_token)
except ApiException as e:
    print("Exception when calling DefaultApi->update_iceberg_profile_data_summarization_raw_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of raw-data-summarization | 
 **raw_data_summarization** | [**RawSchema**](RawSchema.md)| raw_data_summarizationbody object | 
 **x_iam_token** | **str**| authentication header object | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_iceberg_profile_security_ca_profile_by_id**
> update_iceberg_profile_security_ca_profile_by_id(name, ca_profile, x_iam_token=x_iam_token)

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
x_iam_token = 'x_iam_token_example' # str | authentication header object (optional)

try:
    # Update ca-profile by ID
    api_instance.update_iceberg_profile_security_ca_profile_by_id(name, ca_profile, x_iam_token=x_iam_token)
except ApiException as e:
    print("Exception when calling DefaultApi->update_iceberg_profile_security_ca_profile_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of ca-profile | 
 **ca_profile** | [**CaProfileSchema**](CaProfileSchema.md)| ca_profilebody object | 
 **x_iam_token** | **str**| authentication header object | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_iceberg_profile_security_local_certificate_by_id**
> update_iceberg_profile_security_local_certificate_by_id(name, local_certificate, x_iam_token=x_iam_token)

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
x_iam_token = 'x_iam_token_example' # str | authentication header object (optional)

try:
    # Update local-certificate by ID
    api_instance.update_iceberg_profile_security_local_certificate_by_id(name, local_certificate, x_iam_token=x_iam_token)
except ApiException as e:
    print("Exception when calling DefaultApi->update_iceberg_profile_security_local_certificate_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of local-certificate | 
 **local_certificate** | [**LocalCertificateSchema**](LocalCertificateSchema.md)| local_certificatebody object | 
 **x_iam_token** | **str**| authentication header object | [optional] 

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
> update_iceberg_profiles(profile, x_iam_token=x_iam_token)

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
x_iam_token = 'x_iam_token_example' # str | authentication header object (optional)

try:
    # Update profile by ID
    api_instance.update_iceberg_profiles(profile, x_iam_token=x_iam_token)
except ApiException as e:
    print("Exception when calling DefaultApi->update_iceberg_profiles: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **profile** | [**ProfilesSchema**](ProfilesSchema.md)| profilebody object | 
 **x_iam_token** | **str**| authentication header object | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

