from pydantic import BaseModel

class PostCreate(BaseModel):
    title:str
    content:str
    
class PostUpdate(BaseModel):
    title:str | None = None
    content:str | None = None
    
class PostResponse(BaseModel):
    id:int
    title:str
    content:str
    
class PostResponseSmart(PostCreate):
    id:int
    
  