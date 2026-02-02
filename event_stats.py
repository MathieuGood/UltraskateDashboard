from models.event import Event
from models.performance import Performance


class EventStats:
    def __init__(self, event: Event) -> None:
        self.event: Event = event
        self.__sort_performances_total_miles()
        # print(event.date)
        # print(event)

    def __sort_performances_total_miles(self):
        self.event.performances.sort(
            key=lambda performance: performance.get_total_miles(), reverse=True
        )

    def get_top3(self) -> list[Performance] | None:
        if len(self.event.performances) < 3:
            return None
        top3: list[Performance] = []
        for index in range(3):
            top3.append(self.event.performances[index])
        return top3
