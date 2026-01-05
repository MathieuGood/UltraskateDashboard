from models.event_params import EventParams
from models.track import Track
from webscraper.event_scraper import EventScraper
from webscraper.browser_manager import BrowserManager
from models.athlete_registry import AthleteRegistry
from webscraper.jms_site_params import JmsSiteParams
from webscraper.myraceresult_params import MyRaceResultParams

"""

All participants :
https://my4.raceresult.com/192607/RRPublish/data/list?key=9d484a9a9259ff0ae1a4a8570861bc3b&listname=Participants%7CParticipants%20List%20123&page=participants&contest=0&r=all&l=0

Lap details for a given athlete (pid=421 here) :
https://my4.raceresult.com/192607/RRPublish/data/list?key=9d484a9a9259ff0ae1a4a8570861bc3b&listname=Online%7CLap%20Details&page=live&contest=0&r=pid&pid=421
"""

events_url = {
    "2013-01-07": "https://jms.racetecresults.com/results.aspx?CId=16370&RId=13",
    "2014-01-20": "https://jms.racetecresults.com/results.aspx?CId=16370&RId=67",
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
        scraped_site_params=JmsSiteParams(
            ranking_url=events_url["2013-01-07"], position_col_index=0, name_col_index=2
        ),
    )

    miami2014_params = EventParams(
        date="2014-01-20",
        track=homestead_track,
        scraped_site_params=JmsSiteParams(
            ranking_url=events_url["2014-01-20"], position_col_index=0, name_col_index=2
        ),
    )

    miami2015_params = EventParams(
        date="2015-02-12",
        track=homestead_track,
        scraped_site_params=JmsSiteParams(
            ranking_url=events_url["2015-02-12"], position_col_index=0, name_col_index=1
        ),
    )

    miami2016_params = EventParams(
        date="2016-02-26",
        track=homestead_track,
        scraped_site_params=JmsSiteParams(
            ranking_url=events_url["2016-02-26"], position_col_index=0, name_col_index=2
        ),
    )

    miami2017_params = EventParams(
        date="2017-01-16",
        track=homestead_track,
        scraped_site_params=JmsSiteParams(
            ranking_url=events_url["2017-01-16"], position_col_index=1, name_col_index=3
        ),
    )

    miami2018_params = EventParams(
        date="2018-01-10",
        track=homestead_track,
        scraped_site_params=JmsSiteParams(
            ranking_url=events_url["2018-01-10"], position_col_index=1, name_col_index=3
        ),
    )

    miami2019_params = EventParams(
        date="2019-01-18",
        track=homestead_track,
        scraped_site_params=JmsSiteParams(
            ranking_url=events_url["2019-01-18"], position_col_index=1, name_col_index=3
        ),
    )

    miami2020_params = EventParams(
        date="2020-01-17",
        track=homestead_track,
        scraped_site_params=JmsSiteParams(
            ranking_url=events_url["2020-01-17"], position_col_index=1, name_col_index=3
        ),
    )

    miami2021_params = EventParams(
        date="2021-01-29",
        track=homestead_track,
        scraped_site_params=JmsSiteParams(
            ranking_url=events_url["2014-01-20"],
            position_col_index=1,
            name_col_index=4,
            athlete_link_col_index=2,
        ),
    )

    BrowserManager.start()

    try:
        miami2013 = EventScraper.scrape(miami2013_params)
        miami2014 = EventScraper.scrape(miami2014_params)
        miami2015 = EventScraper.scrape(miami2015_params)
        miami2016 = EventScraper.scrape(miami2016_params)
        miami2017 = EventScraper.scrape(miami2017_params)
        miami2018 = EventScraper.scrape(miami2018_params)
        miami2019 = EventScraper.scrape(miami2019_params)
        miami2020 = EventScraper.scrape(miami2020_params)
        miami2021 = EventScraper.scrape(miami2021_params)
    finally:
        BrowserManager.shutdown()

    events = [
        miami2013,
        miami2014,
        miami2015,
        miami2016,
        miami2017,
        miami2018,
        miami2019,
        miami2020,
        miami2021,
    ]

    for event in events:
        if event is None:
            continue
        print("-----")
        print(
            f"Event on {event.date} at {event.track.name}, {event.track.city}, {event.track.country}"
        )
        print(event.performances[0])
        print(event.performances[1])
        print(event.performances[2])
        print("-----\n")

    print(f"{AthleteRegistry.athletes[0]}")

    # for athlete in AthleteRegistry.athletes:
    #     print(athlete)


if __name__ == "__main__":
    main()
