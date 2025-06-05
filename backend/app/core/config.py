from __future__ import annotations

from pydantic import BaseSettings
from typing import List


class Settings(BaseSettings):
    """Application configuration settings."""

    chunk_size: int = 1000
    chunk_stride: int = 200
    rag_versions: List[str] = ["v1", "v2"]


settings = Settings()
