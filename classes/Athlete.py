class Athlete:
    id_counter: int = 0

    def __init__(self, gender):
        Athlete.id_counter += 1
        self.id: int = Athlete.id_counter
        self.gender: str = gender

    def __init__(self, name, gender, city):
        Athlete.id_counter += 1
        self.id: int = Athlete.id_counter
        self.name: str = name
        self.gender: str = gender
        self.city: str = city

    def __init__(self, name: str, gender: str, age="", city="", state="", country=""):
        Athlete.id_counter += 1
        self.id: int = Athlete.id_counter
        self.name: str = name
        self.gender: str = gender
        self.age: str = age
        self.city: str = city
        self.state: str = state
        self.country: str = country
