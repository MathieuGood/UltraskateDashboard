from enum import Enum
from typing import Dict, Union


class TrackOption(Enum):
    MIAMI: Dict[str, Union[str, float]] = {
        "name": "Homestead Speedway",
        "location": "Homestead",
        "length": 1.46,
    }
    SPAARNDAM: Dict[str, Union[str, float]] = {
        "name": "Wheelerplanet",
        "location": "Spaarndam",
        "length": 2.0,
    }
