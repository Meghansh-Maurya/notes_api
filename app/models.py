from pydantic import BaseModel

class NoteClient(BaseModel):
    title: str
    content: str

class NoteServer(BaseModel):
    id : int
    title : str
    content : str