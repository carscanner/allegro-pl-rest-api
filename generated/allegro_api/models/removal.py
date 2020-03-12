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


class Removal(object):
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
        'possible_to': 'datetime',
        'request': 'RemovalRequest'
    }

    attribute_map = {
        'possible_to': 'possibleTo',
        'request': 'request'
    }

    def __init__(self, possible_to=None, request=None, local_vars_configuration=None):  # noqa: E501
        """Removal - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._possible_to = None
        self._request = None
        self.discriminator = None

        self.possible_to = possible_to
        if request is not None:
            self.request = request

    @property
    def possible_to(self):
        """Gets the possible_to of this Removal.  # noqa: E501

        Date until a removal request can be submitted in ISO 8601 format  # noqa: E501

        :return: The possible_to of this Removal.  # noqa: E501
        :rtype: datetime
        """
        return self._possible_to

    @possible_to.setter
    def possible_to(self, possible_to):
        """Sets the possible_to of this Removal.

        Date until a removal request can be submitted in ISO 8601 format  # noqa: E501

        :param possible_to: The possible_to of this Removal.  # noqa: E501
        :type: datetime
        """
        if self.local_vars_configuration.client_side_validation and possible_to is None:  # noqa: E501
            raise ValueError("Invalid value for `possible_to`, must not be `None`")  # noqa: E501

        self._possible_to = possible_to

    @property
    def request(self):
        """Gets the request of this Removal.  # noqa: E501


        :return: The request of this Removal.  # noqa: E501
        :rtype: RemovalRequest
        """
        return self._request

    @request.setter
    def request(self, request):
        """Sets the request of this Removal.


        :param request: The request of this Removal.  # noqa: E501
        :type: RemovalRequest
        """

        self._request = request

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
        if not isinstance(other, Removal):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Removal):
            return True

        return self.to_dict() != other.to_dict()