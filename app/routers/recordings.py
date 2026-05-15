from fastapi import APIRouter, UploadFile, File, Depends
import shutil
import os
from sqlalchemy.orm import Session

from app.services.audio_analysis import analyze_audio
from app.services.llm_feedback import generate_feedback
from app.utils.dependencies import get_db
from app.models.recording import Recording
from app.services.issue_detection import detect_issues
from app.services.scoring import compute_score
from app.services.section_analysis import analyze_sections


from app.services.progress import calculate_progress

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

    issues = detect_issues(analysis)

    score = compute_score(analysis)
    
    sections = analyze_sections(path)

    feedback = generate_feedback(analysis, issues, score, sections)

    

    rec = Recording(

        file_path=path,

        analysis_data=str({
        "analysis": analysis,
        "score": score
    }),
        feedback=feedback
    )

    previous_record = db.query(Recording).order_by(Recording.id.desc()).offset(1).first()

    progress = "Not enough data"

    if previous_record:
        progress = calculate_progress(previous_record.analysis_data, score)

    db.add(rec)

    db.commit()

    return {
        "feedback": feedback,
        "analysis": analysis,
        "issues": issues,
        "score": score,
        "sections": sections,
        "progress": progress,
    }