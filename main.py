import sys, argparse
from scraper import Scraper

def run():

    parser = argparse.ArgumentParser(description='Retrieve the latest prices for a specified video game')
    parser.add_argument('title', help='Title of the game')
    parser.add_argument('-p', '--platform', help='Platform the game is on')
    args = parser.parse_args()

    if (not args.platform):
        platform = "any"
    else:
        platform = args.platform

    scraper = Scraper()
    results = scraper.searchAll(game=args.title, platform=platform)
    for result in results:
        print('${0:6}| {1}'.format(result[1], result[0]))
    # if len(sys.argv) > 1:
    #     game = " ".join(sys.argv[1:])
    #     scrape = Scraper()
    #     results = scrape.searchAll(game=game)
    #     for result in results:
    #         print('${0:6}| {1}'.format(result[1], result[0]))
    # else: 
    #     print("Please put the name of the game you wish to find the price of")

if __name__ == "__main__":
    run()
