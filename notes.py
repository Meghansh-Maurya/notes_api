from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Note(BaseModel):
    title: str
    content: str

notes = []

@app.get('/notes')
async def get_notes():
    return {"notes": notes}

@app.post('/note')
def write_note(note: Note):
    notes.append(note)
    return {"Added" : "Successfuly Added",
            "note": note}