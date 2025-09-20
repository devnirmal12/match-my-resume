import sys
from pathlib import Path
import streamlit as st

PROJECT_ROOT = Path(__file__).parent.parent.resolve()
sys.path.insert(0, str(PROJECT_ROOT))

import parser as parser
import matcher as matcher
import scorer as scorer
import feedback as feedback
from app.db_utils import save_candidate

st.set_page_config(page_title="Resume-JD Analyzer", layout="wide")
st.title("📄 Resume vs Job Description Analyzer")

resume_file = st.file_uploader("Upload Resume PDF", type=["pdf"])
jd_file = st.file_uploader("Upload JD PDF", type=["pdf"])
candidate_name = st.text_input("Candidate Name")
candidate_email = st.text_input("Candidate Email")
location = st.text_input("Location")
job_role = st.text_input("Job Role")

UPLOAD_DIR = Path("data")
resume_path = None
jd_path = None

if st.button("Analyze") and resume_file and jd_file and candidate_name:
    resume_path = UPLOAD_DIR / "resumes" / resume_file.name
    jd_path = UPLOAD_DIR / "jds" / jd_file.name
    resume_path.parent.mkdir(parents=True, exist_ok=True)
    jd_path.parent.mkdir(parents=True, exist_ok=True)

    with open(resume_path, "wb") as f:
        f.write(resume_file.read())
    with open(jd_path, "wb") as f:
        f.write(jd_file.read())

    st.success("Files uploaded successfully!")

    # Parse PDFs
    resume_text = parser.parse_resume(str(resume_path))
    jd_text = parser.parse_jd(str(jd_path))

    # Match & Score
    match_data = matcher.keyword_match(resume_text, jd_text)
    score = scorer.weighted_score(match_data)

    # AI Feedback
    ai_feedback = feedback.generate_feedback(resume_text, jd_text)

    # Save to DB
    save_candidate(
        name=candidate_name,
        email=candidate_email,
        location=location,
        job_role=job_role,
        resume_path=resume_path,
        jd_path=jd_path,
        match_score=score,
        matched_keywords=match_data["matched_keywords"],
        feedback=ai_feedback
    )

    st.subheader("🔍 Match Results")
    st.write(f"**Match Score:** {score}%")
    st.write("**Matched Keywords:**")
    st.write(", ".join(match_data["matched_keywords"]))

    st.subheader("💡 AI Feedback")
    st.text(ai_feedback)
