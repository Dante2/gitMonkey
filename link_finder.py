#class to grab all the desired links from html file fed by spider

from html.parser import HTMLParser
from urllib import parse

class linkFinder(HTMLParser):
    #base url allows us to make static paths when we encounter relative paths
    def __init__(self, base_url, page_url):
        super().__init__()
        self.base_url = base_url
        self.page_url = page_url
        #this set is now available to start being populated by crawlers. we use a set not list because sets avoid duplicate elements
        self.links = set()
    #grabs certain data types in html code
    def handle_starttag(self, tag, attrs):
        #if tag is an anchor we find a link
        if tag == 'a':
            #html has values assigned to attributes. this is being taken from HTMLParser
            for (attribute, value) in attrs:
                if attribute == 'href':
                    # if relative link found it is converted to static url here. If already static it is ignored
                    url = parse.urljoin(self.base_url, value)
                    self.links.add(url)

        #print start tags
        #print(tag)

    def page_links(self):
        return self.links

    #error checking
    def error(self, message):
        pass
