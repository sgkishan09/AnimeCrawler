import episode_data
import utils
from bs4 import BeautifulSoup

def collect_episodes(link):
    page_source = utils.read_page(link)
    listing_table = page_source.findAll("table", { "class" : "listing" })
    episode_links = listing_table[0].findAll('a')
    links = []
    for link in episode_links:
        links.append(utils.BASE_URL + link['href'])
    return episode_data.get_episode_data(links)

#collect_episodes("http://kissanime.to/Anime/hack-Quantum")
