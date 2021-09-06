from cms_namespace import db
from people.service import get_by_id as get_by_person_id
from talk.model import Talk


def get_talk_list():
    return Talk.query.all()


def add_a_talk(data: dict):
    talk = Talk(data.get("title"), data.get("description"), data.get("duration"), data.get("date_time"))
    for participant in data.get("participants"):
        person = get_by_person_id(participant["id"])
        talk.participants.append(person)
    for speaker in data.get("speakers"):
        person = get_by_person_id(speaker["id"])
        talk.speakers.append(person)
    db.session.add(talk)
    db.session.commit()
    return talk


def add_a_speaker_to_talk(talk_id, speaker_id):
    talk = get_by_id(talk_id)
    speaker = get_by_person_id(speaker_id)
    talk.speakers.append(speaker)
    db.session.add(talk)
    db.session.commit()
    return talk


def remove_a_speaker_to_talk(talk_id, speaker_id):
    talk = get_by_id(talk_id)
    speaker = get_by_person_id(speaker_id)
    talk.speakers.remove(speaker)
    db.session.add(talk)
    db.session.commit()
    return talk


def add_a_participant_to_talk(talk_id, participant_id):
    talk = get_by_id(talk_id)
    if not talk:
        return None
    participant = get_by_person_id(participant_id)
    talk.participants.append(participant)
    db.session.add(talk)
    db.session.commit()
    return talk


def remove_a_participant_to_talk(talk_id, participant_id):
    talk = get_by_id(talk_id)
    participant = get_by_person_id(participant_id)
    talk.participants.remove(participant)
    db.session.add(talk)
    db.session.commit()
    return talk


def get_by_id(id):
    return Talk.query.get(id)


def delete_a_talk(id):
    talk = Talk.query.get(id)
    if talk:
        db.session.delete(talk)
        db.session.commit()


def update_a_talk(data: dict, id: int):
    talk = Talk.query.get(id)
    if talk:
        if data.get("title"):
            talk.title = data.get("title")
        if data.get("description"):
            talk.description = data.get("description")
        if data.get("date_time"):
            talk.date_time = data.get("date_time")
        if data.get("duration"):
            talk.duration = data.get("duration")
        if data.get("participants"):
            for participant in data.get("participants"):
                person = get_by_person_id(participant['id'])
                talk.participants.append(person)
        if data.get("speakers"):
            for speaker in data.get("speakers"):
                person = get_by_person_id(speaker['id'])
                talk.speakers.append(person)
        db.session.add(talk)
        db.session.commit()
        return talk
    return None
