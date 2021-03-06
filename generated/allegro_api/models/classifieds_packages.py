# coding: utf-8

"""
    Allegro REST API

    https://developer.allegro.pl/about  # noqa: E501

    The version of the OpenAPI document: 2020.03.12
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from allegro_api.configuration import Configuration


class ClassifiedsPackages(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'base_package': 'ClassifiedPackage',
        'extra_packages': 'list[ClassifiedPackage]'
    }

    attribute_map = {
        'base_package': 'basePackage',
        'extra_packages': 'extraPackages'
    }

    def __init__(self, base_package=None, extra_packages=None, local_vars_configuration=None):  # noqa: E501
        """ClassifiedsPackages - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._base_package = None
        self._extra_packages = None
        self.discriminator = None

        if base_package is not None:
            self.base_package = base_package
        if extra_packages is not None:
            self.extra_packages = extra_packages

    @property
    def base_package(self):
        """Gets the base_package of this ClassifiedsPackages.  # noqa: E501


        :return: The base_package of this ClassifiedsPackages.  # noqa: E501
        :rtype: ClassifiedPackage
        """
        return self._base_package

    @base_package.setter
    def base_package(self, base_package):
        """Sets the base_package of this ClassifiedsPackages.


        :param base_package: The base_package of this ClassifiedsPackages.  # noqa: E501
        :type: ClassifiedPackage
        """

        self._base_package = base_package

    @property
    def extra_packages(self):
        """Gets the extra_packages of this ClassifiedsPackages.  # noqa: E501

        An array of extra packages.  # noqa: E501

        :return: The extra_packages of this ClassifiedsPackages.  # noqa: E501
        :rtype: list[ClassifiedPackage]
        """
        return self._extra_packages

    @extra_packages.setter
    def extra_packages(self, extra_packages):
        """Sets the extra_packages of this ClassifiedsPackages.

        An array of extra packages.  # noqa: E501

        :param extra_packages: The extra_packages of this ClassifiedsPackages.  # noqa: E501
        :type: list[ClassifiedPackage]
        """

        self._extra_packages = extra_packages

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
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

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ClassifiedsPackages):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ClassifiedsPackages):
            return True

        return self.to_dict() != other.to_dict()
