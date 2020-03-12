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


class SellingMode(object):
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
        'format': 'SellingModeFormat',
        'price': 'BuyNowPrice',
        'minimal_price': 'MinimalPrice',
        'starting_price': 'StartingPrice'
    }

    attribute_map = {
        'format': 'format',
        'price': 'price',
        'minimal_price': 'minimalPrice',
        'starting_price': 'startingPrice'
    }

    def __init__(self, format=None, price=None, minimal_price=None, starting_price=None, local_vars_configuration=None):  # noqa: E501
        """SellingMode - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._format = None
        self._price = None
        self._minimal_price = None
        self._starting_price = None
        self.discriminator = None

        if format is not None:
            self.format = format
        if price is not None:
            self.price = price
        if minimal_price is not None:
            self.minimal_price = minimal_price
        if starting_price is not None:
            self.starting_price = starting_price

    @property
    def format(self):
        """Gets the format of this SellingMode.  # noqa: E501


        :return: The format of this SellingMode.  # noqa: E501
        :rtype: SellingModeFormat
        """
        return self._format

    @format.setter
    def format(self, format):
        """Sets the format of this SellingMode.


        :param format: The format of this SellingMode.  # noqa: E501
        :type: SellingModeFormat
        """

        self._format = format

    @property
    def price(self):
        """Gets the price of this SellingMode.  # noqa: E501


        :return: The price of this SellingMode.  # noqa: E501
        :rtype: BuyNowPrice
        """
        return self._price

    @price.setter
    def price(self, price):
        """Sets the price of this SellingMode.


        :param price: The price of this SellingMode.  # noqa: E501
        :type: BuyNowPrice
        """

        self._price = price

    @property
    def minimal_price(self):
        """Gets the minimal_price of this SellingMode.  # noqa: E501


        :return: The minimal_price of this SellingMode.  # noqa: E501
        :rtype: MinimalPrice
        """
        return self._minimal_price

    @minimal_price.setter
    def minimal_price(self, minimal_price):
        """Sets the minimal_price of this SellingMode.


        :param minimal_price: The minimal_price of this SellingMode.  # noqa: E501
        :type: MinimalPrice
        """

        self._minimal_price = minimal_price

    @property
    def starting_price(self):
        """Gets the starting_price of this SellingMode.  # noqa: E501


        :return: The starting_price of this SellingMode.  # noqa: E501
        :rtype: StartingPrice
        """
        return self._starting_price

    @starting_price.setter
    def starting_price(self, starting_price):
        """Sets the starting_price of this SellingMode.


        :param starting_price: The starting_price of this SellingMode.  # noqa: E501
        :type: StartingPrice
        """

        self._starting_price = starting_price

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
        if not isinstance(other, SellingMode):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, SellingMode):
            return True

        return self.to_dict() != other.to_dict()
