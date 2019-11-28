from domain import *
from bs4 import BeautifulSoup as soup
import urllib3

url = 'https://github.com'

repos_get = url_repos(url)
wikies_get = url_wikies(url)
issues_get = url_issues(url)

proxies = {
 'http': 'http: // 46.235.53.26:3128',
}

headers = {
    'USER-AGENT' : 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:70.0) Gecko/20100101 Firefox/70.0'
}

#urllib3 pool manager to handle request
get_it = urllib3.PoolManager()
#make a get request
response_repos = get_it.request('GET', repos_get, headers = headers)
response_wikies = get_it.request('GET', wikies_get, headers = headers)
response_issues = get_it.request('GET', issues_get, headers = headers)
#store the data to a variable
resp_data_repos = response_repos.data
resp_data_wikies = response_wikies.data
resp_data_issues = response_issues.data
#parse that data
resp_soup_repos = soup(resp_data_repos, "html.parser")
resp_soup_wikies = soup(resp_data_wikies, "html.parser")
resp_soup_issues = soup(resp_data_issues, "html.parser")

# print(url)
print(resp_soup_repos.prettify())
# print(resp_soup_wikies.prettify())
# print(resp_soup_issues.prettify())
# print (response_repos.status)
# print (response.headers)
# print('link = ' + str(page_soup.find_all('a')))
