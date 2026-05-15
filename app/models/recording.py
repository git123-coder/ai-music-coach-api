from sqlalchemy import Column, Integer, String, ForeignKey, Text, DateTime
from app.database.db import Base
from datetime import datetime

class Recording(Base):

    __tablename__ = "recordings"

    id = Column(Integer, primary_key=True)

    file_path = Column(String)

    analysis_data = Column(Text)

    feedback = Column(Text)

    created_at = Column(DateTime, default=datetime.utcnow)