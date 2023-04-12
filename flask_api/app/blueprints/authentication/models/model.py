from sqlalchemy import Column, String, Text
from sqlalchemy.ext.hybrid import hybrid_property, hybrid_method

from app.ext.sqlalchemy.model import BaseModel, id_column, int_fk_column


class FlaskUser(BaseModel):
    id = id_column()
    pass
