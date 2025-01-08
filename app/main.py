from fastapi import FastAPI
from app.schema import MatchPredict
import requests
import uvicorn

MICROSERVICE_URL = "http://127.0.0.1:8001/"  
app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.post("/predict")
def predict(match_data: MatchPredict):

    try:
        response = requests.post(MICROSERVICE_URL, json=match_data)
        response_data = response.json()
        return {"prediction": response_data["prediction"]}
    except Exception as e:
        return {"error": str(e)}

if __name__ == "__main__":
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)