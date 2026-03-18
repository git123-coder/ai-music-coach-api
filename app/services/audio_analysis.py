import librosa
import numpy as np

def analyze_audio(file_path):

    y, sr = librosa.load(file_path)

    tempo, beats = librosa.beat.beat_track(y=y, sr=sr)

    pitches, magnitudes = librosa.piptrack(y=y, sr=sr)

    pitch_values = pitches[magnitudes > np.median(magnitudes)]

    pitch_accuracy = float(np.mean(pitch_values)) if len(pitch_values) > 0 else 0

    onset_env = librosa.onset.onset_strength(y=y, sr=sr)

    tempo_consistency = float(np.std(onset_env))

    return {
        "tempo": tempo.item(),
        "pitch_accuracy": pitch_accuracy,
        "timing_variation": tempo_consistency
    }