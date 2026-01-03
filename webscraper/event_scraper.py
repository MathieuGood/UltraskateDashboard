import re
from bs4 import BeautifulSoup

# from bs4.element import PageElement

from models.event import Event
from models.event_params import EventParams
from webscraper.webscraper import Webscraper
from utils import Utils


class EventScraper:
    """
    Class responsible for scraping an entire event
    """

    @classmethod
    def scrape(cls, event_params: EventParams) -> Event:
        # Fetch home page of ranking as a BeautifulSoup object
        # Adding suffix to url in order to get the "advanced view" with page numbers
        ranking_home_soup = Webscraper.fetch_html(
            event_params.url + "&EId=1&dt=0&adv=1"
        )

        # Extract the number of pages from the ranking page
        number_of_pages = cls.__get_number_of_pages(ranking_home_soup)
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
        athletes_urls = cls.__parse_athlete_urls_from_ranking(
            all_ranking_pages_soup=all_ranking_pages, event_params=event_params
        )

        # for url in athletes_urls:
        #     print(url)

        print(
            f"\nNumber of athlete URLs found for {event_params.date.year}: {len(athletes_urls)}\n\n"
        )

        # For each athlete performance url, parse Athlete info and create Athlete object
        # Find all the participants in the table

        return Event(event_params)

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

                # Extract the link and name of the skater
                position = row_tds[position_col_index].text.strip()

                # If position is not a digit, skip the row (it can be a header or other info)
                if not position.isdigit():
                    continue

                name = row_tds[name_col_index].text.strip()
                athlete_full_url = row_links[1]["href"]
                print(
                    f"Row {row_index} -> POS {position} / NAME {name} / URL {athlete_full_url}"
                )
                # Build the complete URL for the skater's personal stats page
                base_url = Utils.extract_base_url(event_params.url)
                athlete_url_end = str(row_links[1]["href"])
                if not base_url or not athlete_url_end:
                    print(f"Skipping {base_url} + {athlete_url_end}")
                    continue
                athlete_full_url = base_url + athlete_url_end
                athletes_urls.append(athlete_full_url)

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
