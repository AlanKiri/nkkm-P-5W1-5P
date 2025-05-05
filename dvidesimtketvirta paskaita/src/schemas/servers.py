from pydantic import BaseModel

class ServersBase(BaseModel):
    region:str
    name:str
    description:str
    private:bool
    
class ServersResponse(ServersBase):
    id: int