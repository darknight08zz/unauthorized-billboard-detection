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
    # Load image to read dimensions (stub for now)
    content = await file.read()
    image = Image.open(io.BytesIO(content)).convert("RGB")
    w, h = image.size
# ---- STUB RESULT ----
    # Replace later with actual YOLOv8 + rules engine
    boxes = [
        {"x": int(w*0.1), "y": int(h*0.1), "w": int(w*0.6), "h": int(h*0.3),
         "label": "billboard", "score": 0.92}
    ]
    reasons = ["Size check pending", "Permit check pending"]

    # Add simple rule hint based on optional lat/lon
    if latitude is not None and longitude is not None:
        reasons.append("Location captured")

    return DetectionResponse(
        boxes=boxes,
        violation_reasons=reasons,
        width=w,
        height=h,
    )
