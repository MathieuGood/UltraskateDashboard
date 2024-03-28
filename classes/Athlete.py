class Athlete:

    id_counter = 0

    def __init__(self, gender):
        Athlete.id_counter += 1
        self.id = Athlete.id_counter
        self.gender = gender

    def __init__(self, name, gender, city):
        Athlete.id_counter += 1
        self.id = Athlete.id_counter
        self.name = name
        self.gender = gender
        self.city = city

    def __init__(self, name, gender, age="", city="", state="", country=""):
        Athlete.id_counter += 1
        self.id = Athlete.id_counter
        self.name = name
        self.gender = gender
        self.age = age
        self.city = city
        self.state = state
        self.country = country

    @classmethod
    def get_Athlete_by_id(self, id):
        if self.id == id:
            return self
