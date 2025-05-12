from pydantic import BaseModel, ConfigDict
from typing import Optional

class ManCreate(BaseModel):
    name:str
    age:int
    
class StoreCreate(BaseModel):
    address:str
    price:int
    owner_id: Optional[int] 
    
class CarsCreate(BaseModel):
    model:str
    brand:str
    owner_id: int
    
# Reads

class StoreInMan(BaseModel):
    id:int
    address:str
    price:int
    
class CarInMan(BaseModel):
    id:int
    model:str
    brand:str

class ManRead(BaseModel):
    id:int
    name:str
    age:int
    
    owned_cars: list[CarInMan]
    owned_stores: list[StoreInMan]
    
    model_config = ConfigDict(from_attributes=True)

    
class CarRead(BaseModel):
    id:int
    model:str
    brand:str
    
    owner_id:int
    owner: ManRead
    
    model_config = ConfigDict(from_attributes=True)

    
class StoreRead(BaseModel):
    id:int
    address:str
    price:int
    
    owner_id:int
    owner:ManRead
    
    model_config = ConfigDict(from_attributes=True)


    