import requests, bs4

class Scraper():
    """
    This class scrapes data from websites and passes it back to whoever calle it.
    """
    _webResources = {
        "ebgames": ("https://ebgames.com.au/any/any?q={}", "%20")
    }

    def __init__(self):
        super().__init__()
    
    def ebgames(self, game, platform='any'):
        """
        Returns the price of the game from EB Games

        Args:
            game: The title of the game to be found
            platform: Optional parameter specifying the target platform

        """
        results = []
 
        res = requests.get(self.searchUri(game, 'ebgames'))
        res.raise_for_status()
        soup = bs4.BeautifulSoup(res.text, features="html.parser")
        items = soup.select('.product')

        for item in items:
            link = item.select('a')[0]
            name = link.attrs['data-name']
            if game.strip(' ').lower() in name.strip(' ').lower():
                price = self.priceClean(link.attrs['data-price'])
                results.append((name, price))
        
        return results

    def priceClean(self, price):
        """
        Ensures the prices are only 2 decimal places long.

        Args:
            price: The price of the game as a string.
        """
        priceParts = price.split('.')
        if len(priceParts) == 2:
            cleanedPrice = '{}.{}'.format(priceParts[0], priceParts[1][:2])
        else:
            cleanedPrice = price
        return cleanedPrice
    
    def searchUri(self, game, resource):
        """
        Generates the search URI from different parts

        Args:
            game: Game title
            resource: web store to search
        """
        uri, seperator = self._webResources[resource]
        return uri.format(seperator.join(game.split(' ')))
        
    def searchAll(self, game, platform):
        """
        Searches all avaible stores for prices.
        """
        results = []
        results.extend(self.ebgames(game))
        return results