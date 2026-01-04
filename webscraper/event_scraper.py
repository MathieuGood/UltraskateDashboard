import re
from bs4 import BeautifulSoup

# from bs4.element import PageElement

from models.event import Event
from models.athlete import Athlete
from models.performance import Performance
from models.athlete_registry import AthleteRegistry
from models.event_params import EventParams
from webscraper.webscraper import Webscraper
from utils import Utils


class EventScraper:
    """
    Class responsible for scraping an entire event
    """

    scraping_attemps: int = 5

    @classmethod
    def scrape(cls, event_params: EventParams) -> Event:
        event = Event(event_params)

        # Fetch all athlete performance URLs from the event ranking page
        athletes_urls = cls.__fetch_all_athlete_performance_urls(event_params)
        print(
            f"\nNumber of athlete URLs found for {event_params.date.year}: {len(athletes_urls)}"
        )

        for athlete_url in athletes_urls:
            performance = cls.__get_performance_from_athlete_url(
                athlete_url, event_params
            )
            if performance:
                event.add_performance(performance)

        print(
            f"Total athletes in registry: {len(AthleteRegistry.athletes)}/ {len(athletes_urls)}\n"
        )

        return event

    @classmethod
    def __get_performance_from_athlete_url(
        cls, athlete_url: str, event_params: EventParams
    ) -> Performance | None:
        """
        From an athlete URL, scrape the athlete info and performance data and return a Performance object
        Args:
            athlete_url (str): URL of the athlete's performance page
            event_params (EventParams): Parameters of the event
        Returns:
            Performance | None: Performance object containing athlete info and performance data, or None if scraping fails
        """
        athlete_performance_soup = Webscraper.fetch_html(athlete_url)
        if not athlete_performance_soup:
            print(f"athlete_performance_soup is empty for URL: {athlete_url}")
        athlete_info = athlete_performance_soup.find(
            name="div", id="ctl00_Content_Main_divLeft"
        )
        # print(f"\nScraping athlete page: {athlete_url}")

        if not athlete_info:
            print(f"Could not find athlete info on page: {athlete_url}")
            print(athlete_performance_soup)
            return None

        athlete_name = ""
        athlete_gender = ""
        athlete_city = ""
        athlete_state = ""
        athlete_country = ""

        # Get athlete name from the specific span
        athlete_name_span = athlete_info.find(
            name="span", id="ctl00_Content_Main_lblName"
        )
        if athlete_name_span:
            athlete_name = athlete_name_span.text.strip()

        # Get other athlete info from the table rows
        athlete_info_rows = athlete_info.find_all("tr")

        for row in athlete_info_rows:
            athlete_row_tds = row.find_all("td")
            if len(athlete_row_tds) < 2:
                continue
            label = athlete_row_tds[0].text.strip().lower()
            value = athlete_row_tds[1].text.strip()

            if "gender" in label:
                # print(f"Found athlete gender: {value}")
                athlete_gender = value
            elif "city" in label:
                # print(f"Found athlete city: {value}")
                athlete_city = value
            elif "state" in label:
                # print(f"Found athlete state: {value}")
                athlete_state = value
            elif "country" in label:
                # print(f"Found athlete country: {value}")
                athlete_country = value

        athlete_laps_table = athlete_performance_soup.find(
            name="div", id="ctl00_Content_Main_divSplitGrid"
        )
        if not athlete_laps_table:
            print(f"No laps table found for athlete: {athlete_name} at {athlete_url}")
            return None

        lap_rows = [
            tr
            for tr in athlete_laps_table.find_all("tr")
            if "lap" in tr.get_text(separator=" ", strip=True).lower()
            and Utils.extract_time(tr.get_text()) is not None
        ]

        laps = cls.__parse_athlete_lap_rows(lap_rows)

        athlete = Athlete(
            name=athlete_name,
            gender=athlete_gender,
            city=athlete_city,
            state=athlete_state,
            country=athlete_country,
        )

        AthleteRegistry.add_athlete(athlete)

        return Performance(athlete=athlete, laps=laps)

    @classmethod
    def __parse_athlete_lap_rows(cls, lap_rows) -> list[int]:
        """
        Parse the lap rows of an athlete's performance table and extract lap times.
        """
        laps = []
        for lap_index, lap_row in enumerate(lap_rows):
            lap_row_cols = lap_row.find_all("td")
            lap_time = lap_row_cols[2]
            extracted_time = str(Utils.extract_time(lap_time.text))
            lap_time = Utils.convert_time_str_to_ss(extracted_time)
            laps.append(lap_time)
            print(f"--- Lap {lap_index+1} -> {extracted_time}")
        return laps

    @classmethod
    def __fetch_all_athlete_performance_urls(
        cls, event_params: EventParams
    ) -> list[str]:
        # Fetch home page of ranking as a BeautifulSoup object
        # Adding suffix to url in order to get the "advanced view" with page numbers
        ranking_home_soup = Webscraper.fetch_html(
            event_params.url + "&EId=1&dt=0&adv=1"
        )

        # Extract the number of pages from the ranking page
        number_of_pages = cls.__get_number_of_pages(ranking_home_soup)
        print(f"{event_params.track} {event_params.date.year} {event_params.url}")
        print(
            f"Number of pages of {event_params.track.name} {event_params.date.year} : {number_of_pages}"
        )

        # HTML content of all the ranking pages
        all_ranking_pages: list[BeautifulSoup] = []

        if number_of_pages == 1:
            # If just one page, no need to scrape other content for now
            all_ranking_pages = [ranking_home_soup]
        else:
            # Build all the pages url
            ranking_pages_urls = cls.__build_all_ranking_pages_urls(
                number_of_pages=number_of_pages, base_url=event_params.url
            )
            for ranking_page_url in ranking_pages_urls:
                all_ranking_pages.append(Webscraper.fetch_html(ranking_page_url))

        # Parse all the athlete individual performances urls across the rows
        return cls.__parse_athlete_urls_from_ranking(
            all_ranking_pages_soup=all_ranking_pages, event_params=event_params
        )

    @classmethod
    def __parse_athlete_urls_from_ranking(
        cls, all_ranking_pages_soup: list[BeautifulSoup], event_params: EventParams
    ) -> list[str]:
        athletes_urls: list[str] = []
        for ranking_page in all_ranking_pages_soup:
            ranking_table = ranking_page.find(
                name="div", id="ctl00_Content_Main_divGrid"
            )
            if not ranking_table:
                continue
            athlete_rows = ranking_table.find_all("tr")

            for row_index, athlete_row in enumerate(athlete_rows):
                row_tds = athlete_row.find_all("td")
                row_links = athlete_row.find_all("a")

                position_col_index = event_params.position_col_index
                name_col_index = event_params.name_col_index
                athlete_link_col_index = event_params.athlete_link_col_index

                # Extract the link and name of the skater
                position = row_tds[position_col_index].text.strip()

                # If position is not a digit, skip the row (it can be a header or other info)
                if not position.isdigit():
                    continue

                name = row_tds[name_col_index].text.strip()

                # Build the complete URL for the skater's personal stats page
                base_url = Utils.extract_base_url(event_params.url)
                athlete_url_end = str(row_links[athlete_link_col_index]["href"])
                if not base_url or not athlete_url_end:
                    # print(f"Skipping {base_url} + {athlete_url_end}")
                    continue
                athlete_full_url = base_url + athlete_url_end
                athletes_urls.append(athlete_full_url)
                # print(
                #     f"Row {row_index} -> POS {position} / NAME {name} / URL {athlete_full_url}"
                # )

        return athletes_urls

    @classmethod
    def __build_all_ranking_pages_urls(
        cls, number_of_pages: int, base_url: str
    ) -> list[str]:
        """
        Build all the ranking pages urls based on the base url and the number of pages

        Args:
            number_of_pages (int): Total number of pages in the ranking
            base_url (str): Base URL of the ranking page
        Returns:
            list[str]: List of all ranking pages URLs
        """

        pages_urls = []
        for i in range(1, number_of_pages + 1):
            pages_urls.append(base_url + "&PageNo=" + str(i))
        return pages_urls

    @classmethod
    def __get_number_of_pages(cls, ranking_home_soup: BeautifulSoup) -> int:
        """
        From a BeautifulSoup objet containing the ranking home page, find the tag contaning pagination info and extract the total number of pages

        Args:
            ranking_home_soup (BeautifulSoup): BeautifulSoup object of the ranking home page
        Returns:
            int: Total number of pages in the ranking
        """

        # print(ranking_home_soup)

        # Look for the tag containing the number of pages
        page_number_span = ranking_home_soup.find_all(
            "span", id="ctl00_Content_Main_lblTopPager"
        )

        # When no page number tag found, it means there is only one page
        if len(page_number_span) == 0:
            return 1

        # Convert bs4 tag to text
        page_number_span = page_number_span[0].text

        # From the string formatted like "Page 1 of 2 (76 items)" extract all the numbers with a regex
        page_number_span = re.findall(r"\d+", page_number_span)

        # Get second int (number of pages)
        number_of_pages = int(page_number_span[1])

        return number_of_pages
