from models.athlete import Athlete


class Performance:
    """Class representing an athlete's performance in an event."""

    def __init__(
        self,
        athlete: Athlete,
        laps: list[int],
    ):
        self.athlete = athlete
        self.laps = laps
