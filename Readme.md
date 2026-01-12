# Live Demo

# Diabetes Risk Prediction 🩺
* A Web based Diabetes risk prediction for analyzing paitents health and predicting the risk level.
* Built using HTML, Css and bootstrap for frontend and machine learning algorithms using python
   libraries like scikit-learn, numpy , pandas ,xgboost, joblib and fastapi for model serving.

# Project Structure 
📦 Diabetes-Prediction-App
├── data/
|   └── diabetes.zip

|
├── 📂 extracted_data/
|   ├── data_ingestion.py
│   └── diabetes.csv

│ 
├── 📁 logic
|   ├── risk.py
|   └── recommendations.py

|
├── 📂 templates/
│   └── index.html

│
├── 📂 static/
│   ├── css/
│   └── images/

│
├── 📂 notebook/
│   ├── pipeline_models/
|      ├── kneighbors.py
|      ├── logistic_regression.py
|      ├── random_forest.py
|      ├── xgboost.py
|      └── reports.py

|
|   ├── src/
|       ├── handle_missing_values.py
|       ├── preprocessing.py
|       └── split_data.py

|   ├── EDA.ipynb
|   └── diabetes_pipeline.joblib

|
├──  main.py  
├── requirements.txt
└── README.md

# Structure Info

### 📂 data/
Collected dataset from kaggle (PIMA) diabetes dataset.

### 📂 extracted_data/
performed data ingestion to extract data from .zip file in data file.

- `data_ingestion.py` – used python logic to extract the .zip file
### 📂 logic/
Implemented logic for diabetes risk and recommendation.

- `risk.py` – used python to calculate risk level
- `recommendation.py` – used python logic to recommend based on risk level

### 📂 templates/
HTML templates rendered using Jinja2.

- `index.html` – User input form and prediction result display
### 📂 static/
Static assets like CSS and images used in frontend UI.

### 📂 notebook/

**pipeline_model/**
performed logic to train and visualize the models accuracy

- `logistic_regression.py` – Perfomed Logistic Regression logic
- `kneighbors.py` – Performed KNeighbors Classigfiers logic
- `random_forest.py` – Performed RandomForest Classifier logic
- `xbgoost_model` – Performed XGBoostClassifier logic
- `reports.py` – Defined logic to evaluate the model using classification report, accuracy and confusion matrix and to compare them.
  
**src/**
used logic to perform basic data cleaning and preprocessing logic.

- `handle_missing_values.py` – Used a logic to clean missing values.
- `preprocessing` – Used logic to scale values using StandardScaler
- `split_data.py` – Used logic to split data into train_test_split and defined features and target values

**EDA.ipynb/**
Performed Exploartory Data Analysis and Model training in notebook and analyzed the models performance

**diabetes_pipeline.joblib/**
saved the best model using joblib

**main.py**
Served model using FastAPI

## ⚙️ How It Works

1. The user enters health parameters such as pregnancies,mGlucose level, BMI, Age, Blood Pressure, SkinThickness and Insulin through the web interface.

2. The submitted form data is sent to the FastAPI backend via an HTTP POST request.

3. The backend preprocesses the input data by:
   - Converting it into a numerical feature array
   - Applying the same scaling and transformations used during model training

4. The preprocessed data is passed to the trained machine learning model to generate:
   - A binary prediction (Diabetic / Non-Diabetic)
   - A probability score indicating risk confidence

5. Based on the predicted probability:
   - Risk level is classified as Low, Medium, or High
   - Personalized health recommendations are generated using rule-based logic

6. The prediction result, probability score, risk level, and recommendations are rendered back to the user on the same web page.

### Risk Level Logic
- Probability < 0.30 → Low Risk
- Probability between 0.30 and 0.60 → Medium Risk
- Probability > 0.60 → High Risk


# Tech Stack ⚙️

| Technology | Usage |
|-----------|--------|
| Python | Backend logic |
| Scikit-learn | Machine learning |
| FastAPI | API framework |
| Pandas | Data processing |
| NumPy | Numerical computation |
| HTML/CSS | Frontend |
| Bootstrap | Styling |


## 🚀 Run Locally

### 1. Clone the Repository
```bash
https://github.com/Ajju-03/diabetes_risk_prediction.git

### 2. Create a Virtual Environment

python -m venv venv

### 3. Activate it

**Windows**

venv\Scripts\activate

**MacOS**

source venv/bin/activate

### 3. install dependencies

pip install -r requirements.txt

### 4. Start the Application
uvicorn app.main:app --reload

### API Documentation
FastAPI automatically generates interactive API docs:

- Swagger UI: http://127.0.0.1:8000/docs
- ReDoc: http://127.0.0.1:8000/redoc

