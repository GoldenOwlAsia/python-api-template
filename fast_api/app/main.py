from fastapi import FastAPI

from api.v1.routes import users

app = FastAPI()

app.include_router(router=users.router)
