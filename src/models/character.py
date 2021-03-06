from sqlalchemy import Column, Integer, String, Enum
from sqlalchemy.orm import relationship, column_property

from ..schemas.character import StatusChoises
from ..database import Base


class Character(Base):
    __tablename__ = "characters"

    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String, nullable=False)
    last_name = Column(String)
    age = Column(Integer)
    species = Column(String, nullable=True)
    height = Column(Integer, nullable=True)
    residence = Column(String)
    status = Column(Enum(StatusChoises))
    full_name = column_property(first_name + '' + last_name)

    titan = relationship("Titan", back_populates="owner", uselist=False)
