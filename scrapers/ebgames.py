from . import utils
from decimal import Decimal
from fuzzywuzzy import fuzz
import requests, bs4

__URL = ("https://ebgames.com.au/any/any?q={}", "%20")

__ALLOWED_BRANDS = [
    'nintendo wii u',
    'nintendo 3ds',
    'nintendo ds',
    'nintendo switch',
    'playstation 4',
    'playstation 3',
    'playstation vita',
    'xbox one',
    #'xbox 360',
]

__DISALLOWED_CATEGORIES = [
    'accessories'
]

__SYSTEM_CODES = {
    'nintendo wii u': 'wii-u',
    'nintendo 3ds': '3ds',
    'nintendo ds': 'nds',
    'nintendo switch': 'switch',
    'playstation 4': 'ps4',
    'playstation 3': 'ps3',
    'playstation vita': 'vita',
    'xbox one': 'xbone',
    'xbox 360': 'x360',
}

def query(game, platform='any'):
    """
    Returns the price of the game from EB Games

    Args:
        game: The title of the game to be found
        platform: Optional parameter specifying the target platform

    """
    results = []

    res = requests.get(utils.searchUri(game, __URL))
    res.raise_for_status()
    soup = bs4.BeautifulSoup(res.text, features="html.parser")
    items = soup.select('.product')
    fuzzyOffset = -10
    while (len(results) == 0 and fuzzyOffset < 90):
        fuzzyOffset += 10
        for item in items:
            link = item.select('a')[0]
            name = link.attrs['data-name']
            brand = link.attrs['data-brand'].lower()
            price = Decimal(utils.priceClean(link.attrs['data-price']))
            
            partialratio = fuzz.partial_ratio(name, game)
            
            correctBrand =  brand in __ALLOWED_BRANDS
            correctCategory = not link.attrs['data-category'].lower() in __DISALLOWED_CATEGORIES
            correctGame = partialratio > (utils.GAME_FUZINESS - fuzzyOffset)

            if  correctGame and correctCategory and correctBrand:
                results.append((name, __SYSTEM_CODES[brand], price, "ebgames"))

    return results
