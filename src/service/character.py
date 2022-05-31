from sqlalchemy import and_
from sqlalchemy.orm import Session

from ..models.character import Character
from ..schemas.character import CharacterBase

def get_character_list(db: Session, skip: int = 0, limit: int = 20, name: str | None = None):
    search = "%{}%".format(name)
    filters = []

    if name is not None:
        filters.append(Character.full_name.like(search))

    return db.query(Character).filter(and_(*filters)).offset(skip).limit(limit).all();

def create_character(db: Session, character: CharacterBase):
    db_character = Character(**character.dict());
    db.add(db_character);
    db.commit();
    db.refresh(db_character);
    return db_character;

def get_character_by_id(db: Session, id: int):
    return db.query(Character).filter_by(id=id).first();

def update_character(db: Session, id: int, update_data: CharacterBase):
    db_char = db.query(Character).filter_by(id=id);
    db_char.update(update_data.dict());
    db.commit();

def delete_character(db: Session, id: int):
    db.query(Character).filter_by(id=id).delete();
    db.commit();