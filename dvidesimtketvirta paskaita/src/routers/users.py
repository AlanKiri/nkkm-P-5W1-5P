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
    db.refresh(db_role)
    return db_role

@router.get('/roles', response_model=list[RoleRead])
def read_roles(db:Session = Depends(get_db)):
    return db.query(RoleORM).all()

@router.post('/users', response_model=UserRead)
def create_user(user: UserCreate, profile: ProfileCreate, db:Session = Depends(get_db)):
    role = db.query(RoleORM).filter(RoleORM.id == user.role_id).first()
    if role is None:
        raise HTTPException(status_code=404, detail='Role not found')
    
    db_user = UserORM(**user.dict())
    db_user.profile = ProfileORM(**profile.dict())
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

@router.get('/users', response_model=list[UserRead])
def read_users(db:Session = Depends(get_db)):
    return db.query(UserORM).all()

@router.get('/users/{user_id}', response_model=UserRead)
def get_user_by_id(user_id:int, db:Session = Depends(get_db)):
    return db.query(UserORM).filter(UserORM.id == user_id).first()

@router.get('/profile/{user_id}', response_model=ProfileRead)
def get_user_profile_by_id(user_id:int, db:Session = Depends(get_db)):
    user = db.query(UserORM).filter(UserORM.id == user_id).first()
    return user.profile
    
    