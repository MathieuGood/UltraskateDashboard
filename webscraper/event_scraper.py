from models.event import Event
from models.event_params import EventParams
from webscraper.webscraper import Webscraper


class EventScraper:

    @classmethod
    def scrape(cls, event_params: EventParams) -> Event:
        rankings_page = Webscraper.fetch_html(event_params.url)
        return Event(event_params)

    @classmethod
    def __scrape_event_ranking_page(cls, event_params : EventParams):
        ranking_page = Webscraper.fetch_html(event_params.url)
        pass

    