from sqlalchemy import create_engine
from sqlalchemy.ext.compiler import compiles
from sqlalchemy.orm import scoped_session, sessionmaker, declarative_base

from .fts import *
from .util import *

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
