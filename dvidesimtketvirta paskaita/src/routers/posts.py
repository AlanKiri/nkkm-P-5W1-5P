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