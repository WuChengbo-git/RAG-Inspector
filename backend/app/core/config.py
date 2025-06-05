from __future__ import annotations

from pydantic_settings import BaseSettings
from typing import List


class Settings(BaseSettings):
    """Application configuration settings."""

    chunk_size: int = 1000
    chunk_stride: int = 200
    rag_versions: List[str] = ["v1", "v2"]
    report_dir: str = "data/reports"


settings = Settings()
