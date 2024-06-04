from classes.AthleteRegistry import AthleteRegistry


class Performance:

    def __init__(self, athlete_id, laps):
        self.athlete_id = athlete_id
        self.laps = laps

    def get_athlete(self):
        return AthleteRegistry.athletes[self.athlete_id]
