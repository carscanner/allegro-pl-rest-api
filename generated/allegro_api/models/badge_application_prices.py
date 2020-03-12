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


class BadgeApplicationPrices(object):
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
        'market': 'BadgeApplicationMarketPrice',
        'bargain': 'BadgeApplicationBargainPrice'
    }

    attribute_map = {
        'market': 'market',
        'bargain': 'bargain'
    }

    def __init__(self, market=None, bargain=None, local_vars_configuration=None):  # noqa: E501
        """BadgeApplicationPrices - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._market = None
        self._bargain = None
        self.discriminator = None

        if market is not None:
            self.market = market
        if bargain is not None:
            self.bargain = bargain

    @property
    def market(self):
        """Gets the market of this BadgeApplicationPrices.  # noqa: E501


        :return: The market of this BadgeApplicationPrices.  # noqa: E501
        :rtype: BadgeApplicationMarketPrice
        """
        return self._market

    @market.setter
    def market(self, market):
        """Sets the market of this BadgeApplicationPrices.


        :param market: The market of this BadgeApplicationPrices.  # noqa: E501
        :type: BadgeApplicationMarketPrice
        """

        self._market = market

    @property
    def bargain(self):
        """Gets the bargain of this BadgeApplicationPrices.  # noqa: E501


        :return: The bargain of this BadgeApplicationPrices.  # noqa: E501
        :rtype: BadgeApplicationBargainPrice
        """
        return self._bargain

    @bargain.setter
    def bargain(self, bargain):
        """Sets the bargain of this BadgeApplicationPrices.


        :param bargain: The bargain of this BadgeApplicationPrices.  # noqa: E501
        :type: BadgeApplicationBargainPrice
        """

        self._bargain = bargain

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
        if not isinstance(other, BadgeApplicationPrices):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, BadgeApplicationPrices):
            return True

        return self.to_dict() != other.to_dict()
