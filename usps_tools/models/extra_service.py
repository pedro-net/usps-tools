from typing import Optional
import marshmallow
from .. import exceptions, models, schemas


class ExtraService:
    """
    ExtraService mode.

    IntlRateV2Response / Package / Service / ExtraServices / ExtraService
    """

    @staticmethod
    def get_instance(data) -> models.Package:
        """
        :param data:
        :return:
        """
        try:
            return ExtraService(**schemas.ExtraService().load(data))
        except marshmallow.exceptions.ValidationError as e:
            raise exceptions.ValidationError(origin=e)

    def __init__(self,
                 unique_id: Optional[int] = None,
                 name: Optional[str] = None,
                 available: Optional[bool] = None,
                 price: Optional[float] = None,
                 ):
        """
        :param unique_id:
        """
        self.unique_id = unique_id  # type: Optional[int]
        self.name = name  # type: Optional[str]
        self.available = available  # type: Optional[bool]
        self.price = price  # type: Optional[float]

    def __repr__(self):
        return "<ExtraService ID: {}, Price: {}>".format(self.unique_id, self.price)
