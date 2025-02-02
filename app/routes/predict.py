from fastapi import APIRouter
import requests
from os import getenv
from dotenv import load_dotenv

from app.schemas import MatchPredictionRequest

load_dotenv()

ML_MICROSERVICE_API_URL = getenv("ML_MICROSERVICE_API_URL")

predict_router = APIRouter()


@predict_router.post("/predict")
def predict(match_data: MatchPredictionRequest):
    response = requests.post(
        f"{ML_MICROSERVICE_API_URL}predict", json=match_data.dict()
    )

    return response.json()
