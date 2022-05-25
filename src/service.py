from sqlalchemy.orm import Session
from . import models, schemas

def get_characters(db: Session, skip: int = 0, limit: int = 20):
    return db.query(models.Character).offset(skip).limit(limit).all();

def create_character(db: Session, character: schemas.CharacterBase):
    db_character = models.Character(**character.dict());
    db.add(db_character);
    db.commit();
    db.refresh(db_character);
    return db_character;

def get_character_by_id(db: Session, id: int):
    return db.query(models.Character).filter(models.Character.id == id).first()
