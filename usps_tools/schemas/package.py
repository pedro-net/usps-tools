from marshmallow import fields, Schema


class Package(Schema):
    """
    """
    unique_id = fields.Integer(required=True, strict=True)
    weight = fields.Decimal(places=2, required=True)
    width = fields.Decimal(places=2, required=True)
    length = fields.Decimal(places=2, required=True)
    height = fields.Decimal(places=2, required=True)
    value_of_contents = fields.Decimal(places=2)
    country = fields.String(required=True)
    origin_zip = fields.String(allow_none=True)
    acceptance_date_time = fields.DateTime(allow_none=True)
    destination_postal_code = fields.String(allow_none=True)
    zip_origination = fields.String(allow_none=True)
    zip_destination = fields.String(allow_none=True)
