import time
from classes.Webscraper import Webscraper

events_url = {
    "Miami": {
        2013: "https://jms.racetecresults.com/results.aspx?CId=16370&RId=13",
        2014: "https://jms.racetecresults.com/results.aspx?CId=16370&RId=67",
        2015: "https://jms.racetecresults.com/results.aspx?CId=16370&RId=121",
        2016: "https://jms.racetecresults.com/results.aspx?CId=16370&RId=179",
        2017: "https://jms.racetecresults.com/results.aspx?CId=16370&RId=240",
        2019: "https://jms.racetecresults.com/results.aspx?CId=16370&RId=352",
        2020: "https://jms.racetecresults.com/results.aspx?CId=16370&RId=400",
        2022: "https://my.raceresult.com/192607",
        2023: "https://my.raceresult.com/204047",
        2024: "https://my.raceresult.com/259072",
    }
}


start_time = time.time()


# Iterate over events_url dictionary (only Miami for now), and print the url value associated with each key
# for year, url in events_url["Miami"].items():
#     Webscraper().fetch_all_skaters_url(events_url["Miami"][2013])


ultra = Webscraper.fetch_skater_stats(
    "https://jms.racetecresults.com/myresults.aspx?uid=16370-13-1-6114"
)

print(ultra.laps)

print(ultra)


# End timer
end_time = time.time()
print(f"Time elapsed: {end_time - start_time} seconds")
