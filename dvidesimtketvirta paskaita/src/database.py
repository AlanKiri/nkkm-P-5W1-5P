from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, Session, sessionmaker

engine = create_engine(url='sqlite:///./shop.db')

Session = sessionmaker(engine)

class Base(DeclarativeBase):
    pass

def get_db():
    db = Session()
    try:
        yield db
    finally:
        db.close()