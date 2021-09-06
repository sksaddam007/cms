from flask_restx import Api
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.ext.declarative import declarative_base
import datetime

Base = declarative_base()
db = SQLAlchemy()

api = Api(title="Conference Management System API", version="1.0", description="A simple API")


class DictMixIn:
    def to_dict(self):
        return {
            column.name: getattr(self, column.name)
            if not isinstance(
                getattr(self, column.name), (datetime.datetime, datetime.date)
            )
            else getattr(self, column.name).isoformat()
            for column in self.__table__.columns
        }
