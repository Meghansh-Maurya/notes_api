from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .routes import router
from app.database import engine
from app.models import Base

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:8501",
        "http://127.0.0.1:8501",
        "https://notesapi.streamlit.app/"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(router)

Base.metadata.create_all(bind=engine)
