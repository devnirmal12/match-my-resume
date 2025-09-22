# app/feedback.py
import os
from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

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
    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.7,
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"Error generating feedback: {e}"
