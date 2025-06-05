from __future__ import annotations

from typing import Dict, List

from ..core.config import settings


class AnswerEvaluator:
    """Evaluate answers from different RAG system versions."""

    def __init__(self, versions: List[str] | None = None) -> None:
        self.versions = versions or settings.rag_versions

    def answer(self, question: str) -> Dict[str, str]:
        """Return answers from all configured RAG versions."""
        responses: Dict[str, str] = {}
        for version in self.versions:
            responses[version] = self._query_system(version, question)
        return responses

    def _query_system(self, version: str, question: str) -> str:
        """Stubbed RAG system call."""
        # Replace with real RAG pipeline call for ``version``.
        return f"{version} says: response to '{question}'"
