from fastapi import FastAPI

app = FastAPI(
    title="Personalized Networking Assistant",
    version="1.0.0"
)

@app.get("/")
def root():
    return {"message": "Personalized Networking Assistant API is running!"}