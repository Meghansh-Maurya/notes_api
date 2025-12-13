from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()


class Note(BaseModel):
    title: str
    content: str


notes = {}


@app.get('/notes/{note_id}')
def get_notes(note_id: int):
    if note_id not in notes:
        raise HTTPException(status_code=404, detail="Note not found")
    return {"note_id": note_id,
            "note": notes[note_id]}


@app.post('/notes/{note_id}')
def write_note(note: Note, note_id: int):

    if note_id in notes:
        raise HTTPException(status_code=400, detail="Note already exists")

    notes[note_id] = note.model_dump()
    return {"message": "Successfully Added",
            "note_id": note_id,
            "note": notes[note_id]}


@app.put('/notes/{note_id}')
def update_note(note_id: int, note: Note):
    if note_id in notes:
        notes[note_id] = note.model_dump()
        return {"message": "Successfully Updated",
                "note_id": note_id,
                "note": notes[note_id]}

    else:
        raise HTTPException(status_code=404, detail="Note not found")


@app.delete('/notes/{note_id}')
def delete_note(note_id: int):
    if note_id not in notes:
        raise HTTPException(status_code=404, detail="Note not found")
    del notes[note_id]
    return {"message": "Successfully Deleted",
            "note_id": note_id}
