class Track:

    MIAMI = ("Homestead Speedway", "Homestead", 1.46)
    SPAARNDAM = ("Wheelerplanet", "Spaarndam", 2.0)

    def __init__(self, name, location, length):
        self.name = name
        self.location = location
        self.length = length

    @property
    def name(self):
        return self._name

    @property
    def location(self):
        return self._location

    @property
    def length(self):
        return self._length
