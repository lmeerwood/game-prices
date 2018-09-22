import requests, bs4

class Scraper():

    _webResources = {
        "ebgames": ("https://ebgames.com.au/any/any?q={}", "%20")
    }

    def __init__(self):
        super().__init__()
    
    def ebgames(self, game):
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
        priceParts = price.split('.')
        if len(priceParts) == 2:
            cleanedPrice = '{}.{}'.format(priceParts[0], priceParts[1][:2])
        else:
            cleanedPrice = price
        return cleanedPrice
    
    def searchUri(self, game, resource):
        uri, seperator = self._webResources[resource]
        return uri.format(seperator.join(game.split(' ')))
        
    def searchAll(self, game):
        results = []
        results.extend(self.ebgames(game))
        return results