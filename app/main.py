from fastapi import FastAPI
from app.database.db import engine, Base
from app.routers import  recordings

app = FastAPI()

Base.metadata.create_all(bind=engine)


app.include_router(recordings.router)