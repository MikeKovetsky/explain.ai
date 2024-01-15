from fastapi import APIRouter, UploadFile, File

from processors.image import process_image
from processors.text import process_text

explain_router = APIRouter(prefix="/explain")


@explain_router.post("/text")
async def analyze_text(text: str, metadata=None):
    if metadata is None:
        metadata = {}
    explanation = process_text(text)
    return {"explanation": explanation}


@explain_router.post("/image")
async def analyze_image(file: UploadFile = File(...), metadata=None):
    if metadata is None:
        metadata = {}
    explanation = process_image(file)
    return {"explanation": explanation}

