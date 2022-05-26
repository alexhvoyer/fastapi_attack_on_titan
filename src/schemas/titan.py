from enum import Enum

from pydantic import BaseModel, Field


class AllegianceChoises(Enum):
    ELDIA = 'eldia'
    MARLEY = 'marley'

titan_example = {
    'name': 'Attack titan',
    'abilities': 'Attack',
    'allegiance': AllegianceChoises.ELDIA,
    'owner_id': 1
}

class TitanBase(BaseModel):

    name: str = Field(title="Name of titan")
    other_names: str | None = Field(title="Other names of titan")
    abilities: str = Field('List of titan\'s abilities')
    allegiance: AllegianceChoises = AllegianceChoises.ELDIA

    class Config:
        schema_extra = {
            'example': titan_example
        }

class TitanCreate(TitanBase):
    owner_id: int | None = None

class Titan(TitanBase):
    id: int
    owner_id: int | None = None

    class Config:
        orm_mode = True