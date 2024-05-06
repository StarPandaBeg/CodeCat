from sqlite3 import Connection as SQLite3Connection
from sqlalchemy import Engine, event


@event.listens_for(Engine, "connect")
def _set_sqlite_pragma(dbapi_connection, connection_record):
    if isinstance(dbapi_connection, SQLite3Connection):
        cursor = dbapi_connection.cursor()
        cursor.execute("PRAGMA foreign_keys=ON;")
        cursor.close()

        dbapi_connection.create_collation("NOCASE", ignore_case_collation)
        dbapi_connection.create_function("LOWER", 1, sqlite_lower)
        dbapi_connection.create_function("UPPER", 1, sqlite_upper)


def sqlite_lower(value_):
    # That's required for case-insensitive search
    return value_.lower()


def sqlite_upper(value_):
    # That's required for case-insensitive search
    return value_.upper()


def ignore_case_collation(value1_, value2_):
    # That's required for case-insensitive search
    if value1_.lower() == value2_.lower():
        return 0
    elif value1_.lower() < value2_.lower():
        return -1
    else:
        return 1
