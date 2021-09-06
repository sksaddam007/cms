from cms_namespace import db, DictMixIn


class Conference(db.Model, DictMixIn):
    __tablename__ = 'conference'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(100), nullable=False)
    start_date = db.Column(db.DateTime, nullable=False)
    end_date = db.Column(db.DateTime, nullable=False)
    talks = db.relationship("Talk", backref="conference", lazy='dynamic')

    def __init__(self, title, description, start_date, end_date):
        self.title = title
        self.description = description
        self.start_date = start_date
        self.end_date = end_date

    def __repr__(self):
        return '<id {}>'.format(self.id)

    def serialize(self):
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'start_date': self.start_date,
            'end_date': self.end_date,
            'talks': self.talks
        }
