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


class OfferPromotion(object):
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
        'emphasized': 'bool',
        'bold': 'bool',
        'highlight': 'bool'
    }

    attribute_map = {
        'emphasized': 'emphasized',
        'bold': 'bold',
        'highlight': 'highlight'
    }

    def __init__(self, emphasized=None, bold=None, highlight=None, local_vars_configuration=None):  # noqa: E501
        """OfferPromotion - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._emphasized = None
        self._bold = None
        self._highlight = None
        self.discriminator = None

        if emphasized is not None:
            self.emphasized = emphasized
        if bold is not None:
            self.bold = bold
        if highlight is not None:
            self.highlight = highlight

    @property
    def emphasized(self):
        """Gets the emphasized of this OfferPromotion.  # noqa: E501

        Indicates whether the offer is promoted.  # noqa: E501

        :return: The emphasized of this OfferPromotion.  # noqa: E501
        :rtype: bool
        """
        return self._emphasized

    @emphasized.setter
    def emphasized(self, emphasized):
        """Sets the emphasized of this OfferPromotion.

        Indicates whether the offer is promoted.  # noqa: E501

        :param emphasized: The emphasized of this OfferPromotion.  # noqa: E501
        :type: bool
        """

        self._emphasized = emphasized

    @property
    def bold(self):
        """Gets the bold of this OfferPromotion.  # noqa: E501

        Indicates whether the offer has bold title option.  # noqa: E501

        :return: The bold of this OfferPromotion.  # noqa: E501
        :rtype: bool
        """
        return self._bold

    @bold.setter
    def bold(self, bold):
        """Sets the bold of this OfferPromotion.

        Indicates whether the offer has bold title option.  # noqa: E501

        :param bold: The bold of this OfferPromotion.  # noqa: E501
        :type: bool
        """

        self._bold = bold

    @property
    def highlight(self):
        """Gets the highlight of this OfferPromotion.  # noqa: E501

        Indicates whether the offer has highlight option.  # noqa: E501

        :return: The highlight of this OfferPromotion.  # noqa: E501
        :rtype: bool
        """
        return self._highlight

    @highlight.setter
    def highlight(self, highlight):
        """Sets the highlight of this OfferPromotion.

        Indicates whether the offer has highlight option.  # noqa: E501

        :param highlight: The highlight of this OfferPromotion.  # noqa: E501
        :type: bool
        """

        self._highlight = highlight

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
        if not isinstance(other, OfferPromotion):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, OfferPromotion):
            return True

        return self.to_dict() != other.to_dict()
