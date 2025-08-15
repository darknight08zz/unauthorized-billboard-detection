from ai_model.detector_stub import detect_billboards  # Import the AI stub
from fastapi import FastAPI, File, UploadFile, Form
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from typing import List, Optional
from PIL import Image
import io

app = FastAPI(title="Unauthorized Billboard Detection API", version="0.1.0")

@app.get("/")
def read_root():
    return {"message": "Unauthorized Billboard Detection API is running"}

class Box(BaseModel):
    x: int
    y: int
    w: int
    h: int
    label: str
    score: float

class DetectionResponse(BaseModel):
    boxes: List[Box]
    violation_reasons: List[str]
    width: int
    height: int

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/detect", response_model=DetectionResponse)
async def detect(
    file: UploadFile = File(...),
    latitude: Optional[float] = Form(None),
    longitude: Optional[float] = Form(None),
    timestamp: Optional[str] = Form(None),
):
    # Load image into PIL format
    content = await file.read()
    image = Image.open(io.BytesIO(content)).convert("RGB")
    w, h = image.size

    # Call AI detection stub (replace with YOLOv8 later)
    boxes = detect_billboards(image)

    # Add violation reasons
    reasons = ["Size check pending", "Permit check pending"]
    if latitude is not None and longitude is not None:
        reasons.append("Location captured")

    return DetectionResponse(
        boxes=boxes,
        violation_reasons=reasons,
        width=w,
        height=h,
    )
