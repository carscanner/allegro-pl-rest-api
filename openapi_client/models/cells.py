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


class Cells(object):
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
        'cells': 'list[str]'
    }

    attribute_map = {
        'cells': 'cells'
    }

    def __init__(self, cells=None):  # noqa: E501
        """Cells - a model defined in OpenAPI"""  # noqa: E501

        self._cells = None
        self.discriminator = None

        self.cells = cells

    @property
    def cells(self):
        """Gets the cells of this Cells.  # noqa: E501


        :return: The cells of this Cells.  # noqa: E501
        :rtype: list[str]
        """
        return self._cells

    @cells.setter
    def cells(self, cells):
        """Sets the cells of this Cells.


        :param cells: The cells of this Cells.  # noqa: E501
        :type: list[str]
        """
        if cells is None:
            raise ValueError("Invalid value for `cells`, must not be `None`")  # noqa: E501

        self._cells = cells

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
        if not isinstance(other, Cells):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
