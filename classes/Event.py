from typing import List
from classes.Track import Track
from classes.Performance import Performance


class Event:
    id_counter = 0

    def __init__(self, date: str = None, track: Track = None):
        Event.id_counter += 1
        self.id: int = Event.id_counter
        self.date: str = date
        self.track: Track = track
        self.performances: List[Performance] = []

    def add_performance(self, performance: Performance) -> None:
        self.performances.append(performance)
