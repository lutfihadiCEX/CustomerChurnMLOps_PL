# -------------------------------
# Dockerfile for Customer Churn MLOps API
# -------------------------------

# 1️⃣ Base image
FROM python:3.10-slim

# 2️⃣ Set working directory
WORKDIR /app

# 3️⃣ Copy project files into the container
COPY . /app

# 4️⃣ Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# 5️⃣ Expose FastAPI port
EXPOSE 8000

# 6️⃣ Start the FastAPI app
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
