from models.athlete import Athlete
from models.lap_stats import LapStats
from models.event import Event
from utils import Utils


class Performance:
    """Class representing an athlete's performance in an event."""

    def __init__(
        self,
        athlete: Athlete,
        laps: list[LapStats],
        event: Event,
    ):
        self.athlete = athlete
        self.laps = laps
        self.event = event
        self.total_time_ss = self.__get_total_time_ss()

    def get_total_time_hhmmss(self) -> str:
        return Utils.seconds_to_hhmmss(self.total_time_ss)

    def __get_total_time_ss(self) -> int:
        return sum(lap.lap_time_ss for lap in self.laps)

    def __str__(self) -> str:
        return f"Performance by {self.athlete}\n -> {len(self.laps)} laps \n -> Total time : {self.get_total_time_hhmmss()}\n -> {len(self.laps)*1.46} miles\n -> {self.event.date.year} {self.event.track.name} at {self.event.track.city}, {self.event.track.country}"
