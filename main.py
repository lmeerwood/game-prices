import sys, argparse
from scraper import Scraper

def run():
    """
    run() fetches the game price using information from the command line
    """
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
        print('${0:6}| {1:7}| {2:8}| {3}'.format(result[2], result[1], result[3], result[0]))

if __name__ == "__main__":
    run()
