import os

from flask import Flask
from flask_migrate import Migrate
from werkzeug.middleware.proxy_fix import ProxyFix

from cms_namespace import api, db
from people.controller import api as people_api
from conference.controller import api as conference_api
from talk.controller import api as talk_api

app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

migrate = Migrate(app, db)

app.wsgi_app = ProxyFix(app.wsgi_app)

api.init_app(app)
api.add_namespace(people_api)
api.add_namespace(conference_api)
api.add_namespace(talk_api)


if __name__ == '__main__':
    app.run(debug=True)
