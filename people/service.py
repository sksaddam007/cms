from cms_namespace import db
from people.model import Person


def get_people():
    return Person.query.all()


def add_a_person(data: dict):
    person = Person(data.get("username"), data.get("email"))
    db.session.add(person)
    db.session.commit()
    return person


def get_by_id(id):
    return Person.query.get(id)


def delete_a_person(id):
    person = Person.query.get(id)
    if person:
        db.session.remove(person)
        db.session.commit()
