import ast

def calculate_progress(previous, current):
    try:
        prev_score = ast.literal_eval(previous)["score"]["overall"]
        curr_score = current["overall"]

        diff = round(curr_score - prev_score, 2)

        if diff > 0:
            return f"Improved by {diff} points"
        elif diff < 0:
            return f"Decreased by {abs(diff)} points"
        else:
            return "No change"

    except:
        return "Not enough data"