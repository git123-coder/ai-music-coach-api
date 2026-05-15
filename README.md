# 📌 AI Music Coach API

AI-powered backend API that analyzes musical performance from audio recordings (guitar/piano) and generates contextual coaching feedback using audio signal processing and LLM integration.

---

# 🚀 Features

* Upload audio recordings via REST API
* Extract musical performance metrics using audio signal processing:

  * Tempo detection
  * Pitch estimation
  * Timing consistency analysis
* Perform section-wise audio analysis for localized performance insights
* Detect performance issues:

  * Timing drift
  * Pitch instability
  * Tempo inconsistency
* Generate contextual coaching feedback using LLM integration via Groq
* Compute performance scores and overall rating
* Track progress across multiple recordings
* Store analysis results in database
* Deployed backend with live API endpoint

---

# 🧠 How It Works

1. User uploads an audio recording
2. Audio is processed using librosa:

   * Beat tracking → tempo analysis
   * Pitch estimation (YIN)
   * Onset detection → timing variation
3. Audio is split into sections for localized analysis
4. System detects performance issues and computes scores
5. Structured metrics are passed to an LLM
6. API returns contextual coaching feedback and analysis results

### ⚡ Note

For performance optimization, analysis is limited to the first few seconds of audio.

---

# 🛠 Tech Stack

* Python
* FastAPI
* SQLAlchemy
* PostgreSQL / SQLite
* librosa
* Groq API
* Uvicorn
* Render

---

# 🌐 Live API

### ⚠️ Note

Free-tier hosting may cause initial cold-start delays (~30–60 seconds).

https://ai-music-coach-api.onrender.com/docs

---

# 📥 API Endpoint

## POST `/analyze`

### Request

`multipart/form-data`

```bash
file: audio_file.wav
```

---

# 📤 Example Response

```json
{
  "analysis": {
    "tempo": 58.73,
    "pitch_accuracy": 931.39,
    "timing_variation": 1.79
  },
  "issues": [
    "timing drift",
    "pitch instability"
  ],
  "score": {
    "timing": 64.2,
    "tempo": 60,
    "pitch": 6.86,
    "overall": 43.69
  },
  "sections": [
    {
      "segment": 1,
      "tempo": 143.55,
      "timing_variation": 1.59
    }
  ],
  "progress": "Not enough data",
  "feedback": "Focus on improving timing consistency using a metronome and repeat difficult sections slowly to stabilize pitch."
}
```

---

# ⚙️ Local Setup

```bash
git clone <your-repo>
cd <repo>

pip install -r requirements.txt

uvicorn app.main:app --reload
```

---

# 🧪 Quick Test

* Open `/docs`
* Use the `/analyze` endpoint
* Upload a `.wav` audio file
* Recommended duration: 5–10 seconds

You can also use:

```bash
/samples/test.wav
```

---

# 🔮 Future Improvements

* Real-time feedback
* Frontend dashboard for visualization
* User authentication & profiles
* More advanced pitch modeling
* Streaming audio analysis
* Personalized practice recommendations
