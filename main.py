import os
from webscraper.event_scraper import EventScraper
from webscraper.browser_manager import BrowserManager
from event_params_data import miami_event_params
from models.event import Event
from models.event_registry import EventRegistry


def scrape_events():

    BrowserManager.start()

    try:
        events = [
            # EventScraper.scrape(miami_event_params[2013]),
            # EventScraper.scrape(miami_event_params[2014]),
            # EventScraper.scrape(miami_event_params[2015]),
            # EventScraper.scrape(miami_event_params[2016]),
            # EventScraper.scrape(miami_event_params[2017]),
            # EventScraper.scrape(miami_event_params[2018]),
            # EventScraper.scrape(miami_event_params[2019]),
            # EventScraper.scrape(miami_event_params[2020]),
            # EventScraper.scrape(miami_event_params[2021]),
            # EventScraper.scrape(miami_event_params[2022]),
            # EventScraper.scrape(miami_event_params[2023]),
            # EventScraper.scrape(miami_event_params[2024]),
            # EventScraper.scrape(miami_event_params[2025]),
        ]
    finally:
        BrowserManager.shutdown()

    for event in events:
        if event is None or len(event.performances) == 0:
            continue

        event.to_json_file(
            os.path.join("ultraskate_miami_" + str(event.date.year) + ".json")
        )


def main():
    print("Hello from ultraskatedashboard!")

    # scrape_events()

    # Get all the filenames in the scraped_events_save directory
    scraped_events_dir = "scraped_events_save"
    files = os.listdir(scraped_events_dir)

    print(files)

    for file in files:
        if file.endswith(".json"):
            event = Event.from_json_file(os.path.join(scraped_events_dir, file))
            EventRegistry.add_event(event)

    for event in EventRegistry.events:
        # if event is None or len(event.performances) == 0:
        #     continue
        print(event)
        # print(event.performances[0].get_average_speed_kph_at_lap(100))


if __name__ == "__main__":
    main()
