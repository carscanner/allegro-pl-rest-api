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


class SellerCreateRebateRequestDto(object):
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
        'benefits': 'list[Benefit]',
        'offer_criteria': 'list[SellerRebateOfferCriterion]'
    }

    attribute_map = {
        'benefits': 'benefits',
        'offer_criteria': 'offerCriteria'
    }

    def __init__(self, benefits=None, offer_criteria=None, local_vars_configuration=None):  # noqa: E501
        """SellerCreateRebateRequestDto - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._benefits = None
        self._offer_criteria = None
        self.discriminator = None

        self.benefits = benefits
        self.offer_criteria = offer_criteria

    @property
    def benefits(self):
        """Gets the benefits of this SellerCreateRebateRequestDto.  # noqa: E501

        What kind of rebate will be given  # noqa: E501

        :return: The benefits of this SellerCreateRebateRequestDto.  # noqa: E501
        :rtype: list[Benefit]
        """
        return self._benefits

    @benefits.setter
    def benefits(self, benefits):
        """Sets the benefits of this SellerCreateRebateRequestDto.

        What kind of rebate will be given  # noqa: E501

        :param benefits: The benefits of this SellerCreateRebateRequestDto.  # noqa: E501
        :type: list[Benefit]
        """
        if self.local_vars_configuration.client_side_validation and benefits is None:  # noqa: E501
            raise ValueError("Invalid value for `benefits`, must not be `None`")  # noqa: E501

        self._benefits = benefits

    @property
    def offer_criteria(self):
        """Gets the offer_criteria of this SellerCreateRebateRequestDto.  # noqa: E501

        What offers will be included  # noqa: E501

        :return: The offer_criteria of this SellerCreateRebateRequestDto.  # noqa: E501
        :rtype: list[SellerRebateOfferCriterion]
        """
        return self._offer_criteria

    @offer_criteria.setter
    def offer_criteria(self, offer_criteria):
        """Sets the offer_criteria of this SellerCreateRebateRequestDto.

        What offers will be included  # noqa: E501

        :param offer_criteria: The offer_criteria of this SellerCreateRebateRequestDto.  # noqa: E501
        :type: list[SellerRebateOfferCriterion]
        """
        if self.local_vars_configuration.client_side_validation and offer_criteria is None:  # noqa: E501
            raise ValueError("Invalid value for `offer_criteria`, must not be `None`")  # noqa: E501

        self._offer_criteria = offer_criteria

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
        if not isinstance(other, SellerCreateRebateRequestDto):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, SellerCreateRebateRequestDto):
            return True

        return self.to_dict() != other.to_dict()
