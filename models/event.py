from datetime import datetime
from models.track import Track
from models.event_params import EventParams


class Event:
    """
    Class representing an event
    """

    def __init__(self, event_params: EventParams) -> None:
        """
        Initialize an Event instance.

        :param date: The date of the event in 'YYYY-MM-DD' format.
        :type date: str
        :param track: The track where the event takes place.
        :type track: Track
        :param url: URL of the rankings page
        :type url : str
        """
        self.date: datetime = event_params.date
        self.track: Track = event_params.track
        self.performances = []

    def add_performance(self, performance) -> None:
        """
        Add an athlete's performance to the event.

        :param performance: The performance to add.
        :type performance: Performance
        """
        self.performances.append(performance)
