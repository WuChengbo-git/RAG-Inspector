from __future__ import annotations

from pathlib import Path
from typing import Iterable
import csv

from fpdf import FPDF

from ..core.config import settings
from ..models import EvaluationScore


class Reporter:
    """Generate evaluation reports in CSV or PDF format."""

    def __init__(self, output_dir: str | Path | None = None) -> None:
        self.output_dir = Path(output_dir or settings.report_dir)
        self.output_dir.mkdir(parents=True, exist_ok=True)

    def to_csv(self, scores: Iterable[EvaluationScore], filename: str) -> Path:
        """Write ``scores`` to ``filename`` in CSV format."""
        dest = self.output_dir / filename
        with open(dest, "w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(["question_id", "score", "notes"])
            for s in scores:
                writer.writerow([s.question_id, s.score, s.notes or ""])
        return dest

    def to_pdf(self, scores: Iterable[EvaluationScore], filename: str) -> Path:
        """Write ``scores`` to ``filename`` as a simple PDF."""
        dest = self.output_dir / filename
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size=12)
        pdf.cell(200, 10, txt="Evaluation Report", ln=1, align="C")
        for s in scores:
            line = f"{s.question_id}: {s.score:.2f}"
            if s.notes:
                line += f" - {s.notes}"
            pdf.cell(200, 10, txt=line, ln=1)
        pdf.output(dest)
        return dest
