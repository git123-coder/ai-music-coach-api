####OPENAI IMPLEMENTATION FOR FEEDBACK GENERATION####

# from openai import OpenAI
# import os

# client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# def generate_feedback(analysis):

#     prompt = f"""

#     A music student submitted a recording.

#     Analysis:

#     Tempo: {analysis['tempo']}
#     Pitch Accuracy: {analysis['pitch_accuracy']}
#     Timing Variation: {analysis['timing_variation']}

#     Give specific actionable feedback to improve.

#     """

#     response = client.chat.completions.create(
#         model="gpt-4o-mini",
#         messages=[{"role":"user","content":prompt}]
#     )

#     return response.choices[0].message.content


def generate_feedback(analysis: dict):

    feedback = []

    tempo = analysis["tempo"]
    pitch_accuracy = analysis["pitch_accuracy"]
    timing_variation = analysis["timing_variation"]

    # Pitch feedback
    if pitch_accuracy < 0.5:
        feedback.append(
            "Pitch accuracy is low. Practice slowly and match each note carefully."
        )
    elif pitch_accuracy < 0.75:
        feedback.append(
            "Pitch accuracy is moderate. Try practicing scales to improve tuning."
        )

    # Timing feedback
    if timing_variation > 0.25:
        feedback.append(
            "Your timing fluctuates significantly. Practice with a metronome at 60 BPM."
        )
    elif timing_variation > 0.15:
        feedback.append(
            "Timing is slightly inconsistent. Focus on steady rhythm while practicing."
        )

    # Tempo feedback
    if tempo < 60:
        feedback.append(
            "The tempo is slow. Once comfortable, gradually increase your practice speed."
        )

    if tempo > 140:
        feedback.append(
            "The tempo is quite fast. Consider practicing slower to maintain accuracy."
        )

    # Default message
    if not feedback:
        feedback.append(
            "Good performance overall. Focus on maintaining consistent timing and pitch."
        )

    return " ".join(feedback)