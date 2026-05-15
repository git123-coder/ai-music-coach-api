def compute_score(analysis: dict):
    tempo = analysis.get("tempo", 0)
    timing = analysis.get("timing_variation", 0)
    pitch = analysis.get("pitch_accuracy", 0)

    # Simple scoring logic (you can tweak later)
    timing_score = max(0, 100 - (timing * 20))
    tempo_score = 80 if 60 <= tempo <= 140 else 60
    pitch_score = max(0, 100 - (pitch / 10))

    overall = (timing_score + tempo_score + pitch_score) / 3

    return {
        "timing": round(timing_score, 2),
        "tempo": round(tempo_score, 2),
        "pitch": round(pitch_score, 2),
        "overall": round(overall, 2)
    }