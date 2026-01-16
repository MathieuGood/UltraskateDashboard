from __future__ import annotations

import json
from datetime import datetime
from typing import TYPE_CHECKING

from models.track import Track
from models.event_params import EventParams

if TYPE_CHECKING:
    from models.performance import Performance


class Event:
    """
    Class representing an event
    """

    def __init__(
        self,
        event_params: EventParams | None = None,
        date: datetime | None = None,
        track: Track | None = None,
    ) -> None:
        """
        Initialize an Event instance.

        :param date: The date of the event in 'YYYY-MM-DD' format.
        :type date: str
        :param track: The track where the event takes place.
        :type track: Track
        :param url: URL of the rankings page
        :type url : str
        """
        self.performances: list[Performance] = []

        if event_params is not None:
            self.date: datetime = event_params.date if event_params else date
            self.track: Track = event_params.track if event_params else track

    def add_performance(self, performance: Performance) -> None:
        """
        Add an athlete's performance to the event.

        :param performance: The performance to add.
        :type performance: Performance
        """
        self.performances.append(performance)

    def to_dict(self) -> dict:
        performances_list: list[dict] = []
        for performance in self.performances:
            performances_list.append(performance.to_dict())
        return {
            "date": self.date.isoformat(),
            "track": self.track.name,
            "city": self.track.city,
            "country": self.track.country,
            "performances": performances_list,
        }

    def to_json_file(self, file_name: str) -> None:
        with open(file_name, "w") as f:
            json.dump(self.to_dict(), f, indent=4)

    @classmethod
    def from_json_file(cls, file_name: str) -> Event:
        with open(file_name, "r") as f:
            data = json.load(f)
            print(data)

        track = Track(
            name=data["track"],
            city=data["city"],
            country=data["country"],
            length_miles=0.0,  # Length is not stored in JSON; set to 0.0 or handle accordingly
        )

        event = cls(
            event_params=None, date=datetime.fromisoformat(data["date"]), track=track
        )
        print(event)

        return event
