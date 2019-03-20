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


class CheckoutFormDiscount(object):
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
        'type': 'str'
    }

    attribute_map = {
        'type': 'type'
    }

    def __init__(self, type=None):  # noqa: E501
        """CheckoutFormDiscount - a model defined in OpenAPI"""  # noqa: E501

        self._type = None
        self.discriminator = None

        self.type = type

    @property
    def type(self):
        """Gets the type of this CheckoutFormDiscount.  # noqa: E501

        Describes type of discount used in checkout form. The types of discounts can be as follows: * `COUPON` - coupon was used during payment * `BUNDLE` - some of the line items were bought as a bundle * `MULTIPACK` - at least one line item was bought with multipack option * `CROSSMULTIPACK` - some of line items each from different offers were bought together as multipack   # noqa: E501

        :return: The type of this CheckoutFormDiscount.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this CheckoutFormDiscount.

        Describes type of discount used in checkout form. The types of discounts can be as follows: * `COUPON` - coupon was used during payment * `BUNDLE` - some of the line items were bought as a bundle * `MULTIPACK` - at least one line item was bought with multipack option * `CROSSMULTIPACK` - some of line items each from different offers were bought together as multipack   # noqa: E501

        :param type: The type of this CheckoutFormDiscount.  # noqa: E501
        :type: str
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501
        allowed_values = ["COUPON", "BUNDLE", "MULTIPACK", "CROSSMULTIPACK"]  # noqa: E501
        if type not in allowed_values:
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"  # noqa: E501
                .format(type, allowed_values)
            )

        self._type = type

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
        if not isinstance(other, CheckoutFormDiscount):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
