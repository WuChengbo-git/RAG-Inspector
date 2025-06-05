from fastapi import FastAPI, File, UploadFile, HTTPException
from typing import List
from uuid import uuid4
from pathlib import Path

from .utils import extract_text, chunk_text
from .storage import (
    init_db,
    save_document_with_chunks,
    save_upload,
    UPLOAD_DIR,
)
from .models import UploadedFile

app = FastAPI()


@app.on_event("startup")
async def startup() -> None:
    """Prepare upload directory and database."""
    init_db()

@app.get("/")
async def read_root():
    return {"message": "Hello, World!"}


@app.post("/upload")
async def upload_files(files: List[UploadFile] = File(...)):
    """Upload one or more files to the temporary storage directory.

    Only files with the following extensions are allowed: ``.html``, ``.pdf``,
    and ``.txt``.
    """

    allowed_extensions = {".html", ".pdf", ".txt"}
    uploaded = []

    for upload in files:
        ext = Path(upload.filename).suffix.lower()
        if ext not in allowed_extensions:
            raise HTTPException(
                status_code=400,
                detail=f"Unsupported file type: {upload.filename}",
            )

        data = await upload.read()
        doc_id = str(uuid4())
        save_path = UPLOAD_DIR / f"{doc_id}{ext}"

        save_upload(data, save_path)

        text = extract_text(save_path)
        chunks = chunk_text(text)
        save_document_with_chunks(doc_id, upload.filename, chunks)

        uploaded.append(
            UploadedFile(
                document_id=doc_id,
                filename=upload.filename,
                size=len(data),
            )
        )

    return {"files": [file.model_dump() for file in uploaded]}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
