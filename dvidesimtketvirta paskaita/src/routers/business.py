from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from models.business import BusinessManORM, CarsORM, StoresORM
from schemas.business import CarRead, ManRead, StoreRead, CarsCreate, ManCreate, StoreCreate
from typing import Optional

business_router = APIRouter()

@business_router.post('/man', response_model=ManRead)
def create_man(man:ManCreate, db:Session = Depends(get_db)):
    db_man = BusinessManORM(**man.dict())
    db.add(db_man)
    db.commit()
    db.refresh(db_man)
    return db_man

@business_router.post('/store', response_model=StoreRead)
def create_store(store:StoreCreate, owner_id:Optional[int], db:Session = Depends(get_db)):
    db_store = StoresORM(**store.dict())
    if owner_id is not None:
        db_store.owner_id = owner_id
    db.add(db_store)
    db.commit()
    db.refresh(db_store)
    return db_store

@business_router.post('/car', response_model=CarRead)
def create_man(car:CarsCreate, owner_id:Optional[int], db:Session = Depends(get_db)):
    db_car = CarsORM(**car.dict())
    if owner_id is not None:
        db_car.owner_id = owner_id
    db.add(db_car)
    db.commit()
    db.refresh(db_car)
    return db_car