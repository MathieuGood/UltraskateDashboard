class Athlete:
    def __init__(
        self,
        name: str,
        gender: str = "",
        city: str = "",
        state: str = "",
        country: str = "",
    ):
        if name == "":
            raise ValueError("Athlete name cannot be empty")
        self.name = name
        self.gender = gender
        self.city = city
        self.state = state
        self.country = country

    def __str__(self) -> str:
        return f"Athlete(name={self.name}, gender={self.gender}, city={self.city}, state={self.state}, country={self.country})"

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Athlete):
            return NotImplemented
        return self.name == other.name

    def __hash__(self) -> int:
        return hash(self.name)
