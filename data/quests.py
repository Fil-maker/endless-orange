import sqlalchemy

from data.db_session import SqlAlchemyBase


class Quests(SqlAlchemyBase):
    __tablename__ = 'quests'

    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)
    quest = sqlalchemy.Column(sqlalchemy.String)
