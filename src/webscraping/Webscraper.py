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
    def find_number_of_pages(cls, soup: BeautifulSoup) -> int:
        page_number_info = soup.find_all("span", id="ctl00_Content_Main_lblTopPager")

        if not page_number_info:
            number_of_pages = 1
        else:
            # From the string "Page 1 of 2 (76 items)" extract the number of pages with a regex
            page_number_info = page_number_info[0].text
            page_number_info = re.findall(r"\d+", page_number_info)
            number_of_pages = int(page_number_info[1])

        return number_of_pages

    @classmethod
    def extract_athlete_info_from_html(cls, fields) -> dict[str, str]:
        name: str = fields[2].text.strip()
        category: str = fields[5].text.strip()
        age: int = int(fields[7].text.strip())
        gender: str = fields[8].text.strip()
        city: str = fields[10].text.strip()
        state: str = fields[11].text.strip()
        print("RESULT :")
        print(name, category, age, gender, city, state)
        return {
            "name": name,
            "category": category,
            "age": age,
            "gender": gender,
            "city": city,
            "state": state,
        }

    @classmethod
    def format_athlete_urls(cls, athlete_urls: list[str], base_url: str) -> list[str]:
        return [StringUtils.extract_base_url(base_url) + url for url in athlete_urls]

    @classmethod
    def fetch_all_athletes_urls_and_info(cls, home_url: str):
        soup = cls.fetch_html(home_url)
        number_of_pages: int = cls.find_number_of_pages(soup)

        # Iterate over all the pages
        for page_number in range(1, number_of_pages + 1):

            if page_number > 1:
                # If it's not the first page, update the URL to include the page number
                home_url = home_url + "&PageNo=" + str(page_number)
                soup = cls.fetch_html(home_url)

            # Build the URL for the current page
            home_url = home_url + "&PageNo=" + str(page_number)
            print(">> Page " + str(page_number) + " >>")
            print(">> URL : " + home_url + " >>")

            # Find all the participants in the table
            athletes_rows = soup.find_all("tr")
            athletes_urls_and_infos = cls.parse_athlete_rows(athletes_rows, home_url)

        return athletes_urls_and_infos

    @classmethod
    def get_right_link_index(cls, home_url: str) -> int:
        if home_url == "https://jms.racetecresults.com/results.aspx?CId=16370&RId=413":
            return 2
        return 1

    @classmethod
    def parse_athlete_rows(cls, athletes_rows, home_url: str) -> tuple[str, list[str]]:
        athletes_urls_and_infos = []
        for athlete in athletes_rows:
            # Skip the first two rows containing table headers
            if athlete == athletes_rows[0] or athlete == athletes_rows[1]:
                continue

            athlete_info_fields = athlete.find_all("td")

            link_index = cls.get_right_link_index(home_url)
            athlete_link = athlete.find_all("a")[link_index]

            athlete_info_fields_cleaned = [
                field.text.strip() for field in athlete_info_fields
            ]
            athlete_link_formatted = (
                    StringUtils.extract_base_url(home_url) + athlete_link["href"]
            )

            athletes_urls_and_infos.append(
                (athlete_link_formatted, athlete_info_fields_cleaned)
            )
        return athletes_urls_and_infos

    @classmethod
    def parse_athlete_info(
            cls, name: str, racer_id: str, athlete_info_table, event_url: str
    ) -> dict[str, str]:
        # Layout of the webpage for the athlete is not consistent year by year
        # The indexes of fields to extract may differ for each event_url
        index = events_fields_indexes[event_url]
        info_table_fields: list = athlete_info_table.find_all("td")

        # Write all the values of info_table_fields to a csv file
        with open("data/info_table_fields.csv", "a") as file:
            for field in info_table_fields:
                file.write(f"{field.text.strip()};")
            file.write("\n")

        gender: str = info_table_fields[index["gender"]].text.strip()
        age: int = int(info_table_fields[index["age"]].text.strip())
        city: str = info_table_fields[index["city"]].text.strip()
        state: str = info_table_fields[index["state"]].text.strip()

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
        athlete_info = cls.parse_athlete_info(
            name, racer_id, athlete_info_table, event_url
        )
        print(athlete_info)

        # Parse data from the athlete laps table
        laps = cls.parse_athlete_laps(athlete_laps_table)

        return {"info": athlete_info, "performance": laps}

    @classmethod
    def fetch_all_athletes_performances(cls, home_url: str) -> list[dict[str, dict]]:
        athletes_urls_and_infos: list[tuple[str, list[str]]]
        athletes_urls_and_infos = cls.fetch_all_athletes_urls_and_info(home_url)
        print("\n>>> URLS AND INFOS :")
        print(athletes_urls_and_infos)
        print(
            f"\n############\nFetchig all athlete performances from URL : {home_url}\n############"
        )

        event_performances = []
        for athlete_url in athletes_urls_and_infos:
            print("\n>>> Athlete URL : " + athlete_url[0])
            # Add the performance to the event
            event_performances.append(
                cls.fetch_athlete_stats(athlete_url[0], event_url=home_url)
            )
            print(event_performances.__len__(), "athlete performances fetched")

        return event_performances

    @classmethod
    def fetch_all_events_performances(
            cls, events_urls: dict[str, str]
    ) -> dict[str, list[dict[str, dict]]]:
        events_performances = {}
        for event_url in events_urls:
            print(
                "\n\nFetching " + event_url + "   >>> URL : " + events_urls[event_url]
            )
            events_performances[event_url] = cls.fetch_all_athletes_performances(
                events_urls[event_url]
            )
        return events_performances
