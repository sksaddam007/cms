from flask_restx import Resource, Namespace

from conference.serializer import conference
from conference.service import get_conference_list, add_a_conference, get_by_id, delete_a_conference, \
    update_a_conference, add_a_talk_in_conference, remove_a_talk_in_conference

api = Namespace("conference", description="conference related operations")


@api.route("/")
class ConferenceList(Resource):
    @api.doc("list_conferences")
    @api.marshal_list_with(conference)
    def get(self):
        """List all conferences"""
        conferences = get_conference_list()
        return [e.serialize() for e in conferences]

    @api.doc("add_conference")
    @api.expect(conference)
    @api.marshal_with(conference, code=201)
    def post(self):
        """add a conference"""
        return add_a_conference(api.payload), 201


@api.route("/<id>")
@api.param("id", "The conference identifier")
@api.response(404, "conference not found")
class Conference(Resource):
    @api.doc("get_conference")
    @api.marshal_with(conference)
    def get(self, id):
        """Fetch a conference given its identifier"""
        aconference = get_by_id(id)
        if aconference:
            return aconference.serialize()
        api.abort(404)

    @api.doc("delete_conference")
    @api.response(204, "conference deleted")
    def delete(self, id):
        """Delete a conference given its identifier"""
        delete_a_conference(id)
        return "", 204

    @api.expect(conference)
    @api.marshal_with(conference)
    def put(self, id):
        """Update a conference given its identifier"""
        aconference = update_a_conference(api.payload, id)
        if aconference:
            return aconference.serialize(), 200
        return "Conference not found", 404


@api.route("/<conference_id>/talk/<talk_id>")
@api.param("conference_id", "The conference talk identifier")
@api.param("talk_id", "The talk conference reference")
@api.response(404, "conference not found")
class ConferenceTalks(Resource):

    @api.marshal_with(conference)
    def post(self, conference_id, talk_id):
        """add a talk to a given conference identifier"""
        aconference = add_a_talk_in_conference(conference_id, talk_id)
        if aconference:
            return aconference.serialize(), 200
        return "Conference not found", 404

    @api.marshal_with(conference)
    def delete(self, conference_id, talk_id):
        """remove a talk to a given conference identifier"""
        aconference = remove_a_talk_in_conference(conference_id, talk_id)
        if aconference:
            return aconference.serialize(), 200
        return "Conference not found", 404

