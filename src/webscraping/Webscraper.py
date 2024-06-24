import re

import requests
from bs4 import BeautifulSoup

from data.events_urls import events_fields_indexes
from src.utils.StringUtils import StringUtils


class Webscraper:
    """
    A class that provides methods for web scraping and extracting information from web pages.
    """

    @classmethod
    def fetch_html(cls, url: str):
        """
        Fetches the HTML content from the specified URL.

        :param url: The URL to fetch the HTML content from.
        :return: The BeautifulSoup object representing the parsed HTML content.
        """
        page = requests.get(url)
        html: BeautifulSoup = BeautifulSoup(page.content, "html.parser")
        return html

    @classmethod
    def fetch_all_athletes_urls(cls, url: str, link_index: int = 1) -> list[str]:
        soup = cls.fetch_html(url)
        base_url = url

        # Find information about the number of pages
        page_number_info = soup.find_all("span", id="ctl00_Content_Main_lblTopPager")

        # Test if the ResultSet number_of_pages is empty
        if not page_number_info:
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
            print(">> Page " + str(i) + " >>")
            print(">> URL : " + url + " >>")

            # Find all the participants in the table
            athletes = soup.find_all("tr")

            for athlete in athletes:
                # Skip the first two rows containing table headers
                if athlete == athletes[0] or athlete == athletes[1]:
                    continue

                fields = athlete.find_all("td")
                links = athlete.find_all("a")
                try:
                    # Extract the link and name of the skater
                    name: str = fields[3].text.strip()
                    end_link: str = links[link_index]["href"]
                    print(name, end_link)
                    # Build the complete URL for the skater's personal stats page
                    link = StringUtils.extract_base_url(base_url) + end_link
                    athletes_urls.append(link)
                except Exception as e:
                    print(f"=> Line with no skater entry\n=> {e}")
                    pass
        print("--> Returning", athletes_urls.__len__(), "athletes URLs")
        return athletes_urls

    @classmethod
    def parse_athlete_info(cls, name: str, racer_id: str, athlete_info_table, event_url: str) -> dict[str, str]:
        # Layout of the webpage for the athlete is not consistent year by year
        # The indexes of fields to extract may differ for each event_url
        index = events_fields_indexes[event_url]
        info_table_fields: list = athlete_info_table.find_all("td")
        # gender: str = info_table_fields[1].text.strip()
        # age: str = info_table_fields[3].text.strip()
        # category: str
        # city: str = info_table_fields[7].text.strip()
        # state: str = info_table_fields[9].text.strip()

        # Write all the values of info_table_fields to a csv file
        with open("data/info_table_fields.csv", "a") as file:
            for field in info_table_fields:
                file.write(f"{field.text.strip()};")
            file.write("\n")

        gender: str = info_table_fields[index['gender']].text.strip()
        age: int = int(info_table_fields[index['age']].text.strip())
        category: str
        city: str = info_table_fields[index['city']].text.strip()
        state: str = info_table_fields[index['state']].text.strip()

        return {
            "name": name,
            "racer_id": racer_id,
            "gender": gender,
            "age": age,
            "city": city,
            "state": state,
        }

    @classmethod
    def parse_athlete_laps(cls, athlete_laps_table) -> dict[int, int]:
        laps_table_rows: list = athlete_laps_table.find_all("tr")

        laps = {}

        for row_count, row in enumerate(laps_table_rows):
            fields = row.find_all("td")

            for field_count, field in enumerate(fields):
                extracted_time = str(StringUtils.extract_time_from_str(field.text))

                if (
                        field_count == 2
                        # and extracted_time is valid
                        and StringUtils.str_is_hhmmss_format(extracted_time)
                ):
                    lap_number = row_count - 1
                    lap_time = StringUtils.convert_time_str_to_ss(extracted_time)
                    laps[lap_number] = lap_time
                    print("---> Lap  ", lap_number, field.text)

        return laps

    @classmethod
    def fetch_athlete_stats(cls, url: str, event_url: str) -> dict[str, dict]:
        soup: BeautifulSoup = cls.fetch_html(url)

        name: str = soup.find("span", id="ctl00_Content_Main_lblName").text
        racer_id: str = soup.find("span", id="ctl00_Content_Main_lblRaceNo").text

        # Find all the table tags
        # First table contains athlete info, second table contains lap times
        athlete_info_table, athlete_laps_table = soup.find_all("table")

        # Parse data from the athlete info table
        athlete_info = cls.parse_athlete_info(name, racer_id, athlete_info_table, event_url)
        print(athlete_info)

        # Parse data from the athlete laps table
        laps = cls.parse_athlete_laps(athlete_laps_table)

        return {"info": athlete_info, "performance": laps}

    @classmethod
    def fetch_all_athletes_performances(cls, url: str) -> list[dict[str, dict]]:
        # Special case f
        if url == "https://jms.racetecresults.com/results.aspx?CId=16370&RId=413":
            urls: list[str] = cls.fetch_all_athletes_urls(url, 2)
        else:
            urls: list[str] = cls.fetch_all_athletes_urls(url)
        print(f"\n############\nFetchig all athlete performances from URL : {url}\n############")

        event_performances = []
        for athlete_url in urls:
            print("\n>>> Athlete URL : " + athlete_url)
            # Add the performance to the event
            event_performances.append(cls.fetch_athlete_stats(athlete_url, event_url=url))
            print(event_performances.__len__(), "athlete performances fetched")

        return event_performances

    @classmethod
    def fetch_all_events_performances(cls, events_urls: dict[str, str]) -> dict[str, list[dict[str, dict]]]:
        events_performances = {}
        for event_url in events_urls:
            print("\n\nFetching " + event_url + "   >>> URL : " + events_urls[event_url])
            events_performances[event_url] = cls.fetch_all_athletes_performances(events_urls[event_url])
        return events_performances
