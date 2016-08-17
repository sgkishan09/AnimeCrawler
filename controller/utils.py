import cfscrape
import episode_data
from bs4 import BeautifulSoup

START=1
END=2
BASE_URL="http://kissanime.to/"

def read_page(url):
    scraper = cfscrape.create_scraper()
    return BeautifulSoup(scraper.get(url).content, 'html.parser')
