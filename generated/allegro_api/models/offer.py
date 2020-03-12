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


class Offer(object):
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
        'additional_services': 'JustId',
        'after_sales_services': 'AfterSalesServices',
        'attachments': 'list[Attachment]',
        'category': 'Category',
        'compatibility_list': 'CompatibilityList',
        'contact': 'JustId',
        'created_at': 'datetime',
        'delivery': 'Delivery',
        'description': 'StandardizedDescription',
        'ean': 'str',
        'external': 'ExternalId',
        'id': 'str',
        'images': 'list[ImageUrl]',
        'location': 'Location',
        'name': 'str',
        'parameters': 'list[Parameter]',
        'payments': 'Payments',
        'product': 'JustId',
        'promotion': 'Promotion',
        'publication': 'Publication',
        'selling_mode': 'SellingMode',
        'size_table': 'JustId',
        'stock': 'Stock',
        'tecdoc_specification': 'TecdocSpecification',
        'updated_at': 'datetime',
        'validation': 'Validation'
    }

    attribute_map = {
        'additional_services': 'additionalServices',
        'after_sales_services': 'afterSalesServices',
        'attachments': 'attachments',
        'category': 'category',
        'compatibility_list': 'compatibilityList',
        'contact': 'contact',
        'created_at': 'createdAt',
        'delivery': 'delivery',
        'description': 'description',
        'ean': 'ean',
        'external': 'external',
        'id': 'id',
        'images': 'images',
        'location': 'location',
        'name': 'name',
        'parameters': 'parameters',
        'payments': 'payments',
        'product': 'product',
        'promotion': 'promotion',
        'publication': 'publication',
        'selling_mode': 'sellingMode',
        'size_table': 'sizeTable',
        'stock': 'stock',
        'tecdoc_specification': 'tecdocSpecification',
        'updated_at': 'updatedAt',
        'validation': 'validation'
    }

    def __init__(self, additional_services=None, after_sales_services=None, attachments=None, category=None, compatibility_list=None, contact=None, created_at=None, delivery=None, description=None, ean=None, external=None, id=None, images=None, location=None, name=None, parameters=None, payments=None, product=None, promotion=None, publication=None, selling_mode=None, size_table=None, stock=None, tecdoc_specification=None, updated_at=None, validation=None, local_vars_configuration=None):  # noqa: E501
        """Offer - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._additional_services = None
        self._after_sales_services = None
        self._attachments = None
        self._category = None
        self._compatibility_list = None
        self._contact = None
        self._created_at = None
        self._delivery = None
        self._description = None
        self._ean = None
        self._external = None
        self._id = None
        self._images = None
        self._location = None
        self._name = None
        self._parameters = None
        self._payments = None
        self._product = None
        self._promotion = None
        self._publication = None
        self._selling_mode = None
        self._size_table = None
        self._stock = None
        self._tecdoc_specification = None
        self._updated_at = None
        self._validation = None
        self.discriminator = None

        if additional_services is not None:
            self.additional_services = additional_services
        if after_sales_services is not None:
            self.after_sales_services = after_sales_services
        if attachments is not None:
            self.attachments = attachments
        if category is not None:
            self.category = category
        if compatibility_list is not None:
            self.compatibility_list = compatibility_list
        if contact is not None:
            self.contact = contact
        if created_at is not None:
            self.created_at = created_at
        if delivery is not None:
            self.delivery = delivery
        if description is not None:
            self.description = description
        if ean is not None:
            self.ean = ean
        if external is not None:
            self.external = external
        if id is not None:
            self.id = id
        if images is not None:
            self.images = images
        if location is not None:
            self.location = location
        self.name = name
        if parameters is not None:
            self.parameters = parameters
        if payments is not None:
            self.payments = payments
        if product is not None:
            self.product = product
        if promotion is not None:
            self.promotion = promotion
        if publication is not None:
            self.publication = publication
        if selling_mode is not None:
            self.selling_mode = selling_mode
        if size_table is not None:
            self.size_table = size_table
        if stock is not None:
            self.stock = stock
        if tecdoc_specification is not None:
            self.tecdoc_specification = tecdoc_specification
        if updated_at is not None:
            self.updated_at = updated_at
        if validation is not None:
            self.validation = validation

    @property
    def additional_services(self):
        """Gets the additional_services of this Offer.  # noqa: E501


        :return: The additional_services of this Offer.  # noqa: E501
        :rtype: JustId
        """
        return self._additional_services

    @additional_services.setter
    def additional_services(self, additional_services):
        """Sets the additional_services of this Offer.


        :param additional_services: The additional_services of this Offer.  # noqa: E501
        :type: JustId
        """

        self._additional_services = additional_services

    @property
    def after_sales_services(self):
        """Gets the after_sales_services of this Offer.  # noqa: E501


        :return: The after_sales_services of this Offer.  # noqa: E501
        :rtype: AfterSalesServices
        """
        return self._after_sales_services

    @after_sales_services.setter
    def after_sales_services(self, after_sales_services):
        """Sets the after_sales_services of this Offer.


        :param after_sales_services: The after_sales_services of this Offer.  # noqa: E501
        :type: AfterSalesServices
        """

        self._after_sales_services = after_sales_services

    @property
    def attachments(self):
        """Gets the attachments of this Offer.  # noqa: E501

        List of offer attachments. You can attach up to 7 files to the offer – one per each attachment type as described in <a href=\"/documentation/#operation/createOfferAttachmentUsingPOST\" target=\"_blank\">uploading offer attachments flow</a>.  # noqa: E501

        :return: The attachments of this Offer.  # noqa: E501
        :rtype: list[Attachment]
        """
        return self._attachments

    @attachments.setter
    def attachments(self, attachments):
        """Sets the attachments of this Offer.

        List of offer attachments. You can attach up to 7 files to the offer – one per each attachment type as described in <a href=\"/documentation/#operation/createOfferAttachmentUsingPOST\" target=\"_blank\">uploading offer attachments flow</a>.  # noqa: E501

        :param attachments: The attachments of this Offer.  # noqa: E501
        :type: list[Attachment]
        """

        self._attachments = attachments

    @property
    def category(self):
        """Gets the category of this Offer.  # noqa: E501


        :return: The category of this Offer.  # noqa: E501
        :rtype: Category
        """
        return self._category

    @category.setter
    def category(self, category):
        """Sets the category of this Offer.


        :param category: The category of this Offer.  # noqa: E501
        :type: Category
        """

        self._category = category

    @property
    def compatibility_list(self):
        """Gets the compatibility_list of this Offer.  # noqa: E501


        :return: The compatibility_list of this Offer.  # noqa: E501
        :rtype: CompatibilityList
        """
        return self._compatibility_list

    @compatibility_list.setter
    def compatibility_list(self, compatibility_list):
        """Sets the compatibility_list of this Offer.


        :param compatibility_list: The compatibility_list of this Offer.  # noqa: E501
        :type: CompatibilityList
        """

        self._compatibility_list = compatibility_list

    @property
    def contact(self):
        """Gets the contact of this Offer.  # noqa: E501


        :return: The contact of this Offer.  # noqa: E501
        :rtype: JustId
        """
        return self._contact

    @contact.setter
    def contact(self, contact):
        """Sets the contact of this Offer.


        :param contact: The contact of this Offer.  # noqa: E501
        :type: JustId
        """

        self._contact = contact

    @property
    def created_at(self):
        """Gets the created_at of this Offer.  # noqa: E501

        Creation date: Format (ISO 8601) - yyyy-MM-dd'T'HH:mm:ss.SSSZ. Cannot be modified.  # noqa: E501

        :return: The created_at of this Offer.  # noqa: E501
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this Offer.

        Creation date: Format (ISO 8601) - yyyy-MM-dd'T'HH:mm:ss.SSSZ. Cannot be modified.  # noqa: E501

        :param created_at: The created_at of this Offer.  # noqa: E501
        :type: datetime
        """

        self._created_at = created_at

    @property
    def delivery(self):
        """Gets the delivery of this Offer.  # noqa: E501


        :return: The delivery of this Offer.  # noqa: E501
        :rtype: Delivery
        """
        return self._delivery

    @delivery.setter
    def delivery(self, delivery):
        """Sets the delivery of this Offer.


        :param delivery: The delivery of this Offer.  # noqa: E501
        :type: Delivery
        """

        self._delivery = delivery

    @property
    def description(self):
        """Gets the description of this Offer.  # noqa: E501


        :return: The description of this Offer.  # noqa: E501
        :rtype: StandardizedDescription
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this Offer.


        :param description: The description of this Offer.  # noqa: E501
        :type: StandardizedDescription
        """

        self._description = description

    @property
    def ean(self):
        """Gets the ean of this Offer.  # noqa: E501


        :return: The ean of this Offer.  # noqa: E501
        :rtype: str
        """
        return self._ean

    @ean.setter
    def ean(self, ean):
        """Sets the ean of this Offer.


        :param ean: The ean of this Offer.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                ean is not None and len(ean) > 18):
            raise ValueError("Invalid value for `ean`, length must be less than or equal to `18`")  # noqa: E501

        self._ean = ean

    @property
    def external(self):
        """Gets the external of this Offer.  # noqa: E501


        :return: The external of this Offer.  # noqa: E501
        :rtype: ExternalId
        """
        return self._external

    @external.setter
    def external(self, external):
        """Sets the external of this Offer.


        :param external: The external of this Offer.  # noqa: E501
        :type: ExternalId
        """

        self._external = external

    @property
    def id(self):
        """Gets the id of this Offer.  # noqa: E501


        :return: The id of this Offer.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Offer.


        :param id: The id of this Offer.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def images(self):
        """Gets the images of this Offer.  # noqa: E501


        :return: The images of this Offer.  # noqa: E501
        :rtype: list[ImageUrl]
        """
        return self._images

    @images.setter
    def images(self, images):
        """Sets the images of this Offer.


        :param images: The images of this Offer.  # noqa: E501
        :type: list[ImageUrl]
        """

        self._images = images

    @property
    def location(self):
        """Gets the location of this Offer.  # noqa: E501


        :return: The location of this Offer.  # noqa: E501
        :rtype: Location
        """
        return self._location

    @location.setter
    def location(self, location):
        """Sets the location of this Offer.


        :param location: The location of this Offer.  # noqa: E501
        :type: Location
        """

        self._location = location

    @property
    def name(self):
        """Gets the name of this Offer.  # noqa: E501

        Name of the offer. Words used in the name field cannot be longer than 30 characters.  # noqa: E501

        :return: The name of this Offer.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Offer.

        Name of the offer. Words used in the name field cannot be longer than 30 characters.  # noqa: E501

        :param name: The name of this Offer.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                name is not None and len(name) > 50):
            raise ValueError("Invalid value for `name`, length must be less than or equal to `50`")  # noqa: E501

        self._name = name

    @property
    def parameters(self):
        """Gets the parameters of this Offer.  # noqa: E501


        :return: The parameters of this Offer.  # noqa: E501
        :rtype: list[Parameter]
        """
        return self._parameters

    @parameters.setter
    def parameters(self, parameters):
        """Sets the parameters of this Offer.


        :param parameters: The parameters of this Offer.  # noqa: E501
        :type: list[Parameter]
        """

        self._parameters = parameters

    @property
    def payments(self):
        """Gets the payments of this Offer.  # noqa: E501


        :return: The payments of this Offer.  # noqa: E501
        :rtype: Payments
        """
        return self._payments

    @payments.setter
    def payments(self, payments):
        """Sets the payments of this Offer.


        :param payments: The payments of this Offer.  # noqa: E501
        :type: Payments
        """

        self._payments = payments

    @property
    def product(self):
        """Gets the product of this Offer.  # noqa: E501


        :return: The product of this Offer.  # noqa: E501
        :rtype: JustId
        """
        return self._product

    @product.setter
    def product(self, product):
        """Sets the product of this Offer.


        :param product: The product of this Offer.  # noqa: E501
        :type: JustId
        """

        self._product = product

    @property
    def promotion(self):
        """Gets the promotion of this Offer.  # noqa: E501


        :return: The promotion of this Offer.  # noqa: E501
        :rtype: Promotion
        """
        return self._promotion

    @promotion.setter
    def promotion(self, promotion):
        """Sets the promotion of this Offer.


        :param promotion: The promotion of this Offer.  # noqa: E501
        :type: Promotion
        """

        self._promotion = promotion

    @property
    def publication(self):
        """Gets the publication of this Offer.  # noqa: E501


        :return: The publication of this Offer.  # noqa: E501
        :rtype: Publication
        """
        return self._publication

    @publication.setter
    def publication(self, publication):
        """Sets the publication of this Offer.


        :param publication: The publication of this Offer.  # noqa: E501
        :type: Publication
        """

        self._publication = publication

    @property
    def selling_mode(self):
        """Gets the selling_mode of this Offer.  # noqa: E501


        :return: The selling_mode of this Offer.  # noqa: E501
        :rtype: SellingMode
        """
        return self._selling_mode

    @selling_mode.setter
    def selling_mode(self, selling_mode):
        """Sets the selling_mode of this Offer.


        :param selling_mode: The selling_mode of this Offer.  # noqa: E501
        :type: SellingMode
        """

        self._selling_mode = selling_mode

    @property
    def size_table(self):
        """Gets the size_table of this Offer.  # noqa: E501


        :return: The size_table of this Offer.  # noqa: E501
        :rtype: JustId
        """
        return self._size_table

    @size_table.setter
    def size_table(self, size_table):
        """Sets the size_table of this Offer.


        :param size_table: The size_table of this Offer.  # noqa: E501
        :type: JustId
        """

        self._size_table = size_table

    @property
    def stock(self):
        """Gets the stock of this Offer.  # noqa: E501


        :return: The stock of this Offer.  # noqa: E501
        :rtype: Stock
        """
        return self._stock

    @stock.setter
    def stock(self, stock):
        """Sets the stock of this Offer.


        :param stock: The stock of this Offer.  # noqa: E501
        :type: Stock
        """

        self._stock = stock

    @property
    def tecdoc_specification(self):
        """Gets the tecdoc_specification of this Offer.  # noqa: E501


        :return: The tecdoc_specification of this Offer.  # noqa: E501
        :rtype: TecdocSpecification
        """
        return self._tecdoc_specification

    @tecdoc_specification.setter
    def tecdoc_specification(self, tecdoc_specification):
        """Sets the tecdoc_specification of this Offer.


        :param tecdoc_specification: The tecdoc_specification of this Offer.  # noqa: E501
        :type: TecdocSpecification
        """

        self._tecdoc_specification = tecdoc_specification

    @property
    def updated_at(self):
        """Gets the updated_at of this Offer.  # noqa: E501

        Last update date: Format (ISO 8601) - yyyy-MM-dd'T'HH:mm:ss.SSSZ. Cannot be modified  # noqa: E501

        :return: The updated_at of this Offer.  # noqa: E501
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this Offer.

        Last update date: Format (ISO 8601) - yyyy-MM-dd'T'HH:mm:ss.SSSZ. Cannot be modified  # noqa: E501

        :param updated_at: The updated_at of this Offer.  # noqa: E501
        :type: datetime
        """

        self._updated_at = updated_at

    @property
    def validation(self):
        """Gets the validation of this Offer.  # noqa: E501


        :return: The validation of this Offer.  # noqa: E501
        :rtype: Validation
        """
        return self._validation

    @validation.setter
    def validation(self, validation):
        """Sets the validation of this Offer.


        :param validation: The validation of this Offer.  # noqa: E501
        :type: Validation
        """

        self._validation = validation

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
        if not isinstance(other, Offer):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Offer):
            return True

        return self.to_dict() != other.to_dict()