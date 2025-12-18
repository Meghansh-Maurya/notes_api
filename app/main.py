from fastapi import FastAPI
from .routes import router
from app.database import engine
from app.models import Base

app = FastAPI()
app.include_router(router)

Base.metadata.create_all(bind=engine)
