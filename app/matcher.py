# app/matcher.py

def keyword_match(resume_text: str, jd_text: str) -> dict:
    """
    Basic keyword matching.
    Returns a dict with matched keywords & counts.
    """
    resume_words = set(resume_text.lower().split())
    jd_words = set(jd_text.lower().split())

    matched = resume_words.intersection(jd_words)
    score = len(matched) / max(len(jd_words), 1) * 100

    return {"matched_keywords": list(matched), "match_score": round(score, 2)}
