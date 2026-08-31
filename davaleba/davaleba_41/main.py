from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy import select
from sqlalchemy.orm import Session

from database import engine, Base, get_session
from models import Trip
from schemas import TripCreate, TripResponse




Base.metadata.create_all(engine)




app = FastAPI(
    title="Travel API"
)




@app.post("/trips", response_model=TripResponse)
def create_trip(
    trip_data: TripCreate,
    session: Session = Depends(get_session)
):
    trip = Trip(
        destination=trip_data.destination,
        country=trip_data.country,
        days=trip_data.days,
        budget=trip_data.budget,
        is_completed=trip_data.is_completed
    )

    session.add(trip)
    session.commit()
    session.refresh(trip)

    return trip




@app.get("/trips", response_model=list[TripResponse])
def get_trips(
    session: Session = Depends(get_session)
):
    statement = select(Trip)

    result = session.execute(statement)

    trips = result.scalars().all()

    return trips




@app.get("/trips/{trip_id}", response_model=TripResponse)
def get_trip(
    trip_id: int,
    session: Session = Depends(get_session)
):
    statement = select(Trip).where(
        Trip.id == trip_id
    )

    result = session.execute(statement)

    trip = result.scalar_one_or_none()

    if trip is None:
        raise HTTPException(
            status_code=404,
            detail="Trip not found"
        )

    return trip




@app.put("/trips/{trip_id}", response_model=TripResponse)
def update_trip(
    trip_id: int,
    trip_data: TripCreate,
    session: Session = Depends(get_session)
):
    statement = select(Trip).where(
        Trip.id == trip_id
    )

    result = session.execute(statement)

    trip = result.scalar_one_or_none()

    if trip is None:
        raise HTTPException(
            status_code=404,
            detail="Trip not found"
        )

    trip.destination = trip_data.destination
    trip.country = trip_data.country
    trip.days = trip_data.days
    trip.budget = trip_data.budget
    trip.is_completed = trip_data.is_completed

    session.commit()
    session.refresh(trip)

    return trip




@app.delete("/trips/{trip_id}")
def delete_trip(
    trip_id: int,
    session: Session = Depends(get_session)
):
    statement = select(Trip).where(
        Trip.id == trip_id
    )

    result = session.execute(statement)

    trip = result.scalar_one_or_none()

    if trip is None:
        raise HTTPException(
            status_code=404,
            detail="Trip not found"
        )

    session.delete(trip)
    session.commit()

    return {
        "message": "Trip deleted successfully"
    }