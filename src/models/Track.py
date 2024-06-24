from src.models.TrackOption import TrackOption


class Track:
    def __init__(self, track_option: TrackOption):
        self.name: str = track_option.value["name"]
        self.location: str = track_option.value["location"]
        self.length: float = track_option.value["length"]
