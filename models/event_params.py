from datetime import datetime
from models.track import Track


class EventParams:
    def __init__(
        self,
        date: str,
        track: Track,
        url: str,
        position_col_index: int,
        name_col_index: int,
        athlete_link_col_index: int = 1,
    ):
        """
        Initializes the parameters for an event.

        Args:
            date (str): The date of the event in ``YYYY-MM-DD`` format.
            track (Track): The track where the event takes place.
            url (str): The URL of the rankings page.
            position_col_index (int): Index of the column in the ranking page containing the athlete's position.
            name_col_index (int): Index of the column in the ranking page containing the athlete's name.
        """
        self.date: datetime = datetime.strptime(date, "%Y-%m-%d")
        self.track: Track = track
        self.url: str = url
        self.position_col_index: int = position_col_index
        self.name_col_index: int = name_col_index
        self.athlete_link_col_index: int = athlete_link_col_index
