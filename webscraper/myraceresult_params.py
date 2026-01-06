from models.scraped_site_params import ScrapedSiteParams


class MyRaceResultParams(ScrapedSiteParams):
    """
    Parameters for scraping the MyRaceResult site.
    """

    def __init__(self, race_id: int):
        self.base_url = "https://my.raceresult.com/"
        self.race_id = race_id
        self.url = f"{self.base_url}{self.race_id}"
        self.participants_url = f"https://my4.raceresult.com/{self.race_id}/RRPublish/data/list?key=9d484a9a9259ff0ae1a4a8570861bc3b&listname=Participants%7CParticipants%20List%20123&page=participants&contest=0&r=all&l=0"
