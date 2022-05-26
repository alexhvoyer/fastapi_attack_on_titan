from fastapi import FastAPI

from .models.character import Base
from . import database
from .routes import character

Base.metadata.create_all(bind=database.engine)
app = FastAPI()


@app.get('/')
async def root():
    return {'message': 'Hello'}

app.include_router(character.router)
