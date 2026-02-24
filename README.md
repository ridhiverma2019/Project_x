# 🚀 Python FastAPI Project with Jenkins CI/CD

This project demonstrates a simple FastAPI backend integrated with Jenkins CI pipeline.

---

## 📌 Features
- FastAPI REST API
- Jenkins CI Pipeline
- Virtual Environment setup
- Dependency installation
- Health check endpoint

---

## 🛠️ Setup Locally

### 1️⃣ Clone the repository
git clone <repo-url>
cd project

### 2️⃣ Create Virtual Environment
python -m venv venv

### 3️⃣ Activate Environment
Windows:
venv\Scripts\activate

Mac/Linux:
source venv/bin/activate

### 4️⃣ Install Dependencies
pip install -r requirements.txt

### 5️⃣ Run Application
uvicorn main:app --reload

Server will run at:
http://127.0.0.1:8000

---

## 🔁 Jenkins CI Pipeline

The Jenkinsfile performs:
- Code checkout
- Virtual environment setup
- Dependency installation
- Basic test stage
- Build status reporting

---

## 🔎 API Endpoints

GET /
Returns welcome message.

GET /health
Returns service health status.

---

## 👩‍💻 Author
Your Name
