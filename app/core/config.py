import os
from dotenv import load_dotenv

load_dotenv()

# DATABASE_URL = os.getenv("DATABASE_URL")
# SECRET_KEY = os.getenv("SECRET_KEY", "supersecret")

# commented out above line and added below line to use sqlite for local development, 
# uncomment above line and set DATABASE_URL in .env to deploy using postgres.

DATABASE_URL = "sqlite:///./music_coach.db"


ALGORITHM = "HS256"

ACCESS_TOKEN_EXPIRE_MINUTES = 60