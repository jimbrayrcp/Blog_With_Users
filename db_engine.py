from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker
import os


SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL",  "sqlite:///blog.db")
engine = create_engine(SQLALCHEMY_DATABASE_URI, convert_unicode=True)
db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))
Base = declarative_base()
Base.query = db_session.query_property()


def init_db():
    """
    Database engine initializer
    :return: database object
    """
    Base.metadata.create_all(bind=engine)