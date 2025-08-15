from typing import List, Dict
from PIL import Image

def detect_billboards(image: Image.Image) -> List[Dict]:
    w, h = image.size
    return [{
        "x": int(w * 0.1),
        "y": int(h * 0.1),
        "w": int(w * 0.6),
        "h": int(h * 0.3),
        "label": "billboard",
        "score": 0.92
    }]
