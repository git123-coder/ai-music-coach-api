from app.database.db import SessionLocal
from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer
from jose import jwt
from app.core.config import ALGORITHM
#from app.core.config import SECRET_KEY, ALGORITHM

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

def get_db():

    db = SessionLocal()

    try:
        yield db
    finally:
        db.close()

def get_current_user(token: str = Depends(oauth2_scheme)):

    payload = jwt.decode(token, algorithms=[ALGORITHM])
    #payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])

    return payload["user_id"]