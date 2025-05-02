from pydantic import BaseModel

class SchoolBase(BaseModel):
    title: str
    address:str
    phone:str
    
class SchoolCreate(SchoolBase):
    pass

    
class SchoolResponse(SchoolBase):
    id: int