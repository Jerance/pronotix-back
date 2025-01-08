from pydantic import BaseModel

class MatchPredict(BaseModel): 
    home_team: str 
    away_team: str 
    tournament: str 