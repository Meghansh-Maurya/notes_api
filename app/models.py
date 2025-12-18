from pydantic import BaseModel
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import declarative_base, relationship


Base = declarative_base()


# ----------------------------Pydantic schemas----------------------------


class CreateUser(BaseModel):
    username: str
    password: str


class NoteClient(BaseModel):
    user_id: int
    title: str
    content: str


class NoteServer(BaseModel):
    id: int
    title: str
    content: str


class NoteUpdate(BaseModel):
    title: str
    content: str


# ----------------------------ORM models----------------------------


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, nullable=False)
    password_hash = Column(String, nullable=False)

    notes = relationship(
        "Note",
        back_populates="owner",
        cascade="all, delete"
    )


class Note(Base):
    __tablename__ = 'notes'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    content = Column(String, nullable=False)

    user_id = Column(
        Integer,
        ForeignKey('users.id', ondelete='CASCADE'),
        nullable=False
    )

    owner = relationship("User", back_populates="notes")
