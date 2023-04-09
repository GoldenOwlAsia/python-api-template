# build a schema using pydantic
from pydantic import BaseModel
from datetime import datetime

class User(BaseModel):
    id: int
    username: str
    password: str
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True
