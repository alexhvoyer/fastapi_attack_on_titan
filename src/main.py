from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from .models.character import Base
from . import database
from .routes import character, titan

Base.metadata.create_all(bind=database.engine)
app = FastAPI(
    title="Attack on titan Api"
)


@app.get('/')
async def root():
    return {'message': 'Hello'}

app.include_router(character.router)
app.include_router(titan.router)

app.mount('/static', StaticFiles(directory="src/static"), name="static")