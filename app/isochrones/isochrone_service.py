from app.isochrones.isochrones_repository import IsochronesRepository
from app.locations.location_repository import StoreRepository

class IsochroneService:
    def __init__(self) -> None:
        self.isochrone_repository = IsochronesRepository()
        self.location_repository = StoreRepository()

    def prepare_isochrones_table(self):
        locations = self.location_repository.get_locations()
        for location in locations:
            self.isochrone_repository.create_location_isochrone(location)
