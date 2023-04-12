from typing import List, Optional
from app.delivery.location_distance_repository import LocationDistanceRepository

from app.delivery.location_delivery import LocationDistance
from app.isochrones.isochrones_repository import IsochronesRepository


class LocationDistanceService:
    def __init__(self) -> None:
        self.isochrone_repository = IsochronesRepository()
        self.location_distance_repository = LocationDistanceRepository()

    def get_locations_near_address(
        self,
        address: str,
        zip: str,
        state: str,
        city: str,
        time_limit_minutes: Optional[int]
    ) -> List[LocationDistance]:
        coordinates = self.isochrone_repository.get_coordinate_from_address(
            address=address,
            zip=zip,
            state=state,
            city=city
        )

        if not coordinates:
            return []
        
        if not time_limit_minutes:
            return self.location_distance_repository.get_locations_near_coordinates(coordinates=coordinates)
        
        return self.location_distance_repository.get_locations_that_reach_address_within_time_range(
            coordinates=coordinates,
            time_limit_minutes=time_limit_minutes
        )