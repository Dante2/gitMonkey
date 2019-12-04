#spider class
# from urllib.request import urlopen
from bs4 import BeautifulSoup as soup
from domain import *
# import urllib3
import requests

class spidey:
    #class variables (shared among all instances). Any spider can set the value of these variables
    def __init__(self, page_url, proxy, keywords):
        self.page_url = page_url
        self.proxy = proxy
        self.keywords = keywords

        # self.heady = heady

    def crawl(self):
        r = requests.get(self.page_url, self.proxy)
        meat = r.text
        meathead =r.url
        meaty = r.encoding
        souped = soup(meat, 'html.parser')
        # return souped
        print(souped.title)
        for link in souped.find_all('a'):
            print(link.get('href'))
        # return souped.prettify()
