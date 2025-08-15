# Unauthorized Billboard Detection

## 📌 Overview
A mobile and web-based solution to detect, verify, and report unauthorized billboards using **AI**, **computer vision**, and **geotagging**.  
The goal is to assist municipal authorities and citizens in identifying non-compliant hoardings in urban landscapes — reducing visual pollution, improving safety, and ensuring regulatory compliance.

---

## 🚀 Features
- 📸 **In-app Camera Detection** – Capture live or upload batch images for analysis.
- 🌐 **Automatic Geotagging & Timestamp** – Location & time metadata is auto-attached.
- 🔍 **AI Detection Model** – Detects billboard size, placement, and content violations.
- 🗂 **Citizen Reporting Portal** – For uploading reports & tracking case status.
- 📊 **Violation Heatmap** – Public or private map visualization of flagged billboards.
- ✅ **Regulatory Cross-check** – Verifies against municipal permit databases.
- 🛡 **Privacy & Security** – Data encrypted in transit & at rest, with user consent.

---

## 🛠 Tech Stack
| Component        | Technology Choices |
|------------------|--------------------|
| Mobile App       | Flutter (Dart) |
| Backend API      | FastAPI (Python) |
| AI Model         | YOLOv8 + OCR (EasyOCR/Tesseract) |
| Database         | PostgreSQL + PostGIS |
| Cloud Storage    | AWS S3 |
| Maps API         | Google Maps / Mapbox |

---

## 📂 Project Structure
unauthorized-billboard-detection/
│
├── mobile_app/ # Flutter mobile application
├── backend/ # FastAPI backend + AI detection service
├── ai_model/ # Training scripts, datasets, model weights
├── docs/ # Architecture diagram, pitch deck, compliance checklist
└── .github/ # GitHub Actions workflows (CI/CD)

yaml
Copy
Edit

---


git clone https://github.com/YOUR_USERNAME/unauthorized-billboard-detection.git
cd unauthorized-billboard-detection
2️⃣ Setup the Mobile App
cd mobile_app
flutter pub get
flutter run

3️⃣ Setup the Backend (FastAPI)
cd backend
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
uvicorn main:app --reload

4️⃣ Environment Variables
Create a .env file in both /backend and /mobile_app for:
GOOGLE_MAPS_API_KEY=your_key
AWS_ACCESS_KEY_ID=your_key
AWS_SECRET_ACCESS_KEY=your_key
DATABASE_URL=postgresql://user:password@host:port/dbname

📸 Usage Flow
Open the App – Select "Live Detection" or "Upload Image".
Capture / Upload – Take a picture of the suspected billboard.
AI Analysis – Model detects violations (size, placement, content).
Review & Submit – User confirms/corrects detection before sending.
Report Storage – Backend saves report with geotag & timestamp.
Authority Dashboard – City officials review flagged cases.
Heatmap View – Aggregated violation trends.

🛡 Data Privacy & Compliance
Complies with India’s Data Protection Act and GDPR principles.
All uploads encrypted in transit (HTTPS) and at rest (AES-256).
No facial recognition or personal surveillance beyond project scope.
Explicit user consent before data submission.

📊 Roadmap
 Initial Flutter app with camera & geotagging
 FastAPI backend + YOLOv8 cloud detection
 PostgreSQL + PostGIS integration
 OCR for billboard text
 Admin dashboard for authorities
 Public heatmap view

📄 License
This project is licensed under the MIT License – see the LICENSE file for details.
🤝 Contributing
Contributions are welcome!

Fork the repo
Create a feature branch (git checkout -b feature-name)
Commit changes (git commit -m 'Add some feature')
Push to branch (git push origin feature-name)
Create a Pull Request

📧 Contact
For queries or collaborations:
Name: Ujjwal Prajapati
Email: prajapatiujjwal0802@gmail.com
GitHub: @darknight08zz
