from os import path
from models.event_params import EventParams
from models.track import Track
from webscraper.event_scraper import EventScraper
from webscraper.browser_manager import BrowserManager
from webscraper.jms_site_params import JmsSiteParams
from webscraper.myraceresult_params import MyRaceResultParams
from event_params_data import miami_event_params

"""

All participants :
https://my4.raceresult.com/192607/RRPublish/data/list?key=9d484a9a9259ff0ae1a4a8570861bc3b&listname=Participants%7CParticipants%20List%20123&page=participants&contest=0&r=all&l=0

Lap details for a given athlete (pid=421 here) :
https://my4.raceresult.com/192607/RRPublish/data/list?key=9d484a9a9259ff0ae1a4a8570861bc3b&listname=Online%7CLap%20Details&page=live&contest=0&r=pid&pid=421
"""

# Miami 2013 https://jms.racetecresults.com/results.aspx?CId=16370&RId=13
# Miami 2014 https://jms.racetecresults.com/results.aspx?CId=16370&RId=67
# Miami 2015 https://jms.racetecresults.com/results.aspx?CId=16370&RId=121  # Age group available as 'category' column
# Miami 2016 https://jms.racetecresults.com/results.aspx?CId=16370&RId=179
# Miami 2017 https://jms.racetecresults.com/results.aspx?CId=16370&RId=240
# Miami 2018 https://jms.racetecresults.com/results.aspx?CId=16370&RId=294
# Miami 2019 https://jms.racetecresults.com/results.aspx?CId=16370&RId=352
# Miami 2020 https://jms.racetecresults.com/results.aspx?CId=16370&RId=400
# Miami 2021 https://jms.racetecresults.com/results.aspx?CId=16370&RId=413
# Miami 2022 https://my.raceresult.com/192607
# Miami 2023 https://my.raceresult.com/204047
# Miami 2024 https://my.raceresult.com/259072
# Miami 2025 https://my.raceresult.com/310199/


def main():
    print("Hello from ultraskatedashboard!")

    MIAMI = ("Homestead Speedway", "Homestead", 1.46)
    SPAARNDAM = ("Wheelerplanet", "Spaarndam", 2.0)

    BrowserManager.start()

    try:
        miami2013 = EventScraper.scrape(miami_event_params[2013])
        miami2014 = EventScraper.scrape(miami_event_params[2014])
        miami2015 = EventScraper.scrape(miami_event_params[2015])
        miami2016 = EventScraper.scrape(miami_event_params[2016])
        miami2017 = EventScraper.scrape(miami_event_params[2017])
        miami2018 = EventScraper.scrape(miami_event_params[2018])
        miami2019 = EventScraper.scrape(miami_event_params[2019])
        miami2020 = EventScraper.scrape(miami_event_params[2020])
        miami2021 = EventScraper.scrape(miami_event_params[2021])
        # miami2022 = EventScraper.scrape(miami_event_params[2022])
        # miami2023 = EventScraper.scrape(miami_event_params[2023])
        # miami2024 = EventScraper.scrape(miami_event_params[2024])
        # miami2025 = EventScraper.scrape(miami_event_params[2025])
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
        # miami2022,
        # miami2023,
        # miami2024,
        # miami2025,
    ]

    for event in events:
        if event is None or len(event.performances) == 0:
            continue
        print("-----")
        print(
            f"Event on {event.date} at {event.track.name}, {event.track.city}, {event.track.country}"
        )
        print(event.performances[0])
        print(event.performances[1])
        print(event.performances[2])
        print("-----\n")
        print("-----\n\n\n\n\n\n")
        event.to_json_file(
            path.join(
                "scraped_events", "ultraskate_miami_" + str(event.date.year) + ".json"
            )
        )


if __name__ == "__main__":
    main()
