from fastapi import FastAPI
from pydantic import BaseModel, Field
import joblib

app = FastAPI(title="Diabetes Prediction API")

model = joblib.load("notebook/diabetes_pipeline.joblib")
THRESHOLD = 0.4

# Input schema (MUST match training feature order)
class DiabetesInput(BaseModel):
    pregnancies: int = Field(..., ge=0, le=20)
    glucose: float = Field(...,ge=50, le=300)
    blood_pressure: float = Field(..., ge=40, le=200)
    skin_thickness: float = Field(..., ge=5, le=100)
    insulin: float = Field(..., ge=10, le=900)
    bmi: float = Field(...,ge=10, le=70)
    diabetes_pedigree: float = Field(..., ge=0.0, le=3.0)
    age: int = Field(..., ge=10, le=120)

@app.get("/")
def health_check():
    return {"status": "API is running"}

@app.get("/model-info")
def model_info():
    return {
        "model_type": type(model.named_steps["model"]).__name__,
        "threshold": THRESHOLD,
        "features": list(model.feature_names_in_)
    }

@app.post("/predict")
def predict(data: DiabetesInput):

    X = [[
        data.pregnancies,
        data.glucose,
        data.blood_pressure,
        data.skin_thickness,
        data.insulin,
        data.bmi,
        data.diabetes_pedigree,
        data.age
    ]]
    prediction = model.predict(X)[0]
    risk_score = model.predict_proba(X)[0][1]
    decision = 1 if risk_score >= 0.4 else 0

    return {
        "prediction": int(prediction),
        "probability": round(float(risk_score), 3),
        "decision": decision
        }


