from __future__ import annotations

from typing import Iterable

from ..models import EvaluationScore


class Scorer:
    """Compute retrieval and answer quality scores."""

    def retrieval_accuracy(
        self, retrieved: Iterable[str], relevant: Iterable[str]
    ) -> float:
        """Return recall-style accuracy for retrieved documents."""
        rset = set(retrieved)
        relset = set(relevant)
        if not relset:
            return 0.0
        return len(rset & relset) / len(relset)

    def answer_quality(self, reference: str, prediction: str) -> float:
        """Simple token overlap metric for answer quality."""
        ref_tokens = set(reference.lower().split())
        pred_tokens = set(prediction.lower().split())
        if not ref_tokens:
            return 0.0
        return len(ref_tokens & pred_tokens) / len(ref_tokens)

    def combine_scores(
        self, question_id: str, retrieval: float, answer: float
    ) -> EvaluationScore:
        """Average retrieval and answer scores for ``question_id``."""
        score = (retrieval + answer) / 2
        return EvaluationScore(question_id=question_id, score=score)
