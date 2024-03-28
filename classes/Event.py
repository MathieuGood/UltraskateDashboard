class Event:

    def __init__(self):
        self.date = None
        self.track = None
        self.performances = []

    def __init__(self, date, track):
        self.date = date
        self.track = track
        self.performances = []

    def add_performance(self, performance):
        self.performances.append(performance)
