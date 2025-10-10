from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import pandas as pd
import mlflow.sklearn

# Initialize FastAPI
app = FastAPI(title="Customer Churn Prediction API")

# Set MLflow tracking URI
mlflow.set_tracking_uri("file:///C:/MLCourse/mlruns")

# Load your MLflow model
model_path = "models/churn_model"
model = mlflow.sklearn.load_model(model_path)

# Define input schema using Pydantic
class CustomerData(BaseModel):
    gender: str
    SeniorCitizen: int
    Partner: str
    Dependents: str
    tenure: int
    PhoneService: str
    MultipleLines: str
    InternetService: str
    OnlineSecurity: str
    OnlineBackup: str
    DeviceProtection: str
    TechSupport: str
    StreamingTV: str
    StreamingMovies: str
    Contract: str
    PaperlessBilling: str
    PaymentMethod: str
    MonthlyCharges: float
    TotalCharges: float

@app.get("/")
def root():
    return {"message": "Customer Churn Prediction API is running"}

@app.post("/predict")
def predict_churn(data: CustomerData):
    try:
        # Convert Pydantic model to DataFrame
        df = pd.DataFrame([data.dict()])

        # Predict
        prediction = model.predict(df)[0]
        result = "Yes" if prediction == 1 else "No"

        return {"churn_prediction": result}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

