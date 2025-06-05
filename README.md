# RAG-Inspector

This project uses [uv](https://github.com/astral-sh/uv) to manage Python dependencies.
Dependencies are defined in `pyproject.toml`.

## Setup

Install uv with pip:

```bash
pip install uv
```

Create a virtual environment and install requirements:

```bash
uv venv
uv pip install -r requirements.txt
```

Run the development server:

```bash
uvicorn backend.app.main:app --reload
```

## Database

The backend persists metadata in a small SQLite database at
`data/database.db`. Tables are created automatically on startup, but you can
also initialize them manually:

```bash
python -c "from backend.app.storage import init_db; init_db()"
```

## Evaluation

Run a stub evaluation and generate report files:

```bash
curl -X POST http://localhost:8000/evaluate
```

Download a generated report:

```bash
curl -O http://localhost:8000/reports/evaluation.csv
```
