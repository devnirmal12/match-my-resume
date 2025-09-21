import sys
from pathlib import Path
import streamlit as st

PROJECT_ROOT = Path(__file__).parent.parent.resolve()
sys.path.insert(0, str(PROJECT_ROOT))

import parser as parser
import matcher as matcher
import scorer as scorer
import feedback as feedback
# from app.db_utils import save_candidate

st.set_page_config(
    page_title="Resume-JD Analyzer",
    page_icon="📄",
    layout="wide",
    initial_sidebar_state="expanded"
)

with st.sidebar:
    st.markdown(
        f"""
            <div style="text-align:center;">
                <img src="https://cdn-icons-png.flaticon.com/512/3135/3135715.png" 
                     width="140">
            </div>
            """,
        unsafe_allow_html=True
    )
    st.title("Controls ⚙️")
    candidate_name = st.text_input("👤 Candidate Name")
    candidate_email = st.text_input("📧 Email")
    location = st.text_input("📍 Location")
    job_role = st.text_input("💼 Job Role")
    st.markdown("---")
    st.markdown("Upload your **Resume** and **Job Description** below:")

    resume_file = st.file_uploader("📄 Upload Resume (PDF)", type=["pdf"])
    jd_file = st.file_uploader("📝 Upload JD (PDF)", type=["pdf"])
st.markdown(
    """
    <div style="text-align: center;">
        <div style="display: inline-flex; align-items: center; gap: 12px;">
            <img src="https://i.ibb.co/NgcTLtHM/resume-icon.png" width="60">
            <h1 style="margin: 0;">Resume vs Job Description Analyzer</h1>
        </div>
    </div>
    <br>
    """,
    unsafe_allow_html=True
)


UPLOAD_DIR = Path("data")
resume_path = None
jd_path = None

if st.sidebar.button("🚀 Analyze") and resume_file and jd_file and candidate_name:
    resume_path = UPLOAD_DIR / "resumes" / resume_file.name
    jd_path = UPLOAD_DIR / "jds" / jd_file.name
    resume_path.parent.mkdir(parents=True, exist_ok=True)
    jd_path.parent.mkdir(parents=True, exist_ok=True)

    with open(resume_path, "wb") as f:
        f.write(resume_file.read())
    with open(jd_path, "wb") as f:
        f.write(jd_file.read())

    st.success("✅ Files uploaded successfully!")


    resume_text = parser.parse_resume(str(resume_path))
    jd_text = parser.parse_jd(str(jd_path))


    match_data = matcher.keyword_match(resume_text, jd_text)
    score = scorer.weighted_score(match_data)


    ai_feedback = feedback.generate_feedback(resume_text, jd_text)


    # save_candidate(
    #     name=candidate_name,
    #     email=candidate_email,
    #     location=location,
    #     job_role=job_role,
    #     resume_path=resume_path,
    #     jd_path=jd_path,
    #     match_score=score,
    #     matched_keywords=match_data["matched_keywords"],
    #     feedback=ai_feedback
    # )

    st.markdown("### 🔍 Match Results")
    col1, col2 = st.columns([1, 2])

    with col1:
        st.metric("📊 Match Score", f"{score}%")
    with col2:
        st.write("**Matched Keywords:**")
        st.write(", ".join(match_data["matched_keywords"]))

    st.markdown("---")
    st.markdown("### 💡 AI Feedback")
    st.info(ai_feedback)

    st.markdown("---")
    st.markdown(
        "<p style='text-align:center; color: grey;'>Made with ❤️ using Streamlit & Ollama</p>",
        unsafe_allow_html=True
    )

else:
    st.warning("⬅️ Please fill candidate details & upload both Resume + JD to continue.")
