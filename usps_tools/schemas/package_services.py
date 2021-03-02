from marshmallow import fields, Schema


class PackageServices(Schema):
    """
    PackageServices schema.
    """
    package = fields.Nested('Package', required=True)
    services = fields.Nested('Service', many=True)
    error_message = fields.String(default='')
