from datetime import timedelta

from classes.Performance import Performance
from classes.Track import TrackOption


class EventAthleteStats:

    def __init__(self, performance: Performance):
        self.performance = performance
        self.laps = performance.laps

    def get_total_time(self) -> timedelta:
        return timedelta(seconds=sum(self.laps.values()))

    def get_lap_count(self) -> int:
        return len(self.laps)

    def get_total_mileage(self) -> float:
        track_length: float = TrackOption.MIAMI.value['length']
        print(track_length)
        mileage: float = self.get_lap_count() * track_length
        return mileage
