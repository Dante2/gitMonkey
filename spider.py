#spider class
from urllib.request import urlopen
from link_finder import linkFinder
from domain import *
from general import *

class Spider:
    #class variables (shared among all instances). Any spider can set the value of these variables
    project_name = ''
    base_url = ''
    domain_name = ''
    queue_file = ''
    crawled_file = ''
    queue = set()
    crawl = set()
    
    def __init__(self, project_name, base_url, domain_name):
        Spider.project_name = project_name
        Spider.base_url = base_url
        Spider.domain_name = domain_name
        Spider.queue_file = Spider.project_name + '/queue.text'
        Spider.crawled_file = Spider.project_name + '/crawled.text'
        self.boot()
        self.crawl_page('First Spider', Spider.base_url)
    
    #telling python that this is static method
    @staticmethod
    def boot():
        create_project_dir(Spider.project_name)
        create_data_files(Spider.project_name, Spider.base_url)
        Spider.queue = file_to_set(Spider.queue_file)
        Spider.crawled = file_to_set(Spider.crawled_file)
    
    @staticmethod
    def crawl_page(thread_name, page_url):
        #make sure we use the crawled set not the file for faster performance
        if page_url not in Spider.crawled:
            #print to user what's going on
            print(thread_name + ' crawling ' + page_url)
            print('Queue' + str(len(Spider.queue)) + ' | crawled ' + str(len(Spider.crawled)))
            #this is the waiting list all spiders can see keeping all their activities synchronised
            Spider.add_links_to_queue(Spider.gather_links(page_url))
            #once page has been crawled remove it from queue and put it in crawled list
            Spider.queue.remove(page_url)
            Spider.crawled.add(page_url)
            #once all these actions are completed update files for saving
            Spider.update_files()

    @staticmethod
    def gather_links(page_links):
        html_string = ''
        #network programming best practice - try and response for handling exceptions
        try:
            response = urlopen(page_url)
            #make sure we're connecting to a web page and not some wierd executable etc
            if response.getheader('Content-Type') == 'text/html':
                #transform the bytes into human readable code
                html_bytes = response.read()
                html_string = html_bytes.decode('utf-8')
            finder = linkFinder(Spider.base_url, page_url)
            finder.feed(html_string)
        except:
            print('Error: can not crawl page')
            #if there are no links return empty set
            return set()
        return finder.page_links

    @staticmethod
    def add_links_to_queue(links):
        for url in links:
            #if url already in queue or crawled set ignore it
            if url in Spider.queue:
                continue
            if url in Spider.crawled:
                continue
            #only crawl page if in specified url
            if Spider.domain_name not in url:
                continue
            Spider.queue.add(url)

    @staticmethod
    def update_files():
        #update files for saving data
        set_to_file(Spider.queue, Spider.queue_file)
        set_to_file(Spider.crawled, Spider.crawled_file)
