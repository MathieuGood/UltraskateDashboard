class Athlete:

    id_counter = 0

    def __init__(self, name, gender, age="", city="", state="", country=""):

        Athlete.id_counter += 1
        self.id = Athlete.id_counter
        self.name = name
        self.gender = gender
        self.age = age
        self.city = city
        self.state = state
        self.country = country

    def __init__(self, gender):
        Athlete.id_counter += 1
        self.id = Athlete.id_counter
        self.gender = gender


