import ollama
import json

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

    # Ollama generate call
    response = ollama.generate(model="mistral", prompt=prompt)

    # Get the actual generated string
    # Some versions: response.response[0].content
    # We'll handle safely:
    if hasattr(response, "response") and len(response.response) > 0:
        llm_output = response.response[0].content  # text from the first response
    else:
        # fallback
        llm_output = str(response)

    # Convert JSON string to dict
    try:
        parsed_jd = json.loads(llm_output)
    except json.JSONDecodeError:
        parsed_jd = {"must_have": [], "nice_to_have": [], "qualifications": []}

    return parsed_jd
