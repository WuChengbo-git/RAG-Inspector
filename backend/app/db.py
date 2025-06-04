from __future__ import annotations

from pathlib import Path
from typing import List, Tuple

from sqlmodel import SQLModel, Field, Session, create_engine

DB_PATH = Path("data/database.db")
engine = create_engine(f"sqlite:///{DB_PATH}")


class Document(SQLModel, table=True):
    id: str = Field(primary_key=True)
    filename: str


class Chunk(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    document_id: str = Field(foreign_key="document.id")
    chunk_number: int
    text: str


def init_db() -> None:
    """Create tables if they do not exist."""
    DB_PATH.parent.mkdir(parents=True, exist_ok=True)
    SQLModel.metadata.create_all(engine)


def save_document_with_chunks(
    doc_id: str, filename: str, chunks: List[Tuple[int, str]]
) -> None:
    """Persist a document record and its chunks."""
    with Session(engine) as session:
        doc = Document(id=doc_id, filename=filename)
        session.add(doc)
        session.commit()
        for num, text in chunks:
            session.add(
                Chunk(document_id=doc_id, chunk_number=num, text=text)
            )
        session.commit()
