from fastapi import FastAPI
from pydantic import BaseModel, Field, EmailStr
from routers.lib import lib_router
# from routers.users_old import users_router
from routers.notes import notes_router
from routers.posts import post_router
from routers.school import school_router
from routers.business import business_router
from routers.servers import servers_router 
from routers.users import router as users_router
# from models.users_old import UserORM
from models.posts import PostORM
from database import Base, engine, get_db, Session

app = FastAPI()

Base.metadata.create_all(engine)

app.include_router(lib_router, prefix='/game', tags=['game'])
app.include_router(users_router, prefix='/users', tags=['user'])
app.include_router(notes_router, prefix='/notes', tags=['notes'])
app.include_router(business_router, prefix='/business', tags=['business'])
app.include_router(post_router, prefix='/posts', tags=['posts'])
app.include_router(school_router, prefix='/school', tags=['school'])
app.include_router(servers_router, prefix='/servers', tags=['servers'])

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
    
@app.get('/test')
def test(test:int):
    return test

@app.post('/combined/{path_param}', tags=['main'])
def combined(path_param, something:Something, query_param: str = None):
    return {"path_param":path_param, "something":something, "query_param":query_param}

class UserORM(BaseModel):
    name: str = Field(max_length=20, min_length=3)
    age: int = Field(ge=18)
    terms:bool = Field(default=True)
    email: EmailStr

# @app.post('/register', tags=['main'])
# def register(user:User):
#     return user


# Task 1: Hello endpoint
@app.get("/hello")
def hello(name: str):
    return {"message": f"Hello, {name}!"}

# Task 2: Add endpoint
@app.get("/add")
def add(a: int, b: int):
    return {"result": a + b}

# Task 3: Register endpoint
class UserORM(BaseModel):
    username: str
    email: str
    password: str

@app.post("/register")
def register(user: UserORM):
    return {"message": f"User {user.username} registered successfully"}

# Task 4: Get item by ID
@app.get("/items/{item_id}")
def get_item(item_id: int):
    return {"item_id": item_id, "description": "This is a sample item."}