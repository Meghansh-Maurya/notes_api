from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from app.models import CreateUser, NoteClient, NoteServer, NoteUpdate, User, Note
from app.database import get_db


router = APIRouter()


@router.post("/users")
def create_user(user: CreateUser, db: Session = Depends(get_db)):
    # TEMP: password not hashed yet (auth not implemented)
    db_user = User(username=user.username, password_hash=user.password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return {
        "id": db_user.id,
        "username": db_user.username
    }


@router.get('/notes/{note_id}', response_model=NoteServer)
def get_notes(note_id: int, db: Session = Depends(get_db)):
    note = db.query(Note).filter(Note.id == note_id).first()
    if not note:
        raise HTTPException(status_code=404, detail="Note not found")
    return {
        "id": note.id,
        "title": note.title,
        "content": note.content
    }


@router.post('/notes', response_model=NoteServer)
def write_note(note: NoteClient, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id == note.user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    db_note = Note(title=note.title, content=note.content,
                   user_id=note.user_id)
    db.add(db_note)
    db.commit()
    db.refresh(db_note)
    return {
        "id": db_note.id,
        "title": db_note.title,
        "content": db_note.content
    }


@router.put('/notes/{note_id}', response_model=NoteServer)
def update_note(note_id: int, note: NoteUpdate, db: Session = Depends(get_db)):
    note_record = db.query(Note).filter(Note.id == note_id).first()

    if not note_record:
        raise HTTPException(status_code=404, detail="Note not found")

    note_record.title = note.title
    note_record.content = note.content
    db.commit()
    db.refresh(note_record)
    return {
        "id": note_record.id,
        "title": note_record.title,
        "content": note_record.content
    }


@router.delete('/notes/{note_id}/')
def delete_note(note_id: int, db: Session = Depends(get_db)):
    note_record = db.query(Note).filter(Note.id == note_id).first()
    if not note_record:
        raise HTTPException(status_code=404, detail="Note not found")
    db.delete(note_record)
    db.commit()
    return {
        "detail": f"Note {note_id} deleted"
    }
