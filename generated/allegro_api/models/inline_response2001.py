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


class InlineResponse2001(object):
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
        'delivery_methods': 'list[InlineResponse2001DeliveryMethods]'
    }

    attribute_map = {
        'delivery_methods': 'deliveryMethods'
    }

    def __init__(self, delivery_methods=None, local_vars_configuration=None):  # noqa: E501
        """InlineResponse2001 - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._delivery_methods = None
        self.discriminator = None

        if delivery_methods is not None:
            self.delivery_methods = delivery_methods

    @property
    def delivery_methods(self):
        """Gets the delivery_methods of this InlineResponse2001.  # noqa: E501


        :return: The delivery_methods of this InlineResponse2001.  # noqa: E501
        :rtype: list[InlineResponse2001DeliveryMethods]
        """
        return self._delivery_methods

    @delivery_methods.setter
    def delivery_methods(self, delivery_methods):
        """Sets the delivery_methods of this InlineResponse2001.


        :param delivery_methods: The delivery_methods of this InlineResponse2001.  # noqa: E501
        :type: list[InlineResponse2001DeliveryMethods]
        """

        self._delivery_methods = delivery_methods

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
        if not isinstance(other, InlineResponse2001):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, InlineResponse2001):
            return True

        return self.to_dict() != other.to_dict()
