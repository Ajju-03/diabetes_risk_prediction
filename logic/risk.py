def get_risk_level(probability, glucose, bmi):
    if probability >= 0.7 and (glucose >= 160 or bmi >= 35):
        return "High Risk"
    elif probability >= 0.4 or (120 <= glucose < 160) or (25 <= bmi > 35):
        return "Medium Risk"
    else:
        return "Low Risk"