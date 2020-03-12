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


class ChangePriceInput(object):
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
        'buy_now_price': 'Price'
    }

    attribute_map = {
        'buy_now_price': 'buyNowPrice'
    }

    def __init__(self, buy_now_price=None, local_vars_configuration=None):  # noqa: E501
        """ChangePriceInput - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._buy_now_price = None
        self.discriminator = None

        self.buy_now_price = buy_now_price

    @property
    def buy_now_price(self):
        """Gets the buy_now_price of this ChangePriceInput.  # noqa: E501


        :return: The buy_now_price of this ChangePriceInput.  # noqa: E501
        :rtype: Price
        """
        return self._buy_now_price

    @buy_now_price.setter
    def buy_now_price(self, buy_now_price):
        """Sets the buy_now_price of this ChangePriceInput.


        :param buy_now_price: The buy_now_price of this ChangePriceInput.  # noqa: E501
        :type: Price
        """
        if self.local_vars_configuration.client_side_validation and buy_now_price is None:  # noqa: E501
            raise ValueError("Invalid value for `buy_now_price`, must not be `None`")  # noqa: E501

        self._buy_now_price = buy_now_price

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
        if not isinstance(other, ChangePriceInput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ChangePriceInput):
            return True

        return self.to_dict() != other.to_dict()
