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


class ListingResponseSearchMeta(object):
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
        'available_count': 'int',
        'total_count': 'int',
        'fallback': 'bool'
    }

    attribute_map = {
        'available_count': 'availableCount',
        'total_count': 'totalCount',
        'fallback': 'fallback'
    }

    def __init__(self, available_count=None, total_count=None, fallback=None, local_vars_configuration=None):  # noqa: E501
        """ListingResponseSearchMeta - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._available_count = None
        self._total_count = None
        self._fallback = None
        self.discriminator = None

        if available_count is not None:
            self.available_count = available_count
        if total_count is not None:
            self.total_count = total_count
        if fallback is not None:
            self.fallback = fallback

    @property
    def available_count(self):
        """Gets the available_count of this ListingResponseSearchMeta.  # noqa: E501

        The number of results available for navigation. If this number is less than total count, the search criteria (categories, filters, etc.) should be narrowed down to make all results available.  # noqa: E501

        :return: The available_count of this ListingResponseSearchMeta.  # noqa: E501
        :rtype: int
        """
        return self._available_count

    @available_count.setter
    def available_count(self, available_count):
        """Sets the available_count of this ListingResponseSearchMeta.

        The number of results available for navigation. If this number is less than total count, the search criteria (categories, filters, etc.) should be narrowed down to make all results available.  # noqa: E501

        :param available_count: The available_count of this ListingResponseSearchMeta.  # noqa: E501
        :type: int
        """

        self._available_count = available_count

    @property
    def total_count(self):
        """Gets the total_count of this ListingResponseSearchMeta.  # noqa: E501

        The total number of search results with given parameters.  # noqa: E501

        :return: The total_count of this ListingResponseSearchMeta.  # noqa: E501
        :rtype: int
        """
        return self._total_count

    @total_count.setter
    def total_count(self, total_count):
        """Sets the total_count of this ListingResponseSearchMeta.

        The total number of search results with given parameters.  # noqa: E501

        :param total_count: The total_count of this ListingResponseSearchMeta.  # noqa: E501
        :type: int
        """

        self._total_count = total_count

    @property
    def fallback(self):
        """Gets the fallback of this ListingResponseSearchMeta.  # noqa: E501

        Indicates whether the search fallback was used. If true, no items matching exact given phrase were found and related items are presented.  # noqa: E501

        :return: The fallback of this ListingResponseSearchMeta.  # noqa: E501
        :rtype: bool
        """
        return self._fallback

    @fallback.setter
    def fallback(self, fallback):
        """Sets the fallback of this ListingResponseSearchMeta.

        Indicates whether the search fallback was used. If true, no items matching exact given phrase were found and related items are presented.  # noqa: E501

        :param fallback: The fallback of this ListingResponseSearchMeta.  # noqa: E501
        :type: bool
        """

        self._fallback = fallback

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
        if not isinstance(other, ListingResponseSearchMeta):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ListingResponseSearchMeta):
            return True

        return self.to_dict() != other.to_dict()