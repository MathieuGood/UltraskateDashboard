from models.athlete import Athlete


class AthleteRegistry:
    def __init__(self) -> None:
        self.athletes: list[Athlete] = []
    
    def add_athlete(self, athlete : Athlete):
        # Check if athlete already exists
        # Check name (fuzzy match) + age
        #   If it does not exist, add it to list
        #   If it already exists, do not add them
        self.athletes.append(athlete)

        
