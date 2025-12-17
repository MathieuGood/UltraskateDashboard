from typing import List

from src.models.Track import Track
from src.models.Performance import Performance


class Event:
    id_counter = 0

    def __init__(self, date: str | None = None, track: Track | None = None):
        Event.id_counter += 1
        self.id: int = Event.id_counter
        self.date: str | None = date
        self.track: Track | None = track
        self.performances: List[Performance] = []

    def add_performance(self, performance: Performance) -> None:
        self.performances.append(performance)
