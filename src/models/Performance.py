from src.models.Athlete import Athlete
from src.registries.AthleteRegistry import AthleteRegistry


class Performance:

    def __init__(
        self,
        athlete_id: int,
        laps: dict[int, int],
        athlete_age: int | None = None,
        category: str | None = None,
    ):
        self.athlete_id = athlete_id
        self.athlete_age = athlete_age
        self.category = category
        self.laps = laps

    def __str__(self):
        return (
            f"Performance(Athlete ID: {self.athlete_id},"
            f" Age: {self.athlete_age},"
            f" Category: {self.category},"
            f" Laps: {self.laps.values().__len__()})"
        )

    def get_athlete(self) -> Athlete:
        return AthleteRegistry.athletes[self.athlete_id]
