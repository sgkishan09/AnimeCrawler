import utils
from episode_data import *
from episode_list import *
from BeautifulSoup import BeautifulSoup
import pymongo

def collect_list(page):
    anime_list=page.table.findAll('a')
    final_list=[]
    for i in anime_list:
        final_list.append({'name':i.contents[0].strip(),'url':str(i['href'])})
    return final_list

def get_shows(list_of_shows):
    for i in list_of_shows:
         for j in i:
             if(not "?id=" in j['url']):
                print j['name']
                collect_episodes(utils.BASE_URL+j['url'])
def start():
    total=[]
    for i in range(utils.START,utils.END):
        try:
            total.append(collect_list(utils.read_page(utils.BASE_URL+"AnimeList?page="+str(i))))
            print str(i) + " " + str(len(total))
        except:
            print 'Error'
    get_shows(total)
