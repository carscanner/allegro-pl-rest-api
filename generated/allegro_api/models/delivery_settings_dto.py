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


class DeliverySettingsDto(object):
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
        'free_delivery': 'DeliverySettingsDtoFreeDelivery',
        'join_policy': 'DeliverySettingsDtoJoinPolicy',
        'custom_cost': 'DeliverySettingsDtoCustomCost',
        'updated_at': 'str'
    }

    attribute_map = {
        'free_delivery': 'freeDelivery',
        'join_policy': 'joinPolicy',
        'custom_cost': 'customCost',
        'updated_at': 'updatedAt'
    }

    def __init__(self, free_delivery=None, join_policy=None, custom_cost=None, updated_at=None, local_vars_configuration=None):  # noqa: E501
        """DeliverySettingsDto - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._free_delivery = None
        self._join_policy = None
        self._custom_cost = None
        self._updated_at = None
        self.discriminator = None

        if free_delivery is not None:
            self.free_delivery = free_delivery
        if join_policy is not None:
            self.join_policy = join_policy
        if custom_cost is not None:
            self.custom_cost = custom_cost
        if updated_at is not None:
            self.updated_at = updated_at

    @property
    def free_delivery(self):
        """Gets the free_delivery of this DeliverySettingsDto.  # noqa: E501


        :return: The free_delivery of this DeliverySettingsDto.  # noqa: E501
        :rtype: DeliverySettingsDtoFreeDelivery
        """
        return self._free_delivery

    @free_delivery.setter
    def free_delivery(self, free_delivery):
        """Sets the free_delivery of this DeliverySettingsDto.


        :param free_delivery: The free_delivery of this DeliverySettingsDto.  # noqa: E501
        :type: DeliverySettingsDtoFreeDelivery
        """

        self._free_delivery = free_delivery

    @property
    def join_policy(self):
        """Gets the join_policy of this DeliverySettingsDto.  # noqa: E501


        :return: The join_policy of this DeliverySettingsDto.  # noqa: E501
        :rtype: DeliverySettingsDtoJoinPolicy
        """
        return self._join_policy

    @join_policy.setter
    def join_policy(self, join_policy):
        """Sets the join_policy of this DeliverySettingsDto.


        :param join_policy: The join_policy of this DeliverySettingsDto.  # noqa: E501
        :type: DeliverySettingsDtoJoinPolicy
        """

        self._join_policy = join_policy

    @property
    def custom_cost(self):
        """Gets the custom_cost of this DeliverySettingsDto.  # noqa: E501


        :return: The custom_cost of this DeliverySettingsDto.  # noqa: E501
        :rtype: DeliverySettingsDtoCustomCost
        """
        return self._custom_cost

    @custom_cost.setter
    def custom_cost(self, custom_cost):
        """Sets the custom_cost of this DeliverySettingsDto.


        :param custom_cost: The custom_cost of this DeliverySettingsDto.  # noqa: E501
        :type: DeliverySettingsDtoCustomCost
        """

        self._custom_cost = custom_cost

    @property
    def updated_at(self):
        """Gets the updated_at of this DeliverySettingsDto.  # noqa: E501

        Date and time of the last modification of the set in UTC ISO 8601 format. When updating (Put) settings the field is ignored.  # noqa: E501

        :return: The updated_at of this DeliverySettingsDto.  # noqa: E501
        :rtype: str
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this DeliverySettingsDto.

        Date and time of the last modification of the set in UTC ISO 8601 format. When updating (Put) settings the field is ignored.  # noqa: E501

        :param updated_at: The updated_at of this DeliverySettingsDto.  # noqa: E501
        :type: str
        """

        self._updated_at = updated_at

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
        if not isinstance(other, DeliverySettingsDto):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, DeliverySettingsDto):
            return True

        return self.to_dict() != other.to_dict()