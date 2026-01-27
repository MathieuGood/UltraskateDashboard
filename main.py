from os import path
from webscraper.event_scraper import EventScraper
from webscraper.browser_manager import BrowserManager
from event_params_data import miami_event_params
from models.event import Event


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
            path.join("ultraskate_miami_" + str(event.date.year) + ".json")
        )


def main():
    print("Hello from ultraskatedashboard!")

    # scrape_events()

    events = [
        Event.from_json_file("scraped_events_save/ultraskate_miami_2013.json"),
        Event.from_json_file("scraped_events_save/ultraskate_miami_2014.json"),
        Event.from_json_file("scraped_events_save/ultraskate_miami_2015.json"),
        Event.from_json_file("scraped_events_save/ultraskate_miami_2016.json"),
        Event.from_json_file("scraped_events_save/ultraskate_miami_2017.json"),
        Event.from_json_file("scraped_events_save/ultraskate_miami_2018.json"),
        Event.from_json_file("scraped_events_save/ultraskate_miami_2019.json"),
        Event.from_json_file("scraped_events_save/ultraskate_miami_2020.json"),
        Event.from_json_file("scraped_events_save/ultraskate_miami_2021.json"),
        Event.from_json_file("scraped_events_save/ultraskate_miami_2022.json"),
        Event.from_json_file("scraped_events_save/ultraskate_miami_2023.json"),
        Event.from_json_file("scraped_events_save/ultraskate_miami_2024.json"),
        Event.from_json_file("scraped_events_save/ultraskate_miami_2025.json"),
    ]

    for event in events:
        # if event is None or len(event.performances) == 0:
        #     continue
        print(event.summary())


if __name__ == "__main__":
    main()
