from models.scraped_site_params import ScrapedSiteParams


class MyRaceResultParams(ScrapedSiteParams):
    """
    Parameters for scraping the MyRaceResult site.
    """

    def __init__(self, race_id: int, all_participants_url: str):
        self.base_url = "https://my.raceresult.com/"
        self.race_id = race_id
        self.url = f"{self.base_url}{self.race_id}"
        self.participants_url = all_participants_url
