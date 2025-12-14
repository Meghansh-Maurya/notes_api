from fastapi import APIRouter, HTTPException
from .models import NoteClient, NoteServer
import app.storage as storage

router = APIRouter()

@router.get('/notes/{note_id}', response_model=NoteServer)
def get_notes(note_id: int):
    if note_id not in storage.notes:
        raise HTTPException(status_code=404, detail="Note not found")
    return storage.notes[note_id]


@router.post('/notes/', response_model=NoteServer)
def write_note(note: NoteClient):
    storage.note_id += 1

    storage.notes[storage.note_id] = note.model_dump() #model_dump() converts pydantic model to dictionary
    storage.notes[storage.note_id]['id'] = storage.note_id #adding id to the note dictionary

    # note_data = note.model_dump()
    # note_data["id"] = storage.note_id
    # storage.notes[storage.note_id] = note_data
    
    return storage.notes[storage.note_id]


@router.put('/notes/{note_id}', response_model=NoteServer)
def update_note(note_id: int, note: NoteClient):
    if note_id in storage.notes:
        storage.notes[note_id] = note.model_dump()
        storage.notes[note_id]['id'] = note_id
        return storage.notes[note_id]

    else:
        raise HTTPException(status_code=404, detail="Note not found")


@router.delete('/notes/{note_id}')
def delete_note(note_id: int):
    if note_id not in storage.notes:
        raise HTTPException(status_code=404, detail="Note not found")
    del storage.notes[note_id]
    return {"message": "Successfully Deleted",
            "note_id": note_id}