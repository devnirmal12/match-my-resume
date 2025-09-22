# app/llm_helper.py
import os
import json
from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def llm_parse_jd(jd_text: str) -> dict:
    prompt = f"""
Extract this job description into JSON with keys:
- must_have
- nice_to_have
- qualifications

JD Text:
{jd_text}

Respond ONLY with valid JSON.
"""
    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": prompt}],
            temperature=0,
        )
        return json.loads(response.choices[0].message.content.strip())
    except json.JSONDecodeError:
        return {"must_have": [], "nice_to_have": [], "qualifications": []}
    except Exception as e:
        return {"error": str(e)}
