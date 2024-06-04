from enum import Enum
from typing import Dict, Union


class TrackOption(Enum):
    MIAMI: Dict[str, Union[str, float]] = {"name": "Homestead Speedway", "location": "Homestead", "length": 1.46}
    SPAARNDAM: Dict[str, Union[str, float]] = {"name": "Wheelerplanet", "location": "Spaarndam", "length": 2.0}


class Track:
    def __init__(self, track_option: TrackOption):
        self.name: str = track_option.value["name"]
        self.location: str = track_option.value["location"]
        self.length: float = track_option.value["length"]
