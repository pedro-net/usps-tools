from typing import List
import marshmallow
from marshmallow import class_registry
from .. import exceptions, models, schemas


class PackageServices:
    """
    PackageServices model.
    """

    @staticmethod
    def get_instance(data) -> 'PackageServices':
        """
        :param data:
        :return:
        :raise ValidationError:
        """
        #
        # Package
        #
        package_schema = class_registry.get_class('Package')()
        try:
            params_package = package_schema.load(data.pop('package', {}))
        except marshmallow.exceptions.ValidationError as e:
            params_package = e.valid_data
        #
        # Services
        #
        service_schema = class_registry.get_class('Service')()
        try:
            params_services = service_schema.load(data.pop('services', []), many=True)
        except marshmallow.exceptions.ValidationError as e:
            params_services = e.valid_data
        #
        # Params
        #
        try:
            params = schemas.PackageServices().load(data)
        except marshmallow.exceptions.ValidationError as e:
            raise exceptions.ValidationError(origin=e)
        params['package'] = models.Package(**params_package) if params_package else None
        params['services'] = [models.Service(**param_service) for param_service in params_services]
        #
        #
        return PackageServices(**params)

    def __init__(self,
                 package: models.Package,
                 services: List[models.Service] = [],
                 error_message: str = '',
                 error_dict: dict = {},
                 ):
        """
        :param package:
        :param services:
        :param error_message:
        """
        self.package = package  # type: models.Package
        self.services = services  # type: List[models.Service]
        self.error_message = error_message  # type: str
        self.error_dict = error_dict  # type: dict
