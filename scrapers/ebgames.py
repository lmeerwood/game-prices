from . import utils
import requests, bs4

__URL = ("https://ebgames.com.au/any/any?q={}", "%20")

__ALLOWED_BRANDS = [
    'nintendo wii u',
    'nintendo 3ds',
    'nintendo ds',
    'nintendo switch',
]

__DISALLOWED_CATEGORIES = [
    'accessories'
]

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

    for item in items:
        link = item.select('a')[0]
        name = link.attrs['data-name']
        correctGame = game.strip(' ').lower() in name.strip(' ').lower()
        correctBrand = link.attrs['data-brand'].lower() in __ALLOWED_BRANDS
        correctCategory = not link.attrs['data-category'].lower() in __DISALLOWED_CATEGORIES
        if correctGame and correctCategory and correctBrand:
            price = utils.priceClean(link.attrs['data-price'])
            results.append((name, price))
    
    return results