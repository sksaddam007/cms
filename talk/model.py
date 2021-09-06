from cms_namespace import db


class Talk(db.Model):
    __tablename__ = 'talk'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(100), nullable=False)
    duration = db.Column(db.String(100), nullable=False)
    date_time = db.Column(db.DateTime, nullable=False)
    conference_id = db.Column(db.Integer, db.ForeignKey('conference.id'))
    speakers = db.relationship("Person", backref="talk_speaker", foreign_keys="Person.talk_speaker_id", lazy='dynamic')
    participants = db.relationship("Person", backref="talk_participant", foreign_keys="Person.talk_participant_id", lazy='dynamic')

    def __init__(self, title, description, duration, date_time):
        self.title = title
        self.description = description
        self.duration = duration
        self.date_time = date_time

    def __repr__(self):
        return '<id {}>'.format(self.id)

    def serialize(self):
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'duration': self.duration,
            'date_time': self.date_time,
            'speakers': self.speakers,
            'participants': self.participants

        }
