def priceClean(price):
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

def searchUri(game, resource):
    """
    Generates the search URI from different parts

    Args:
        game: Game title
        resource: web store to search
    """
    uri, seperator = resource
    return uri.format(seperator.join(game.split(' ')))