import time

from data.events_urls import events_url
from src.models.Event import Event
from src.registries.AthleteRegistry import AthleteRegistry
from src.registries.EventRegistry import EventRegistry
from src.use_cases.AthleteStatsProcessor import AthleteStatsProcessor
from src.use_cases.EventManager import EventManager
from src.use_cases.FuzzyWuzzyMatcher import FuzzyWuzzyMatcher
from src.utils.JsonUtils import JsonUtils
from src.webscraping.Webscraper import Webscraper


def scrape_one_event(event_url: str):
    event_performances = Webscraper.fetch_all_athletes_performances(event_url)
    for athlete in event_performances:
        print(athlete)


def scrape_events(urls: dict[str, str]):
    scraped_events = Webscraper.fetch_all_events_performances(urls)
    print(scraped_events)
    JsonUtils.write_to_json(scraped_events, "data/events.json")


def parse_events() -> dict[int, Event]:
    EventManager.parse_json_events("data/events.json")
    events = EventRegistry.get_all_events()
    for event in events.values():
        print(f"{event.date} {event.track.name}, {event.track.location}")
    print(f"Total events: {len(events)}")
    return events


def manipulate_event(events: dict[int, Event]):
    ultra2020 = events[8]
    performance = ultra2020.performances[0]
    print(performance)

    athlete_stats = AthleteStatsProcessor(performance)
    print(f"Total time : {athlete_stats.get_total_time()}")
    print(f"Lap count : {athlete_stats.get_lap_count()}")
    print(f"Total mileage : {athlete_stats.get_total_mileage()} miles")

    # total_time = timedelta(seconds=sum(performance.laps.values()))
    # lap_count = len(performance.laps)
    # track_length = ultra2020.track.length
    # print(track_length)
    # total_distance = lap_count * track_length
    # print(f"Total distance: {total_distance} miles")
    # print(total_time)


def one_skater_info_in_each_event(events: dict[int, Event]):
    for event in events.values():
        print("")
        print(event.performances[0])
        print(event.date, AthleteRegistry.get_athlete(event.performances[0].athlete_id))
        print(f"Athlete age : {event.performances[0].athlete_age}")


def fuzzy_test():
    s1 = "Andrew Andras"
    s2 = "Andy Andras"
    fuzz = FuzzyWuzzyMatcher.match(s1, s2)
    print(f"Fuzzy Matching ratio test between '{s1}' and '{s2}' -> {fuzz}")


def main():
    scrape_events(events_url)
    events = parse_events()
    # manipulate_event(events)
    one_skater_info_in_each_event(events)

    fuzzy_test()


if __name__ == "__main__":
    start_time = time.time()
    main()
    end_time = time.time()
    print(f"\n\nTime elapsed: {end_time - start_time} seconds")
