from sqlalchemy.orm import Session

from src.models.character import Character

from ..schemas.titan import TitanCreate
from ..models.titan import Titan

def create_titan(db: Session, titan: TitanCreate):
    db_titan = Titan(**titan.dict());
    db.add(db_titan);
    db.commit();
    db.refresh(db_titan);
    return db_titan;

def get_titan_by_id(db: Session, id: int):
    return db.query(Titan).filter(Titan.id == id).first()