from classes.Event import Event


class EventRegistry:

    events = {}

    @classmethod
    def add_event(cls, event: Event) -> None:
        cls.events[event.id] = event

    @classmethod
    def remove_event(cls, event: Event) -> None:
        cls.events.remove(event)

    @classmethod
    def get_all_events(cls) -> dict[str, Event]:
        return cls.events
