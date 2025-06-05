from pydantic import BaseModel
from typing import Optional

class UploadedFile(BaseModel):
    """Metadata about an uploaded file."""

    document_id: str
    filename: str
    size: int

class GeneratedQuestion(BaseModel):
    """A question produced from a document."""

    question_id: str
    document_id: str
    text: str

class Answer(BaseModel):
    """Answer text for a given question."""

    question_id: str
    text: str

class EvaluationScore(BaseModel):
    """Score assigned to an answer."""

    question_id: str
    score: float
    notes: Optional[str] = None
