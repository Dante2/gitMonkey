#spider class
from urllib.request import urlopen
from bs4 import BeautifulSoup as soup
# from link_finder import linkFinder
from domain import *
import urllib3
from proxy_generator import random_proxy

class spidey:
    #class variables (shared among all instances). Any spider can set the value of these variables
    # base_url = ''
    def __init__(self, page_url):
        self.page_url = page_url

    def crawl(self):
        proxies_nice = {
         'http': 'http: // 46.235.53.26:3128',
        }
        headers = {
            'USER-AGENT' : 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:70.0) Gecko/20100101 Firefox/70.0'
        }
        get_it = urllib3.PoolManager()
        response = get_it.request('GET', self.page_url, random_proxy(), headers = headers)
        resp_data = response.data
        resp_soup = soup(resp_data, "html.parser")
        return resp_soup
