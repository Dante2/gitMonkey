#import urllib.request, urllib.parse, urllib.error
#import requests
# from urllib3 import HTTPConnectionPool
from bs4 import BeautifulSoup as soup
import urllib3
from fake_useragent import UserAgent
import random
from urllib.request import Request, urlopen


#urllib3 pool manager to handle request
get_it = urllib3.PoolManager()
#make a get request
# response = get_it.request('GET', url, headers = headers)

url = 'https://github.com/search?q=repositories'


#make http request
response = get_it.request('GET', url)
#store the data to a variable
response_data = response.data
#parse that data
page_soup = soup(response_data, "html.parser")
#close the connection for cpu efficiency
response.close






#page_html = response.read()





# tag = page_soup.css
#
#
# print(type(tag))
# tag['id'] = 'css'

# for link in page_soup.find_all('a'):
#      print(link.get('href'))



# print(url)
# print(page_soup.prettify())
print('title = ' + str(page_soup.title))
# print('title name = ' + str(page_soup.title.name))
# print('title string = ' + str(page_soup.title.string))
# print('title parent name = ' + str(page_soup.title.parent.name))
#print('link = ' + str(page_soup.find_all('a')))

#print(response.getheader('Type'))

#containers = page_soup.findAll("div", {"search":"repositories"})
#print(page_html)
#print(containers)
#soup(response.data.decode('utf-8'))
#content = get_it.read()
#print (response.data)
#print (response.status)
#print (response.headers)
#print (soup)
#soup(content)

#print (r.content)

# fhand = urllib.request.urlopen('https://api.github.com/search/repositories?')
# for line in fhand:
#     print (line.decode().strip())
