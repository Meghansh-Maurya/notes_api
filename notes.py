from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()


class NoteClient(BaseModel):
    title: str
    content: str

class NoteServer(BaseModel):
    id : int
    title : str
    content : str

notes = {}

note_id = 0


@app.get('/notes/{note_id}', response_model=NoteServer)
def get_notes(note_id: int):
    if note_id not in notes:
        raise HTTPException(status_code=404, detail="Note not found")
    return notes[note_id]


@app.post('/notes/', response_model=NoteServer)
def write_note(note: NoteClient):
    global note_id
    note_id += 1

    notes[note_id] = note.model_dump() #model_dump() converts pydantic model to dictionary
    notes[note_id]['id'] = note_id #adding id to the note dictionary

    # note_data = note.model_dump()
    # note_data["id"] = note_id
    # notes[note_id] = note_data
    
    return notes[note_id]


@app.put('/notes/{note_id}', response_model=NoteServer)
def update_note(note_id: int, note: NoteClient):
    if note_id in notes:
        notes[note_id] = note.model_dump()
        notes[note_id]['id'] = note_id
        return notes[note_id]

    else:
        raise HTTPException(status_code=404, detail="Note not found")


@app.delete('/notes/{note_id}')
def delete_note(note_id: int):
    if note_id not in notes:
        raise HTTPException(status_code=404, detail="Note not found")
    del notes[note_id]
    return {"message": "Successfully Deleted",
            "note_id": note_id}
