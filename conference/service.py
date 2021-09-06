from cms_namespace import db
from conference.model import Conference
from talk.service import get_by_id as get_by_talk_id


def get_conference_list():
    return Conference.query.all()


def add_a_conference(data: dict):
    conference = Conference(data.get("title"), data.get("description"), data.get("start_date"), data.get("end_date"))
    for talk in data.get("talks"):
        talk = get_by_talk_id(talk["id"])
        conference.talks.append(talk)
    db.session.add(conference)
    db.session.commit()
    return conference


def get_by_id(id):
    return Conference.query.get(id)


def delete_a_conference(id):
    conference = Conference.query.get(id)
    if conference:
        db.session.delete(conference)
        db.session.commit()


def remove_a_talk_in_conference(conference_id, talk_id):
    conference = Conference.query.get(conference_id)
    if not conference:
        return None
    talk = get_by_talk_id(talk_id)
    conference.talks.remove(talk)
    db.session.add(conference)
    db.session.commit()
    return conference


def add_a_talk_in_conference(conference_id, talk_id):
    conference = Conference.query.get(conference_id)
    if not conference:
        return None
    talk = get_by_talk_id(talk_id)
    conference.talks.append(talk)
    db.session.add(conference)
    db.session.commit()
    return conference


def update_a_conference(data: dict, id: int):
    conference = Conference.query.get(id)
    if conference:
        if data.get("title"):
            conference.title = data.get("titile")
        if data.get("description"):
            conference.description = data.get("description")
        if data.get("start_date"):
            conference.start_date = data.get("start_date")
        if data.get("end_date"):
            conference.end_date = data.get("end_date")
        if data.get("talks"):
            for talk in data.get("talks"):
                talk = get_by_talk_id(talk["id"])
                conference.talks.append(talk)
        db.session.add(conference)
        db.session.commit()
        return conference
    return None
