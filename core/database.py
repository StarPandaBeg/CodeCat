from sqlalchemy import DDLElement, Engine, create_engine, event
from sqlalchemy.ext.compiler import compiles
from sqlalchemy.orm import scoped_session, sessionmaker, declarative_base
from sqlite3 import Connection as SQLite3Connection

from bootstrap.config import app_config

engine = create_engine(app_config['DATABASE_URL'])
db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))
Base = declarative_base()
Base.query = db_session.query_property()

# use it for helper tables like fts
# models with this base are not created automatically
Base2 = declarative_base()
Base2.query = db_session.query_property()


def init_db():
    import core.models
    Base.metadata.create_all(bind=engine)


@event.listens_for(Engine, "connect")
def _set_sqlite_pragma(dbapi_connection, connection_record):
    if isinstance(dbapi_connection, SQLite3Connection):
        cursor = dbapi_connection.cursor()
        cursor.execute("PRAGMA foreign_keys=ON;")
        cursor.close()


class CreateFtsTable(DDLElement):
    """Represents a CREATE VIRTUAL TABLE ... USING fts5 statement, for indexing
    a given table.
    """

    def __init__(self, table, version=5):
        self.table = table
        self.version = version


@compiles(CreateFtsTable)
def compile_create_fts_table(element, compiler, **kw):
    tbl = element.table
    version = element.version
    preparer = compiler.preparer

    vtbl_name = preparer.quote(tbl.__table__.name)

    columns = [x.name for x in tbl.__mapper__.columns]
    columns.append('tokenize="porter unicode61"')
    columns = ', '.join(columns)

    return f"CREATE VIRTUAL TABLE IF NOT EXISTS {vtbl_name} USING FTS{version} ({columns})"
