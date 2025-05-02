from fastapi import APIRouter, Depends, HTTPException
from database import get_db
from schemas.users import User
from schemas.new_users import UserCreate, UserResponse
from sqlalchemy.orm import Session
from models.users import UserORM

users_router = APIRouter()

# users: list[User] = []

# @users_router.post('/')
# def create_user(new_user: User):
#     users.append(new_user)
#     return new_user

# @users_router.get('/')
# def get_users():
#     return users

# @users_router.delete('/{user_index}')
# def delete_user(user_index):
#     del users[user_index]
#     return users

# @users_router.put('/{user_index}')
# def update_user(user_index:int, updated_user:User):
#     users[user_index] = updated_user
#     return users

@users_router.post('/', response_model=UserResponse)
def create_user(user:UserCreate, db:Session = Depends(get_db)):
    db_user = UserORM(name=user.name, email=user.email)
    db.add(db_user)
    db.commit()
    return db_user

@users_router.get('/{user_id}', response_model=UserResponse)
def get_user(user_id:int, db:Session = Depends(get_db)):
    user = db.query(UserORM).filter(UserORM.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

