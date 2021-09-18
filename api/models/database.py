from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import os


# class DataBase():
DB_NAME = 'rank.db'

databese_path = os.path.join(os.path.abspath(os.path.dirname(__file__)), DB_NAME)
engine = create_engine('sqlite:///' + databese_path, convert_unicode=True)
db_session = scoped_session(sessionmaker(autocommit=False,autoflush=False,bind=engine))
Base = declarative_base()
Base.query = db_session.query_property()


def init_db():
    Base.metadata.create_all(bind=engine)


class DatabaseBase():

    def __init__(self) -> None:
        super().__init__()
        self.DB_NAME = 'rank.db'

        self.databese_path = os.path.join(os.path.abspath(os.path.dirname(__file__)), DB_NAME)
        self.engine = create_engine('sqlite:///' + databese_path, convert_unicode=True)
        self.db_session = scoped_session(sessionmaker(autocommit=False,autoflush=False,bind=engine))
        self.Base = declarative_base()
        self.Base.query = db_session.query_property()   # なに？

    def init_db():
        Base.metadata.create_all(bind=engine)
