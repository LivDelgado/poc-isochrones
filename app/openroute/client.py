from typing import Dict, List, Tuple
import openrouteservice

THIRTY_MINUTES = 30*60
ONE_HOUR = 60*60
TWO_HOURS = 120*60
RANGE = [THIRTY_MINUTES, ONE_HOUR]
INTERVAL = THIRTY_MINUTES
PROFILE = 'driving-car'
RANGE_TYPE = 'time'

class OpenRouteClient: 

    def __init__(self) -> None:
        self.client = openrouteservice.Client(key='5b3ce3597851110001cf6248ce160bba12f246b181faf24c0f39780c')
        
    def get_isochrones_api(self, coordinates: List[Tuple[float, float]]) -> Dict:
        isochrones = openrouteservice.isochrones.isochrones(
            self.client,
            coordinates,
            profile=PROFILE,
            range_type=RANGE_TYPE,
            range=RANGE
        )

        return isochrones
    
    def get_coordinates_api(self, address: str, zip: str, state: str, city: str) -> Dict:
        coordinates = openrouteservice.geocode.pelias_structured(
            client=self.client,
            address=address,
            locality=city,
            region=state,
            postalcode=zip,
            country='US'
        )

        return coordinates