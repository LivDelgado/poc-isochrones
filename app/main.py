from os import stat
from typing import Optional, List
from fastapi import FastAPI
from app.delivery.delivery_service import LocationDistanceService
from app.delivery.location_delivery import LocationDistance
from app.isochrones.isochrone_service import IsochroneService
from app.locations.location_service import LocationService
from app.locations.location import Location

def start_application():
    app = FastAPI(
        title="Isochrones PoC",
    )

    return app

app = start_application()

location_service = LocationService()
isochrone_service = IsochroneService()
delivery_service = LocationDistanceService()

@app.on_event("startup")
def app_startup():
    isochrone_service.prepare_isochrones_table()

@app.get("/locations", response_model=List[Location])
def get_locations():
    return location_service.get_locations()

@app.get("/locations/{location_id}", response_model=Optional[Location])
def get_location(location_id: str):
    return location_service.get_location(location_id)

@app.get("/deliveries", response_model=Optional[List[LocationDistance]])
def get_locations_that_can_deliver_to_address(
    address: str,
    zip: str,
    state: str,
    city: str,
    time_limit_minutes: Optional[int] = None
):
    return delivery_service.get_locations_near_address(
        address=address,
        zip=zip,
        state=state,
        city=city,
        time_limit_minutes=time_limit_minutes
    )