class EventRegistry:

    events = {}

    @classmethod
    def add_event(cls, event):
        cls.events[event.id] = event

    @classmethod
    def remove_event(cls, athlete):
        cls.events.remove(athlete)

    @classmethod
    def get_all_events(cls):
        return cls.events
