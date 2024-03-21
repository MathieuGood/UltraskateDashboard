import requests
import re
from bs4 import BeautifulSoup
from classes.Utils import Utils
from classes.Performance import Performance
from classes.Skater import Skater


class Webscraper:

    @classmethod
    def fetch_html(self, url):
        """
        @brief Fetches the HTML content from the specified URL.

        @return: The BeautifulSoup object representing the parsed HTML content.
        """
        page = requests.get(url)
        html = BeautifulSoup(page.content, "html.parser")
        return html

    def extract_base_url(self, url):
        """
        @brief Extracts the base URL from the given URL.

        @param url: The URL to extract the base URL from.

        @return: The base URL.
        """
        regex = r"^https?://(?:www\.)?[^/]+/"
        match = re.search(regex, url)
        if Utils.check_url_format(url):
            return match.group(0)
        else:
            return None

    def fetch_all_skaters_url(self, url):
        """
        @brief Fetches the URLs of all skaters' personal stats pages.

        @param url: The URL of the page containing skater information.
        @return: A list of skater information, including name, category, gender, city, state, country, and link.
        """
        soup = self.fetch_html(url)
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

        skaters = []

        # Iterate over all the pages
        for i in range(1, number_of_pages + 1):

            if i > 1:
                # If it's not the first page, update the URL to include the page number
                url = base_url + "&PageNo=" + str(i)
                soup = self.fetch_html(url)

            # Build the URL for the current page
            url = base_url + "&PageNo=" + str(i)
            print(">>>>>>>>> Page " + str(i) + " >>>>>>>>>")
            print(">>>>>>>>> URL : " + url + " >>>>>>>>>")

            # Find all the participants in the table
            participants = soup.find_all("tr")

            for skater in participants:
                fields = skater.find_all("td")
                links = skater.find_all("a")
                try:
                    # Extract the link and name of the skater
                    name = fields[3].text.strip()
                    link = links[1]["href"]
                    print(name, link)
                    # Build the complete URL for the skater's personal stats page
                    link = self.extract_base_url(base_url) + links[1]["href"]
                    skaters.append([link])
                except:
                    print("- Line with no skater entry -")
                    pass

        return skaters

    @classmethod
    def fetch_skater_stats(self, url):
        """
        @brief Fetches the personal stats of a skater.

        @param url: The URL of the skater's personal stats page.
        @return: A list containing the skater's name, category
        """
        soup = self.fetch_html(url)

        name = soup.find("span", id="ctl00_Content_Main_lblName").text
        racer_id = soup.find("span", id="ctl00_Content_Main_lblRaceNo").text

        # Find all the tbdody tags
        tables = soup.find_all("table")

        # Fetch skater info
        info_table = tables[0].find_all("td")
        gender = info_table[1].text
        age = info_table[3].text
        city = info_table[7].text
        state = info_table[9].text
        total_distance = float(info_table[19].text)
        print(name, racer_id, gender, age, city, state, total_distance)

        # Fetch laps info
        laps_table = tables[1].find_all("td")

        # Build list with lap times that match the HH:MM:SS format
        laps = [
            Utils.convert_time_str_to_ss(lap.text)
            for lap in laps_table
            if Utils.check_hhmmss_format(lap.text)
        ]

        return Performance(
            "2013-01-07", "Miami", Skater(name, gender, age, city, state), laps
        )
