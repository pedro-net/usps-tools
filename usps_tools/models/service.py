from typing import List, Optional
import marshmallow
from marshmallow import class_registry
from .. import exceptions, models, schemas


class Service:
    """
    Service model.

    IntlRateV2Response / Package / Service
    """

    @staticmethod
    def get_instance(data) -> 'Service':
        """
        :param data:
        :return:
        """
        #
        # Extra Services
        #
        extra_service_schema = class_registry.get_class('ExtraService')()
        try:
            params_extra_services = extra_service_schema.load(data.pop('extra_services', []), many=True)
        except marshmallow.exceptions.ValidationError as e:
            params_extra_services = e.valid_data
        #
        # Params
        #
        try:
            params = schemas.Service().load(data)
        except marshmallow.exceptions.ValidationError as e:
            raise exceptions.ValidationError(origin=e)
        params['extra_services'] = [models.ExtraService(**param_extra_service) for param_extra_service in params_extra_services]
        #
        #
        return Service(**params)

    def __init__(self,
                 unique_id: Optional[int] = None,
                 name: Optional[str] = None,
                 rate: Optional[float] = None,
                 is_international: Optional[bool] = None,
                 extra_services: List[models.ExtraService] = [],
                 ):
        """
        :param unique_id:
        """
        self.unique_id = unique_id  # type: Optional[int]
        self.name = name  # type: Optional[str]
        self.rate = rate  # type: Optional[float]
        self.is_international = is_international  # type: Optional[bool]
        self.extra_services = extra_services  # type: List[models.ExtraService]

    def __repr__(self):
        return "<Service ID: {}, Rate: {}>".format(self.unique_id, self.rate)
