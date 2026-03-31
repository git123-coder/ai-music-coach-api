from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from app.core.config import DATABASE_URL

engine = create_engine(DATABASE_URL,
    connect_args={"check_same_thread": False})  

# connect_args required for SQLite, remove it if using PostgreSQL.

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

Base = declarative_base()