# RAG Inspector

RAG Inspector is a minimal project demonstrating a retrieval-augmented generation (RAG)
evaluation workflow. It exposes a FastAPI backend for uploading documents, running stub
evaluations, and exporting reports, alongside a small static frontend.

## Goals

- Ingest documents and break them into chunks for retrieval
- Evaluate retrieval and answer quality metrics
- Persist metadata in SQLite and export results as CSV or PDF

## Directory Layout

```
backend/       FastAPI application and storage utilities
frontend/      Placeholder web UI served separately
data/          Local database and uploaded files
pyproject.toml Python package configuration
requirements.txt List of packages for `uv` to install
```

## Setup

[RAG Inspector](https://github.com/astral-sh/uv) uses `uv` to manage Python
dependencies.

1. Install `uv`:
   ```bash
   pip install uv
   ```
2. Create a virtual environment and install requirements:
   ```bash
   uv venv
   uv pip install -r requirements.txt
   ```

## Running the Backend

Start the API with [Uvicorn](https://www.uvicorn.org/):

```bash
uvicorn backend.app.main:app --reload
```

The API provides endpoints to upload files (`/upload`), trigger an evaluation
(`/evaluate`), and download generated reports (`/reports/{filename}`).

## Running the Frontend

A very small HTML page lives in the `frontend` directory. Serve it with any static
file server, e.g.:

```bash
python -m http.server 8001 --directory frontend
```

Then open <http://localhost:8001> in your browser.

## Documentation Links

- [FastAPI documentation](https://fastapi.tiangolo.com/)
- [Uvicorn documentation](https://www.uvicorn.org/)
- [uv documentation](https://github.com/astral-sh/uv)
