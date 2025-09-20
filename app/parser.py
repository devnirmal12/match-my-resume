# app/parser.py
import fitz  # PyMuPDF

def extract_text(pdf_path: str) -> str:
    """Extract text from a PDF file."""
    text = ""
    doc = fitz.open(pdf_path)
    for page in doc:
        text += page.get_text()
    return text

def parse_resume(resume_path: str) -> str:
    return extract_text(resume_path)

def parse_jd(jd_path: str) -> str:
    return extract_text(jd_path)
