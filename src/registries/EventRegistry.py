from src.models.Event import Event


class EventRegistry:
    events = {}

    @classmethod
    def add_event(cls, event: Event) -> None:
        cls.events[event.id] = event

    @classmethod
    def remove_event(cls, event: Event) -> None:
        cls.events.remove(event)

    @classmethod
    def get_all_events(cls) -> dict[int, Event]:
        return cls.events
