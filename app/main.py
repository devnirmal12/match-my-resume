# app/main.py
from fastapi import FastAPI, UploadFile, File
from pathlib import Path
from app.parser import parse_resume, parse_jd
from app.matcher import keyword_match
from app.scorer import weighted_score
from app.feedback import generate_feedback


app = FastAPI()
UPLOAD_DIR = Path("data")

@app.post("/analyze/")
async def analyze(resume: UploadFile = File(...), jd: UploadFile = File(...)):
    # Save uploaded files
    resume_path = UPLOAD_DIR / "resumes" / resume.filename
    jd_path = UPLOAD_DIR / "jds" / jd.filename
    resume_path.parent.mkdir(parents=True, exist_ok=True)
    jd_path.parent.mkdir(parents=True, exist_ok=True)

    with open(resume_path, "wb") as f:
        f.write(await resume.read())
    with open(jd_path, "wb") as f:
        f.write(await jd.read())

    # Parse
    resume_text = parse_resume(str(resume_path))
    jd_text = parse_jd(str(jd_path))

    # Match & Score
    match_data = keyword_match(resume_text, jd_text)
    score = weighted_score(match_data)

    # Generate feedback
    feedback = generate_feedback(resume_text, jd_text)

    return {
        "match_data": match_data,
        "score": score,
        "feedback": feedback
    }

