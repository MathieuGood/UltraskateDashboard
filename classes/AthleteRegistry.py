from classes.Athlete import Athlete


class AthleteRegistry:

    athletes = {}

    @classmethod
    def add_athlete(cls, athlete: Athlete) -> None:
        cls.athletes[athlete.id] = athlete

    @classmethod
    def remove_athlete(cls, athlete: Athlete) -> None:
        cls.athletes.remove(athlete)

    @classmethod
    def get_all_athletes(cls) -> dict[int, Athlete]:
        return cls.athletes

    @classmethod
    def get_athlete(cls, athlete_id: int) -> Athlete:
        return cls.athletes[athlete_id]
