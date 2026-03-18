from sqlalchemy import Column, Integer, String, ForeignKey, Text
from app.database.db import Base

class Recording(Base):

    __tablename__ = "recordings"

    id = Column(Integer, primary_key=True)

    file_path = Column(String)

    analysis_data = Column(Text)

    feedback = Column(Text)