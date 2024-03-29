# coding: utf-8

"""
    Paragon Insights APIs

    API interface for PI application  # noqa: E501

    OpenAPI spec version: 4.0.0
    Contact: healthbot-feedback@juniper.net
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class DeviceSchemaVendorOthervendor(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'operating_system': 'str',
        'platform': 'str',
        'product': 'str',
        'release': 'str',
        'vendor_name': 'str'
    }

    attribute_map = {
        'operating_system': 'operating-system',
        'platform': 'platform',
        'product': 'product',
        'release': 'release',
        'vendor_name': 'vendor-name'
    }

    def __init__(self, operating_system=None, platform=None, product=None, release=None, vendor_name=None):  # noqa: E501
        """DeviceSchemaVendorOthervendor - a model defined in Swagger"""  # noqa: E501

        self._operating_system = None
        self._platform = None
        self._product = None
        self._release = None
        self._vendor_name = None
        self.discriminator = None

        if operating_system is not None:
            self.operating_system = operating_system
        if platform is not None:
            self.platform = platform
        if product is not None:
            self.product = product
        if release is not None:
            self.release = release
        self.vendor_name = vendor_name

    @property
    def operating_system(self):
        """Gets the operating_system of this DeviceSchemaVendorOthervendor.  # noqa: E501

        Vendor operating system, Should be of pattern [a-zA-Z][a-zA-Z0-9_-]*  # noqa: E501

        :return: The operating_system of this DeviceSchemaVendorOthervendor.  # noqa: E501
        :rtype: str
        """
        return self._operating_system

    @operating_system.setter
    def operating_system(self, operating_system):
        """Sets the operating_system of this DeviceSchemaVendorOthervendor.

        Vendor operating system, Should be of pattern [a-zA-Z][a-zA-Z0-9_-]*  # noqa: E501

        :param operating_system: The operating_system of this DeviceSchemaVendorOthervendor.  # noqa: E501
        :type: str
        """
        if operating_system is not None and len(operating_system) > 64:
            raise ValueError("Invalid value for `operating_system`, length must be less than or equal to `64`")  # noqa: E501
        if operating_system is not None and not re.search(r'^[a-zA-Z][a-zA-Z0-9_-]*$', operating_system):  # noqa: E501
            raise ValueError("Invalid value for `operating_system`, must be a follow pattern or equal to `/^[a-zA-Z][a-zA-Z0-9_-]*$/`")  # noqa: E501

        self._operating_system = operating_system

    @property
    def platform(self):
        """Gets the platform of this DeviceSchemaVendorOthervendor.  # noqa: E501

        Platform name of the device, Example: MX240  # noqa: E501

        :return: The platform of this DeviceSchemaVendorOthervendor.  # noqa: E501
        :rtype: str
        """
        return self._platform

    @platform.setter
    def platform(self, platform):
        """Sets the platform of this DeviceSchemaVendorOthervendor.

        Platform name of the device, Example: MX240  # noqa: E501

        :param platform: The platform of this DeviceSchemaVendorOthervendor.  # noqa: E501
        :type: str
        """
        if platform is not None and len(platform) > 64:
            raise ValueError("Invalid value for `platform`, length must be less than or equal to `64`")  # noqa: E501
        if platform is not None and len(platform) < 1:
            raise ValueError("Invalid value for `platform`, length must be greater than or equal to `1`")  # noqa: E501

        self._platform = platform

    @property
    def product(self):
        """Gets the product of this DeviceSchemaVendorOthervendor.  # noqa: E501

        Product category of the device, Example: MX  # noqa: E501

        :return: The product of this DeviceSchemaVendorOthervendor.  # noqa: E501
        :rtype: str
        """
        return self._product

    @product.setter
    def product(self, product):
        """Sets the product of this DeviceSchemaVendorOthervendor.

        Product category of the device, Example: MX  # noqa: E501

        :param product: The product of this DeviceSchemaVendorOthervendor.  # noqa: E501
        :type: str
        """
        if product is not None and len(product) > 64:
            raise ValueError("Invalid value for `product`, length must be less than or equal to `64`")  # noqa: E501
        if product is not None and len(product) < 1:
            raise ValueError("Invalid value for `product`, length must be greater than or equal to `1`")  # noqa: E501

        self._product = product

    @property
    def release(self):
        """Gets the release of this DeviceSchemaVendorOthervendor.  # noqa: E501

        Release string of the device, Example: 19.2R1  # noqa: E501

        :return: The release of this DeviceSchemaVendorOthervendor.  # noqa: E501
        :rtype: str
        """
        return self._release

    @release.setter
    def release(self, release):
        """Sets the release of this DeviceSchemaVendorOthervendor.

        Release string of the device, Example: 19.2R1  # noqa: E501

        :param release: The release of this DeviceSchemaVendorOthervendor.  # noqa: E501
        :type: str
        """
        if release is not None and len(release) > 64:
            raise ValueError("Invalid value for `release`, length must be less than or equal to `64`")  # noqa: E501
        if release is not None and len(release) < 1:
            raise ValueError("Invalid value for `release`, length must be greater than or equal to `1`")  # noqa: E501

        self._release = release

    @property
    def vendor_name(self):
        """Gets the vendor_name of this DeviceSchemaVendorOthervendor.  # noqa: E501

        Vendor-name, Should be of pattern [a-zA-Z][a-zA-Z0-9_-]*  # noqa: E501

        :return: The vendor_name of this DeviceSchemaVendorOthervendor.  # noqa: E501
        :rtype: str
        """
        return self._vendor_name

    @vendor_name.setter
    def vendor_name(self, vendor_name):
        """Sets the vendor_name of this DeviceSchemaVendorOthervendor.

        Vendor-name, Should be of pattern [a-zA-Z][a-zA-Z0-9_-]*  # noqa: E501

        :param vendor_name: The vendor_name of this DeviceSchemaVendorOthervendor.  # noqa: E501
        :type: str
        """
        if vendor_name is None:
            raise ValueError("Invalid value for `vendor_name`, must not be `None`")  # noqa: E501
        if vendor_name is not None and len(vendor_name) > 64:
            raise ValueError("Invalid value for `vendor_name`, length must be less than or equal to `64`")  # noqa: E501
        if vendor_name is not None and not re.search(r'^[a-zA-Z][a-zA-Z0-9_-]*$', vendor_name):  # noqa: E501
            raise ValueError("Invalid value for `vendor_name`, must be a follow pattern or equal to `/^[a-zA-Z][a-zA-Z0-9_-]*$/`")  # noqa: E501

        self._vendor_name = vendor_name

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(DeviceSchemaVendorOthervendor, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, DeviceSchemaVendorOthervendor):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
