import sys
from scraper import Scraper

def run():
    if len(sys.argv) > 1:
        game = " ".join(sys.argv[1:])
        scrape = Scraper()
        results = scrape.searchAll(game=game)
        for result in results:
            print('${0:6}| {1}'.format(result[1], result[0]))
    else: 
        print("Please put the name of the game you wish to find the price of")

if __name__ == "__main__":
    run()
        