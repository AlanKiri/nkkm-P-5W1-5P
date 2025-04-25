from fastapi import APIRouter
from pydantic import BaseModel
from typing import Dict

notes_router = APIRouter()

class Note(BaseModel):
    title: str
    content: str

notes_db: Dict[int, Note] = {}
note_counter = 1

@notes_router.post("/notes")
def create_note(note: Note):
    global note_counter
    notes_db[note_counter] = note
    note_counter += 1
    return {"id": note_counter - 1, "message": "Note created"}

@notes_router.get("/notes/{note_id}")
def read_note(note_id: int):
    note = notes_db.get(note_id)
    if note:
        return note
    return {"error": "Note not found"}

@notes_router.put("/notes/{note_id}")
def update_note(note_id: int, updated_note: Note):
    if note_id in notes_db:
        notes_db[note_id] = updated_note
        return {"message": "Note updated"}
    return {"error": "Note not found"}

@notes_router.delete("/notes/{note_id}")
def delete_note(note_id: int):
    if note_id in notes_db:
        del notes_db[note_id]
        return {"message": "Note deleted"}
    return {"error": "Note not found"}