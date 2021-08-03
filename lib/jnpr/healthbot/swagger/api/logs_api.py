# coding: utf-8

"""
    Paragon Insights APIs

    API interface for PI application  # noqa: E501

    OpenAPI spec version: 4.0.0
    Contact: healthbot-feedback@juniper.net
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from jnpr.healthbot.swagger.api_client import ApiClient


class LogsApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def retrieve_logs_for_device_group(self, device_group_name, **kwargs):  # noqa: E501
        """Logs for the given device-group.  # noqa: E501

        Get the logs for all the services for the given {device_group_name}  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.retrieve_logs_for_device_group(device_group_name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str device_group_name: Device group name (required)
        :param str x_iam_token: authentication header object
        :param bool download: Download the logs
        :param str filename: Name of the log file
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.retrieve_logs_for_device_group_with_http_info(device_group_name, **kwargs)  # noqa: E501
        else:
            (data) = self.retrieve_logs_for_device_group_with_http_info(device_group_name, **kwargs)  # noqa: E501
            return data

    def retrieve_logs_for_device_group_with_http_info(self, device_group_name, **kwargs):  # noqa: E501
        """Logs for the given device-group.  # noqa: E501

        Get the logs for all the services for the given {device_group_name}  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.retrieve_logs_for_device_group_with_http_info(device_group_name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str device_group_name: Device group name (required)
        :param str x_iam_token: authentication header object
        :param bool download: Download the logs
        :param str filename: Name of the log file
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['device_group_name', 'x_iam_token', 'download', 'filename']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method retrieve_logs_for_device_group" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'device_group_name' is set
        if ('device_group_name' not in params or
                params['device_group_name'] is None):
            raise ValueError("Missing the required parameter `device_group_name` when calling `retrieve_logs_for_device_group`")  # noqa: E501

        if ('filename' in params and
                len(params['filename']) > 64):
            raise ValueError("Invalid value for parameter `filename` when calling `retrieve_logs_for_device_group`, length must be less than or equal to `64`")  # noqa: E501
        if 'filename' in params and not re.search(r'^[a-zA-Z][a-zA-Z0-9_-]*$', params['filename']):  # noqa: E501
            raise ValueError("Invalid value for parameter `filename` when calling `retrieve_logs_for_device_group`, must conform to the pattern `/^[a-zA-Z][a-zA-Z0-9_-]*$/`")  # noqa: E501
        collection_formats = {}

        path_params = {}
        if 'device_group_name' in params:
            path_params['device_group_name'] = params['device_group_name']  # noqa: E501

        query_params = []
        if 'download' in params:
            query_params.append(('download', params['download']))  # noqa: E501
        if 'filename' in params:
            query_params.append(('filename', params['filename']))  # noqa: E501

        header_params = {}
        if 'x_iam_token' in params:
            header_params['x-iam-token'] = params['x_iam_token']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/gzip', 'application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json', 'multipart/form-data'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/logs/device-group/{device_group_name}/', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def retrieve_logs_for_device_group_service(self, device_group_name, service_name, **kwargs):  # noqa: E501
        """Get the logs for the given service running for the given device-group.  # noqa: E501

        Get the logs for the service {service_name} for the given {device_group_name}  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.retrieve_logs_for_device_group_service(device_group_name, service_name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str device_group_name: Device group name (required)
        :param str service_name: Device-group service name (required)
        :param str x_iam_token: authentication header object
        :param bool download: Download the logs
        :param str filename: Name of the log file
        :param int number_of_lines: Number of lines to show from the end of the logs
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.retrieve_logs_for_device_group_service_with_http_info(device_group_name, service_name, **kwargs)  # noqa: E501
        else:
            (data) = self.retrieve_logs_for_device_group_service_with_http_info(device_group_name, service_name, **kwargs)  # noqa: E501
            return data

    def retrieve_logs_for_device_group_service_with_http_info(self, device_group_name, service_name, **kwargs):  # noqa: E501
        """Get the logs for the given service running for the given device-group.  # noqa: E501

        Get the logs for the service {service_name} for the given {device_group_name}  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.retrieve_logs_for_device_group_service_with_http_info(device_group_name, service_name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str device_group_name: Device group name (required)
        :param str service_name: Device-group service name (required)
        :param str x_iam_token: authentication header object
        :param bool download: Download the logs
        :param str filename: Name of the log file
        :param int number_of_lines: Number of lines to show from the end of the logs
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['device_group_name', 'service_name', 'x_iam_token', 'download', 'filename', 'number_of_lines']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method retrieve_logs_for_device_group_service" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'device_group_name' is set
        if ('device_group_name' not in params or
                params['device_group_name'] is None):
            raise ValueError("Missing the required parameter `device_group_name` when calling `retrieve_logs_for_device_group_service`")  # noqa: E501
        # verify the required parameter 'service_name' is set
        if ('service_name' not in params or
                params['service_name'] is None):
            raise ValueError("Missing the required parameter `service_name` when calling `retrieve_logs_for_device_group_service`")  # noqa: E501

        if ('filename' in params and
                len(params['filename']) > 64):
            raise ValueError("Invalid value for parameter `filename` when calling `retrieve_logs_for_device_group_service`, length must be less than or equal to `64`")  # noqa: E501
        if 'filename' in params and not re.search(r'^[a-zA-Z][a-zA-Z0-9_-]*$', params['filename']):  # noqa: E501
            raise ValueError("Invalid value for parameter `filename` when calling `retrieve_logs_for_device_group_service`, must conform to the pattern `/^[a-zA-Z][a-zA-Z0-9_-]*$/`")  # noqa: E501
        if 'number_of_lines' in params and params['number_of_lines'] > 100000:  # noqa: E501
            raise ValueError("Invalid value for parameter `number_of_lines` when calling `retrieve_logs_for_device_group_service`, must be a value less than or equal to `100000`")  # noqa: E501
        if 'number_of_lines' in params and params['number_of_lines'] < 1:  # noqa: E501
            raise ValueError("Invalid value for parameter `number_of_lines` when calling `retrieve_logs_for_device_group_service`, must be a value greater than or equal to `1`")  # noqa: E501
        collection_formats = {}

        path_params = {}
        if 'device_group_name' in params:
            path_params['device_group_name'] = params['device_group_name']  # noqa: E501
        if 'service_name' in params:
            path_params['service_name'] = params['service_name']  # noqa: E501

        query_params = []
        if 'download' in params:
            query_params.append(('download', params['download']))  # noqa: E501
        if 'filename' in params:
            query_params.append(('filename', params['filename']))  # noqa: E501
        if 'number_of_lines' in params:
            query_params.append(('number_of_lines', params['number_of_lines']))  # noqa: E501

        header_params = {}
        if 'x_iam_token' in params:
            header_params['x-iam-token'] = params['x_iam_token']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/gzip', 'application/json', 'text/plain'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json', 'multipart/form-data'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/logs/device-group/{device_group_name}/service/{service_name}/', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def retrieve_logs_for_network_group(self, network_group_name, **kwargs):  # noqa: E501
        """Logs for the given network group.  # noqa: E501

        Get the logs for the service {service_name} for the given {network_group_name}  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.retrieve_logs_for_network_group(network_group_name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str network_group_name: Network group name (required)
        :param str x_iam_token: authentication header object
        :param bool download: Download the logs
        :param str filename: Name of the log file
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.retrieve_logs_for_network_group_with_http_info(network_group_name, **kwargs)  # noqa: E501
        else:
            (data) = self.retrieve_logs_for_network_group_with_http_info(network_group_name, **kwargs)  # noqa: E501
            return data

    def retrieve_logs_for_network_group_with_http_info(self, network_group_name, **kwargs):  # noqa: E501
        """Logs for the given network group.  # noqa: E501

        Get the logs for the service {service_name} for the given {network_group_name}  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.retrieve_logs_for_network_group_with_http_info(network_group_name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str network_group_name: Network group name (required)
        :param str x_iam_token: authentication header object
        :param bool download: Download the logs
        :param str filename: Name of the log file
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['network_group_name', 'x_iam_token', 'download', 'filename']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method retrieve_logs_for_network_group" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'network_group_name' is set
        if ('network_group_name' not in params or
                params['network_group_name'] is None):
            raise ValueError("Missing the required parameter `network_group_name` when calling `retrieve_logs_for_network_group`")  # noqa: E501

        if ('filename' in params and
                len(params['filename']) > 64):
            raise ValueError("Invalid value for parameter `filename` when calling `retrieve_logs_for_network_group`, length must be less than or equal to `64`")  # noqa: E501
        if 'filename' in params and not re.search(r'^[a-zA-Z][a-zA-Z0-9_-]*$', params['filename']):  # noqa: E501
            raise ValueError("Invalid value for parameter `filename` when calling `retrieve_logs_for_network_group`, must conform to the pattern `/^[a-zA-Z][a-zA-Z0-9_-]*$/`")  # noqa: E501
        collection_formats = {}

        path_params = {}
        if 'network_group_name' in params:
            path_params['network_group_name'] = params['network_group_name']  # noqa: E501

        query_params = []
        if 'download' in params:
            query_params.append(('download', params['download']))  # noqa: E501
        if 'filename' in params:
            query_params.append(('filename', params['filename']))  # noqa: E501

        header_params = {}
        if 'x_iam_token' in params:
            header_params['x-iam-token'] = params['x_iam_token']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/gzip', 'application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json', 'multipart/form-data'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/logs/network-group/{network_group_name}/', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def retrieve_logs_for_network_group_service(self, network_group_name, service_name, **kwargs):  # noqa: E501
        """Get the logs for the given service running for the given network-group.  # noqa: E501

        Get the logs for all the services for the given {network_group_name}  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.retrieve_logs_for_network_group_service(network_group_name, service_name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str network_group_name: Network group name (required)
        :param str service_name: Network group service name (required)
        :param str x_iam_token: authentication header object
        :param bool download: Download the logs
        :param str filename: Name of the log file
        :param int number_of_lines: Number of lines to show from the end of the logs
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.retrieve_logs_for_network_group_service_with_http_info(network_group_name, service_name, **kwargs)  # noqa: E501
        else:
            (data) = self.retrieve_logs_for_network_group_service_with_http_info(network_group_name, service_name, **kwargs)  # noqa: E501
            return data

    def retrieve_logs_for_network_group_service_with_http_info(self, network_group_name, service_name, **kwargs):  # noqa: E501
        """Get the logs for the given service running for the given network-group.  # noqa: E501

        Get the logs for all the services for the given {network_group_name}  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.retrieve_logs_for_network_group_service_with_http_info(network_group_name, service_name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str network_group_name: Network group name (required)
        :param str service_name: Network group service name (required)
        :param str x_iam_token: authentication header object
        :param bool download: Download the logs
        :param str filename: Name of the log file
        :param int number_of_lines: Number of lines to show from the end of the logs
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['network_group_name', 'service_name', 'x_iam_token', 'download', 'filename', 'number_of_lines']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method retrieve_logs_for_network_group_service" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'network_group_name' is set
        if ('network_group_name' not in params or
                params['network_group_name'] is None):
            raise ValueError("Missing the required parameter `network_group_name` when calling `retrieve_logs_for_network_group_service`")  # noqa: E501
        # verify the required parameter 'service_name' is set
        if ('service_name' not in params or
                params['service_name'] is None):
            raise ValueError("Missing the required parameter `service_name` when calling `retrieve_logs_for_network_group_service`")  # noqa: E501

        if ('filename' in params and
                len(params['filename']) > 64):
            raise ValueError("Invalid value for parameter `filename` when calling `retrieve_logs_for_network_group_service`, length must be less than or equal to `64`")  # noqa: E501
        if 'filename' in params and not re.search(r'^[a-zA-Z][a-zA-Z0-9_-]*$', params['filename']):  # noqa: E501
            raise ValueError("Invalid value for parameter `filename` when calling `retrieve_logs_for_network_group_service`, must conform to the pattern `/^[a-zA-Z][a-zA-Z0-9_-]*$/`")  # noqa: E501
        if 'number_of_lines' in params and params['number_of_lines'] > 100000:  # noqa: E501
            raise ValueError("Invalid value for parameter `number_of_lines` when calling `retrieve_logs_for_network_group_service`, must be a value less than or equal to `100000`")  # noqa: E501
        if 'number_of_lines' in params and params['number_of_lines'] < 1:  # noqa: E501
            raise ValueError("Invalid value for parameter `number_of_lines` when calling `retrieve_logs_for_network_group_service`, must be a value greater than or equal to `1`")  # noqa: E501
        collection_formats = {}

        path_params = {}
        if 'network_group_name' in params:
            path_params['network_group_name'] = params['network_group_name']  # noqa: E501
        if 'service_name' in params:
            path_params['service_name'] = params['service_name']  # noqa: E501

        query_params = []
        if 'download' in params:
            query_params.append(('download', params['download']))  # noqa: E501
        if 'filename' in params:
            query_params.append(('filename', params['filename']))  # noqa: E501
        if 'number_of_lines' in params:
            query_params.append(('number_of_lines', params['number_of_lines']))  # noqa: E501

        header_params = {}
        if 'x_iam_token' in params:
            header_params['x-iam-token'] = params['x_iam_token']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/gzip', 'application/json', 'text/plain'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json', 'multipart/form-data'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/logs/network-group/{network_group_name}/service/{service_name}/', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
