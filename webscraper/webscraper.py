from bs4 import BeautifulSoup
from webscraper.browser_manager import BrowserManager

from utils import Utils


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
        page = BrowserManager.new_page()
        page.goto(url, timeout=60_000, wait_until="domcontentloaded")
        page.wait_for_load_state("domcontentloaded")
        html = page.content()
        page.close()

        soup = BeautifulSoup(html, "html.parser")

        title_tag = soup.title
        if title_tag and title_tag.get_text(strip=True) == "Just a moment...":
            print("Encountered Cloudflare protection page : page not scraped.")
        return soup

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
