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


class ProposeSaleProductRequest(object):
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
        'name': 'str',
        'category': 'Category',
        'eans': 'list[str]',
        'images': 'list[ImageUrl]',
        'parameters': 'list[ProductParameter]',
        'description': 'StandardizedDescription'
    }

    attribute_map = {
        'name': 'name',
        'category': 'category',
        'eans': 'eans',
        'images': 'images',
        'parameters': 'parameters',
        'description': 'description'
    }

    def __init__(self, name=None, category=None, eans=None, images=None, parameters=None, description=None, local_vars_configuration=None):  # noqa: E501
        """ProposeSaleProductRequest - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._name = None
        self._category = None
        self._eans = None
        self._images = None
        self._parameters = None
        self._description = None
        self.discriminator = None

        self.name = name
        self.category = category
        if eans is not None:
            self.eans = eans
        self.images = images
        self.parameters = parameters
        if description is not None:
            self.description = description

    @property
    def name(self):
        """Gets the name of this ProposeSaleProductRequest.  # noqa: E501

        Suggested product name.  # noqa: E501

        :return: The name of this ProposeSaleProductRequest.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ProposeSaleProductRequest.

        Suggested product name.  # noqa: E501

        :param name: The name of this ProposeSaleProductRequest.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                name is not None and len(name) > 50):
            raise ValueError("Invalid value for `name`, length must be less than or equal to `50`")  # noqa: E501

        self._name = name

    @property
    def category(self):
        """Gets the category of this ProposeSaleProductRequest.  # noqa: E501


        :return: The category of this ProposeSaleProductRequest.  # noqa: E501
        :rtype: Category
        """
        return self._category

    @category.setter
    def category(self, category):
        """Sets the category of this ProposeSaleProductRequest.


        :param category: The category of this ProposeSaleProductRequest.  # noqa: E501
        :type: Category
        """
        if self.local_vars_configuration.client_side_validation and category is None:  # noqa: E501
            raise ValueError("Invalid value for `category`, must not be `None`")  # noqa: E501

        self._category = category

    @property
    def eans(self):
        """Gets the eans of this ProposeSaleProductRequest.  # noqa: E501

        A list of codes that identify this product. Currently this can include EAN, ISBN, and UPC identifier types.  # noqa: E501

        :return: The eans of this ProposeSaleProductRequest.  # noqa: E501
        :rtype: list[str]
        """
        return self._eans

    @eans.setter
    def eans(self, eans):
        """Sets the eans of this ProposeSaleProductRequest.

        A list of codes that identify this product. Currently this can include EAN, ISBN, and UPC identifier types.  # noqa: E501

        :param eans: The eans of this ProposeSaleProductRequest.  # noqa: E501
        :type: list[str]
        """

        self._eans = eans

    @property
    def images(self):
        """Gets the images of this ProposeSaleProductRequest.  # noqa: E501

        List of product images. At least one image is required.  # noqa: E501

        :return: The images of this ProposeSaleProductRequest.  # noqa: E501
        :rtype: list[ImageUrl]
        """
        return self._images

    @images.setter
    def images(self, images):
        """Sets the images of this ProposeSaleProductRequest.

        List of product images. At least one image is required.  # noqa: E501

        :param images: The images of this ProposeSaleProductRequest.  # noqa: E501
        :type: list[ImageUrl]
        """
        if self.local_vars_configuration.client_side_validation and images is None:  # noqa: E501
            raise ValueError("Invalid value for `images`, must not be `None`")  # noqa: E501

        self._images = images

    @property
    def parameters(self):
        """Gets the parameters of this ProposeSaleProductRequest.  # noqa: E501

        List of product parameters.  # noqa: E501

        :return: The parameters of this ProposeSaleProductRequest.  # noqa: E501
        :rtype: list[ProductParameter]
        """
        return self._parameters

    @parameters.setter
    def parameters(self, parameters):
        """Sets the parameters of this ProposeSaleProductRequest.

        List of product parameters.  # noqa: E501

        :param parameters: The parameters of this ProposeSaleProductRequest.  # noqa: E501
        :type: list[ProductParameter]
        """
        if self.local_vars_configuration.client_side_validation and parameters is None:  # noqa: E501
            raise ValueError("Invalid value for `parameters`, must not be `None`")  # noqa: E501

        self._parameters = parameters

    @property
    def description(self):
        """Gets the description of this ProposeSaleProductRequest.  # noqa: E501


        :return: The description of this ProposeSaleProductRequest.  # noqa: E501
        :rtype: StandardizedDescription
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ProposeSaleProductRequest.


        :param description: The description of this ProposeSaleProductRequest.  # noqa: E501
        :type: StandardizedDescription
        """

        self._description = description

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
        if not isinstance(other, ProposeSaleProductRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ProposeSaleProductRequest):
            return True

        return self.to_dict() != other.to_dict()
