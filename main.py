import requests, bs4, sys

def loadWebsites():
    websites = [
        ("EB Games", "https://ebgames.com.au/any/any?q={}", "%20"),
    ]
    return websites

def scanWebsites(webList, query):
    results = []
    for web in webList:
        name, address, seperator = web
        if name == "EB Games":
            preppedQuery = seperator.join(query.split(" "))
            queryUrl = address.format(preppedQuery)
            results.extend(ebscan(queryUrl, query))
    return results

def ebscan(queryUrl, query):

    results = []

    res = requests.get(queryUrl)
    res.raise_for_status()
    soup = bs4.BeautifulSoup(res.text, features="html.parser")
    items = soup.select('.product')

    for item in items:
        link = item.select('a')[0]
        name = link.attrs['data-name']
        if query.strip(' ').lower() in name.strip(' ').lower():
            price = priceClean(link.attrs['data-price'])
            results.append((name, price))
    
    return results

def priceClean(price):
    priceParts = price.split('.')
    if len(priceParts) == 2:
        cleanedPrice = '{}.{}'.format(priceParts[0], priceParts[1][:2])
    else:
        cleanedPrice = price
    return cleanedPrice

def run():
    if len(sys.argv) > 1:
        query = " ".join(sys.argv[2:])    
        websites = loadWebsites()
        results = scanWebsites(websites, query)
        for result in results:
            print('${} | {}'.format(result[1], result[0]))
    else: 
        print("Please put the name of the game you wish to find the price of")

if __name__ == "__main__":
    run()
        