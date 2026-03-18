from fastapi import APIRouter, UploadFile, File, Depends
import shutil
import os
from sqlalchemy.orm import Session

from app.services.audio_analysis import analyze_audio
from app.services.ai_feedback import generate_feedback
from app.utils.dependencies import get_db
from app.models.recording import Recording

router = APIRouter()

UPLOAD_DIR = "uploads"

os.makedirs(UPLOAD_DIR, exist_ok=True)


@router.post("/analyze")

def analyze_recording(

    file: UploadFile = File(...),
    db: Session = Depends(get_db)

):

    path = f"{UPLOAD_DIR}/{file.filename}"

    with open(path, "wb") as buffer:

        shutil.copyfileobj(file.file, buffer)

    analysis = analyze_audio(path)

    feedback = generate_feedback(analysis)

    rec = Recording(

        file_path=path,

        analysis_data=str(analysis),

        feedback=feedback
    )

    db.add(rec)

    db.commit()

    return {
        "analysis": analysis,
        "feedback": feedback
    }