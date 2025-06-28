from fastapi import FastAPI

app = FastAPI()

@app.get("/health")
def health_check():
    """Check service status."""
    return {"status": "OK"}
