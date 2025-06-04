from __future__ import annotations

from pathlib import Path
from typing import List, Tuple

from bs4 import BeautifulSoup
from pdfminer.high_level import extract_text as pdf_extract_text


def extract_text(path: Path) -> str:
    """Return cleaned text from a supported document file."""
    ext = path.suffix.lower()
    if ext == ".txt":
        return path.read_text(encoding="utf-8")
    if ext == ".html":
        with open(path, "r", encoding="utf-8") as f:
            soup = BeautifulSoup(f, "html.parser")
            return soup.get_text(separator=" ", strip=True)
    if ext == ".pdf":
        return pdf_extract_text(str(path))
    raise ValueError(f"Unsupported file type: {ext}")


def chunk_text(
    text: str, window_size: int = 1000, stride: int = 200
) -> List[Tuple[int, str]]:
    """Split ``text`` into overlapping chunks.

    Returns a list of ``(chunk_id, chunk_text)`` tuples.
    """
    chunks: List[Tuple[int, str]] = []
    start = 0
    idx = 0
    length = len(text)
    while start < length:
        chunk = text[start : start + window_size]
        if not chunk:
            break
        chunks.append((idx, chunk))
        idx += 1
        start += stride
    return chunks
