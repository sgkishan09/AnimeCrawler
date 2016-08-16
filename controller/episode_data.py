import cfscrape
import utils
from bs4 import BeautifulSoup

def get_episode_data(links):
    episodes = []
    for link in links:
        page_source = utils.read_page(link)

        image_tag = page_source.findAll("meta", {"property": "og:image"})
        image_url = image_tag[0]['content']

        name_tag = page_source.findAll("select", {"id" : "selectEpisode"})
        name_dump = name_tag[0].findAll('option')
        name = name_dump[0].contents[0].strip()

        quality = page_source.findAll("select", {"id" : "selectQuality"})
        top_quality = quality[0].findAll('option')
        epi = {}
        epi['hash'] = top_quality[0]['value']
        epi['name'] = name
        epi['image_url'] = image_url
        episodes.append(epi)

    print episodes
