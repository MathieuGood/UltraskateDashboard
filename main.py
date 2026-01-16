from os import path
from webscraper.event_scraper import EventScraper
from webscraper.browser_manager import BrowserManager
from event_params_data import miami_event_params
from models.event import Event


def main():
    print("Hello from ultraskatedashboard!")

    # BrowserManager.start()

    # try:
    #     # miami2013 = EventScraper.scrape(miami_event_params[2013])
    #     # miami2014 = EventScraper.scrape(miami_event_params[2014])
    #     # miami2015 = EventScraper.scrape(miami_event_params[2015])
    #     # miami2016 = EventScraper.scrape(miami_event_params[2016])
    #     # miami2017 = EventScraper.scrape(miami_event_params[2017])
    #     # miami2018 = EventScraper.scrape(miami_event_params[2018])
    #     # miami2019 = EventScraper.scrape(miami_event_params[2019])
    #     # miami2020 = EventScraper.scrape(miami_event_params[2020])
    #     # miami2021 = EventScraper.scrape(miami_event_params[2021])
    #     # miami2022 = EventScraper.scrape(miami_event_params[2022])
    #     # miami2023 = EventScraper.scrape(miami_event_params[2023])
    #     # miami2024 = EventScraper.scrape(miami_event_params[2024])
    #     # miami2025 = EventScraper.scrape(miami_event_params[2025])
    # finally:
    #     BrowserManager.shutdown()

    events = [
        # miami2013,
        # miami2014,
        # miami2015,
        # miami2016,
        # miami2017,
        # miami2018,
        # miami2019,
        # miami2020,
        # miami2021,
        # miami2022,
        # miami2023,
        # miami2024,
        # miami2025,
    ]

    events = [
        Event.from_json_file("scraped_events_save/ultraskate_miami_2013.json"),
    ]

    for event in events:
        if event is None or len(event.performances) == 0:
            continue
        print("-----")
        print(
            f"Event on {event.date} at {event.track.name}, {event.track.city}, {event.track.country}"
        )
        print(event.performances[0])
        print(event.performances[1])
        print(event.performances[2])
        print(f"Total performances scraped: {len(event.performances)}")
        print("-----\n")
        print("-----\n\n\n\n\n\n")

        # Save event to JSON file
        # event.to_json_file(
        #     path.join("ultraskate_miami_" + str(event.date.year) + ".json")
        # )


if __name__ == "__main__":
    main()
