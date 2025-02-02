from pydantic import BaseModel


class MatchPredictionRequest(BaseModel):
    home_team: str
    away_team: str
    tournament: str
