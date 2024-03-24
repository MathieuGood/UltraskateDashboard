import time
from classes.Webscraper import Webscraper
from classes.Utils import Utils
from classes.Performance import Performance
from classes.Athlete import Athlete
from classes.Track import Track
from classes.Event import Event


events_url = {
        "2013-01-07": "https://jms.racetecresults.com/results.aspx?CId=16370&RId=13",
        # 2013 OK
        "2014-01-20": "https://jms.racetecresults.com/results.aspx?CId=16370&RId=67",
        # 2014 OK
        # Country available
        "2015-02-12": "https://jms.racetecresults.com/results.aspx?CId=16370&RId=121",
        # 2015 OK
        "2016-02-26": "https://jms.racetecresults.com/results.aspx?CId=16370&RId=179",
        # 2016 OK
        "2017-01-16": "https://jms.racetecresults.com/results.aspx?CId=16370&RId=240",
        # 2017 OK
        "2018-01-10": "https://jms.racetecresults.com/results.aspx?CId=16370&RId=294",
        # 2018 OK
        "2019-01-18": "https://jms.racetecresults.com/results.aspx?CId=16370&RId=352",
        # 2019 OK
        "2020-01-17": "https://jms.racetecresults.com/results.aspx?CId=16370&RId=400",
        # 2020 OK
        "2021-01-29": "https://jms.racetecresults.com/results.aspx?CId=16370&RId=413",
        # 2021 NOT OK

        "2022-02-19": "https://my.raceresult.com/192607",
        "2023-02-10": "https://my.raceresult.com/204047",
        "2024-02-15": "https://my.raceresult.com/259072",
    }


# Iterate over events_url to print all the content of each entry

for years in events_url:
    print(years)
    print(events_url[years])

start_time = time.time()


# Iterate over events_url dictionary (only Miami for now), and print the url value associated with each key
# for year, url in events_url["Miami"].items():
#     Webscraper().fetch_all_athletes_url(events_url["Miami"][2013])


event = Webscraper.fetch_all_athletes_performances(events_url["2020-01-17"])
for athlete in event:
    print(athlete)

# End timer
end_time = time.time()
print(f"Time elapsed: {end_time - start_time} seconds")
