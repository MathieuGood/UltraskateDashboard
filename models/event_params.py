from datetime import datetime
from models.track import Track


class EventParams:
    def __init__(self, date: str, track: Track, url: str):
        """
        Initialize an Event parameters instance.

        :param date: The date of the event in 'YYYY-MM-DD' format.
        :type date: str
        :param track: The track where the event takes place.
        :type track: Track
        :param url: URL of the rankings page
        :type url : str
        """
        self.date: datetime = datetime.strptime(date, "%Y-%m-%d")
        self.track: Track = track
        self.url: str = url
