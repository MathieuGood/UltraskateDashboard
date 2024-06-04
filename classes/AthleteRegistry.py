class AthleteRegistry:

    athletes = {}

    @classmethod
    def add_athlete(cls, athlete):
        cls.athletes[athlete.id] = athlete

    @classmethod
    def remove_athlete(cls, athlete):
        cls.athletes.remove(athlete)

    @classmethod
    def get_all_athletes(cls):
        return cls.athletes
