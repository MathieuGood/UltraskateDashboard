from models.event import Event
from models.event_params import EventParams
from models.track import Track
from webscraper.event_scraper import EventScraper

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


def main():
    print("Hello from ultraskatedashboard!")

    MIAMI = ("Homestead Speedway", "Homestead", 1.46)
    SPAARNDAM = ("Wheelerplanet", "Spaarndam", 2.0)

    homestead_track = Track(
        name="Homestead Speedway", city="Homestead", country="USA", length_miles=1.46
    )

    miami2013_params = EventParams(
        date="2013-01-07",
        track=homestead_track,
        url=events_url["2013-01-07"],
    )

    miami2014_params = EventParams(
        date="2015-02-12", track=homestead_track, url=events_url["2015-02-12"]
    )

    EventScraper.scrape(miami2013_params)
    EventScraper.scrape(miami2014_params)


if __name__ == "__main__":
    main()
