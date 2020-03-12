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


class CheckoutFormDeliveryAddress(object):
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
        'first_name': 'str',
        'last_name': 'str',
        'street': 'str',
        'city': 'str',
        'zip_code': 'str',
        'country_code': 'str',
        'company_name': 'str',
        'phone_number': 'str'
    }

    attribute_map = {
        'first_name': 'firstName',
        'last_name': 'lastName',
        'street': 'street',
        'city': 'city',
        'zip_code': 'zipCode',
        'country_code': 'countryCode',
        'company_name': 'companyName',
        'phone_number': 'phoneNumber'
    }

    def __init__(self, first_name=None, last_name=None, street=None, city=None, zip_code=None, country_code=None, company_name=None, phone_number=None, local_vars_configuration=None):  # noqa: E501
        """CheckoutFormDeliveryAddress - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._first_name = None
        self._last_name = None
        self._street = None
        self._city = None
        self._zip_code = None
        self._country_code = None
        self._company_name = None
        self._phone_number = None
        self.discriminator = None

        self.first_name = first_name
        self.last_name = last_name
        self.street = street
        self.city = city
        self.zip_code = zip_code
        self.country_code = country_code
        if company_name is not None:
            self.company_name = company_name
        if phone_number is not None:
            self.phone_number = phone_number

    @property
    def first_name(self):
        """Gets the first_name of this CheckoutFormDeliveryAddress.  # noqa: E501

        Receiver's first name  # noqa: E501

        :return: The first_name of this CheckoutFormDeliveryAddress.  # noqa: E501
        :rtype: str
        """
        return self._first_name

    @first_name.setter
    def first_name(self, first_name):
        """Sets the first_name of this CheckoutFormDeliveryAddress.

        Receiver's first name  # noqa: E501

        :param first_name: The first_name of this CheckoutFormDeliveryAddress.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and first_name is None:  # noqa: E501
            raise ValueError("Invalid value for `first_name`, must not be `None`")  # noqa: E501

        self._first_name = first_name

    @property
    def last_name(self):
        """Gets the last_name of this CheckoutFormDeliveryAddress.  # noqa: E501

        Receiver's last name  # noqa: E501

        :return: The last_name of this CheckoutFormDeliveryAddress.  # noqa: E501
        :rtype: str
        """
        return self._last_name

    @last_name.setter
    def last_name(self, last_name):
        """Sets the last_name of this CheckoutFormDeliveryAddress.

        Receiver's last name  # noqa: E501

        :param last_name: The last_name of this CheckoutFormDeliveryAddress.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and last_name is None:  # noqa: E501
            raise ValueError("Invalid value for `last_name`, must not be `None`")  # noqa: E501

        self._last_name = last_name

    @property
    def street(self):
        """Gets the street of this CheckoutFormDeliveryAddress.  # noqa: E501

        Street name  # noqa: E501

        :return: The street of this CheckoutFormDeliveryAddress.  # noqa: E501
        :rtype: str
        """
        return self._street

    @street.setter
    def street(self, street):
        """Sets the street of this CheckoutFormDeliveryAddress.

        Street name  # noqa: E501

        :param street: The street of this CheckoutFormDeliveryAddress.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and street is None:  # noqa: E501
            raise ValueError("Invalid value for `street`, must not be `None`")  # noqa: E501

        self._street = street

    @property
    def city(self):
        """Gets the city of this CheckoutFormDeliveryAddress.  # noqa: E501

        City name  # noqa: E501

        :return: The city of this CheckoutFormDeliveryAddress.  # noqa: E501
        :rtype: str
        """
        return self._city

    @city.setter
    def city(self, city):
        """Sets the city of this CheckoutFormDeliveryAddress.

        City name  # noqa: E501

        :param city: The city of this CheckoutFormDeliveryAddress.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and city is None:  # noqa: E501
            raise ValueError("Invalid value for `city`, must not be `None`")  # noqa: E501

        self._city = city

    @property
    def zip_code(self):
        """Gets the zip_code of this CheckoutFormDeliveryAddress.  # noqa: E501

        Postal code  # noqa: E501

        :return: The zip_code of this CheckoutFormDeliveryAddress.  # noqa: E501
        :rtype: str
        """
        return self._zip_code

    @zip_code.setter
    def zip_code(self, zip_code):
        """Sets the zip_code of this CheckoutFormDeliveryAddress.

        Postal code  # noqa: E501

        :param zip_code: The zip_code of this CheckoutFormDeliveryAddress.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and zip_code is None:  # noqa: E501
            raise ValueError("Invalid value for `zip_code`, must not be `None`")  # noqa: E501

        self._zip_code = zip_code

    @property
    def country_code(self):
        """Gets the country_code of this CheckoutFormDeliveryAddress.  # noqa: E501

        Country code  # noqa: E501

        :return: The country_code of this CheckoutFormDeliveryAddress.  # noqa: E501
        :rtype: str
        """
        return self._country_code

    @country_code.setter
    def country_code(self, country_code):
        """Sets the country_code of this CheckoutFormDeliveryAddress.

        Country code  # noqa: E501

        :param country_code: The country_code of this CheckoutFormDeliveryAddress.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and country_code is None:  # noqa: E501
            raise ValueError("Invalid value for `country_code`, must not be `None`")  # noqa: E501

        self._country_code = country_code

    @property
    def company_name(self):
        """Gets the company_name of this CheckoutFormDeliveryAddress.  # noqa: E501

        Company name  # noqa: E501

        :return: The company_name of this CheckoutFormDeliveryAddress.  # noqa: E501
        :rtype: str
        """
        return self._company_name

    @company_name.setter
    def company_name(self, company_name):
        """Sets the company_name of this CheckoutFormDeliveryAddress.

        Company name  # noqa: E501

        :param company_name: The company_name of this CheckoutFormDeliveryAddress.  # noqa: E501
        :type: str
        """

        self._company_name = company_name

    @property
    def phone_number(self):
        """Gets the phone_number of this CheckoutFormDeliveryAddress.  # noqa: E501

        Phone number  # noqa: E501

        :return: The phone_number of this CheckoutFormDeliveryAddress.  # noqa: E501
        :rtype: str
        """
        return self._phone_number

    @phone_number.setter
    def phone_number(self, phone_number):
        """Sets the phone_number of this CheckoutFormDeliveryAddress.

        Phone number  # noqa: E501

        :param phone_number: The phone_number of this CheckoutFormDeliveryAddress.  # noqa: E501
        :type: str
        """

        self._phone_number = phone_number

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
        if not isinstance(other, CheckoutFormDeliveryAddress):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CheckoutFormDeliveryAddress):
            return True

        return self.to_dict() != other.to_dict()
