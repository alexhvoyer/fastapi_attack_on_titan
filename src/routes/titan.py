from http.client import HTTPException
from fastapi import APIRouter, Query, status, Depends, Body
from sqlalchemy.orm import Session

from ..service import titan as service
from ..schemas.titan import TitanCreate, Titan, titan_example
from ..dependencies import get_db

router = APIRouter(
    prefix='/titans',
    tags=['titans'],
    responses={404: {"description": "Not found"}},
)


@router.post('/', status_code=status.HTTP_201_CREATED, response_model=Titan)
def create_titan(titan: TitanCreate = Body(..., example=titan_example), db: Session = Depends(get_db)):
    titan_db = service.create_titan(db, titan)
    return titan_db


@router.get('/')
def get_titan_list(
    skip: int = 0,
    limit: int = 20,
    name: str | None = Query(default=None, max_length=20, description="Search by name"),
    db: Session = Depends(get_db)
    ):
    return service.get_titan_list(db, skip, limit, name)


@router.get('/{id}', response_model=Titan)
def get_titan(id: str, db: Session = Depends(get_db)):
    return service.get_titan_by_id(db, id)


@router.put('/{id}', status_code=status.HTTP_204_NO_CONTENT)
def update_titan(id: str, data: TitanCreate, db: Session = Depends(get_db)):
    db_titan = service.get_titan_by_id(db, id)
    if db_titan is None:
        raise HTTPException(status_code=404, detail="Titan not Found")
    service.update_titan(db, id, data)
    return


@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
def delete_titan(id: str, db: Session = Depends(get_db)):
    service.delete_titan(db, id)
