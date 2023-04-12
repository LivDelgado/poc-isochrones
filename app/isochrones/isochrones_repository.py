from typing import List, Optional, Tuple
from postgis import Polygon, Point

from app.database.config import DatabaseConfig
from app.isochrones.isochrone import Isochrone
from app.openroute.client import OpenRouteClient
from app.locations.location import Location

class IsochronesRepository:
    def __init__(self) -> None:
        self.open_route_client = OpenRouteClient()
        self.database_config = DatabaseConfig()
    
    def create_location_isochrone(self, location: Location):
        if not location.coordinates:
            coordinates = self.get_coordinate_from_location(location)
            if coordinates:
                self.save_coordinates_database(location.id, coordinates)
                location.coordinates = coordinates

        if not location.coordinates:
            return
        
        isochrones = self.get_isochrones_from_database(location)
        if isochrones:
            return

        isochrones = self.get_isochrones_from_api([location.coordinates])
        self.save_isochrones_database(location, isochrones)

    def get_coordinate_from_location(self, location: Location):
        return self.get_coordinate_from_address(
            address=location.address,
            zip=location.zip,
            state=location.state,
            city=location.city
        )
    
    def get_coordinate_from_address(self, address: str, zip: str, state: str, city: str):
        api_return = self.open_route_client.get_coordinates_api(
            address=address,
            zip=zip,
            state=state,
            city=city
        )

        if not api_return:
            return None

        features = api_return.get("features")
        coordinates = ()
        if features:
            feature = features[0]
            geometry = feature.get("geometry")
            coordinates = tuple(geometry.get("coordinates"))

        return coordinates
    
    def save_coordinates_database(self, location_id: int, coordinates: Tuple[float, float]):
        """
        update location register in the db - add coordinates
        """

        UPDATE_QUERY = f"""
            UPDATE Stores SET coordinates = %s WHERE id = %s
        """
        self.database_config.update_one_register(UPDATE_QUERY, (Point(x=coordinates[0], y=coordinates[1], srid=4326), location_id))

    def save_isochrones_database(self, location: Location, isochrones: List[Isochrone]):
        """
        save new isochrone register in the database
        """
        INSERT_QUERY = """
            INSERT INTO Stores_Isochrones
            VALUES (%s, %s, %s)
        """
        values_to_insert = [
            (
                location.id,
                isochrone.value,
                Polygon((tuple(isochrone.coordinates),), srid=4326)
            ) for isochrone in isochrones
        ]
        self.database_config.insert_multiple_registers(INSERT_QUERY, values_to_insert)

    def get_isochrones_from_api(self, coordinates: List[Tuple[float, float]]) -> List[Isochrone]:
        api_return = self.open_route_client.get_isochrones_api(coordinates=coordinates)

        if not api_return:
            return []

        isochrones = []
        for feature in api_return.get("features"):
            properties = feature.get("properties")
            geometry = feature.get("geometry")
            
            isochrone = Isochrone(
                value = int(properties.get("value")),
                center = tuple(properties.get("center")),
                coordinates = [tuple(c) for c in geometry.get("coordinates")[0]]
            )

            isochrones.append(isochrone)

        return isochrones

    def get_isochrones_from_database(self, location: Location):
        SELECT_BY_QUERY = f"""
        SELECT 
            location_id,
            interval,
            isochrone
        FROM STORES_ISOCHRONES
        WHERE location_id = '{location.id}'"""
        
        number_of_registers, registers = self.database_config.get_registers(SELECT_BY_QUERY)

        return registers
