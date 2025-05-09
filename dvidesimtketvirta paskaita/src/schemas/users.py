from pydantic import BaseModel, ConfigDict

class RoleCreate(BaseModel):
    name:str
    slug:str
    default:bool
    
class UserCreate(BaseModel):
    first_name:str
    last_name:str
    birthdate_unix:int
    role_id:int
    
class ProfileCreate(BaseModel):
    nicename:str
    bio:str
    avatar:str
    
class RoleRead(BaseModel):
    id:int
    name:str
    slug:str
    default:bool
    
    model_config = ConfigDict(from_attributes=True)
    
class UserRead(BaseModel):
    id:int
    first_name:str
    last_name:str
    birthdate_unix:int
    
    model_config = ConfigDict(from_attributes=True)
    
class ProfileRead(BaseModel):
    id:int
    bio:str
    
    model_config = ConfigDict(from_attributes=True)
    
    
    
