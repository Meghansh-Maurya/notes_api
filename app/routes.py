from fastapi import APIRouter, HTTPException, Depends
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session
from app.models import CreateUser, LoginUser, NoteClient, NoteServer, NoteUpdate, User, Note
from app.database import get_db
from app.security import hash_password, verify_password, create_access_token, verify_access_token


router = APIRouter()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/login")

def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    user_id = verify_access_token(token)

    if user_id is None:
        raise HTTPException(status_code=401, detail="Invalid or expired token")

    current_user = db.query(User).filter(User.id == user_id).first()

    if current_user is None:
        raise HTTPException(status_code=401, detail="User not found")
    
    return current_user


@router.post("/signup")
def create_user(user: CreateUser, db: Session = Depends(get_db)):
    existing_user = db.query(User).filter(User.username == user.username).first()
    
    if existing_user:
        raise HTTPException(
            status_code=400,
            detail="Username already registered, choose another one"
        )
    
    hashed_pwd = hash_password(user.password)
    db_user = User(username=user.username, password_hash=hashed_pwd)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return {
        "id": db_user.id,
        "username": db_user.username
    }

@router.post("/login")
def login_user(user: LoginUser, db : Session = Depends(get_db)):
    db_user = db.query(User).filter(User.username == user.username).first()

    if not db_user or not verify_password(user.password, db_user.password_hash):
        raise HTTPException(
            status_code=401,
            detail="Invalid username or password"
        )
    
    access_token = create_access_token(
        data = {"sub": str(db_user.id)}
    )

    return {
        "access_token": access_token,
        "token_type": "bearer"
    }


@router.get('/notes/{note_id}', response_model=NoteServer)
def get_notes(note_id: int, current_user: User = Depends(get_current_user), db: Session = Depends(get_db)):
    note = db.query(Note).filter(Note.id == note_id, Note.user_id == current_user.id).first()
    if not note:
        raise HTTPException(status_code=404, detail="Note not found")
    return {
        "id": note.id,
        "title": note.title,
        "content": note.content
    }


@router.post('/notes', response_model=NoteServer)
def write_note(note: NoteClient, current_user: User = Depends(get_current_user), db: Session = Depends(get_db)):
    db_note = Note(title=note.title, content=note.content,
                   user_id=current_user.id)
    db.add(db_note)
    db.commit()
    db.refresh(db_note)
    return {
        "id": db_note.id,
        "title": db_note.title,
        "content": db_note.content
    }


@router.put('/notes/{note_id}', response_model=NoteServer)
def update_note(note_id: int, note: NoteUpdate, current_user: User = Depends(get_current_user), db: Session = Depends(get_db)):
    db_note = db.query(Note).filter(Note.id == note_id, Note.user_id == current_user.id).first()

    if not db_note:
        raise HTTPException(status_code=404, detail="Note not found")

    db_note.title = note.title
    db_note.content = note.content
    db.commit()
    db.refresh(db_note)
    return {
        "id": db_note.id,
        "title": db_note.title,
        "content": db_note.content
    }


@router.delete('/notes/{note_id}')
def delete_note(note_id: int, current_user: User = Depends(get_current_user), db: Session = Depends(get_db)):
    note = db.query(Note).filter(Note.id == note_id, Note.user_id == current_user.id).first()
    if not note:
        raise HTTPException(status_code=404, detail="Note not found")
    db.delete(note)
    db.commit()
    return {
        "detail": f"Note {note_id} deleted"
    }