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


class ContactRequest(object):
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
        'name': 'str',
        'emails': 'list[EmailRequest]',
        'phones': 'list[PhonesRequest]'
    }

    attribute_map = {
        'name': 'name',
        'emails': 'emails',
        'phones': 'phones'
    }

    def __init__(self, name=None, emails=None, phones=None):  # noqa: E501
        """ContactRequest - a model defined in OpenAPI"""  # noqa: E501

        self._name = None
        self._emails = None
        self._phones = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if emails is not None:
            self.emails = emails
        if phones is not None:
            self.phones = phones

    @property
    def name(self):
        """Gets the name of this ContactRequest.  # noqa: E501


        :return: The name of this ContactRequest.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ContactRequest.


        :param name: The name of this ContactRequest.  # noqa: E501
        :type: str
        """
        if name is not None and len(name) > 250:
            raise ValueError("Invalid value for `name`, length must be less than or equal to `250`")  # noqa: E501

        self._name = name

    @property
    def emails(self):
        """Gets the emails of this ContactRequest.  # noqa: E501


        :return: The emails of this ContactRequest.  # noqa: E501
        :rtype: list[EmailRequest]
        """
        return self._emails

    @emails.setter
    def emails(self, emails):
        """Sets the emails of this ContactRequest.


        :param emails: The emails of this ContactRequest.  # noqa: E501
        :type: list[EmailRequest]
        """

        self._emails = emails

    @property
    def phones(self):
        """Gets the phones of this ContactRequest.  # noqa: E501


        :return: The phones of this ContactRequest.  # noqa: E501
        :rtype: list[PhonesRequest]
        """
        return self._phones

    @phones.setter
    def phones(self, phones):
        """Sets the phones of this ContactRequest.


        :param phones: The phones of this ContactRequest.  # noqa: E501
        :type: list[PhonesRequest]
        """

        self._phones = phones

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
        if not isinstance(other, ContactRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other