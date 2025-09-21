# app/feedback.py
import requests

OLLAMA_URL = "http://localhost:11434/api/generate"

def generate_feedback(resume_text: str, jd_text: str) -> str:
    prompt = f"""
Resume:
{resume_text}

Job Description:
{jd_text}

Please provide:
1. Suggestions to improve resume for this JD.
2. Missing skills or keywords.
3. Any general feedback in bullet points.
"""

    payload = {
        "model": "mistral",  # or llama2, depending on what you're running
        "prompt": prompt,
        "stream": False
    }

    try:
        response = requests.post(OLLAMA_URL, json=payload)
        response.raise_for_status()
        return response.json().get("response", "").strip()
    except requests.RequestException as e:
        return f"Error: {str(e)}"
