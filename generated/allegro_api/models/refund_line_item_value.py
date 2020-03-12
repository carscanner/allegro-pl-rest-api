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


class RefundLineItemValue(object):
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
        'amount': 'str',
        'currency': 'str'
    }

    attribute_map = {
        'amount': 'amount',
        'currency': 'currency'
    }

    def __init__(self, amount=None, currency=None, local_vars_configuration=None):  # noqa: E501
        """RefundLineItemValue - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._amount = None
        self._currency = None
        self.discriminator = None

        self.amount = amount
        self.currency = currency

    @property
    def amount(self):
        """Gets the amount of this RefundLineItemValue.  # noqa: E501

        The amount provided in a string format to avoid rounding errors.  # noqa: E501

        :return: The amount of this RefundLineItemValue.  # noqa: E501
        :rtype: str
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        """Sets the amount of this RefundLineItemValue.

        The amount provided in a string format to avoid rounding errors.  # noqa: E501

        :param amount: The amount of this RefundLineItemValue.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and amount is None:  # noqa: E501
            raise ValueError("Invalid value for `amount`, must not be `None`")  # noqa: E501

        self._amount = amount

    @property
    def currency(self):
        """Gets the currency of this RefundLineItemValue.  # noqa: E501

        The currency provided as a 3-letter code in accordance with ISO 4217 standard (https://en.wikipedia.org/wiki/ISO_4217).  # noqa: E501

        :return: The currency of this RefundLineItemValue.  # noqa: E501
        :rtype: str
        """
        return self._currency

    @currency.setter
    def currency(self, currency):
        """Sets the currency of this RefundLineItemValue.

        The currency provided as a 3-letter code in accordance with ISO 4217 standard (https://en.wikipedia.org/wiki/ISO_4217).  # noqa: E501

        :param currency: The currency of this RefundLineItemValue.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and currency is None:  # noqa: E501
            raise ValueError("Invalid value for `currency`, must not be `None`")  # noqa: E501

        self._currency = currency

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
        if not isinstance(other, RefundLineItemValue):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, RefundLineItemValue):
            return True

        return self.to_dict() != other.to_dict()
