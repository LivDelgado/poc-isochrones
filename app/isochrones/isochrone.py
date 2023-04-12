from typing import List, Optional, Tuple
from pydantic.dataclasses import dataclass

@dataclass
class Isochrone:
    value: int
    center: Tuple[float, float]
    coordinates: List[Tuple[float, float]]

    def __init__(
        self,
        value: int,
        center: Tuple[float, float],
        coordinates: List[Tuple[float, float]]
    ):
        self.value = value
        self.center = center
        self.coordinates = coordinates