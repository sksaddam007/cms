from flask_restx import Resource, Namespace

from talk.serializer import talk
from talk.service import get_talk_list, add_a_talk, get_by_id, delete_a_talk, update_a_talk, add_a_speaker_to_talk, \
    remove_a_speaker_to_talk, add_a_participant_to_talk, remove_a_participant_to_talk

api = Namespace("talk", description="talk related operations")


@api.route("/")
class TalkList(Resource):
    @api.doc("list_talks")
    @api.marshal_list_with(talk)
    def get(self):
        """List all talks"""
        talks = get_talk_list()
        return [e.serialize() for e in talks]

    @api.doc("add_talk")
    @api.expect(talk)
    @api.marshal_with(talk, code=201)
    def post(self):
        """add a talk"""
        return add_a_talk(api.payload), 201


@api.route("/<id>")
@api.param("id", "The talk identifier")
@api.response(404, "talk not found")
class Talk(Resource):
    @api.doc("get_talk")
    @api.marshal_with(talk)
    def get(self, id):
        """Fetch a talk given its identifier"""
        atalk = get_by_id(id)
        if atalk:
            return atalk.serialize()
        api.abort(404)

    @api.doc("delete_talk")
    @api.response(204, "talk deleted")
    def delete(self, id):
        """Delete a talk given its identifier"""
        delete_a_talk(id)
        return "", 204

    @api.expect(talk)
    @api.marshal_with(talk)
    def put(self, id):
        """Update a conference given its identifier"""
        atalk = update_a_talk(api.payload, id)
        if atalk:
            return atalk.serialize(), 200
        return "Talk not found", 404


@api.route("/<talk_id>/speaker/<speaker_id>")
@api.param("talk_id", "The talk identifier")
@api.param("speaker_id", "The speaker identifier")
@api.response(404, "talk not found")
class TalkSpeaker(Resource):

    @api.doc("add_talk_speaker")
    @api.expect(talk)
    @api.marshal_with(talk, code=201)
    def post(self, talk_id, speaker_id):
        """add a speaker to talk"""
        return add_a_speaker_to_talk(talk_id, speaker_id), 201

    @api.doc("remove_talk_speaker")
    @api.expect(talk)
    @api.marshal_with(talk, code=201)
    def delete(self, talk_id, speaker_id):
        """remove a speaker to talk"""
        return remove_a_speaker_to_talk(talk_id, speaker_id), 201


@api.route("/<talk_id>/participant/<participant_id>")
@api.param("talk_id", "The talk identifier")
@api.param("participant_id", "The participant identifier")
@api.response(404, "talk not found")
class TalkSpeaker(Resource):

    @api.doc("add_talk_participant")
    @api.expect(talk)
    @api.marshal_with(talk, code=201)
    def post(self, talk_id, participant_id):
        """add a participant to talk"""
        atalk = add_a_participant_to_talk(talk_id, participant_id)
        if atalk:
            return atalk, 201
        api.abort(404)

    @api.doc("remove_talk_participant")
    @api.expect(talk)
    @api.marshal_with(talk, code=201)
    def delete(self, talk_id, participant_id):
        """remove a participant to talk"""
        atalk = remove_a_participant_to_talk(talk_id, participant_id)
        if atalk:
            return atalk, 201
        api.abort(404)
