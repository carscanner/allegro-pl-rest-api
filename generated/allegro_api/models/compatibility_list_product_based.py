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


class CompatibilityListProductBased(object):
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
        'id': 'str',
        'items': 'list[CompatibilityListItemProductBased]'
    }

    attribute_map = {
        'id': 'id',
        'items': 'items'
    }

    def __init__(self, id=None, items=None, local_vars_configuration=None):  # noqa: E501
        """CompatibilityListProductBased - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._items = None
        self.discriminator = None

        self.id = id
        if items is not None:
            self.items = items

    @property
    def id(self):
        """Gets the id of this CompatibilityListProductBased.  # noqa: E501

        Id of product-based compatibility list.  # noqa: E501

        :return: The id of this CompatibilityListProductBased.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this CompatibilityListProductBased.

        Id of product-based compatibility list.  # noqa: E501

        :param id: The id of this CompatibilityListProductBased.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and id is None:  # noqa: E501
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def items(self):
        """Gets the items of this CompatibilityListProductBased.  # noqa: E501

        Text representation of the compatibility list items. Provided for informational purposes only - ignored when creating (Post) or updating (Put) compatibility list in the offer.  # noqa: E501

        :return: The items of this CompatibilityListProductBased.  # noqa: E501
        :rtype: list[CompatibilityListItemProductBased]
        """
        return self._items

    @items.setter
    def items(self, items):
        """Sets the items of this CompatibilityListProductBased.

        Text representation of the compatibility list items. Provided for informational purposes only - ignored when creating (Post) or updating (Put) compatibility list in the offer.  # noqa: E501

        :param items: The items of this CompatibilityListProductBased.  # noqa: E501
        :type: list[CompatibilityListItemProductBased]
        """

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
        if not isinstance(other, CompatibilityListProductBased):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CompatibilityListProductBased):
            return True

        return self.to_dict() != other.to_dict()
