from pydantic import BaseModel


class TripCreate(BaseModel):
    destination: str
    country: str
    days: int
    budget: int
    is_completed: bool


class TripResponse(BaseModel):
    id: int
    destination: str
    country: str
    days: int
    budget: int
    is_completed: bool

    class ConfigDict:
        from_attributes = True