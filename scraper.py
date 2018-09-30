import requests, bs4
from scrapers import ebgames, jbhifi

class Scraper():
    """
    This class scrapes data from websites and passes it back to whoever calle it.
    """

    def __init__(self):
        super().__init__()

        
    def searchAll(self, game, platform):
        """
        Searches all avaible stores for prices.
        """
        results = []
        results.extend(ebgames.query(game))
        results.extend(jbhifi.query(game))
        return sorted(results, key=getKeyPrice, reverse=True)

def getKeyPrice(item):
    return item[1], item[0], item[2]