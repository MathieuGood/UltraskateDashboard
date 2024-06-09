import time

from classes.EventAthleteStats import EventAthleteStats
from classes.EventManager import EventManager
from classes.EventRegistry import EventRegistry
from classes.Utils import Utils
from classes.Webscraper import Webscraper

events_url = {
    "2013-01-07": "https://jms.racetecresults.com/results.aspx?CId=16370&RId=13",
    "2014-01-20": "https://jms.racetecresults.com/results.aspx?CId=16370&RId=67",
    # 2014 Country available
    "2015-02-12": "https://jms.racetecresults.com/results.aspx?CId=16370&RId=121",
    "2016-02-26": "https://jms.racetecresults.com/results.aspx?CId=16370&RId=179",
    "2017-01-16": "https://jms.racetecresults.com/results.aspx?CId=16370&RId=240",
    "2018-01-10": "https://jms.racetecresults.com/results.aspx?CId=16370&RId=294",
    "2019-01-18": "https://jms.racetecresults.com/results.aspx?CId=16370&RId=352",
    "2020-01-17": "https://jms.racetecresults.com/results.aspx?CId=16370&RId=400",
    # "2021-01-29": "https://jms.racetecresults.com/results.aspx?CId=16370&RId=413",
    # # 2021 NOT OK
    # "2022-02-19": "https://my.raceresult.com/192607",
    # "2023-02-10": "https://my.raceresult.com/204047",
    # "2024-02-15": "https://my.raceresult.com/259072",
}

start_time = time.time()

# one_event = Webscraper.fetch_all_athletes_performances(events_url["2020-01-17"])
# for athlete in one_event:
#     print(athlete)


scraped_events = Webscraper.fetch_all_events_performances(events_url)
print(scraped_events)

# # Write all the data in events to a JSON file
# Utils.write_to_json(scraped_events, "events.json")

EventManager.parse_json_events("events.json")

events = EventRegistry.get_all_events()

for event in events.values():
    # print(event.name, event.date, event.track["name"], event.track["location"])
    print(f"{event.date} {event.track.name}, {event.track.location}")

ultra2020 = events[8]
performance = ultra2020.performances[0]
print(performance)

athlete_stats = EventAthleteStats(performance)
print(f"Total time : {athlete_stats.get_total_time()}")
print(f"Lap count : {athlete_stats.get_lap_count()}")
print(f"Total mileage : {athlete_stats.get_total_mileage()} miles")

# Get first items of ultra2020 dictionary

# total_time = timedelta(seconds=sum(performance.laps.values()))
# lap_count = len(performance.laps)
# track_length = ultra2020.track.length
# print(track_length)
# total_distance = lap_count * track_length
# print(f"Total distance: {total_distance} miles")
# print(total_time)

# End timer
end_time = time.time()
print(f"\n\nTime elapsed: {end_time - start_time} seconds")
