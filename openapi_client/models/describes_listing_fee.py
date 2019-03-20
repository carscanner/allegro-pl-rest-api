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


class DescribesListingFee(object):
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
        'fee': 'Fee',
        'name': 'str',
        'type': 'str',
        'cycle_duration': 'str'
    }

    attribute_map = {
        'fee': 'fee',
        'name': 'name',
        'type': 'type',
        'cycle_duration': 'cycleDuration'
    }

    def __init__(self, fee=None, name=None, type=None, cycle_duration=None):  # noqa: E501
        """DescribesListingFee - a model defined in OpenAPI"""  # noqa: E501

        self._fee = None
        self._name = None
        self._type = None
        self._cycle_duration = None
        self.discriminator = None

        self.fee = fee
        self.name = name
        self.type = type
        self.cycle_duration = cycle_duration

    @property
    def fee(self):
        """Gets the fee of this DescribesListingFee.  # noqa: E501


        :return: The fee of this DescribesListingFee.  # noqa: E501
        :rtype: Fee
        """
        return self._fee

    @fee.setter
    def fee(self, fee):
        """Sets the fee of this DescribesListingFee.


        :param fee: The fee of this DescribesListingFee.  # noqa: E501
        :type: Fee
        """
        if fee is None:
            raise ValueError("Invalid value for `fee`, must not be `None`")  # noqa: E501

        self._fee = fee

    @property
    def name(self):
        """Gets the name of this DescribesListingFee.  # noqa: E501


        :return: The name of this DescribesListingFee.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this DescribesListingFee.


        :param name: The name of this DescribesListingFee.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def type(self):
        """Gets the type of this DescribesListingFee.  # noqa: E501


        :return: The type of this DescribesListingFee.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this DescribesListingFee.


        :param type: The type of this DescribesListingFee.  # noqa: E501
        :type: str
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type

    @property
    def cycle_duration(self):
        """Gets the cycle_duration of this DescribesListingFee.  # noqa: E501

        Pricing cycle duration, ISO 8601 duration format  # noqa: E501

        :return: The cycle_duration of this DescribesListingFee.  # noqa: E501
        :rtype: str
        """
        return self._cycle_duration

    @cycle_duration.setter
    def cycle_duration(self, cycle_duration):
        """Sets the cycle_duration of this DescribesListingFee.

        Pricing cycle duration, ISO 8601 duration format  # noqa: E501

        :param cycle_duration: The cycle_duration of this DescribesListingFee.  # noqa: E501
        :type: str
        """
        if cycle_duration is None:
            raise ValueError("Invalid value for `cycle_duration`, must not be `None`")  # noqa: E501

        self._cycle_duration = cycle_duration

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
        if not isinstance(other, DescribesListingFee):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
