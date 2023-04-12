from typing import List, Optional
from app.locations.location import Location
from app.locations.location_repository import StoreRepository

class LocationService():
    location_repository = StoreRepository()
    locations = List[Location]

    def __init__(self) -> None:
        pass

    def get_locations(self) -> List[Location]:
        return self.location_repository.get_locations()

    def get_location(self, id: str) -> Optional[Location]:
        return self.location_repository.get_location(id)
