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


class ChangePriceWithoutOutput(object):
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
        'id': 'str',
        'input': 'ChangePriceInput'
    }

    attribute_map = {
        'id': 'id',
        'input': 'input'
    }

    def __init__(self, id=None, input=None, local_vars_configuration=None):  # noqa: E501
        """ChangePriceWithoutOutput - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._input = None
        self.discriminator = None

        if id is not None:
            self.id = id
        self.input = input

    @property
    def id(self):
        """Gets the id of this ChangePriceWithoutOutput.  # noqa: E501

        The unique command id generated by you. This should be the same UUID as used in the path.  # noqa: E501

        :return: The id of this ChangePriceWithoutOutput.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ChangePriceWithoutOutput.

        The unique command id generated by you. This should be the same UUID as used in the path.  # noqa: E501

        :param id: The id of this ChangePriceWithoutOutput.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def input(self):
        """Gets the input of this ChangePriceWithoutOutput.  # noqa: E501


        :return: The input of this ChangePriceWithoutOutput.  # noqa: E501
        :rtype: ChangePriceInput
        """
        return self._input

    @input.setter
    def input(self, input):
        """Sets the input of this ChangePriceWithoutOutput.


        :param input: The input of this ChangePriceWithoutOutput.  # noqa: E501
        :type: ChangePriceInput
        """
        if self.local_vars_configuration.client_side_validation and input is None:  # noqa: E501
            raise ValueError("Invalid value for `input`, must not be `None`")  # noqa: E501

        self._input = input

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
        if not isinstance(other, ChangePriceWithoutOutput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ChangePriceWithoutOutput):
            return True

        return self.to_dict() != other.to_dict()