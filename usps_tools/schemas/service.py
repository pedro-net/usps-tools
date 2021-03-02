from marshmallow import fields, Schema


class Service(Schema):
    """
    """
    unique_id = fields.Integer(required=True, strict=True)
    name = fields.String(required=True)
    rate = fields.Decimal(places=2, required=True)
    is_international = fields.Boolean()
    extra_services = fields.Nested('ExtraService', many=True)
