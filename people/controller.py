from flask_restx import Resource, Namespace

from people.serializer import people
from people.service import get_people, add_a_person, get_by_id, delete_a_person

api = Namespace("people", description="people related operations")


@api.route("/")
class PeopleList(Resource):
    @api.doc("list_people")
    @api.marshal_list_with(people)
    def get(self):
        """List all people"""
        persons = get_people()
        return [e.serialize() for e in persons]

    @api.doc("add_person")
    @api.expect(people)
    @api.marshal_with(people, code=201)
    def post(self):
        """add a person"""
        return add_a_person(api.payload), 201


@api.route("/<id>")
@api.param("id", "The person identifier")
@api.response(404, "person not found")
class People(Resource):
    @api.doc("get_person")
    @api.marshal_with(people)
    def get(self, id):
        """Fetch a person given its identifier"""
        person = get_by_id(id)
        if person:
            return person.serialize()
        api.abort(404)

    @api.doc("delete_person")
    @api.response(204, "Person deleted")
    def delete(self, id):
        """Delete a person given its identifier"""
        delete_a_person(id)
        return "", 204

    # @api.expect(people)
    # @api.marshal_with(people)
    # def put(self, id):
    #     """Update a task given its identifier"""
    #     return DAO.update(id, api.payload)



