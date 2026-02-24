from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Jenkins CI/CD is working successfully!"}

@app.get("/health")
def health_check():
    return {"status": "healthy"}
