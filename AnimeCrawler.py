import cfscrape
from BeautifulSoup import BeautifulSoup
START=1
END=3
BASE_URL="http://kissanime.to/"
import pymongo
def readPage(url):
    scraper = cfscrape.create_scraper()
    return BeautifulSoup(scraper.get(url).content)
def collectList(page):
    anime_list=page.table.findAll('a')
    final_list=[]
    for i in anime_list:
        final_list.append({'name':i.contents[0].strip(),'url':str(i['href'])})
    return final_list
def getShows(listOfShows):    
    for i in listOfShows:
         for j in i:
             if(not "?id=" in j['url']):
                collectEpisodes(BASE_URL+j['url'])
def start():                
    total=[]
    for i in range(START,END):
        try:
            total.append(collectList(readPage(BASE_URL+"AnimeList?page="+str(i))))
            print str(i) + " " + str(len(total))
        except:
            print 'Error'
    getShows(total)
