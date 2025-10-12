# 🧠 Customer Churn Prediction — End-to-End MLOps Project

This project demonstrates a **complete MLOps pipeline** for predicting customer churn using machine learning.  
It covers data preprocessing, model training, experiment tracking, containerization, and CI/CD automation with GitHub Actions and Docker.

---

## 🚀 Project Overview

The goal is to build a **production-ready ML pipeline** that predicts whether a customer is likely to churn based on historical behavior and demographic data.

**Key steps implemented:**
- 🧹 **Data Preprocessing:** Cleaned and encoded categorical features.  
- 🤖 **Model Training:** Trained multiple ML models (Random Forest, XGBoost, Logistic Regression, Gradient Boosting).  
- 🧾 **Model Tracking:** Used MLflow to log metrics, parameters, and artifacts.  
- 💾 **Model Packaging:** The best-performing model is saved and versioned in the `churn_model/` directory.  
- 🌐 **API Deployment:** Served via FastAPI application with Uvicorn.  
- 🐳 **Containerization:** Dockerized the entire app for consistent deployment.  
- 🔁 **Automation (CI/CD):** GitHub Actions automatically builds and pushes the latest Docker image to DockerHub on every commit to `main`.

---

## 🧰 Tech Stack

| **Category**          | **Tools / Libraries**                     |
|------------------------|------------------------------------------|
| **Language**           | Python 3.10                              |
| **ML Libraries**       | scikit-learn, XGBoost                    |
| **Experiment Tracking**| MLflow                                   |
| **Web Framework**      | FastAPI                                  |
| **Model Serving**      | Uvicorn                                  |
| **Containerization**   | Docker                                   |
| **Automation**         | GitHub Actions                           |
| **Data Handling**      | Pandas, NumPy                            |
| **Visualization**      | Matplotlib, Seaborn *(optional)*         |

---

## 📁 Project Structure

```
customer_churn_mlops/
│
├── app.py                  # FastAPI app for model inference
├── train.py                # Model training & MLflow logging
├── Dockerfile              # Docker build configuration
├── requirements.txt        # Python dependencies
│
├── churn_model/            # Saved model artifacts
│   ├── model.pkl
│   └── preprocessing.pkl
│
├── .github/workflows/
│   └── docker-build.yml    # GitHub Actions for Docker CI/CD
│
└── README.md               # Project documentation
```

---

## 🧪 How to Run Locally

### 1️⃣ Clone the repository
```bash
git clone https://github.com/<your-username>/customer_churn_mlops.git
cd customer_churn_mlops
```

### 2️⃣ Install dependencies
```bash
pip install -r requirements.txt
```

### 3️⃣ Train the model
```bash
python train.py
```

### 4️⃣ Run the FastAPI app
```bash
uvicorn app:app --reload
```

Then open:  
👉 **http://127.0.0.1:8000/docs** — to test the API using Swagger UI.

---

## 🐳 Run with Docker

### Build the Docker image
```bash
docker build -t customer-churn-mlops .
```

### Run the container
```bash
docker run -p 8000:8000 customer-churn-mlops
```

Now open:  
👉 **http://localhost:8000/docs**

---

## 📦 Example JSON Request
```json
{
  "gender": "Male",
  "SeniorCitizen": 0,
  "Partner": "Yes",
  "Dependents": "No",
  "tenure": 5,
  "PhoneService": "Yes",
  "InternetService": "Fiber optic",
  "Contract": "Month-to-month",
  "PaperlessBilling": "Yes",
  "PaymentMethod": "Electronic check",
  "MonthlyCharges": 75.35,
  "TotalCharges": 375.5
}
```

### Sample Response
```json
{
  "churn_prediction": "Yes"
}
```

---

## ⚙️ CI/CD Pipeline Summary

Every push to the `main` branch triggers a GitHub Actions workflow that:
- Builds the latest Docker image  
- Pushes it to DockerHub  
- Ensures the project stays **deployment-ready at all times**

---

## 👨‍💻 Author

**Lutfihadi**  


