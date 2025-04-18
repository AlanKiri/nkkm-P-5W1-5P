from pydantic import BaseModel

class Game(BaseModel):
    title:str
    description:str
    publisher:str
    daily_players:int
    age_limit:str
    