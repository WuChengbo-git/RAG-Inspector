from __future__ import annotations

from pathlib import Path
from typing import List
from uuid import uuid4

from ..core.config import settings
from ..models import GeneratedQuestion
from ..utils import extract_text, chunk_text


class QuestionGenerator:
    """Create questions from document text chunks."""

    def __init__(self, chunk_size: int | None = None, chunk_stride: int | None = None):
        self.chunk_size = chunk_size or settings.chunk_size
        self.chunk_stride = chunk_stride or settings.chunk_stride

    def generate_from_file(self, doc_id: str, path: Path) -> List[GeneratedQuestion]:
        """Extract text from ``path`` and generate questions for ``doc_id``."""
        text = extract_text(path)
        return self.generate_from_text(doc_id, text)

    def generate_from_text(self, doc_id: str, text: str) -> List[GeneratedQuestion]:
        """Generate questions for ``doc_id`` using supplied ``text``."""
        chunks = chunk_text(text, window_size=self.chunk_size, stride=self.chunk_stride)
        questions: List[GeneratedQuestion] = []
        for _idx, chunk in chunks:
            qtext = self._llm_generate_question(chunk)
            questions.append(
                GeneratedQuestion(
                    question_id=str(uuid4()), document_id=doc_id, text=qtext
                )
            )
        return questions

    def _llm_generate_question(self, chunk: str) -> str:
        """Stubbed LLM call to create a question for a text chunk."""
        # Replace this with a real LLM integration.
        snippet = chunk[:50].replace("\n", " ")
        return f"What is discussed in: '{snippet}'?"
