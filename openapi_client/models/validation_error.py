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


class ValidationError(object):
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
        'code': 'str',
        'details': 'str',
        'message': 'str',
        'path': 'str',
        'user_message': 'str'
    }

    attribute_map = {
        'code': 'code',
        'details': 'details',
        'message': 'message',
        'path': 'path',
        'user_message': 'userMessage'
    }

    def __init__(self, code=None, details=None, message=None, path=None, user_message=None):  # noqa: E501
        """ValidationError - a model defined in OpenAPI"""  # noqa: E501

        self._code = None
        self._details = None
        self._message = None
        self._path = None
        self._user_message = None
        self.discriminator = None

        if code is not None:
            self.code = code
        if details is not None:
            self.details = details
        if message is not None:
            self.message = message
        if path is not None:
            self.path = path
        if user_message is not None:
            self.user_message = user_message

    @property
    def code(self):
        """Gets the code of this ValidationError.  # noqa: E501


        :return: The code of this ValidationError.  # noqa: E501
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code):
        """Sets the code of this ValidationError.


        :param code: The code of this ValidationError.  # noqa: E501
        :type: str
        """

        self._code = code

    @property
    def details(self):
        """Gets the details of this ValidationError.  # noqa: E501


        :return: The details of this ValidationError.  # noqa: E501
        :rtype: str
        """
        return self._details

    @details.setter
    def details(self, details):
        """Sets the details of this ValidationError.


        :param details: The details of this ValidationError.  # noqa: E501
        :type: str
        """

        self._details = details

    @property
    def message(self):
        """Gets the message of this ValidationError.  # noqa: E501


        :return: The message of this ValidationError.  # noqa: E501
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this ValidationError.


        :param message: The message of this ValidationError.  # noqa: E501
        :type: str
        """

        self._message = message

    @property
    def path(self):
        """Gets the path of this ValidationError.  # noqa: E501


        :return: The path of this ValidationError.  # noqa: E501
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        """Sets the path of this ValidationError.


        :param path: The path of this ValidationError.  # noqa: E501
        :type: str
        """

        self._path = path

    @property
    def user_message(self):
        """Gets the user_message of this ValidationError.  # noqa: E501


        :return: The user_message of this ValidationError.  # noqa: E501
        :rtype: str
        """
        return self._user_message

    @user_message.setter
    def user_message(self, user_message):
        """Sets the user_message of this ValidationError.


        :param user_message: The user_message of this ValidationError.  # noqa: E501
        :type: str
        """

        self._user_message = user_message

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
        if not isinstance(other, ValidationError):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
