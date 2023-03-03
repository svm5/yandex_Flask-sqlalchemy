import datetime
import sqlalchemy
from sqlalchemy import orm
from flask_login import UserMixin

from .db_session import SqlAlchemyBase

class User(SqlAlchemyBase, UserMixin):
    __tablename__ = 'users'

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    email = sqlalchemy.Column(sqlalchemy.String, index=True, unique=True, nullable=True)
    password = sqlalchemy.Column(sqlalchemy.String, index=True, unique=True, nullable=True)
    remember_me = sqlalchemy.Column(sqlalchemy.Boolean, nullable=True)

    # jobs = orm.relationship("Jobs", back_populates='user')

    def __repr__(self) -> str:
        return str(self.id) + " " + self.email
    

    def check_password(self, entered_password):
        print(self.password)
        return entered_password == self.password

