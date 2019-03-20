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


class VariantSet(object):
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
        'offers': 'list[VariantSetOffer]',
        'name': 'str',
        'parameters': 'list[VariantSetParameter]'
    }

    attribute_map = {
        'offers': 'offers',
        'name': 'name',
        'parameters': 'parameters'
    }

    def __init__(self, offers=None, name=None, parameters=None):  # noqa: E501
        """VariantSet - a model defined in OpenAPI"""  # noqa: E501

        self._offers = None
        self._name = None
        self._parameters = None
        self.discriminator = None

        self.offers = offers
        self.name = name
        self.parameters = parameters

    @property
    def offers(self):
        """Gets the offers of this VariantSet.  # noqa: E501


        :return: The offers of this VariantSet.  # noqa: E501
        :rtype: list[VariantSetOffer]
        """
        return self._offers

    @offers.setter
    def offers(self, offers):
        """Sets the offers of this VariantSet.


        :param offers: The offers of this VariantSet.  # noqa: E501
        :type: list[VariantSetOffer]
        """
        if offers is None:
            raise ValueError("Invalid value for `offers`, must not be `None`")  # noqa: E501

        self._offers = offers

    @property
    def name(self):
        """Gets the name of this VariantSet.  # noqa: E501


        :return: The name of this VariantSet.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this VariantSet.


        :param name: The name of this VariantSet.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501
        if name is not None and len(name) > 50:
            raise ValueError("Invalid value for `name`, length must be less than or equal to `50`")  # noqa: E501

        self._name = name

    @property
    def parameters(self):
        """Gets the parameters of this VariantSet.  # noqa: E501


        :return: The parameters of this VariantSet.  # noqa: E501
        :rtype: list[VariantSetParameter]
        """
        return self._parameters

    @parameters.setter
    def parameters(self, parameters):
        """Sets the parameters of this VariantSet.


        :param parameters: The parameters of this VariantSet.  # noqa: E501
        :type: list[VariantSetParameter]
        """
        if parameters is None:
            raise ValueError("Invalid value for `parameters`, must not be `None`")  # noqa: E501

        self._parameters = parameters

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
        if not isinstance(other, VariantSet):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
