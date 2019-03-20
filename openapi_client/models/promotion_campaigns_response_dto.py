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


class PromotionCampaignsResponseDto(object):
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
        'promotion_campaigns': 'list[SinglePromotionCampaignResponseDto]',
        'total_count': 'int'
    }

    attribute_map = {
        'promotion_campaigns': 'promotionCampaigns',
        'total_count': 'totalCount'
    }

    def __init__(self, promotion_campaigns=None, total_count=None):  # noqa: E501
        """PromotionCampaignsResponseDto - a model defined in OpenAPI"""  # noqa: E501

        self._promotion_campaigns = None
        self._total_count = None
        self.discriminator = None

        self.promotion_campaigns = promotion_campaigns
        self.total_count = total_count

    @property
    def promotion_campaigns(self):
        """Gets the promotion_campaigns of this PromotionCampaignsResponseDto.  # noqa: E501


        :return: The promotion_campaigns of this PromotionCampaignsResponseDto.  # noqa: E501
        :rtype: list[SinglePromotionCampaignResponseDto]
        """
        return self._promotion_campaigns

    @promotion_campaigns.setter
    def promotion_campaigns(self, promotion_campaigns):
        """Sets the promotion_campaigns of this PromotionCampaignsResponseDto.


        :param promotion_campaigns: The promotion_campaigns of this PromotionCampaignsResponseDto.  # noqa: E501
        :type: list[SinglePromotionCampaignResponseDto]
        """
        if promotion_campaigns is None:
            raise ValueError("Invalid value for `promotion_campaigns`, must not be `None`")  # noqa: E501

        self._promotion_campaigns = promotion_campaigns

    @property
    def total_count(self):
        """Gets the total_count of this PromotionCampaignsResponseDto.  # noqa: E501


        :return: The total_count of this PromotionCampaignsResponseDto.  # noqa: E501
        :rtype: int
        """
        return self._total_count

    @total_count.setter
    def total_count(self, total_count):
        """Sets the total_count of this PromotionCampaignsResponseDto.


        :param total_count: The total_count of this PromotionCampaignsResponseDto.  # noqa: E501
        :type: int
        """
        if total_count is None:
            raise ValueError("Invalid value for `total_count`, must not be `None`")  # noqa: E501

        self._total_count = total_count

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
        if not isinstance(other, PromotionCampaignsResponseDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
