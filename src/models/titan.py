from sqlalchemy import Column, Enum, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from ..schemas.titan import AllegianceChoises
from ..database import Base

class Titan(Base):
    __tablename__ = "titans"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    other_names = Column(String)
    abilities = Column(String)
    allegiance = Column(Enum(AllegianceChoises), default=AllegianceChoises.ELDIA)
    owner_id = Column(Integer, ForeignKey('characters.id'))

    owner = relationship("Character", uselist=False, foreign_keys=[owner_id], back_populates="titan")