import datetime as dt
from typing import List, Optional
import marshmallow
from .. import exceptions, schemas


class Package:
    """
    Package model.

    IntlRateV2Response / Package
    RateV4Request / Package
    """

    @staticmethod
    def get_instance(data) -> 'Package':
        """
        :param data:
        :return:
        """
        try:
            return Package(**schemas.Package().load(data))
        except marshmallow.exceptions.ValidationError as e:
            raise exceptions.ValidationError(origin=e)

    @staticmethod
    def get_instances(data) -> List['Package']:
        """
        :param data:
        :return:
        """
        try:
            return [Package(**values) for values in schemas.Package().load(data, many=True)]
        except marshmallow.exceptions.ValidationError as e:
            raise exceptions.ValidationError(origin=e)

    def __init__(self,
                 unique_id: Optional[int] = None,
                 weight: Optional[float] = None,
                 width: Optional[float] = None,
                 length: Optional[float] = None,
                 height: Optional[float] = None,
                 value_of_contents: Optional[float] = None,
                 country: Optional[str] = None,
                 origin_zip: Optional[str] = None,
                 acceptance_date_time: Optional[dt.datetime] = None,
                 destination_postal_code: Optional[str] = None,
                 zip_origination: Optional[str] = None,
                 zip_destination: Optional[str] = None,
                 ):
        """
        :param unique_id:
        """
        self.unique_id = unique_id  # type: Optional[int]
        self.weight = weight  # type: Optional[float]
        self.width = width  # type: Optional[float]
        self.length = length  # type: Optional[float]
        self.height = height  # type: Optional[float]
        self.value_of_contents = value_of_contents  # type: Optional[float]
        self.country = country  # type: Optional[str]
        self.origin_zip = origin_zip  # type: Optional[str]
        self.acceptance_date_time = acceptance_date_time  # type: Optional[dt.datetime]
        self.destination_postal_code = destination_postal_code  # type: Optional[str]
        self.zip_origination = zip_origination  # type: Optional[str]
        self.zip_destination = zip_destination  # type: Optional[str]

        self._schema = schemas.Package()

    def __repr__(self):
        return "<Package ID: {}>".format(self.unique_id)

    def check_is_domestic_shipping(self) -> bool:
        """
        :return:
        """
        return self.country and self.country.lower() == 'united states'

    def to_dict(self) -> dict:
        """
        :return:
        """
        return self._schema.dump(self)

    def validate(self) -> dict:
        """
        Validate against schema.
        :return:
        """
        return self._schema.validate(self._schema.dump(self))
