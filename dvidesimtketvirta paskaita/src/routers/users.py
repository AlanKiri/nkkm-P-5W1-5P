from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from database import get_db
from models.users import UserORM, RoleORM, ProfileORM
from schemas.users import ProfileCreate, ProfileRead, RoleRead, UserCreate, UserRead, RoleCreate

router = APIRouter()

@router.post('/roles', response_model=RoleRead)
def create_role(role:RoleCreate, db:Session = Depends(get_db)):
    db_role = RoleORM(**role.dict())
    db.add(db_role)
    db.commit()
    db.refresh()
    return db_role

@router.get('/roles', response_model=list[RoleRead])
def read_roles(db:Session = Depends(get_db)):
    return db.query(RoleORM).all()

