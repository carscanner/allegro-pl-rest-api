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


class Address(object):
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
        'street': 'str',
        'city': 'str',
        'zip_code': 'str',
        'state': 'str',
        'country_code': 'str',
        'coordinates': 'Coordinates'
    }

    attribute_map = {
        'street': 'street',
        'city': 'city',
        'zip_code': 'zipCode',
        'state': 'state',
        'country_code': 'countryCode',
        'coordinates': 'coordinates'
    }

    def __init__(self, street=None, city=None, zip_code=None, state=None, country_code=None, coordinates=None, local_vars_configuration=None):  # noqa: E501
        """Address - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._street = None
        self._city = None
        self._zip_code = None
        self._state = None
        self._country_code = None
        self._coordinates = None
        self.discriminator = None

        if street is not None:
            self.street = street
        self.city = city
        self.zip_code = zip_code
        self.state = state
        self.country_code = country_code
        if coordinates is not None:
            self.coordinates = coordinates

    @property
    def street(self):
        """Gets the street of this Address.  # noqa: E501


        :return: The street of this Address.  # noqa: E501
        :rtype: str
        """
        return self._street

    @street.setter
    def street(self, street):
        """Sets the street of this Address.


        :param street: The street of this Address.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                street is not None and len(street) > 80):
            raise ValueError("Invalid value for `street`, length must be less than or equal to `80`")  # noqa: E501

        self._street = street

    @property
    def city(self):
        """Gets the city of this Address.  # noqa: E501


        :return: The city of this Address.  # noqa: E501
        :rtype: str
        """
        return self._city

    @city.setter
    def city(self, city):
        """Sets the city of this Address.


        :param city: The city of this Address.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and city is None:  # noqa: E501
            raise ValueError("Invalid value for `city`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                city is not None and len(city) > 40):
            raise ValueError("Invalid value for `city`, length must be less than or equal to `40`")  # noqa: E501

        self._city = city

    @property
    def zip_code(self):
        """Gets the zip_code of this Address.  # noqa: E501


        :return: The zip_code of this Address.  # noqa: E501
        :rtype: str
        """
        return self._zip_code

    @zip_code.setter
    def zip_code(self, zip_code):
        """Sets the zip_code of this Address.


        :param zip_code: The zip_code of this Address.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and zip_code is None:  # noqa: E501
            raise ValueError("Invalid value for `zip_code`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                zip_code is not None and len(zip_code) > 10):
            raise ValueError("Invalid value for `zip_code`, length must be less than or equal to `10`")  # noqa: E501

        self._zip_code = zip_code

    @property
    def state(self):
        """Gets the state of this Address.  # noqa: E501


        :return: The state of this Address.  # noqa: E501
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this Address.


        :param state: The state of this Address.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and state is None:  # noqa: E501
            raise ValueError("Invalid value for `state`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                state is not None and len(state) > 40):
            raise ValueError("Invalid value for `state`, length must be less than or equal to `40`")  # noqa: E501

        self._state = state

    @property
    def country_code(self):
        """Gets the country_code of this Address.  # noqa: E501


        :return: The country_code of this Address.  # noqa: E501
        :rtype: str
        """
        return self._country_code

    @country_code.setter
    def country_code(self, country_code):
        """Sets the country_code of this Address.


        :param country_code: The country_code of this Address.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and country_code is None:  # noqa: E501
            raise ValueError("Invalid value for `country_code`, must not be `None`")  # noqa: E501

        self._country_code = country_code

    @property
    def coordinates(self):
        """Gets the coordinates of this Address.  # noqa: E501


        :return: The coordinates of this Address.  # noqa: E501
        :rtype: Coordinates
        """
        return self._coordinates

    @coordinates.setter
    def coordinates(self, coordinates):
        """Sets the coordinates of this Address.


        :param coordinates: The coordinates of this Address.  # noqa: E501
        :type: Coordinates
        """

        self._coordinates = coordinates

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
        if not isinstance(other, Address):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Address):
            return True

        return self.to_dict() != other.to_dict()
