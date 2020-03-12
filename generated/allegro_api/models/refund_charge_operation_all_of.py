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


class RefundChargeOperationAllOf(object):
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
        'type': 'str',
        'payment': 'OperationPayment',
        'participant': 'BuyerParticipant'
    }

    attribute_map = {
        'type': 'type',
        'payment': 'payment',
        'participant': 'participant'
    }

    def __init__(self, type='REFUND_CHARGE', payment=None, participant=None, local_vars_configuration=None):  # noqa: E501
        """RefundChargeOperationAllOf - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._type = None
        self._payment = None
        self._participant = None
        self.discriminator = None

        if type is not None:
            self.type = type
        if payment is not None:
            self.payment = payment
        if participant is not None:
            self.participant = participant

    @property
    def type(self):
        """Gets the type of this RefundChargeOperationAllOf.  # noqa: E501


        :return: The type of this RefundChargeOperationAllOf.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this RefundChargeOperationAllOf.


        :param type: The type of this RefundChargeOperationAllOf.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def payment(self):
        """Gets the payment of this RefundChargeOperationAllOf.  # noqa: E501


        :return: The payment of this RefundChargeOperationAllOf.  # noqa: E501
        :rtype: OperationPayment
        """
        return self._payment

    @payment.setter
    def payment(self, payment):
        """Sets the payment of this RefundChargeOperationAllOf.


        :param payment: The payment of this RefundChargeOperationAllOf.  # noqa: E501
        :type: OperationPayment
        """

        self._payment = payment

    @property
    def participant(self):
        """Gets the participant of this RefundChargeOperationAllOf.  # noqa: E501


        :return: The participant of this RefundChargeOperationAllOf.  # noqa: E501
        :rtype: BuyerParticipant
        """
        return self._participant

    @participant.setter
    def participant(self, participant):
        """Sets the participant of this RefundChargeOperationAllOf.


        :param participant: The participant of this RefundChargeOperationAllOf.  # noqa: E501
        :type: BuyerParticipant
        """

        self._participant = participant

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
        if not isinstance(other, RefundChargeOperationAllOf):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, RefundChargeOperationAllOf):
            return True

        return self.to_dict() != other.to_dict()
