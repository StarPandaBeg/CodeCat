from sqlalchemy import Engine, create_engine, event
from sqlalchemy.orm import scoped_session, sessionmaker, declarative_base
from sqlite3 import Connection as SQLite3Connection

from bootstrap.config import app_config

engine = create_engine(app_config['DATABASE_URL'])
db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))
Base = declarative_base()
Base.query = db_session.query_property()


def init_db():
    import core.models
    Base.metadata.create_all(bind=engine)


@event.listens_for(Engine, "connect")
def _set_sqlite_pragma(dbapi_connection, connection_record):
    if isinstance(dbapi_connection, SQLite3Connection):
        cursor = dbapi_connection.cursor()
        cursor.execute("PRAGMA foreign_keys=ON;")
        cursor.close()
