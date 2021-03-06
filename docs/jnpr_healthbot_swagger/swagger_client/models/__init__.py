# coding: utf-8

# flake8: noqa
"""
    Healthbot APIs

    API interface for Healthbot application  # noqa: E501

    OpenAPI spec version: 3.1.0
    Contact: healthbot-feedback@juniper.net
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

# import models into model package
from swagger_client.models.affected_groups import AffectedGroups
from swagger_client.models.apply_macro_schema import ApplyMacroSchema
from swagger_client.models.applymacro_schema_data import ApplymacroSchemaData
from swagger_client.models.associated_group_schema import AssociatedGroupSchema
from swagger_client.models.associated_role_schema import AssociatedRoleSchema
from swagger_client.models.associated_user_schema import AssociatedUserSchema
from swagger_client.models.associated_user_schema_inner import AssociatedUserSchemaInner
from swagger_client.models.ca_profile_schema import CaProfileSchema
from swagger_client.models.command_rpc import CommandRpc
from swagger_client.models.commit_job import CommitJob
from swagger_client.models.credential import Credential
from swagger_client.models.custom_plugin_schema import CustomPluginSchema
from swagger_client.models.custom_plugins_schema import CustomPluginsSchema
from swagger_client.models.customplugin_schema_parameters import CustompluginSchemaParameters
from swagger_client.models.customplugin_schema_securityparameters import CustompluginSchemaSecurityparameters
from swagger_client.models.customplugin_schema_securityparameters_tls import CustompluginSchemaSecurityparametersTls
from swagger_client.models.customplugin_schema_securityparameters_userauthentication import CustompluginSchemaSecurityparametersUserauthentication
from swagger_client.models.datastore_schema import DatastoreSchema
from swagger_client.models.debug_arguments_schema import DebugArgumentsSchema
from swagger_client.models.debug_job_response_schema import DebugJobResponseSchema
from swagger_client.models.destination_schema import DestinationSchema
from swagger_client.models.destination_schema_disk import DestinationSchemaDisk
from swagger_client.models.destination_schema_email import DestinationSchemaEmail
from swagger_client.models.destinations_schema import DestinationsSchema
from swagger_client.models.device_field_capture_schema import DeviceFieldCaptureSchema
from swagger_client.models.device_group_field_capture_schema import DeviceGroupFieldCaptureSchema
from swagger_client.models.device_group_health_tree import DeviceGroupHealthTree
from swagger_client.models.device_group_schema import DeviceGroupSchema
from swagger_client.models.device_groups_schema import DeviceGroupsSchema
from swagger_client.models.device_health_schema import DeviceHealthSchema
from swagger_client.models.device_health_tree import DeviceHealthTree
from swagger_client.models.device_schema import DeviceSchema
from swagger_client.models.device_schema_flow import DeviceSchemaFlow
from swagger_client.models.device_schema_i_agent import DeviceSchemaIAgent
from swagger_client.models.device_schema_openconfig import DeviceSchemaOpenconfig
from swagger_client.models.device_schema_snmp import DeviceSchemaSnmp
from swagger_client.models.device_schema_snmp_v2 import DeviceSchemaSnmpV2
from swagger_client.models.device_schema_syslog import DeviceSchemaSyslog
from swagger_client.models.device_schema_variable import DeviceSchemaVariable
from swagger_client.models.device_schema_vendor import DeviceSchemaVendor
from swagger_client.models.device_schema_vendor_arista import DeviceSchemaVendorArista
from swagger_client.models.device_schema_vendor_cisco import DeviceSchemaVendorCisco
from swagger_client.models.device_schema_vendor_juniper import DeviceSchemaVendorJuniper
from swagger_client.models.device_schema_vendor_linux import DeviceSchemaVendorLinux
from swagger_client.models.device_schema_vendor_othervendor import DeviceSchemaVendorOthervendor
from swagger_client.models.device_schema_vendor_paloalto import DeviceSchemaVendorPaloalto
from swagger_client.models.devicegroup_schema_authentication import DevicegroupSchemaAuthentication
from swagger_client.models.devicegroup_schema_authentication_password import DevicegroupSchemaAuthenticationPassword
from swagger_client.models.devicegroup_schema_authentication_ssh import DevicegroupSchemaAuthenticationSsh
from swagger_client.models.devicegroup_schema_authentication_ssl import DevicegroupSchemaAuthenticationSsl
from swagger_client.models.devicegroup_schema_flow import DevicegroupSchemaFlow
from swagger_client.models.devicegroup_schema_flow_netflow import DevicegroupSchemaFlowNetflow
from swagger_client.models.devicegroup_schema_logging import DevicegroupSchemaLogging
from swagger_client.models.devicegroup_schema_logging_byoi import DevicegroupSchemaLoggingByoi
from swagger_client.models.devicegroup_schema_logging_byoi_service import DevicegroupSchemaLoggingByoiService
from swagger_client.models.devicegroup_schema_logging_flow import DevicegroupSchemaLoggingFlow
from swagger_client.models.devicegroup_schema_logging_i_agent import DevicegroupSchemaLoggingIAgent
from swagger_client.models.devicegroup_schema_logging_m_lmodelbuilder import DevicegroupSchemaLoggingMLmodelbuilder
from swagger_client.models.devicegroup_schema_logging_nativegpb import DevicegroupSchemaLoggingNativegpb
from swagger_client.models.devicegroup_schema_logging_nonsensorrules import DevicegroupSchemaLoggingNonsensorrules
from swagger_client.models.devicegroup_schema_logging_openconfig import DevicegroupSchemaLoggingOpenconfig
from swagger_client.models.devicegroup_schema_logging_reportsgeneration import DevicegroupSchemaLoggingReportsgeneration
from swagger_client.models.devicegroup_schema_logging_snmp import DevicegroupSchemaLoggingSnmp
from swagger_client.models.devicegroup_schema_logging_syslog import DevicegroupSchemaLoggingSyslog
from swagger_client.models.devicegroup_schema_logging_triggerevaluation import DevicegroupSchemaLoggingTriggerevaluation
from swagger_client.models.devicegroup_schema_nativegpb import DevicegroupSchemaNativegpb
from swagger_client.models.devicegroup_schema_notification import DevicegroupSchemaNotification
from swagger_client.models.devicegroup_schema_openconfig import DevicegroupSchemaOpenconfig
from swagger_client.models.devicegroup_schema_openconfig_gnmi import DevicegroupSchemaOpenconfigGnmi
from swagger_client.models.devicegroup_schema_publish import DevicegroupSchemaPublish
from swagger_client.models.devicegroup_schema_rawdata import DevicegroupSchemaRawdata
from swagger_client.models.devicegroup_schema_rawdata_summarize import DevicegroupSchemaRawdataSummarize
from swagger_client.models.devicegroup_schema_scheduler import DevicegroupSchemaScheduler
from swagger_client.models.devicegroup_schema_syslog import DevicegroupSchemaSyslog
from swagger_client.models.devicegroup_schema_variable import DevicegroupSchemaVariable
from swagger_client.models.devicegroup_schema_variablevalue import DevicegroupSchemaVariablevalue
from swagger_client.models.devices_schema import DevicesSchema
from swagger_client.models.error import Error
from swagger_client.models.event import Event
from swagger_client.models.field_capture_schema import FieldCaptureSchema
from swagger_client.models.field_field_capture_schema import FieldFieldCaptureSchema
from swagger_client.models.flow_schema import FlowSchema
from swagger_client.models.flow_schema_flow import FlowSchemaFlow
from swagger_client.models.flow_schema_flow_recognitionpattern import FlowSchemaFlowRecognitionpattern
from swagger_client.models.flow_schema_flow_template import FlowSchemaFlowTemplate
from swagger_client.models.frequency_profile_schema import FrequencyProfileSchema
from swagger_client.models.frequencyprofile_schema_nonsensor import FrequencyprofileSchemaNonsensor
from swagger_client.models.frequencyprofile_schema_sensor import FrequencyprofileSchemaSensor
from swagger_client.models.group import Group
from swagger_client.models.group_health_schema import GroupHealthSchema
from swagger_client.models.groupgroupid_roles import GroupgroupidRoles
from swagger_client.models.groupgroupid_users import GroupgroupidUsers
from swagger_client.models.groups import Groups
from swagger_client.models.health_schema import HealthSchema
from swagger_client.models.ingest_mapping_schema import IngestMappingSchema
from swagger_client.models.ingest_mappings_schema import IngestMappingsSchema
from swagger_client.models.ingest_settings_schema import IngestSettingsSchema
from swagger_client.models.ingestmapping_schema_i_agent import IngestmappingSchemaIAgent
from swagger_client.models.ingestmapping_schema_i_agent_useplugin import IngestmappingSchemaIAgentUseplugin
from swagger_client.models.ingestmapping_schema_nativegpb import IngestmappingSchemaNativegpb
from swagger_client.models.ingestmapping_schema_netflow import IngestmappingSchemaNetflow
from swagger_client.models.ingestmapping_schema_openconfig import IngestmappingSchemaOpenconfig
from swagger_client.models.ingestmapping_schema_snmp import IngestmappingSchemaSnmp
from swagger_client.models.ingestmapping_schema_syslog import IngestmappingSchemaSyslog
from swagger_client.models.inline_response200 import InlineResponse200
from swagger_client.models.inline_response2001 import InlineResponse2001
from swagger_client.models.inline_response2002 import InlineResponse2002
from swagger_client.models.inline_response2003 import InlineResponse2003
from swagger_client.models.inline_response2004 import InlineResponse2004
from swagger_client.models.inline_response2005 import InlineResponse2005
from swagger_client.models.inline_response2006 import InlineResponse2006
from swagger_client.models.inline_response2007 import InlineResponse2007
from swagger_client.models.inline_response2008 import InlineResponse2008
from swagger_client.models.inline_response2009 import InlineResponse2009
from swagger_client.models.instance_schedule_state_schema import InstanceScheduleStateSchema
from swagger_client.models.instances_schedule_state_schema import InstancesScheduleStateSchema
from swagger_client.models.lhs_rhs_group import LhsRhsGroup
from swagger_client.models.license_feature_schema import LicenseFeatureSchema
from swagger_client.models.license_features_schema import LicenseFeaturesSchema
from swagger_client.models.license_key_schema import LicenseKeySchema
from swagger_client.models.license_keys_schema import LicenseKeysSchema
from swagger_client.models.license_raw_key_schema import LicenseRawKeySchema
from swagger_client.models.license_raw_keys_schema import LicenseRawKeysSchema
from swagger_client.models.licensekey_schema_features import LicensekeySchemaFeatures
from swagger_client.models.local_certificate_schema import LocalCertificateSchema
from swagger_client.models.network_group_schema import NetworkGroupSchema
from swagger_client.models.network_groups_schema import NetworkGroupsSchema
from swagger_client.models.network_health_tree import NetworkHealthTree
from swagger_client.models.networkgroup_schema_logging import NetworkgroupSchemaLogging
from swagger_client.models.networkgroup_schema_notification import NetworkgroupSchemaNotification
from swagger_client.models.networkgroup_schema_publish import NetworkgroupSchemaPublish
from swagger_client.models.notification_schema import NotificationSchema
from swagger_client.models.notification_schema_emails import NotificationSchemaEmails
from swagger_client.models.notification_schema_emails_filter import NotificationSchemaEmailsFilter
from swagger_client.models.notification_schema_httppost import NotificationSchemaHttppost
from swagger_client.models.notification_schema_httppost_basic import NotificationSchemaHttppostBasic
from swagger_client.models.notification_schema_kafkapublish import NotificationSchemaKafkapublish
from swagger_client.models.notification_schema_kafkapublish_sasl import NotificationSchemaKafkapublishSasl
from swagger_client.models.notification_schema_microsoftteams import NotificationSchemaMicrosoftteams
from swagger_client.models.notification_schema_slack import NotificationSchemaSlack
from swagger_client.models.notifications_schema import NotificationsSchema
from swagger_client.models.password import Password
from swagger_client.models.pattern_schema import PatternSchema
from swagger_client.models.pattern_schema_constant import PatternSchemaConstant
from swagger_client.models.pattern_schema_field import PatternSchemaField
from swagger_client.models.pattern_set_schema import PatternSetSchema
from swagger_client.models.playbook_schema import PlaybookSchema
from swagger_client.models.playbooks_schema import PlaybooksSchema
from swagger_client.models.profile_schema import ProfileSchema
from swagger_client.models.profile_schema_datasummarization import ProfileSchemaDatasummarization
from swagger_client.models.profile_schema_datasummarization_path import ProfileSchemaDatasummarizationPath
from swagger_client.models.profile_schema_datasummarization_raw import ProfileSchemaDatasummarizationRaw
from swagger_client.models.profile_schema_security import ProfileSchemaSecurity
from swagger_client.models.profiles_schema import ProfilesSchema
from swagger_client.models.profiles_schema_profile import ProfilesSchemaProfile
from swagger_client.models.raw_data_summarizations_schema import RawDataSummarizationsSchema
from swagger_client.models.raw_schema import RawSchema
from swagger_client.models.raw_schema_datatype import RawSchemaDatatype
from swagger_client.models.raw_schema_path import RawSchemaPath
from swagger_client.models.refresh_token import RefreshToken
from swagger_client.models.report_generation_schema import ReportGenerationSchema
from swagger_client.models.report_schema import ReportSchema
from swagger_client.models.report_schema_canvaspanel import ReportSchemaCanvaspanel
from swagger_client.models.report_schema_graphcanvas import ReportSchemaGraphcanvas
from swagger_client.models.reports_schema import ReportsSchema
from swagger_client.models.retention_policies_schema import RetentionPoliciesSchema
from swagger_client.models.retention_policy_schema import RetentionPolicySchema
from swagger_client.models.role_schema import RoleSchema
from swagger_client.models.role_schema_inner import RoleSchemaInner
from swagger_client.models.rule_field_capture_schema import RuleFieldCaptureSchema
from swagger_client.models.rule_schema import RuleSchema
from swagger_client.models.rule_schema_argument import RuleSchemaArgument
from swagger_client.models.rule_schema_byoi import RuleSchemaByoi
from swagger_client.models.rule_schema_byoi_plugin import RuleSchemaByoiPlugin
from swagger_client.models.rule_schema_byoi_plugin_parameters import RuleSchemaByoiPluginParameters
from swagger_client.models.rule_schema_constant import RuleSchemaConstant
from swagger_client.models.rule_schema_dataifmissing import RuleSchemaDataifmissing
from swagger_client.models.rule_schema_field import RuleSchemaField
from swagger_client.models.rule_schema_flow import RuleSchemaFlow
from swagger_client.models.rule_schema_formula import RuleSchemaFormula
from swagger_client.models.rule_schema_formula1 import RuleSchemaFormula1
from swagger_client.models.rule_schema_formula1_and import RuleSchemaFormula1And
from swagger_client.models.rule_schema_formula1_or import RuleSchemaFormula1Or
from swagger_client.models.rule_schema_formula1_unique import RuleSchemaFormula1Unique
from swagger_client.models.rule_schema_formula1_unless import RuleSchemaFormula1Unless
from swagger_client.models.rule_schema_formula_anomalydetection import RuleSchemaFormulaAnomalydetection
from swagger_client.models.rule_schema_formula_count import RuleSchemaFormulaCount
from swagger_client.models.rule_schema_formula_dynamicthreshold import RuleSchemaFormulaDynamicthreshold
from swagger_client.models.rule_schema_formula_eval import RuleSchemaFormulaEval
from swagger_client.models.rule_schema_formula_max import RuleSchemaFormulaMax
from swagger_client.models.rule_schema_formula_mean import RuleSchemaFormulaMean
from swagger_client.models.rule_schema_formula_microburst import RuleSchemaFormulaMicroburst
from swagger_client.models.rule_schema_formula_min import RuleSchemaFormulaMin
from swagger_client.models.rule_schema_formula_outlierdetection import RuleSchemaFormulaOutlierdetection
from swagger_client.models.rule_schema_formula_outlierdetection_algorithm import RuleSchemaFormulaOutlierdetectionAlgorithm
from swagger_client.models.rule_schema_formula_outlierdetection_algorithm_dbscan import RuleSchemaFormulaOutlierdetectionAlgorithmDbscan
from swagger_client.models.rule_schema_formula_outlierdetection_algorithm_dbscan_sensitivity import RuleSchemaFormulaOutlierdetectionAlgorithmDbscanSensitivity
from swagger_client.models.rule_schema_formula_outlierdetection_algorithm_kfold3sigma import RuleSchemaFormulaOutlierdetectionAlgorithmKfold3sigma
from swagger_client.models.rule_schema_formula_predict import RuleSchemaFormulaPredict
from swagger_client.models.rule_schema_formula_rateofchange import RuleSchemaFormulaRateofchange
from swagger_client.models.rule_schema_formula_stddev import RuleSchemaFormulaStddev
from swagger_client.models.rule_schema_formula_sum import RuleSchemaFormulaSum
from swagger_client.models.rule_schema_formula_userdefinedfunction import RuleSchemaFormulaUserdefinedfunction
from swagger_client.models.rule_schema_formula_userdefinedfunction_argument import RuleSchemaFormulaUserdefinedfunctionArgument
from swagger_client.models.rule_schema_function import RuleSchemaFunction
from swagger_client.models.rule_schema_i_agent import RuleSchemaIAgent
from swagger_client.models.rule_schema_i_agent_args import RuleSchemaIAgentArgs
from swagger_client.models.rule_schema_nativegpb import RuleSchemaNativegpb
from swagger_client.models.rule_schema_openconfig import RuleSchemaOpenconfig
from swagger_client.models.rule_schema_reference import RuleSchemaReference
from swagger_client.models.rule_schema_reference_dataifmissing import RuleSchemaReferenceDataifmissing
from swagger_client.models.rule_schema_ruleproperties import RuleSchemaRuleproperties
from swagger_client.models.rule_schema_ruleproperties_catalogue import RuleSchemaRulepropertiesCatalogue
from swagger_client.models.rule_schema_ruleproperties_helperfiles import RuleSchemaRulepropertiesHelperfiles
from swagger_client.models.rule_schema_ruleproperties_supporteddevices import RuleSchemaRulepropertiesSupporteddevices
from swagger_client.models.rule_schema_ruleproperties_supporteddevices_juniper import RuleSchemaRulepropertiesSupporteddevicesJuniper
from swagger_client.models.rule_schema_ruleproperties_supporteddevices_juniper_operatingsystem import RuleSchemaRulepropertiesSupporteddevicesJuniperOperatingsystem
from swagger_client.models.rule_schema_ruleproperties_supporteddevices_juniper_products import RuleSchemaRulepropertiesSupporteddevicesJuniperProducts
from swagger_client.models.rule_schema_ruleproperties_supporteddevices_juniper_releases import RuleSchemaRulepropertiesSupporteddevicesJuniperReleases
from swagger_client.models.rule_schema_ruleproperties_supporteddevices_othervendor import RuleSchemaRulepropertiesSupporteddevicesOthervendor
from swagger_client.models.rule_schema_sensor import RuleSchemaSensor
from swagger_client.models.rule_schema_sensor1 import RuleSchemaSensor1
from swagger_client.models.rule_schema_snmp import RuleSchemaSnmp
from swagger_client.models.rule_schema_syslog import RuleSchemaSyslog
from swagger_client.models.rule_schema_term import RuleSchemaTerm
from swagger_client.models.rule_schema_then import RuleSchemaThen
from swagger_client.models.rule_schema_then_argument import RuleSchemaThenArgument
from swagger_client.models.rule_schema_then_status import RuleSchemaThenStatus
from swagger_client.models.rule_schema_then_userdefinedaction import RuleSchemaThenUserdefinedaction
from swagger_client.models.rule_schema_trigger import RuleSchemaTrigger
from swagger_client.models.rule_schema_variable import RuleSchemaVariable
from swagger_client.models.rule_schema_vector import RuleSchemaVector
from swagger_client.models.rule_schema_when import RuleSchemaWhen
from swagger_client.models.rule_schema_when_doesnotmatchwith import RuleSchemaWhenDoesnotmatchwith
from swagger_client.models.rule_schema_when_equalto import RuleSchemaWhenEqualto
from swagger_client.models.rule_schema_when_exists import RuleSchemaWhenExists
from swagger_client.models.rule_schema_when_increasingatleastbyrate import RuleSchemaWhenIncreasingatleastbyrate
from swagger_client.models.rule_schema_when_increasingatleastbyvalue import RuleSchemaWhenIncreasingatleastbyvalue
from swagger_client.models.rule_schema_when_maxrateofincrease import RuleSchemaWhenMaxrateofincrease
from swagger_client.models.rule_schema_when_range import RuleSchemaWhenRange
from swagger_client.models.rule_schema_when_userdefinedfunction import RuleSchemaWhenUserdefinedfunction
from swagger_client.models.rule_schema_where import RuleSchemaWhere
from swagger_client.models.scheduler_schema import SchedulerSchema
from swagger_client.models.scheduler_schema_repeat import SchedulerSchemaRepeat
from swagger_client.models.scheduler_schema_repeat_interval import SchedulerSchemaRepeatInterval
from swagger_client.models.scheduler_schema_runfor import SchedulerSchemaRunfor
from swagger_client.models.schedulers_schema import SchedulersSchema
from swagger_client.models.service_status import ServiceStatus
from swagger_client.models.ssh_key_profile_schema import SshKeyProfileSchema
from swagger_client.models.syslog_schema import SyslogSchema
from swagger_client.models.syslog_schema_syslog import SyslogSchemaSyslog
from swagger_client.models.system_settings_schema import SystemSettingsSchema
from swagger_client.models.table_schema import TableSchema
from swagger_client.models.tagging_profile_schema import TaggingProfileSchema
from swagger_client.models.tagging_profiles_schema import TaggingProfilesSchema
from swagger_client.models.taggingprofile_schema_policy import TaggingprofileSchemaPolicy
from swagger_client.models.taggingprofile_schema_term import TaggingprofileSchemaTerm
from swagger_client.models.taggingprofile_schema_then import TaggingprofileSchemaThen
from swagger_client.models.taggingprofile_schema_then_addfield import TaggingprofileSchemaThenAddfield
from swagger_client.models.taggingprofile_schema_then_addkey import TaggingprofileSchemaThenAddkey
from swagger_client.models.taggingprofile_schema_when import TaggingprofileSchemaWhen
from swagger_client.models.taggingprofile_schema_when_doesnotmatchwith import TaggingprofileSchemaWhenDoesnotmatchwith
from swagger_client.models.taggingprofile_schema_when_equalto import TaggingprofileSchemaWhenEqualto
from swagger_client.models.taggingprofile_schema_when_eval import TaggingprofileSchemaWhenEval
from swagger_client.models.taggingprofile_schema_when_matcheswithscheduler import TaggingprofileSchemaWhenMatcheswithscheduler
from swagger_client.models.template_schema import TemplateSchema
from swagger_client.models.time_range_mandatory import TimeRangeMandatory
from swagger_client.models.tlive_kafka_oc_schema import TliveKafkaOcSchema
from swagger_client.models.tlive_kafka_ocs_schema import TliveKafkaOcsSchema
from swagger_client.models.tlivekafkaoc_schema_security import TlivekafkaocSchemaSecurity
from swagger_client.models.tlivekafkaoc_schema_security_sasl import TlivekafkaocSchemaSecuritySasl
from swagger_client.models.token import Token
from swagger_client.models.topic_field_capture_schema import TopicFieldCaptureSchema
from swagger_client.models.topic_schema import TopicSchema
from swagger_client.models.topics_schema import TopicsSchema
from swagger_client.models.trigger_schema import TriggerSchema
from swagger_client.models.trigger_schema_triggers import TriggerSchemaTriggers
from swagger_client.models.tsdb_error import TsdbError
from swagger_client.models.tsdb_error_results import TsdbErrorResults
from swagger_client.models.tsdb_post_body import TsdbPostBody
from swagger_client.models.tsdb_post_body_items import TsdbPostBodyItems
from swagger_client.models.tsdb_results import TsdbResults
from swagger_client.models.tsdb_results_results import TsdbResultsResults
from swagger_client.models.tsdb_results_series import TsdbResultsSeries
from swagger_client.models.tsdb_schema import TsdbSchema
from swagger_client.models.user import User
from swagger_client.models.user1 import User1
from swagger_client.models.user_schema import UserSchema
from swagger_client.models.user_schema_groups import UserSchemaGroups
from swagger_client.models.when_lhs_rhs_group import WhenLhsRhsGroup
