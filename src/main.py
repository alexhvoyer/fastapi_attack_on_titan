from fastapi import Body, Depends, FastAPI, status
from sqlalchemy.orm import Session
from . import models, database, service, schemas

models.Base.metadata.create_all(bind=database.engine)
app = FastAPI()

def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]

@app.get('/')
async def root():
    return { 'message': 'Hello' }

@app.get('/characters')
async def getCharacters(skip: int = 0, limit: int = 20, db: Session = Depends(get_db)):
    return service.get_characters(db, skip, limit)

@app.post('/characters', status_code=status.HTTP_201_CREATED, response_model=schemas.Character)
async def createCharacter(character: schemas.CharacterBase = Body(..., example=schemas.character_example), db: Session = Depends(get_db)):
    characted_db = service.create_character(db, character)
    return characted_db.__dict__

@app.get('/characters/{id}', response_model=schemas.CharacterOut)
async def getCharacterById(id: str, db: Session = Depends(get_db)):
    return service.get_character_by_id(db, id)