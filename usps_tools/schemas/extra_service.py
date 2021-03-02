from marshmallow import fields, Schema


class ExtraService(Schema):
    """
    ExtraService schema.
    """
    unique_id = fields.Integer(required=True, strict=True)
    name = fields.String(default='')
    available = fields.Boolean()
    price = fields.Decimal(places=2, required=True)
