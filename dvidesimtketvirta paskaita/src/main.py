from fastapi import FastAPI
from pydantic import BaseModel, Field, EmailStr
from routers.lib import lib_router
from routers.users import users_router

app = FastAPI()

app.include_router(lib_router, prefix='/game', tags=['game'])
app.include_router(users_router, prefix='/users', tags=['user'])


# Path params
# https://www.reddit.com/r/{subreddit}/{topic}

@app.get('/{my_text}/{tema}/{naudotojas}/{kalba}', tags=['main'])
def hello_world(my_text, tema, naudotojas, kalba):
    return my_text, tema, naudotojas, kalba

# Query params
# https://www.reddit.com/r?raktas=value&raktas=value2

@app.get('/query', tags=['main'])
def query_funkcija(page = None):
    return page

class Book(BaseModel):
    title: str
    year: int
    author_name: str
    price: float
    
# Body params
# https://www.reddit.com

@app.post('/query', tags=['main'])
def post_funkcija(book: Book):
    book.price = book.price * 2
    return book

    
class Something(BaseModel):
    test: str

@app.post('/combined/{path_param}', tags=['main'])
def combined(path_param, something:Something, query_param: str = None):
    return {"path_param":path_param, "something":something, "query_param":query_param}

class User(BaseModel):
    name: str = Field(max_length=20, min_length=3)
    age: int = Field(ge=18)
    terms:bool = Field(default=True)
    email: EmailStr

@app.post('/register', tags=['main'])
def register(user:User):
    return user
