import requests
import re
from bs4 import BeautifulSoup
from classes.Utils import Utils
from classes.Performance import Performance
from classes.Athlete import Athlete
from classes.Event import Event
from classes.Track import Track


class Webscraper:
    """
    A class that provides methods for web scraping and extracting information from web pages.
    """

    @classmethod
    def fetch_html(cls, url):
        """
        Fetches the HTML content from the specified URL.

        :param url: The URL to fetch the HTML content from.
        :return: The BeautifulSoup object representing the parsed HTML content.
        """
        page = requests.get(url)
        html = BeautifulSoup(page.content, "html.parser")
        return html

    @classmethod
    def fetch_all_athletes_urls(cls, url):
        """
        Fetches the URLs of all skaters' personal stats pages.

        :param url: The URL of the page containing skater information.
        :return: A list of skater information, including name, category, gender, city, state, field_country, and link.
        """
        soup = cls.fetch_html(url)
        base_url = url

        # Find information about the number of pages
        page_number_info = soup.find_all("span", id="ctl00_Content_Main_lblTopPager")

        # Test if the ResultSet number_of_pages is empty
        if page_number_info == []:
            number_of_pages = 1
        else:
            # From the string "Page 1 of 2 (76 items)" extract the number of pages with a regex
            page_number_info = page_number_info[0].text
            page_number_info = re.findall(r"\d+", page_number_info)
            number_of_pages = int(page_number_info[1])

        athletes_urls = []

        # Iterate over all the pages
        for i in range(1, number_of_pages + 1):

            if i > 1:
                # If it's not the first page, update the URL to include the page number
                url = base_url + "&PageNo=" + str(i)
                soup = cls.fetch_html(url)

            # Build the URL for the current page
            url = base_url + "&PageNo=" + str(i)
            print(">>>>>>>>> Page " + str(i) + " >>>>>>>>>")
            print(">>>>>>>>> URL : " + url + " >>>>>>>>>")

            # Find all the participants in the table
            athletes = soup.find_all("tr")

            for athlete in athletes:
                if athlete == athletes[0] or athlete == athletes[1]:
                    continue

                fields = athlete.find_all("td")
                links = athlete.find_all("a")
                try:
                    # Extract the link and name of the skater
                    name = fields[3].text.strip()
                    link = links[1]["href"]
                    print(name, link)
                    # Build the complete URL for the skater's personal stats page
                    link = Utils.extract_base_url(base_url) + links[1]["href"]
                    athletes_urls.append(link)
                except:
                    # print("- Line with no skater entry -")
                    pass

        return athletes_urls

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
