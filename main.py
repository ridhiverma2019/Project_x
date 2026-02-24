from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Jenkins pipeline working successfully"}

@app.get("/health")
def health():
    return {"status": "ok"}
