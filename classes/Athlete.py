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

    def __str__(self):
        green = "\033[32m"
        orange = "\033[38;5;214m"
        reset = "\033[0m"
        separator = "*"
        return (
            f"{orange}Athlete{reset} {separator} "
            f"{green}name:{reset} {self.name} {separator} "
            f"{green}gender:{reset} {self.gender} {separator} "
            f"{green}age:{reset} {self.age} {separator} "
            f"{green}city:{reset} {self.city} {separator} "
            f"{green}state:{reset} {self.state} {separator} "
            f"{green}country:{reset} {self.country}"
        )
