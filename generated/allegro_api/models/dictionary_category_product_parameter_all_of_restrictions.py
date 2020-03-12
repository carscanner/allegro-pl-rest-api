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


class DictionaryCategoryProductParameterAllOfRestrictions(object):
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
        'multiple_choices': 'bool'
    }

    attribute_map = {
        'multiple_choices': 'multipleChoices'
    }

    def __init__(self, multiple_choices=None, local_vars_configuration=None):  # noqa: E501
        """DictionaryCategoryProductParameterAllOfRestrictions - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._multiple_choices = None
        self.discriminator = None

        if multiple_choices is not None:
            self.multiple_choices = multiple_choices

    @property
    def multiple_choices(self):
        """Gets the multiple_choices of this DictionaryCategoryProductParameterAllOfRestrictions.  # noqa: E501

        Indicates whether this parameter can have more than one value.  # noqa: E501

        :return: The multiple_choices of this DictionaryCategoryProductParameterAllOfRestrictions.  # noqa: E501
        :rtype: bool
        """
        return self._multiple_choices

    @multiple_choices.setter
    def multiple_choices(self, multiple_choices):
        """Sets the multiple_choices of this DictionaryCategoryProductParameterAllOfRestrictions.

        Indicates whether this parameter can have more than one value.  # noqa: E501

        :param multiple_choices: The multiple_choices of this DictionaryCategoryProductParameterAllOfRestrictions.  # noqa: E501
        :type: bool
        """

        self._multiple_choices = multiple_choices

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
        if not isinstance(other, DictionaryCategoryProductParameterAllOfRestrictions):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, DictionaryCategoryProductParameterAllOfRestrictions):
            return True

        return self.to_dict() != other.to_dict()
