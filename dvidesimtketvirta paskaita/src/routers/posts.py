from fastapi import APIRouter, Depends, HTTPException
from database import get_db
from sqlalchemy.orm import Session
from models.posts import PostORM
from schemas.posts import PostResponse, PostCreate

post = {
  "title": "string",
  "year": 0,
  "author_name": "string",
  "price": 0
}

post_router = APIRouter()

# @post_router.post('/users/{user_id}/posts/', response_model=PostResponse)
# def create_post_for_user(user_id:int, post: PostCreate, db:Session = Depends(get_db)):
#     db_post = PostORM(title='safafa', content='sfasfas')
#     db_post = PostORM(post)
#     db_post = PostORM({
#   "title": "string",
#   "year": 0,
#   "author_name": "string",
#   "price": 0
# })
#     db_post = PostORM(**post)
#     db_post = PostORM(title='string', year=0, author_name="string", price=0)
    
    
# def sukurt_nama(spalva:str, ilgis:int, pirtis:bool):
    
#     pass

# sukurt_nama(ilgis=2412, spalva='red', pirtis=True)