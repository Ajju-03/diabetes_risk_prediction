def get_risk_level(prob, glucose, bmi):
    if prob >= 0.7 or glucose >= 160 or bmi >= 35:
        return "High"
    elif prob >= 0.4 or glucose >= 120 or bmi >= 25:
        return "Medium"
    else:
        return "Low"