from pydantic import BaseModel, Field
from enum import Enum

class StatusChoises(Enum):
    ALIVE = 'alive'
    DECEASED = 'deceased'
    UNKNOWN = 'unknown'


character_example = {
    'first_name': 'Armin',
    'last_name': 'Arlert',
    'age': 19,
    'species': 'Lol',
    'residence': 'Wall Rose',
    'status': StatusChoises.UNKNOWN
}

class CharacterBase(BaseModel):

    first_name: str = Field(..., title="First name of character", max_length=20);
    last_name: str = Field(..., example="Akkermann");
    age: int = Field(..., gt=0);
    species: str;
    height: int | None = None;
    residence: str;
    status: StatusChoises = StatusChoises.UNKNOWN;

    class Config:
        schema_extra = {
            'example': character_example
        }

class CharacterOut(BaseModel):
    first_name: str;

class Character(CharacterBase):
    id: int;

    class Config:
        orm_mode = True;
