# Backend (FastAPI)

## Run (dev)
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate
pip install -r requirements.txt
uvicorn main:app --reload --host 0.0.0.0 --port 8000

## Test
curl http://localhost:8000/health

# Detect (replace sample.jpg with a real image path)
curl -X POST "http://localhost:8000/detect" \
  -F "file=@sample.jpg" \
  -F "latitude=22.57" \
  -F "longitude=88.36" \
  -F "timestamp=$(date -u +%Y-%m-%dT%H:%M:%SZ)"
