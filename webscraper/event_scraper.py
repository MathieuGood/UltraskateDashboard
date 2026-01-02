import re
from bs4 import BeautifulSoup
from bs4.element import PageElement
from models.event import Event
from models.event_params import EventParams
from webscraper.webscraper import Webscraper


class EventScraper:

    @classmethod
    def scrape(cls, event_params: EventParams) -> Event:
        # Fetch home page of ranking as a BeautifulSoup object
        ranking_home_soup = Webscraper.fetch_html(event_params.url)

        # Extrat the number of pages from the ranking page
        number_of_pages = cls.__get_number_of_pages(ranking_home_soup)
        print(
            f"Number of pages of {event_params.track.name} {event_params.date.year} : {number_of_pages}"
        )

        if number_of_pages > 1:
            pass
            # Fetch all pages

        return Event(event_params)

    @classmethod
    def __get_number_of_pages(cls, ranking_home_soup: BeautifulSoup) -> int:
        """
        From a BeautifulSoup objet containing the ranking home page, find the tag contaning pagination info and extract the total number of pages

        :param ranking_home_soup: BeautifulSoup object containing ranking home page content
        :type ranking_home_soup: BeautifulSoup
        :return: Total number of pages
        :rtype: int
        """

        # print(ranking_home_soup)

        # Look for the tag containing the number of pages
        page_number_span = ranking_home_soup.find_all(
            "span", id="ctl00_Content_Main_lblTopPager"
        )

        print(page_number_span)

        # When no page number tag found, it means there is only one page
        if len(page_number_span) == 0:
            return 1

        # Convert bs4 tag to text
        page_number_span = page_number_span[0].text
        print(page_number_span)

        # From the string formatted like "Page 1 of 2 (76 items)" extract all the numbers with a regex
        page_number_span = re.findall(r"\d+", page_number_span)

        # Get second int (number of pages)
        number_of_pages = int(page_number_span[1])

        return number_of_pages

    @classmethod
    def __scrape_event_ranking(cls, event_params: EventParams):
        ranking_home_url: str = event_params.url

        # Fetch the content of the ranking home page
        ranking_home_soup: PageElement = Webscraper.fetch_html(ranking_home_url)

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

        pass
