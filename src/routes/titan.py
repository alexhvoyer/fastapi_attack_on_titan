from fastapi import APIRouter, status, Depends, Body
from sqlalchemy.orm import Session

from ..service.titan import create_titan, get_titan_by_id
from ..schemas.titan import TitanCreate, Titan, titan_example
from ..dependencies import get_db

router = APIRouter(
    prefix='/titans',
    tags=['titans'],
    responses={404: {"description": "Not found"}},
)


@router.post('/', status_code=status.HTTP_201_CREATED, response_model=Titan)
def create_titan(titan: TitanCreate = Body(..., example=titan_example), db: Session = Depends(get_db)):
    titan_db = create_titan(db, titan)
    return titan_db.__dict__

@router.get('/{id}')
def get_titan(id: str, db: Session = Depends(get_db)):
    return get_titan_by_id(db, id)