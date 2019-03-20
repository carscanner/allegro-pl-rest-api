# coding: utf-8

"""
    Allegro REST API

    https://developer.allegro.pl/about  # noqa: E501

    OpenAPI spec version: latest
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six


class WarrantiesListWarrantyBasic(object):
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
        'count': 'int',
        'warranties': 'list[WarrantyBasic]'
    }

    attribute_map = {
        'count': 'count',
        'warranties': 'warranties'
    }

    def __init__(self, count=None, warranties=None):  # noqa: E501
        """WarrantiesListWarrantyBasic - a model defined in OpenAPI"""  # noqa: E501

        self._count = None
        self._warranties = None
        self.discriminator = None

        if count is not None:
            self.count = count
        if warranties is not None:
            self.warranties = warranties

    @property
    def count(self):
        """Gets the count of this WarrantiesListWarrantyBasic.  # noqa: E501


        :return: The count of this WarrantiesListWarrantyBasic.  # noqa: E501
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        """Sets the count of this WarrantiesListWarrantyBasic.


        :param count: The count of this WarrantiesListWarrantyBasic.  # noqa: E501
        :type: int
        """

        self._count = count

    @property
    def warranties(self):
        """Gets the warranties of this WarrantiesListWarrantyBasic.  # noqa: E501


        :return: The warranties of this WarrantiesListWarrantyBasic.  # noqa: E501
        :rtype: list[WarrantyBasic]
        """
        return self._warranties

    @warranties.setter
    def warranties(self, warranties):
        """Sets the warranties of this WarrantiesListWarrantyBasic.


        :param warranties: The warranties of this WarrantiesListWarrantyBasic.  # noqa: E501
        :type: list[WarrantyBasic]
        """

        self._warranties = warranties

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
        if not isinstance(other, WarrantiesListWarrantyBasic):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
