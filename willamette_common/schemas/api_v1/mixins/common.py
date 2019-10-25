from marshmallow import fields


class SourceAccounting:
    datetime_acquired = fields.DateTime()
    data_origin = fields.String(required=True)
