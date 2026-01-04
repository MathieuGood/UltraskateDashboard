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
        self.total_time_ss = sum(laps)

    def __str__(self) -> str:
        return f"Performance by {self.athlete} : {len(self.laps)} laps - Total time : {self.total_time_ss / 60 :.2f} minutes"
