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


class UserCampaignEligibility(object):
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
        'eligible': 'bool',
        'refusal_reasons': 'list[CampaignRefusalReason]'
    }

    attribute_map = {
        'eligible': 'eligible',
        'refusal_reasons': 'refusalReasons'
    }

    def __init__(self, eligible=None, refusal_reasons=None, local_vars_configuration=None):  # noqa: E501
        """UserCampaignEligibility - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._eligible = None
        self._refusal_reasons = None
        self.discriminator = None

        self.eligible = eligible
        self.refusal_reasons = refusal_reasons

    @property
    def eligible(self):
        """Gets the eligible of this UserCampaignEligibility.  # noqa: E501

        Information whether user is eligible to participate in this campaign.  # noqa: E501

        :return: The eligible of this UserCampaignEligibility.  # noqa: E501
        :rtype: bool
        """
        return self._eligible

    @eligible.setter
    def eligible(self, eligible):
        """Sets the eligible of this UserCampaignEligibility.

        Information whether user is eligible to participate in this campaign.  # noqa: E501

        :param eligible: The eligible of this UserCampaignEligibility.  # noqa: E501
        :type: bool
        """
        if self.local_vars_configuration.client_side_validation and eligible is None:  # noqa: E501
            raise ValueError("Invalid value for `eligible`, must not be `None`")  # noqa: E501

        self._eligible = eligible

    @property
    def refusal_reasons(self):
        """Gets the refusal_reasons of this UserCampaignEligibility.  # noqa: E501

        Information why user is not able to participate in the campaign.  # noqa: E501

        :return: The refusal_reasons of this UserCampaignEligibility.  # noqa: E501
        :rtype: list[CampaignRefusalReason]
        """
        return self._refusal_reasons

    @refusal_reasons.setter
    def refusal_reasons(self, refusal_reasons):
        """Sets the refusal_reasons of this UserCampaignEligibility.

        Information why user is not able to participate in the campaign.  # noqa: E501

        :param refusal_reasons: The refusal_reasons of this UserCampaignEligibility.  # noqa: E501
        :type: list[CampaignRefusalReason]
        """
        if self.local_vars_configuration.client_side_validation and refusal_reasons is None:  # noqa: E501
            raise ValueError("Invalid value for `refusal_reasons`, must not be `None`")  # noqa: E501

        self._refusal_reasons = refusal_reasons

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
        if not isinstance(other, UserCampaignEligibility):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, UserCampaignEligibility):
            return True

        return self.to_dict() != other.to_dict()
