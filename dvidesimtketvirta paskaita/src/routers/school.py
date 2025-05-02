from fastapi import APIRouter, Depends, HTTPException
from schemas.schools import SchoolResponse, SchoolCreate
from models.schools import SchoolOrm
from database import get_db
from sqlalchemy.orm import Session

school_router = APIRouter()

@school_router.post('/', response_model=SchoolResponse)
def create_school(school: SchoolCreate, db:Session = Depends(get_db)):
    db_school = SchoolOrm(**school.dict())
    db.add(db_school)
    db.commit()
    return db_school
    
    