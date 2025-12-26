import fitz  # PyMuPDF
import re
from pathlib import Path

def clean_text(text: str) -> str:
    text = re.sub(r"\s+", " ", text)
    text = re.sub(r"©.*?\d{4}", "", text)   # remove copyright lines
    return text.strip()

def parse_pdf(pdf_path: str) -> dict:
    doc = fitz.open(pdf_path)
    pages = []

    for page in doc:
        blocks = page.get_text("blocks")
        page_text = " ".join(b[4] for b in blocks if len(b[4]) > 20)
        page_text = clean_text(page_text)
        pages.append(page_text)

    full_text = " ".join(pages)

    return {
        "file": Path(pdf_path).name,
        "text": full_text
    }
