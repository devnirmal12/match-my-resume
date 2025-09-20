# app/scorer.py

def weighted_score(match_data: dict, weights: dict = None) -> float:
    """
    Apply weights to different aspects of resume-JD match.
    For now, only using keyword match. Can extend later.
    """
    if weights is None:
        weights = {"keyword_match": 1.0}  # simple 100% weight

    score = match_data.get("match_score", 0) * weights["keyword_match"]
    return round(score, 2)
