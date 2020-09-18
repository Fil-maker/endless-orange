import sqlalchemy
from sqlalchemy_serializer import SerializerMixin

from data.db_session import SqlAlchemyBase


class Quests(SqlAlchemyBase, SerializerMixin):
    __tablename__ = 'quests'

    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)
    quest = sqlalchemy.Column(sqlalchemy.String)
    image = sqlalchemy.Column(sqlalchemy.Boolean)
    erudition = sqlalchemy.Column(sqlalchemy.Boolean)
    leader = sqlalchemy.Column(sqlalchemy.Boolean)
    players = sqlalchemy.Column(sqlalchemy.Boolean)
