from groq import Groq
import os

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def generate_feedback(analysis: dict, issues: list, score: dict, sections: list) -> str:
    prompt = f"""
You are a professional music coach.

Performance Data:
- Tempo: {analysis.get('tempo')}
- Pitch Accuracy: {analysis.get('pitch_accuracy')}
- Timing Variation: {analysis.get('timing_variation')}
- Issues: {issues}
- Scores: {score}
- Sections: {sections}

Instructions:
- Give 2–3 short, direct sentences
- If tempo is already slow (<70 BPM), do NOT suggest slowing down
- Focus on timing and pitch improvement if present
- Suggest realistic actions (metronome, repetition, slow practice only if tempo is high)
- If a section has worse timing, mention it (e.g., “middle section has timing issues”)
- Only refer to section timing issues (NOT pitch per section)
- If mentioning sections, base it ONLY on timing_variation
- If section tempos vary a lot, mention "inconsistent tempo across sections"
- Be concise and specific

Output only plain text. No quotes.
"""

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.4,
    )

    return response.choices[0].message.content.strip().replace("\n", " ")