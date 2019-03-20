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


class RemovalRequest(object):
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
        'created_at': 'datetime',
        'message': 'str'
    }

    attribute_map = {
        'created_at': 'createdAt',
        'message': 'message'
    }

    def __init__(self, created_at=None, message=None):  # noqa: E501
        """RemovalRequest - a model defined in OpenAPI"""  # noqa: E501

        self._created_at = None
        self._message = None
        self.discriminator = None

        self.created_at = created_at
        self.message = message

    @property
    def created_at(self):
        """Gets the created_at of this RemovalRequest.  # noqa: E501

        Removal request creation datetime in ISO 8601 format  # noqa: E501

        :return: The created_at of this RemovalRequest.  # noqa: E501
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this RemovalRequest.

        Removal request creation datetime in ISO 8601 format  # noqa: E501

        :param created_at: The created_at of this RemovalRequest.  # noqa: E501
        :type: datetime
        """
        if created_at is None:
            raise ValueError("Invalid value for `created_at`, must not be `None`")  # noqa: E501

        self._created_at = created_at

    @property
    def message(self):
        """Gets the message of this RemovalRequest.  # noqa: E501

        Message containing explanation for removing rating  # noqa: E501

        :return: The message of this RemovalRequest.  # noqa: E501
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this RemovalRequest.

        Message containing explanation for removing rating  # noqa: E501

        :param message: The message of this RemovalRequest.  # noqa: E501
        :type: str
        """
        if message is None:
            raise ValueError("Invalid value for `message`, must not be `None`")  # noqa: E501

        self._message = message

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
        if not isinstance(other, RemovalRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
