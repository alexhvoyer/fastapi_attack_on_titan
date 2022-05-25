from sqlalchemy import Column, Integer, String, Enum
from .schemas import StatusChoises
from .database import Base

class Character(Base):
    __tablename__ = "characters"

    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String)
    last_name = Column(String)
    age = Column(Integer)
    species = Column(String, nullable=True)
    height = Column(Integer, nullable=True)
    residence = Column(String)
    status = Column(Enum(StatusChoises))