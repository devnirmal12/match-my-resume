import string

def keyword_match(resume_text: str, jd_text: str) -> dict:
    """
    Weighted keyword matching using only important JD keywords.
    """
    # Helper to clean words
    def clean_words(text):
        translator = str.maketrans("", "", string.punctuation)
        words = text.lower().translate(translator).split()
        return set(words)

    resume_words = clean_words(resume_text)
    jd_words = clean_words(jd_text)

    # Important keywords
    skill_keywords =  {"python", "java", "c++", "c", "c#", "javascript", "typescript", "ruby", "php", "swift", "kotlin",
                      "html", "css", "react", "angular", "vue", "jquery", "bootstrap", "django", "flask", "fastapi",
                      "spring", "nodejs", "express", "rails", "sql", "mysql", "postgresql", "mongodb", "redis", "aws",
                      "azure", "gcp", "docker", "kubernetes", "terraform", "ml", "ai", "machine learning",
                      "deep learning", "tensorflow", "pytorch", "scikit-learn", "pandas", "numpy", "git", "github",
                      "excel", "powerbi", "tableau", "jira", "confluence", "communication", "teamwork", "leadership",
                      "management", "planning", "organization", "python", "java", "c++", "artificial intelligence", "machine learning", "ml", "ai",
                      "gcloud", "google cloud", "cloud computing", "virtual machine", "docker",
                      "code snippets", "technical workshops", "event logistics", "tensorflow", "pytorch",
                      "scikit-learn", "pandas", "numpy"}
    experience_keywords = {"experience", "project", "internship", "development", "worked", "facilitator", "volunteer", "workshop", "hacktoberfest", "session management",
                          "coding competition", "team collaboration", "event coordination",
                          "technical support", "leadership", "hands-on experience"}
    education_keywords = {"btech", "bachelor", "msc", "degree", "college", "university", "btech", "bachelor", "computer science", "ai", "ml", "degree", "college", "university"}

    matched_keywords = set()
    total_weight = 0
    matched_weight = 0

    for word in jd_words:
        if word in skill_keywords:
            weight = 10
        elif word in experience_keywords:
            weight = 7
        elif word in education_keywords:
            weight = 5
        else:
            continue  # ignore generic words

        total_weight += weight
        if word in resume_words:
            matched_keywords.add(word)
            matched_weight += weight

    score = matched_weight / max(total_weight, 1) * 100

    return {"matched_keywords": list(matched_keywords), "match_score": round(score, 2)}
