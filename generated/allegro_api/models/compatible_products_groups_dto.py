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


class CompatibleProductsGroupsDto(object):
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
        'groups': 'list[CompatibleProductsGroupsDtoGroups]',
        'count': 'int',
        'total_count': 'int'
    }

    attribute_map = {
        'groups': 'groups',
        'count': 'count',
        'total_count': 'totalCount'
    }

    def __init__(self, groups=None, count=None, total_count=None, local_vars_configuration=None):  # noqa: E501
        """CompatibleProductsGroupsDto - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._groups = None
        self._count = None
        self._total_count = None
        self.discriminator = None

        if groups is not None:
            self.groups = groups
        if count is not None:
            self.count = count
        if total_count is not None:
            self.total_count = total_count

    @property
    def groups(self):
        """Gets the groups of this CompatibleProductsGroupsDto.  # noqa: E501

        List of groups for given type of compatible products.  # noqa: E501

        :return: The groups of this CompatibleProductsGroupsDto.  # noqa: E501
        :rtype: list[CompatibleProductsGroupsDtoGroups]
        """
        return self._groups

    @groups.setter
    def groups(self, groups):
        """Sets the groups of this CompatibleProductsGroupsDto.

        List of groups for given type of compatible products.  # noqa: E501

        :param groups: The groups of this CompatibleProductsGroupsDto.  # noqa: E501
        :type: list[CompatibleProductsGroupsDtoGroups]
        """

        self._groups = groups

    @property
    def count(self):
        """Gets the count of this CompatibleProductsGroupsDto.  # noqa: E501

        Number of returned elements.  # noqa: E501

        :return: The count of this CompatibleProductsGroupsDto.  # noqa: E501
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        """Sets the count of this CompatibleProductsGroupsDto.

        Number of returned elements.  # noqa: E501

        :param count: The count of this CompatibleProductsGroupsDto.  # noqa: E501
        :type: int
        """

        self._count = count

    @property
    def total_count(self):
        """Gets the total_count of this CompatibleProductsGroupsDto.  # noqa: E501

        Total number of available elements.  # noqa: E501

        :return: The total_count of this CompatibleProductsGroupsDto.  # noqa: E501
        :rtype: int
        """
        return self._total_count

    @total_count.setter
    def total_count(self, total_count):
        """Sets the total_count of this CompatibleProductsGroupsDto.

        Total number of available elements.  # noqa: E501

        :param total_count: The total_count of this CompatibleProductsGroupsDto.  # noqa: E501
        :type: int
        """

        self._total_count = total_count

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
        if not isinstance(other, CompatibleProductsGroupsDto):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CompatibleProductsGroupsDto):
            return True

        return self.to_dict() != other.to_dict()
