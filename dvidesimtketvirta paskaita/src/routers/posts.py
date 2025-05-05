from fastapi import APIRouter, Depends, HTTPException
from database import get_db
from sqlalchemy.orm import Session
from models.posts import PostORM
from schemas.posts import PostResponse, PostCreate, PostUpdate
from typing import List

post = {
  "title": "string",
  "year": 0,
  "author_name": "string",
  "price": 0
}

post_router = APIRouter()

@post_router.post('/users/{user_id}/posts/', response_model=PostResponse)
def create_post_for_user(user_id: int, post: PostCreate, db:Session = Depends(get_db)):
    # db_post = PostORM(title=post.title, content=post.content)
    db_post = PostORM(**post.dict())
    db.add(db_post)
    db.commit()
    return db_post
  
@post_router.get("/posts/{post_id}", response_model=PostResponse)
def get_post(post_id, db:Session = Depends(get_db)):
  post = db.query(PostORM).filter(PostORM.id == post_id).first()
  if not post:
    raise HTTPException(status_code=404, detail='Post not found')
  else:
    return post
    
@post_router.get('/posts', response_model=List[PostResponse])
def get_all_posts(db:Session = Depends(get_db)):
  return db.query(PostORM).all()

@post_router.delete('/posts/{post_id}')
def delete_post(post_id:int, db:Session = Depends(get_db)):
  post = db.query(PostORM).filter(PostORM.id == post_id).first()
  if not post:
    raise HTTPException(status_code=404, detail="Post not found")
  db.delete(post)
  db.commit()
  return 'Success'

@post_router.put('/posts/{post_id}', response_model=PostResponse)
def update_post(post_id:int, updated_post:PostUpdate, db:Session = Depends(get_db)):
  post = db.query(PostORM).filter(PostORM.id == post_id).first()
  if not post:
    raise HTTPException(status_code=404, detail="Post not found")
  for field, value in updated_post.dict(exclude_unset=True).items():
    setattr(post, field, value)
  db.commit()
  db.refresh(post)
  return post


# @post_router.post('/users/{user_id}/posts/', response_model=PostResponse)
# def create_post_for_user(user_id:int, post: PostCreate, db:Session = Depends(get_db)):
#     db_post = PostORM(title='safafa', content='sfasfas')
#     db_post = PostORM(post)
#     db_post = PostORM({
#   "title": "string",
#   "content": 'content'
# })
#     db_post = PostORM(**post)
#     db_post = PostORM(title='string', year=0, author_name="string", price=0)
    
    
# def sukurt_nama(spalva:str, ilgis:int, pirtis:bool):
    
#     pass

# sukurt_nama(ilgis=2412, spalva='red', pirtis=True)