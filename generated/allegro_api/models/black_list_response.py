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


class BlackListResponse(object):
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
        'user': 'BlacklistUser',
        'note': 'str',
        'created_at': 'datetime'
    }

    attribute_map = {
        'user': 'user',
        'note': 'note',
        'created_at': 'createdAt'
    }

    def __init__(self, user=None, note=None, created_at=None, local_vars_configuration=None):  # noqa: E501
        """BlackListResponse - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._user = None
        self._note = None
        self._created_at = None
        self.discriminator = None

        if user is not None:
            self.user = user
        if note is not None:
            self.note = note
        if created_at is not None:
            self.created_at = created_at

    @property
    def user(self):
        """Gets the user of this BlackListResponse.  # noqa: E501


        :return: The user of this BlackListResponse.  # noqa: E501
        :rtype: BlacklistUser
        """
        return self._user

    @user.setter
    def user(self, user):
        """Sets the user of this BlackListResponse.


        :param user: The user of this BlackListResponse.  # noqa: E501
        :type: BlacklistUser
        """

        self._user = user

    @property
    def note(self):
        """Gets the note of this BlackListResponse.  # noqa: E501

        Note about reason of blacklisting.  # noqa: E501

        :return: The note of this BlackListResponse.  # noqa: E501
        :rtype: str
        """
        return self._note

    @note.setter
    def note(self, note):
        """Sets the note of this BlackListResponse.

        Note about reason of blacklisting.  # noqa: E501

        :param note: The note of this BlackListResponse.  # noqa: E501
        :type: str
        """

        self._note = note

    @property
    def created_at(self):
        """Gets the created_at of this BlackListResponse.  # noqa: E501

        Date and time of the creation in ISO 8601 format.  # noqa: E501

        :return: The created_at of this BlackListResponse.  # noqa: E501
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this BlackListResponse.

        Date and time of the creation in ISO 8601 format.  # noqa: E501

        :param created_at: The created_at of this BlackListResponse.  # noqa: E501
        :type: datetime
        """

        self._created_at = created_at

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
        if not isinstance(other, BlackListResponse):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, BlackListResponse):
            return True

        return self.to_dict() != other.to_dict()
