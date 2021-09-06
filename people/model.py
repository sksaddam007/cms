from cms_namespace import db


class Person(db.Model):
    __tablename__ = 'person'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    talk_speaker_id = db.Column(db.Integer, db.ForeignKey('talk.id'))
    talk_participant_id = db.Column(db.Integer, db.ForeignKey('talk.id'))

    def __init__(self, username, email):
        self.username = username
        self.email = email

    def __repr__(self):
        return '<id {}>'.format(self.id)

    def serialize(self):
        return {
            'id': self.id,
            'username': self.username,
            'email': self.email
        }
