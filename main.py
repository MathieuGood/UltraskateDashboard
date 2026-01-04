from models.event import Event
from models.event_params import EventParams
from models.track import Track
from webscraper.event_scraper import EventScraper
from webscraper.browser_manager import BrowserManager
from models.athlete_registry import AthleteRegistry

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
    "2021-01-29": "https://jms.racetecresults.com/results.aspx?CId=16370&RId=413",
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
        position_col_index=0,
        name_col_index=2,
    )

    miami2014_params = EventParams(
        date="2014-01-20",
        track=homestead_track,
        url=events_url["2014-01-20"],
        position_col_index=0,
        name_col_index=2,
    )

    miami2015_params = EventParams(
        date="2015-02-12",
        track=homestead_track,
        url=events_url["2015-02-12"],
        position_col_index=0,
        name_col_index=1,
    )

    miami2016_params = EventParams(
        date="2016-02-26",
        track=homestead_track,
        url=events_url["2016-02-26"],
        position_col_index=0,
        name_col_index=2,
    )

    miami2017_params = EventParams(
        date="2017-01-16",
        track=homestead_track,
        url=events_url["2017-01-16"],
        position_col_index=1,
        name_col_index=3,
    )

    miami2018_params = EventParams(
        date="2018-01-10",
        track=homestead_track,
        url=events_url["2018-01-10"],
        position_col_index=1,
        name_col_index=3,
    )

    miami2019_params = EventParams(
        date="2019-01-18",
        track=homestead_track,
        url=events_url["2019-01-18"],
        position_col_index=1,
        name_col_index=3,
    )

    miami2020_params = EventParams(
        date="2020-01-17",
        track=homestead_track,
        url=events_url["2020-01-17"],
        position_col_index=1,
        name_col_index=3,
    )

    miami2021_params = EventParams(
        date="2021-01-29",
        track=homestead_track,
        url=events_url["2021-01-29"],
        position_col_index=1,
        name_col_index=4,
        athlete_link_col_index=2,
    )

    BrowserManager.start()

    try:
        EventScraper.scrape(miami2013_params)
        EventScraper.scrape(miami2014_params)
        EventScraper.scrape(miami2015_params)
        EventScraper.scrape(miami2016_params)
        EventScraper.scrape(miami2017_params)
        EventScraper.scrape(miami2018_params)
        EventScraper.scrape(miami2019_params)
        EventScraper.scrape(miami2020_params)
        EventScraper.scrape(miami2021_params)
    finally:
        BrowserManager.shutdown()

    for athlete in AthleteRegistry.athletes:
        print(athlete)


if __name__ == "__main__":
    main()
