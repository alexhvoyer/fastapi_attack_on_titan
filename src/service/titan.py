from sqlalchemy.orm import Session

from ..schemas.titan import TitanBase
from ..models.titan import Titan

def create_titan(db: Session, titan: TitanBase):
    db_titan = Titan(**titan.dict());
    db.add(db_titan);
    db.commit();
    db.refresh(db_titan);
    return db_titan;

def get_titan_by_id(db: Session, id: int):
    return db.query(Titan).filter(Titan.id == id).first()