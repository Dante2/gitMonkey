from bs4 import BeautifulSoup as soup
import urllib3
from fake_useragent import UserAgent
import random
from urllib.request import Request, urlopen

url = 'https://github.com/search?q=repositories'

#urllib3 pool manager to handle request
get_it = urllib3.PoolManager()
#make http request
response = get_it.request('GET', url)
#store the data to a variable
response_data = response.data
#parse that data
page_soup = soup(response_data, "html.parser")
#close the connection for cpu efficiency
response.close

for link in page_soup.find_all('a'):
     print(link.get('href'))

# print(url)
# print(page_soup.prettify())
print('title = ' + str(page_soup.title))
