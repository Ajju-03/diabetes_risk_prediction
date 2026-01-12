from fastapi import FastAPI, Request, Form
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
import joblib
from logic.risk import get_risk_level
from logic.recommendations import generate_recommendations
import numpy as np

app = FastAPI()

templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")

model = joblib.load("notebook/diabetes_pipeline.joblib")

@app.get("/", response_class=HTMLResponse)
def read_form(request: Request):
    return templates.TemplateResponse(
        "index.html",
        {"request": request, "result": None}
    )

@app.post("/predict", response_class=HTMLResponse)
def predict(
    request: Request,
    Pregnancies: int = Form(...),
    Glucose: float = Form(...),
    BloodPressure: float = Form(...),
    SkinThickness: float = Form(...),
    Insulin: float = Form(...),
    BMI: float = Form(...),
    DiabetesPedigreeFunction: float = Form(...),
    Age: int = Form(...)
):
    input_data = {
        "Pregnancies":Pregnancies,
        "Glucose": Glucose, 
        "BloodPressure": BloodPressure,
        "SkinThickness": SkinThickness,
        "Insulin": Insulin,
        "BMI": BMI,
        "DiabetesPedigreeFunction": DiabetesPedigreeFunction,
        "Age": Age}
    features = np.array([[Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age]])

    prediction = model.predict(features)[0]
    probability = model.predict_proba(features)[0][1]
    risk_level = get_risk_level(probability, Glucose, BMI)
    recs_list = generate_recommendations(input_data, probability)
    recommendations_text = " . ".join(recs_list)

    return templates.TemplateResponse("index.html",{"request": request,
       "prediction": "Diabetic" if prediction == 1 else "Non-Diabetic",
       "probability": round(probability, 2),
       "risk_level": risk_level,
       "recommendation": recommendations_text
        })

