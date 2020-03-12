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


class BadgeApplication(object):
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
        'id': 'str',
        'created_at': 'str',
        'updated_at': 'str',
        'campaign': 'BadgeApplicationCampaign',
        'offer': 'BadgeApplicationOffer',
        'prices': 'BadgeApplicationPrices',
        'process': 'BadgeApplicationProcess',
        'purchase_constraints': 'BadgeApplicationPurchaseConstraints'
    }

    attribute_map = {
        'id': 'id',
        'created_at': 'createdAt',
        'updated_at': 'updatedAt',
        'campaign': 'campaign',
        'offer': 'offer',
        'prices': 'prices',
        'process': 'process',
        'purchase_constraints': 'purchaseConstraints'
    }

    def __init__(self, id=None, created_at=None, updated_at=None, campaign=None, offer=None, prices=None, process=None, purchase_constraints=None, local_vars_configuration=None):  # noqa: E501
        """BadgeApplication - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._created_at = None
        self._updated_at = None
        self._campaign = None
        self._offer = None
        self._prices = None
        self._process = None
        self._purchase_constraints = None
        self.discriminator = None

        self.id = id
        self.created_at = created_at
        self.updated_at = updated_at
        self.campaign = campaign
        self.offer = offer
        if prices is not None:
            self.prices = prices
        self.process = process
        if purchase_constraints is not None:
            self.purchase_constraints = purchase_constraints

    @property
    def id(self):
        """Gets the id of this BadgeApplication.  # noqa: E501

        Badge application ID.  # noqa: E501

        :return: The id of this BadgeApplication.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this BadgeApplication.

        Badge application ID.  # noqa: E501

        :param id: The id of this BadgeApplication.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and id is None:  # noqa: E501
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def created_at(self):
        """Gets the created_at of this BadgeApplication.  # noqa: E501

        Provided in [ISO 8601 format](link: https://en.wikipedia.org/wiki/ISO_8601).  # noqa: E501

        :return: The created_at of this BadgeApplication.  # noqa: E501
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this BadgeApplication.

        Provided in [ISO 8601 format](link: https://en.wikipedia.org/wiki/ISO_8601).  # noqa: E501

        :param created_at: The created_at of this BadgeApplication.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and created_at is None:  # noqa: E501
            raise ValueError("Invalid value for `created_at`, must not be `None`")  # noqa: E501

        self._created_at = created_at

    @property
    def updated_at(self):
        """Gets the updated_at of this BadgeApplication.  # noqa: E501

        Provided in [ISO 8601 format](link: https://en.wikipedia.org/wiki/ISO_8601).  # noqa: E501

        :return: The updated_at of this BadgeApplication.  # noqa: E501
        :rtype: str
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this BadgeApplication.

        Provided in [ISO 8601 format](link: https://en.wikipedia.org/wiki/ISO_8601).  # noqa: E501

        :param updated_at: The updated_at of this BadgeApplication.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and updated_at is None:  # noqa: E501
            raise ValueError("Invalid value for `updated_at`, must not be `None`")  # noqa: E501

        self._updated_at = updated_at

    @property
    def campaign(self):
        """Gets the campaign of this BadgeApplication.  # noqa: E501


        :return: The campaign of this BadgeApplication.  # noqa: E501
        :rtype: BadgeApplicationCampaign
        """
        return self._campaign

    @campaign.setter
    def campaign(self, campaign):
        """Sets the campaign of this BadgeApplication.


        :param campaign: The campaign of this BadgeApplication.  # noqa: E501
        :type: BadgeApplicationCampaign
        """
        if self.local_vars_configuration.client_side_validation and campaign is None:  # noqa: E501
            raise ValueError("Invalid value for `campaign`, must not be `None`")  # noqa: E501

        self._campaign = campaign

    @property
    def offer(self):
        """Gets the offer of this BadgeApplication.  # noqa: E501


        :return: The offer of this BadgeApplication.  # noqa: E501
        :rtype: BadgeApplicationOffer
        """
        return self._offer

    @offer.setter
    def offer(self, offer):
        """Sets the offer of this BadgeApplication.


        :param offer: The offer of this BadgeApplication.  # noqa: E501
        :type: BadgeApplicationOffer
        """
        if self.local_vars_configuration.client_side_validation and offer is None:  # noqa: E501
            raise ValueError("Invalid value for `offer`, must not be `None`")  # noqa: E501

        self._offer = offer

    @property
    def prices(self):
        """Gets the prices of this BadgeApplication.  # noqa: E501


        :return: The prices of this BadgeApplication.  # noqa: E501
        :rtype: BadgeApplicationPrices
        """
        return self._prices

    @prices.setter
    def prices(self, prices):
        """Sets the prices of this BadgeApplication.


        :param prices: The prices of this BadgeApplication.  # noqa: E501
        :type: BadgeApplicationPrices
        """

        self._prices = prices

    @property
    def process(self):
        """Gets the process of this BadgeApplication.  # noqa: E501


        :return: The process of this BadgeApplication.  # noqa: E501
        :rtype: BadgeApplicationProcess
        """
        return self._process

    @process.setter
    def process(self, process):
        """Sets the process of this BadgeApplication.


        :param process: The process of this BadgeApplication.  # noqa: E501
        :type: BadgeApplicationProcess
        """
        if self.local_vars_configuration.client_side_validation and process is None:  # noqa: E501
            raise ValueError("Invalid value for `process`, must not be `None`")  # noqa: E501

        self._process = process

    @property
    def purchase_constraints(self):
        """Gets the purchase_constraints of this BadgeApplication.  # noqa: E501


        :return: The purchase_constraints of this BadgeApplication.  # noqa: E501
        :rtype: BadgeApplicationPurchaseConstraints
        """
        return self._purchase_constraints

    @purchase_constraints.setter
    def purchase_constraints(self, purchase_constraints):
        """Sets the purchase_constraints of this BadgeApplication.


        :param purchase_constraints: The purchase_constraints of this BadgeApplication.  # noqa: E501
        :type: BadgeApplicationPurchaseConstraints
        """

        self._purchase_constraints = purchase_constraints

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
        if not isinstance(other, BadgeApplication):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, BadgeApplication):
            return True

        return self.to_dict() != other.to_dict()