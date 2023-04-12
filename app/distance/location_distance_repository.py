from typing import List, Optional, Tuple
from app.database.config import DatabaseConfig
from app.delivery.location_delivery import LocationDistance

SECONDS_IN_MINUTE = 60

class LocationDistanceRepository:
    def __init__(self) -> None:
        self.database_config = DatabaseConfig()
    
    def get_locations_near_coordinates(self, coordinates: Tuple) -> List[LocationDistance]:
        SELECT_BY_QUERY = f"""
            SELECT DISTINCT id, MIN(interval)
            FROM locations_isochrones
            JOIN locations ON (locations.id = locations_isochrones.location_id)
            WHERE 
                ST_Contains(
                    locations_isochrones.isochrone, 
                    ST_SetSRID(ST_MakePoint({coordinates[0]},{coordinates[1]}),
                    4326)
                )
            GROUP BY id
        """
        
        number_of_registers, registers = self.database_config.get_registers(SELECT_BY_QUERY)

        if not registers:
            return []

        return [
            LocationDistance(
                id=register[0],
                duration=register[3]/SECONDS_IN_MINUTE
            )
            for register in registers
        ]

    def get_locations_that_reach_address_within_time_range(
        self,
        coordinates: Tuple,
        time_limit_minutes: int,
        time_min: Optional[int] = 0
    ) -> List[LocationDistance]:
        time_limit_seconds = time_limit_minutes * SECONDS_IN_MINUTE
        time_min_seconds = time_min * SECONDS_IN_MINUTE

        SELECT_BY_QUERY = f"""
            SELECT id, MIN(interval)
            FROM locations_isochrones
            JOIN locations ON (locations.id = locations_isochrones.location_id)
            WHERE 
                ST_Contains(
                    locations_isochrones.isochrone, 
                    ST_SetSRID(ST_MakePoint({coordinates[0]},{coordinates[1]}),
                    4326)
                )
                AND interval between {time_min_seconds} and {time_limit_seconds}
            GROUP BY id
        """
        
        number_of_registers, registers = self.database_config.get_registers(SELECT_BY_QUERY)

        if not registers:
            return []

        return [
            LocationDistance(
                id=register[0],
                duration=register[3]/SECONDS_IN_MINUTE
            )
            for register in registers
        ]