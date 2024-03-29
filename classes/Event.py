class Event:

    id_counter = 0

    def __init__(self):
        Event.id_counter += 1
        self.id  = Event.id_counter
        self.date = None
        self.track = None
        self.performances = []
        

    def __init__(self, date, track):
        Event.id_counter += 1
        self.id  = Event.id_counter
        self.date = date
        self.track = track
        self.performances = []
        

    def add_performance(self, performance):
        self.performances.append(performance)
