from flask_restx import fields

from cms_namespace import api

people = api.model(
    "People",
    {
        "id": fields.String(required=True, description="The people identifier"),
        "username": fields.String(required=True, description="The people username"),
        "email": fields.String(required=True, description="The people email")
    },
)
