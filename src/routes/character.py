from fastapi import APIRouter, Query, status, Depends, Body, HTTPException
from sqlalchemy.orm import Session

from src.utils.errors import create_404_error

from ..service import character as service
from ..schemas.character import CharacterBase, Character, character_example
from ..dependencies import get_db

router = APIRouter(
    prefix='/characters',
    tags=['characters'],
    responses={404: {"description": "Not found"}},
)

exception_404 = create_404_error(detail="Character not found")

@router.get('/')
def get_characters(
    skip: int = 0,
    limit: int = 20,
    name: str | None = Query(default=None, max_length=20, description="Search by name"),
    db: Session = Depends(get_db)
    ):
    return service.get_character_list(db, skip, limit, name)


@router.post('/', status_code=status.HTTP_201_CREATED, response_model=Character)
def create_character(character: CharacterBase = Body(..., example=character_example), db: Session = Depends(get_db)):
    characted_db = service.create_character(db, character)
    return characted_db.__dict__


@router.get('/{id}', response_model=Character)
def get_character_by_id(id: str, db: Session = Depends(get_db)):
    character_db = service.get_character_by_id(db, id);
    if character_db is None:
        raise exception_404
    return character_db

@router.put('/{id}', status_code=status.HTTP_204_NO_CONTENT)
def update_titan(id: str, data: Character, db: Session = Depends(get_db)):
    db_character = service.get_character_by_id(db, id)
    if db_character is None:
        raise exception_404
    service.update_character(db, id, data)


@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
def delete_character(id: str, db: Session = Depends(get_db)):
    service.delete_character(db, id)
