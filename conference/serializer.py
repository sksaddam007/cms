from flask_restx import fields
from talk.serializer import talk

from cms_namespace import api

conference = api.model(
    "Conference",
    {
        "id": fields.String(required=True, description="The conference identifier"),
        "title": fields.String(required=False, description="The conference title"),
        "description": fields.String(required=False, description="The conference description"),
        "start_date": fields.DateTime(required=False, description="The conference start date and time"),
        "end_date": fields.DateTime(required=False, description="The conference end date and time"),
        "talks": fields.List(fields.Nested(talk, skip_none=True))
    },
)
