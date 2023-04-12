from typing import Any, Optional, Tuple
from pydantic.dataclasses import dataclass

@dataclass
class Location:
    id: int
    address: str
    zip: str
    state: str
    city: str
    coordinates: Optional[Tuple] = None

    def __init__(
        self,
        id: int,
        address: str,
        zip: str,
        state: str,
        city: str,
        coordinates: Optional[Tuple] = None
    ):
        self.id = id
        self.address = address
        self.zip = zip
        self.state = state
        self.city = city
        self.coordinates = coordinates
