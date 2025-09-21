# # app/db_utils.py
# from app.db import SessionLocal, Candidate
#
# def save_candidate(name, email, location, job_role, resume_path, jd_path, match_score, matched_keywords, feedback):
#     db = SessionLocal()
#     candidate = Candidate(
#         name=name,
#         email=email,
#         location=location,
#         job_role=job_role,
#         resume_path=str(resume_path),
#         jd_path=str(jd_path),
#         match_score=match_score,
#         matched_keywords=matched_keywords,
#         feedback=feedback
#     )
#     db.add(candidate)
#     db.commit()
#     db.refresh(candidate)
#     db.close()
#     return candidate.id
