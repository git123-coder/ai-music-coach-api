📌 AI Music Coach API

A backend API that analyzes a student's musical performance (guitar/piano) from an audio recording and provides actionable feedback on timing, tempo, and pitch.

🚀 Features

Upload audio recordings via API

Extract musical features using signal processing:

Tempo detection

Pitch analysis

Timing consistency

Generate human-readable feedback

Store analysis results

🧠 How It Works

User uploads an audio file

Audio is processed using librosa:

Beat tracking → tempo

Pitch estimation

Onset detection → timing variation

Extracted metrics are passed into a feedback engine

API returns structured analysis + actionable suggestions

🛠 Tech Stack

FastAPI (backend)

PostgreSQL (database)

Librosa (audio analysis)

Python

📥 API Endpoint
Upload Recording
POST /analyze

Request:

multipart/form-data

file: audio file

Response:

{
  "analysis": {
    "tempo": 184.57,
    "pitch_accuracy": 1000.01,
    "timing_variation": 1.47
  },
  "feedback": "Your timing fluctuates significantly. Practice with a metronome at 60 BPM."
}
⚙️ Setup
git clone <your-repo>
cd <repo>
pip install -r requirements.txt
uvicorn app.main:app --reload
🔮 Future Improvements

Real-time feedback

User authentication & profiles

Better pitch accuracy modeling

Visual performance graphs

AI-based personalized practice plans