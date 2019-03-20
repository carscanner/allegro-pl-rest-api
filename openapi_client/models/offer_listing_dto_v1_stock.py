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


class OfferListingDtoV1Stock(object):
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
        'available': 'int',
        'sold': 'int'
    }

    attribute_map = {
        'available': 'available',
        'sold': 'sold'
    }

    def __init__(self, available=None, sold=None):  # noqa: E501
        """OfferListingDtoV1Stock - a model defined in OpenAPI"""  # noqa: E501

        self._available = None
        self._sold = None
        self.discriminator = None

        if available is not None:
            self.available = available
        if sold is not None:
            self.sold = sold

    @property
    def available(self):
        """Gets the available of this OfferListingDtoV1Stock.  # noqa: E501


        :return: The available of this OfferListingDtoV1Stock.  # noqa: E501
        :rtype: int
        """
        return self._available

    @available.setter
    def available(self, available):
        """Sets the available of this OfferListingDtoV1Stock.


        :param available: The available of this OfferListingDtoV1Stock.  # noqa: E501
        :type: int
        """

        self._available = available

    @property
    def sold(self):
        """Gets the sold of this OfferListingDtoV1Stock.  # noqa: E501


        :return: The sold of this OfferListingDtoV1Stock.  # noqa: E501
        :rtype: int
        """
        return self._sold

    @sold.setter
    def sold(self, sold):
        """Sets the sold of this OfferListingDtoV1Stock.


        :param sold: The sold of this OfferListingDtoV1Stock.  # noqa: E501
        :type: int
        """

        self._sold = sold

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
        if not isinstance(other, OfferListingDtoV1Stock):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
