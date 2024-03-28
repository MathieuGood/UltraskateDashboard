import time
from classes.Webscraper import Webscraper
from classes.Utils import Utils
from classes.Performance import Performance
from classes.Athlete import Athlete
from classes.Track import Track
from classes.Event import Event
from classes.EventManager import EventManager
from classes.AthleteRegistry import AthleteRegistry
import json


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

# Iterate over events_url to print all the content of each entry

for years in events_url:
    print(years)
    print(events_url[years])

start_time = time.time()


# event = Webscraper.fetch_all_athletes_performances(events_url["2020-01-17"])
# for athlete in event:
#     print(athlete)


# events = Webscraper.fetch_all_events_performances(events_url)
# print(events)

# # Write all the data in events to a JSON file
# Utils.write_to_json(events, "events.json")

events = EventManager.parse_json_events("events.json")




# EventManager.create_new_event(events_url["2013-01-07"])

# End timer
end_time = time.time()
print(f"Time elapsed: {end_time - start_time} seconds")
