from typing import List, Optional, Tuple
from pydantic.dataclasses import dataclass

@dataclass
class LocationDistance:
    id: int
    duration: int

    def __init__(
        self,
        id: int,
        duration: int
    ):
        self.id = id
        self.duration = duration