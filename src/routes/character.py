from fastapi import APIRouter, status, Depends, Body
from sqlalchemy.orm import Session

from ..service.character import create_character, get_character_by_id, get_characters
from ..schemas.character import CharacterBase, CharacterOut, Character, character_example
from ..dependencies import get_db

router = APIRouter(
    prefix='/characters',
    tags=['characters'],
    responses={404: {"description": "Not found"}},
)


@router.get('/')
async def getCharacters(skip: int = 0, limit: int = 20, db: Session = Depends(get_db)):
    return get_characters(db, skip, limit)


@router.post('/', status_code=status.HTTP_201_CREATED, response_model=Character)
async def createCharacter(character: CharacterBase = Body(..., example=character_example), db: Session = Depends(get_db)):
    characted_db = create_character(db, character)
    return characted_db.__dict__


@router.get('/{id}', response_model=CharacterOut)
async def getCharacterById(id: str, db: Session = Depends(get_db)):
    return get_character_by_id(db, id)
