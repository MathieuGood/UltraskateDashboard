class Athlete:

    def __init__(self, name, gender, city="", state="", country=""):
        self.name = name
        self.gender = gender
        self.city = city
        self.state = state
        self.country = country

    def __str__(self) -> str:
        return f"Athlete(name={self.name}, gender={self.gender}, city={self.city}, state={self.state}, country={self.country})"
