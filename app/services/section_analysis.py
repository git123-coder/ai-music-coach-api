import librosa
import numpy as np

def analyze_sections(file_path: str, segment_duration: int = 3):
    y, sr = librosa.load(file_path)

    segment_length = segment_duration * sr
    sections = []

    for i, start in enumerate(range(0, len(y), segment_length)):
        segment = y[start:start + segment_length]

        if len(segment) < sr:  # skip very short segments
            continue

        tempo, _ = librosa.beat.beat_track(y=segment, sr=sr)
        tempo_value = float(tempo[0]) if hasattr(tempo, "__len__") else float(tempo)
        onset_env = librosa.onset.onset_strength(y=segment, sr=sr)
        timing_variation = float(np.std(onset_env))

        sections.append({
            "segment": i + 1,
            "tempo": round(tempo_value, 2),
            "timing_variation": round(timing_variation, 2)
        })

    return sections