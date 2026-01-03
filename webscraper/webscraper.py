import re
from bs4 import BeautifulSoup
from utils import Utils
from models.performance import Performance
from models.athlete import Athlete
from models.event import Event
from models.track import Track

from playwright.sync_api import sync_playwright


class Webscraper:
    """
    A class that provides methods for web scraping and extracting information from web pages.
    """

    @classmethod
    def fetch_html(cls, url: str) -> BeautifulSoup:
        """
        Fetches the HTML content from the specified URL.

        :param url: The URL to fetch the HTML content from.
        :return: The BeautifulSoup object representing the parsed HTML content.
        """

        # TODO : Condiser refactoring the Browser session into a singleton class
        with sync_playwright() as p:
            browser = p.chromium.launch(
                headless=True, args=["--disable-blink-features=AutomationControlled"]
            )
            context = browser.new_context(
                user_agent=(
                    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
                    "AppleWebKit/537.36 (KHTML, like Gecko) "
                    "Chrome/120.0.0.0 Safari/537.36"
                ),
                locale="en-US",
            )
            page = context.new_page()
            page.goto(url, timeout=60_000, wait_until="domcontentloaded")
            page.wait_for_load_state("domcontentloaded")
            html = BeautifulSoup(page.content(), "html.parser")
            return html

    @classmethod
    def parse_athlete_info(cls, name, racer_id, athlete_info_table):
        info_table_fields = athlete_info_table.find_all("td")
        gender = info_table_fields[1].text.strip()
        age = info_table_fields[3].text.strip()
        city = info_table_fields[7].text.strip()
        state = info_table_fields[9].text.strip()

        return {
            "name": name,
            "racer_id": racer_id,
            "gender": gender,
            "age": age,
            "city": city,
            "state": state,
        }

    @classmethod
    def parse_athlete_laps(cls, athlete_laps_table):
        laps_table_rows = athlete_laps_table.find_all("tr")

        laps = {}

        for row_count, row in enumerate(laps_table_rows):
            fields = row.find_all("td")

            for field_count, field in enumerate(fields):
                extracted_time = str(Utils.extract_time(field.text))

                if (
                    field_count == 2
                    # and extracted_time is not None
                    and Utils.check_hhmmss_format(extracted_time)
                ):

                    lap_number = row_count - 1
                    lap_time = Utils.convert_time_str_to_ss(extracted_time)
                    laps[lap_number] = lap_time
                    print("--- Lap  ", lap_number, field.text)

        return laps

    @classmethod
    def fetch_athlete_stats(cls, url):
        """
        Fetches the personal stats of an athlete.

        :param url: The URL of the skater's personal stats page.
        :return: A list containing the athlete's name, category
        """
        soup = cls.fetch_html(url)

        name = soup.find("span", id="ctl00_Content_Main_lblName").text
        racer_id = soup.find("span", id="ctl00_Content_Main_lblRaceNo").text

        # Find all the table tags
        # First table contains athlete info, second table contains lap times
        athlete_info_table, athlete_laps_table = soup.find_all("table")

        # Parse data from the athlete info table
        athlete_info = cls.parse_athlete_info(name, racer_id, athlete_info_table)
        print(athlete_info)

        # Parse data from the athlete laps table
        laps = cls.parse_athlete_laps(athlete_laps_table)

        return {"athlete_info": athlete_info, "athlete_performance": laps}

    @classmethod
    def fetch_all_athletes_performances(cls, url):
        urls = cls.fetch_all_athletes_urls(url)

        event_performances = []
        for athlete_url in urls:
            print("\n\n>>> URL : " + athlete_url)
            # Add the performance to the event
            event_performances.append(cls.fetch_athlete_stats(athlete_url))
            print(event_performances.__len__(), "athlete performances fetched")

        return event_performances

    @classmethod
    def fetch_several_events_performances(cls, events_urls):
        events_performances = {}
        for event_url in events_urls:
            print("Key of the event : ", event_url.key())
            cls.fetch_all_athletes_performances(event_url)
