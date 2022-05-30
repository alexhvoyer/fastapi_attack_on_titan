from sqlalchemy import and_
from sqlalchemy.orm import Session

from ..schemas.titan import TitanCreate
from ..models.titan import Titan

def create_titan(db: Session, titan: TitanCreate):
    db_titan = Titan(**titan.dict());
    db.add(db_titan);
    db.commit();
    db.refresh(db_titan);
    return db_titan.__dict__;

def get_titan_list(db: Session, offset: int = 0, limit: int = 20, name: str | None = None):
    search = "%{}%".format(name)
    filters = []

    if name is not None:
        filters.append(Titan.name.like(search))

    return db.query(Titan).filter(and_(*filters)).offset(offset).limit(limit).all();

def get_titan_by_id(db: Session, id: int):
    return db.query(Titan).filter_by(id=id).first();

def update_titan(db: Session, id: int, update_data: TitanCreate):
    db_titan = db.query(Titan).filter_by(id=id);
    db_titan.update(update_data.dict());
    db.commit();

def delete_titan(db: Session, id: int):
    db.query(Titan).filter_by(id=id).delete();
    db.commit();