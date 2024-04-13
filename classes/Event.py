class Event:

    id_counter = 0

    def __init__(self, date=None, track=None):
        Event.id_counter += 1
        self.id  = Event.id_counter
        self.date = date
        self.track = track
        self.performances = []
        

    def add_performance(self, performance):
        self.performances.append(performance)
