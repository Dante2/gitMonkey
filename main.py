from domain import *
from bs4 import BeautifulSoup as soup
import urllib3
from spider import spidey

url = 'https://github.com'

# input json types to these variables
repos_get = url_repos(url)
wikies_get = url_wikies(url)
issues_get = url_issues(url)

# 3 instances of the spider class to get each respective type. these staticly declared but the most efficient implamentation would dynamic
spidey_repos = spidey(repos_get)
spidey_wikies = spidey(wikies_get)
spidey_issues = spidey(issues_get)

print(spidey_repos.crawl().prettify())

# print(url)
# print(resp_soup_repos.prettify())
# print(resp_soup_wikies.prettify())
# print(resp_soup_issues.prettify())

# print (response.headers)
# print('link = ' + str(page_soup.find_all('a')))
