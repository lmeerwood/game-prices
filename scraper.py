import requests, bs4
from scrapers import ebgames

class Scraper():
    """
    This class scrapes data from websites and passes it back to whoever calle it.
    """
    _webResources = {
        "ebgames": ("https://ebgames.com.au/any/any?q={}", "%20")
    }

    def __init__(self):
        super().__init__()

        
    def searchAll(self, game, platform):
        """
        Searches all avaible stores for prices.
        """
        results = []
        results.extend(ebgames.query(game))
        return results