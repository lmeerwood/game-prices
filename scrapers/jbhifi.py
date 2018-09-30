from algoliasearch import algoliasearch
from fuzzywuzzy import fuzz
from decimal import Decimal
from . import utils

APP_ID = "QFXLKG0GNM"
API_KEY = "dca87593d507ef800701dfb6f0d0fbfc"
INDEX_NAME = "PRODUCTS"

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
    'nintendo wii u': 'wiiu',
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
    Returns the price of the game from JB HIFI

    Args:
        game: The title of the game to be found
        platform: Optional parameter specifying the target platform

    """
    client = algoliasearch.Client(APP_ID, API_KEY)
    index = client.init_index(INDEX_NAME)

    search = index.search('mario kart')
    hits = search["hits"] 
    results = []
    fuzzyOffset = -10
    while (len(results) == 0 and fuzzyOffset < 90):
        fuzzyOffset += 10
        for hit in hits:

            name = hit['ProductPrimaryName']
            brand = hit['Brand'].lower()
            price = Decimal(hit['Pricing']['SellPriceInc'])
            
            partialratio = fuzz.partial_ratio(name, game)

            correctBrand =  brand in __ALLOWED_BRANDS
            correctCategory = not brand.lower() in __DISALLOWED_CATEGORIES
            correctGame = partialratio > (utils.GAME_FUZINESS - fuzzyOffset)

            if correctGame and correctCategory and correctBrand:
                results.append((name, __SYSTEM_CODES[brand], price, "jb-hifi"))
    
    return results