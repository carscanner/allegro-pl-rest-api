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


class CompatibilityListManual(object):
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
        'items': 'list[CompatibilityListItem]'
    }

    attribute_map = {
        'items': 'items'
    }

    def __init__(self, items=None, local_vars_configuration=None):  # noqa: E501
        """CompatibilityListManual - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._items = None
        self.discriminator = None

        self.items = items

    @property
    def items(self):
        """Gets the items of this CompatibilityListManual.  # noqa: E501

        List of the compatible items. Maximum number of elements on the list depends on type of included compatible items. Configuration and details concerning the compatible items in selected category are provided in the response for GET <a href=\"/documentation/#tag/Compatibility-List/paths/~1sale~1compatibility-list~1supported-categories/get\"> supported-categories</a> resource in `validationRules` object.  # noqa: E501

        :return: The items of this CompatibilityListManual.  # noqa: E501
        :rtype: list[CompatibilityListItem]
        """
        return self._items

    @items.setter
    def items(self, items):
        """Sets the items of this CompatibilityListManual.

        List of the compatible items. Maximum number of elements on the list depends on type of included compatible items. Configuration and details concerning the compatible items in selected category are provided in the response for GET <a href=\"/documentation/#tag/Compatibility-List/paths/~1sale~1compatibility-list~1supported-categories/get\"> supported-categories</a> resource in `validationRules` object.  # noqa: E501

        :param items: The items of this CompatibilityListManual.  # noqa: E501
        :type: list[CompatibilityListItem]
        """
        if self.local_vars_configuration.client_side_validation and items is None:  # noqa: E501
            raise ValueError("Invalid value for `items`, must not be `None`")  # noqa: E501

        self._items = items

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
        if not isinstance(other, CompatibilityListManual):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CompatibilityListManual):
            return True

        return self.to_dict() != other.to_dict()
