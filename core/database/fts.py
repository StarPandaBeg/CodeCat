from sqlalchemy import DDLElement
from sqlalchemy.ext.compiler import compiles


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
