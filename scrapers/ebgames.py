from . import utils
import requests, bs4

__URL = ("https://ebgames.com.au/any/any?q={}", "%20")

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
        if game.strip(' ').lower() in name.strip(' ').lower():
            price = utils.priceClean(link.attrs['data-price'])
            results.append((name, price))
    
    return results