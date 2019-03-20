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


class CommandTask(object):
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
        'field': 'str',
        'finished_at': 'datetime',
        'message': 'str',
        'offer': 'OfferId',
        'scheduled_at': 'datetime',
        'status': 'str'
    }

    attribute_map = {
        'field': 'field',
        'finished_at': 'finishedAt',
        'message': 'message',
        'offer': 'offer',
        'scheduled_at': 'scheduledAt',
        'status': 'status'
    }

    def __init__(self, field=None, finished_at=None, message=None, offer=None, scheduled_at=None, status=None):  # noqa: E501
        """CommandTask - a model defined in OpenAPI"""  # noqa: E501

        self._field = None
        self._finished_at = None
        self._message = None
        self._offer = None
        self._scheduled_at = None
        self._status = None
        self.discriminator = None

        if field is not None:
            self.field = field
        if finished_at is not None:
            self.finished_at = finished_at
        if message is not None:
            self.message = message
        if offer is not None:
            self.offer = offer
        if scheduled_at is not None:
            self.scheduled_at = scheduled_at
        if status is not None:
            self.status = status

    @property
    def field(self):
        """Gets the field of this CommandTask.  # noqa: E501

        Modified field as JSON path  # noqa: E501

        :return: The field of this CommandTask.  # noqa: E501
        :rtype: str
        """
        return self._field

    @field.setter
    def field(self, field):
        """Sets the field of this CommandTask.

        Modified field as JSON path  # noqa: E501

        :param field: The field of this CommandTask.  # noqa: E501
        :type: str
        """

        self._field = field

    @property
    def finished_at(self):
        """Gets the finished_at of this CommandTask.  # noqa: E501

        Date of completion of the modification. Format (ISO 8601) - yyyy-MM-dd'T'HH:mm:ss.SSSZ  # noqa: E501

        :return: The finished_at of this CommandTask.  # noqa: E501
        :rtype: datetime
        """
        return self._finished_at

    @finished_at.setter
    def finished_at(self, finished_at):
        """Sets the finished_at of this CommandTask.

        Date of completion of the modification. Format (ISO 8601) - yyyy-MM-dd'T'HH:mm:ss.SSSZ  # noqa: E501

        :param finished_at: The finished_at of this CommandTask.  # noqa: E501
        :type: datetime
        """

        self._finished_at = finished_at

    @property
    def message(self):
        """Gets the message of this CommandTask.  # noqa: E501

        Fail reason description  # noqa: E501

        :return: The message of this CommandTask.  # noqa: E501
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this CommandTask.

        Fail reason description  # noqa: E501

        :param message: The message of this CommandTask.  # noqa: E501
        :type: str
        """

        self._message = message

    @property
    def offer(self):
        """Gets the offer of this CommandTask.  # noqa: E501


        :return: The offer of this CommandTask.  # noqa: E501
        :rtype: OfferId
        """
        return self._offer

    @offer.setter
    def offer(self, offer):
        """Sets the offer of this CommandTask.


        :param offer: The offer of this CommandTask.  # noqa: E501
        :type: OfferId
        """

        self._offer = offer

    @property
    def scheduled_at(self):
        """Gets the scheduled_at of this CommandTask.  # noqa: E501

        Date of the modification schedule. Format (ISO 8601) - yyyy-MM-dd'T'HH:mm:ss.SSSZ  # noqa: E501

        :return: The scheduled_at of this CommandTask.  # noqa: E501
        :rtype: datetime
        """
        return self._scheduled_at

    @scheduled_at.setter
    def scheduled_at(self, scheduled_at):
        """Sets the scheduled_at of this CommandTask.

        Date of the modification schedule. Format (ISO 8601) - yyyy-MM-dd'T'HH:mm:ss.SSSZ  # noqa: E501

        :param scheduled_at: The scheduled_at of this CommandTask.  # noqa: E501
        :type: datetime
        """

        self._scheduled_at = scheduled_at

    @property
    def status(self):
        """Gets the status of this CommandTask.  # noqa: E501

        Available statuses: NEW, SUCCESS, FAIL  # noqa: E501

        :return: The status of this CommandTask.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this CommandTask.

        Available statuses: NEW, SUCCESS, FAIL  # noqa: E501

        :param status: The status of this CommandTask.  # noqa: E501
        :type: str
        """

        self._status = status

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
        if not isinstance(other, CommandTask):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
