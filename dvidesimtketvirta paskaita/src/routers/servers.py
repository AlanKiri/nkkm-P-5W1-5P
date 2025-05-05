from fastapi import APIRouter, Depends, HTTPException
from database import get_db
from models.servers import ServersOrm
from schemas.servers import ServersBase, ServersResponse
from sqlalchemy.orm import Session


servers_router = APIRouter()

@servers_router.post('/', response_model=ServersResponse)
def create_server(server:ServersBase, db:Session = Depends(get_db)):
    server_db = ServersOrm(**server.dict())
    db.add(server_db)
    db.commit()
    db.refresh(server_db)
    return server_db

@servers_router.get('/{server_id}', response_model=ServersResponse)
def get_server(server_id:int, db:Session = Depends(get_db)):
    server = db.query(ServersOrm).filter(ServersOrm.id == server_id).first()
    db.query(ServersOrm).all()
    if not server:
        raise HTTPException(status_code=404, detail='Server not found')
    return server
    
    