import time

from classes.AthleteRegistry import AthleteRegistry
from classes.Event import Event
from classes.EventAthleteStats import EventAthleteStats
from classes.EventManager import EventManager
from classes.EventRegistry import EventRegistry
from classes.Utils import Utils
from classes.Webscraper import Webscraper
from properties import Properties

events_url = {
    "2013-01-07": "https://jms.racetecresults.com/results.aspx?CId=16370&RId=13",
    "2014-01-20": "https://jms.racetecresults.com/results.aspx?CId=16370&RId=67",  # 2014 Country available
    "2015-02-12": "https://jms.racetecresults.com/results.aspx?CId=16370&RId=121",
    "2016-02-26": "https://jms.racetecresults.com/results.aspx?CId=16370&RId=179",
    "2017-01-16": "https://jms.racetecresults.com/results.aspx?CId=16370&RId=240",
    "2018-01-10": "https://jms.racetecresults.com/results.aspx?CId=16370&RId=294",
    "2019-01-18": "https://jms.racetecresults.com/results.aspx?CId=16370&RId=352",
    "2020-01-17": "https://jms.racetecresults.com/results.aspx?CId=16370&RId=400",
    "2021-01-29": "https://jms.racetecresults.com/results.aspx?CId=16370&RId=413",
    # "2022-02-19": "https://my.raceresult.com/192607",
    # "2023-02-10": "https://my.raceresult.com/204047",
    # "2024-02-15": "https://my.raceresult.com/259072",
}

events_fields_indexes = {
    events_url["2013-01-07"]:
        {"name": 1, "gender": 1, "age": 3, "category": 4, "age_category": 5, "city": 7, "state": 9, },
    events_url["2014-01-20"]:
        {"name": 1, "gender": 1, "age": 3, "category": 4, "age_category": 5, "city": 7, "state": 9, },
    events_url["2015-02-12"]:
        {"name": 1, "gender": 1, "age": 3, "category": 4, "age_category": 5, "city": 7, "state": 9, },
    events_url["2016-02-26"]:
        {"name": 1, "gender": 1, "age": 3, "category": 4, "age_category": 5, "city": 7, "state": 9, },
    events_url["2017-01-16"]:
        {"name": 1, "gender": 1, "age": 3, "category": 4, "age_category": 5, "city": 7, "state": 9, },
    events_url["2018-01-10"]:
        {"name": 1, "gender": 1, "age": 3, "category": 4, "age_category": 5, "city": 7, "state": 9, },
    events_url["2019-01-18"]:
        {"name": 1, "gender": 1, "age": 3, "category": 4, "age_category": 5, "city": 7, "state": 9, },
    events_url["2020-01-17"]:
        {"name": 1, "gender": 1, "age": 3, "category": 4, "age_category": 5, "city": 7, "state": 9, },
    events_url["2021-01-29"]:
        {"name": 1, "gender": 1, "age": 3, "category": 4, "age_category": 5, "city": 7, "state": 9, },
}


def scrape_one_event(event_url: str):
    event_performances = Webscraper.fetch_all_athletes_performances(event_url)
    for athlete in event_performances:
        print(athlete)


def scrape_events(urls: dict[str, str]):
    scraped_events = Webscraper.fetch_all_events_performances(urls)
    print(scraped_events)
    Utils.write_to_json(scraped_events, "data/events.json")


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

    athlete_stats = EventAthleteStats(performance)
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


def one_skater_info_per_event(events: dict[int, Event]):
    for event in events.values():
        print(event.date, AthleteRegistry.get_athlete(event.performances[0].athlete_id))


def main():
    scrape_events(events_url)
    # events = parse_events()
    # manipulate_event(events)
    # one_skater_info_per_event(events)


if __name__ == "__main__":
    start_time = time.time()
    main()
    end_time = time.time()
    print(f"\n\nTime elapsed: {end_time - start_time} seconds")
