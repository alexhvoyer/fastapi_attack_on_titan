from sqlalchemy.orm import Session

from ..models.character import Character
from ..schemas.character import CharacterBase

def get_characters(db: Session, skip: int = 0, limit: int = 20):
    return db.query(Character).offset(skip).limit(limit).all();

def create_character(db: Session, character: CharacterBase):
    db_character = character.Character(**character.dict());
    db.add(db_character);
    db.commit();
    db.refresh(db_character);
    return db_character;

def get_character_by_id(db: Session, id: int):
    return db.query(Character).filter(Character.id == id).first()
