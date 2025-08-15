"""
AI Detection Stub for Unauthorized Billboard Detection
-------------------------------------------------------
Replace this with real YOLOv8/TFLite inference later.
The function signature should remain the same.
"""

from typing import List, Dict
from PIL import Image

def detect_billboards(image: Image.Image) -> List[Dict]:
    """
    Pretend to detect billboards in the image.
    Returns a list of bounding boxes with dummy data.
    """
    w, h = image.size
    return [{
        "x": int(w * 0.1),
        "y": int(h * 0.1),
        "w": int(w * 0.6),
        "h": int(h * 0.3),
        "label": "billboard",
        "score": 0.92
    }]
