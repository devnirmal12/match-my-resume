# app/feedback.py
import subprocess

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
        # Ollama CLI expects the prompt as a positional argument
        result = subprocess.run(
            ["ollama", "run", "mistral", prompt],
            capture_output=True,
            text=True,
            check=True
        )
        return result.stdout.strip()
    except subprocess.CalledProcessError as e:
        return f"Error: {e.stderr.strip()}"
