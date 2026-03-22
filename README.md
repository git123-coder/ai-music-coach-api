📌 AI Music Coach API

A backend API that analyzes musical performance from audio recordings (guitar/piano) and returns actionable feedback on tempo, pitch characteristics, and timing consistency.

🚀 Features
Upload audio recordings via API
Extract musical features using audio signal processing:
Tempo detection
Pitch estimation
Timing consistency
Generate human-readable feedback using rule-based logic
Store analysis results in PostgreSQL
Deployed backend with live API endpoint

🧠 How It Works
User uploads an audio file
Audio is processed using librosa:
Beat tracking → tempo
Pitch estimation (YIN)
Onset detection → timing variation
Extracted metrics are passed into a rule-based feedback engine
API returns structured analysis + actionable suggestions

⚡ Note: For performance, analysis is limited to the first few seconds of audio.

🛠 Tech Stack
FastAPI (backend)
PostgreSQL (database)
Librosa (audio analysis)
Python


🌐 Live API
https://ai-music-coach-api.onrender.com/docs

(Replace with your actual deployed URL)

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


⚙️ Setup (Local)
git clone <your-repo>
cd <repo>
pip install -r requirements.txt
uvicorn app.main:app --reload


🧪 Quick Test

You can test using any short .wav file or use the sample file in /samples/test.wav for testing.

Go to /docs
Use the /analyze endpoint
Upload an audio file (5–10 seconds recommended)

🔮 Future Improvements
Session-based progress tracking
Real-time feedback
Visual performance graphs
More accurate pitch modeling
Frontend interface for audio upload and visualization