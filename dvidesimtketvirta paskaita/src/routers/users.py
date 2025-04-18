from fastapi import APIRouter
from schemas.users import User

users_router = APIRouter()

users: list[User] = []

@users_router.post('/')
def create_user(new_user: User):
    users.append(new_user)
    return new_user

@users_router.get('/')
def get_users():
    return users

@users_router.delete('/{user_index}')
def delete_user(user_index):
    del users[user_index]
    return users

@users_router.put('/{user_index}')
def update_user(user_index:int, updated_user:User):
    users[user_index] = updated_user
    return users