import os
from file_manager import FileManager
from webscraper.event_scraper import EventScraper
from webscraper.browser_manager import BrowserManager
from event_params_data import miami_event_params
from models.event import Event
from models.event_registry import EventRegistry
from event_stats import EventStats


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
    # scrape_events()

    for file in FileManager.get_all_json_in_dir("scraped_events_save"):
        event = Event.from_json_file(file)
        EventRegistry.add_event(event)

    for event in EventRegistry.events:
        if event.date.year == 2023:
            print("\n", event.track.city, event.date.year)

            # Print all the unique sports in this event
            unique_sports = set()
            for performance in event.performances:
                unique_sports.add(performance.sport)
            print("Unique sports in this event:")
            for sport in sorted(unique_sports):
                print("-", sport)

            # event_stats = EventStats(event)
            # event_stats.print_all(
            #     event_stats.top(3, event_stats.by_sport("skateboard"))
            # )

            event_stats2 = EventStats(event)
            event_stats2.print_all(event_stats2.top(100))

            # Output to CSV
            # with open("event_stats_" + str(event.date.year) + ".csv", "w") as f:
            #     f.write(
            #         "Name,Sport,Discipline,Age Category,Total Miles,Total Laps,Average Speed (kph),Total Time (HH:MM:SS)\n"
            #     )
            #     for performance in event_stats2.top(100):
            #         f.write(
            #             f"{performance.athlete.name},{performance.sport},{performance.discipline},{performance.age_category},{performance.get_total_miles():.2f},{performance.get_total_laps()},{performance.get_average_speed_kph():.2f},{performance.get_total_time_hhmmss()}\n"
            #         )


if __name__ == "__main__":
    main()
