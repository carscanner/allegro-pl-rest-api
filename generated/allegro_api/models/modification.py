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


class Modification(object):
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
        'additional_services_group': 'AdditionalServicesGroup',
        'delivery': 'ModificationDelivery',
        'payments': 'ModificationPayments',
        'promotion': 'ModificationPromotion',
        'size_table': 'ModificationSizeTable',
        'publication': 'ModificationPublication'
    }

    attribute_map = {
        'additional_services_group': 'additionalServicesGroup',
        'delivery': 'delivery',
        'payments': 'payments',
        'promotion': 'promotion',
        'size_table': 'sizeTable',
        'publication': 'publication'
    }

    def __init__(self, additional_services_group=None, delivery=None, payments=None, promotion=None, size_table=None, publication=None, local_vars_configuration=None):  # noqa: E501
        """Modification - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._additional_services_group = None
        self._delivery = None
        self._payments = None
        self._promotion = None
        self._size_table = None
        self._publication = None
        self.discriminator = None

        if additional_services_group is not None:
            self.additional_services_group = additional_services_group
        if delivery is not None:
            self.delivery = delivery
        if payments is not None:
            self.payments = payments
        if promotion is not None:
            self.promotion = promotion
        if size_table is not None:
            self.size_table = size_table
        if publication is not None:
            self.publication = publication

    @property
    def additional_services_group(self):
        """Gets the additional_services_group of this Modification.  # noqa: E501


        :return: The additional_services_group of this Modification.  # noqa: E501
        :rtype: AdditionalServicesGroup
        """
        return self._additional_services_group

    @additional_services_group.setter
    def additional_services_group(self, additional_services_group):
        """Sets the additional_services_group of this Modification.


        :param additional_services_group: The additional_services_group of this Modification.  # noqa: E501
        :type: AdditionalServicesGroup
        """

        self._additional_services_group = additional_services_group

    @property
    def delivery(self):
        """Gets the delivery of this Modification.  # noqa: E501


        :return: The delivery of this Modification.  # noqa: E501
        :rtype: ModificationDelivery
        """
        return self._delivery

    @delivery.setter
    def delivery(self, delivery):
        """Sets the delivery of this Modification.


        :param delivery: The delivery of this Modification.  # noqa: E501
        :type: ModificationDelivery
        """

        self._delivery = delivery

    @property
    def payments(self):
        """Gets the payments of this Modification.  # noqa: E501


        :return: The payments of this Modification.  # noqa: E501
        :rtype: ModificationPayments
        """
        return self._payments

    @payments.setter
    def payments(self, payments):
        """Sets the payments of this Modification.


        :param payments: The payments of this Modification.  # noqa: E501
        :type: ModificationPayments
        """

        self._payments = payments

    @property
    def promotion(self):
        """Gets the promotion of this Modification.  # noqa: E501


        :return: The promotion of this Modification.  # noqa: E501
        :rtype: ModificationPromotion
        """
        return self._promotion

    @promotion.setter
    def promotion(self, promotion):
        """Sets the promotion of this Modification.


        :param promotion: The promotion of this Modification.  # noqa: E501
        :type: ModificationPromotion
        """

        self._promotion = promotion

    @property
    def size_table(self):
        """Gets the size_table of this Modification.  # noqa: E501


        :return: The size_table of this Modification.  # noqa: E501
        :rtype: ModificationSizeTable
        """
        return self._size_table

    @size_table.setter
    def size_table(self, size_table):
        """Sets the size_table of this Modification.


        :param size_table: The size_table of this Modification.  # noqa: E501
        :type: ModificationSizeTable
        """

        self._size_table = size_table

    @property
    def publication(self):
        """Gets the publication of this Modification.  # noqa: E501


        :return: The publication of this Modification.  # noqa: E501
        :rtype: ModificationPublication
        """
        return self._publication

    @publication.setter
    def publication(self, publication):
        """Sets the publication of this Modification.


        :param publication: The publication of this Modification.  # noqa: E501
        :type: ModificationPublication
        """

        self._publication = publication

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
        if not isinstance(other, Modification):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Modification):
            return True

        return self.to_dict() != other.to_dict()
