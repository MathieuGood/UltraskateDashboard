from enum import Enum


class TrackOption(Enum):
    MIAMI = {"name": "Homestead Speedway", "location": "Homestead", "length": 1.46}
    SPAARNDAM = {"name": "Wheelerplanet", "location": "Spaarndam", "length": 2.0}


class Track:
    def __init__(self, track_option):
        self.name = track_option.value["name"]
        self.location = track_option.value["location"]
        self.length = track_option.value["length"]
