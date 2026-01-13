from __future__ import annotations
from typing import TYPE_CHECKING

from models.athlete import Athlete
from models.lap_stats import LapStats
from utils import Utils

if TYPE_CHECKING:
    from models.event import Event


class Performance:
    """Class representing an athlete's performance in an event."""

    def __init__(
        self,
        athlete: Athlete,
        laps: list[LapStats],
        event: Event,
        discipline: str = "",
        age_category: str = "",
    ):
        self.athlete = athlete
        self.laps = laps
        self.discipline = discipline
        self.age_category = age_category
        self.event = event
        self.total_time_ss = self.__get_total_time_ss()

    def get_total_time_hhmmss(self) -> str:
        return Utils.seconds_to_hhmmss(self.total_time_ss)

    def __get_total_time_ss(self) -> int:
        return sum(lap.lap_time_ss for lap in self.laps)

    def get_total_laps(self) -> int:
        return len(self.laps)

    def get_total_miles(self) -> float:
        return self.event.track.length_miles * self.get_total_laps()

    def get_total_km(self) -> float:
        return self.get_total_miles() * 1.60934

    def to_dict(self) -> dict:
        return {
            "athlete": {
                "name": self.athlete.name,
                "gender": self.athlete.gender,
                "city": self.athlete.city,
                "state": self.athlete.state,
                "country": self.athlete.country,
            },
            "category": self.discipline,
            "age_group": self.age_category,
            "total_time_hhmmss": self.get_total_time_hhmmss(),
            "total_laps": self.get_total_laps(),
            "total_miles": self.get_total_miles(),
            "total_km": self.get_total_km(),
            "laps": [
                {"number": lap.lap_number, "time": lap.get_lap_time_hhmmss()}
                for lap in self.laps
            ],
        }

    def __str__(self) -> str:
        return f"Performance by {self.athlete}\n -> {len(self.laps)} laps \n -> Total time : {self.get_total_time_hhmmss()}\n -> {len(self.laps) * 1.46} miles\n -> {self.event.date.year} {self.event.track.name} at {self.event.track.city}, {self.event.track.country}"
