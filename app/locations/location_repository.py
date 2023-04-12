from typing import List
from app.database.config import DatabaseConfig
from app.locations.location import Location

INSERT_QUERY = """INSERT INTO STORES VALUES(%s)"""
SELECT_ALL_QUERY = """
    SELECT
        id,
        address_street,
        zip_code,
        address_state,
        address_city,
        ST_X(coordinates),
        ST_Y(coordinates)
    FROM STORES
"""

class StoreRepository:
    def __init__(self) -> None:
        self.database_config = DatabaseConfig()

    def insert_location(self, location: Location):
        self.database_config.insert_one_register(INSERT_QUERY, tuple(location))

    def insert_locations(self, locations: List[Location]):
        self.database_config.insert_multiple_registers(INSERT_QUERY, locations)
    
    def get_locations(self) -> List[Location]:
        number_of_registers, all_locations_db = self.database_config.get_registers(SELECT_ALL_QUERY)
        locations = []

        for location_tuple in all_locations_db:
            id, address, zip, state, city, coordinates_x, coordinates_y = location_tuple
            locations.append(Location(id, address, zip, state, city, (coordinates_x, coordinates_y)))
        
        return locations
    
    def get_location(self, id: str) -> Location:
        SELECT_BY_QUERY = f"""
        SELECT 
            id,
            address_street,
            zip_code,
            address_state,
            address_city,
            ST_X(coordinates),
            ST_Y(coordinates)
        FROM STORES 
        WHERE id '{id}'"""
        
        number_of_registers, location_db = self.database_config.get_registers(SELECT_BY_QUERY)

        if not location_db:
            return None

        id, address, zip, state, city, coordinates_x, coordinates_y = location_db[0]

        return Location(id, address, zip, state, city, (coordinates_x, coordinates_y))
