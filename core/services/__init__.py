from typing import Any
from flask import abort
from sqlalchemy.orm import QueryPropertyDescriptor


def get_or_404(query: QueryPropertyDescriptor, ident: Any):
    rv = query.get(ident)  # type: ignore
    if rv == None:
        abort(404, "Model not found")
    return rv
