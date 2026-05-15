def detect_issues(analysis: dict):
    issues = []

    tempo = analysis.get("tempo", 0)
    timing = analysis.get("timing_variation", 0)
    pitch = analysis.get("pitch_accuracy", 0)

    if timing > 1.0:
        issues.append("timing drift")

    if tempo > 160:
        issues.append("high tempo")

    if pitch > 500:  # adjust based on your scale
        issues.append("pitch instability")

    return issues