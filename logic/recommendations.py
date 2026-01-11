def generate_recommendations(data, prob):
    recs = []

    if data["Glucose"] > 140:
        recs.append("Reduce intake of sugary foods and refined carbohydrates.")

    if data["BMI"] >= 30:
        recs.append("Weight reduction through diet and regular physical activity is advised")

    if data["Age"] > 40:
        recs.append("Regular blood glucose monitoring is recommended.")

    if data["DiabetesPedigreeFunction"] > 0.5:
        recs.append("Family history detected - early medical screening is important.")

    if prob >= 0.6:
        recs.append("Consult a healthcare professional for confirmatory diagnostic tests.")

    if not recs:
        recs.append("Maintain a healthy lifestyle with balanced diet and exercise.")

    return recs                        