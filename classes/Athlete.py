class Athlete:

    def __init__(
        self, name, gender, performances, age="", city="", state="", country=""
    ):
        self.name = name
        self.gender = gender
        self.performances = [performances]
        self.age = age
        self.city = city
        self.state = state
        self.country = country

    def add_performance(self, performance):
        self.performances.append(performance)
