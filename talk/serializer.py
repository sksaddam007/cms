from flask_restx import fields
from people.serializer import people

from cms_namespace import api

talk = api.model(
    "Talk",
    {
        "id": fields.String(required=True, description="The talk identifier"),
        "title": fields.String(required=False, description="The talk title"),
        "description": fields.String(required=False, description="The talk description"),
        "duration": fields.String(required=False, description="The talk duration"),
        "date_time": fields.DateTime(required=False, description="The talk date and time"),
        "speakers": fields.List(fields.Nested(people, skip_none=True, description="The talk speakers")),
        "participants": fields.List(fields.Nested(people, skip_none=True, description="The talk participants"))
    },
)
