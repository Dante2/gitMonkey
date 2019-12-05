from domain import *
from spider import *
import ip_generator
import requests

url = 'https://github.com'
heady = {
    'USER-AGENT' : 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:70.0) Gecko/20100101 Firefox/70.0'
}

# input json types to these variables
repos_get = url_repos(url)
wikies_get = url_wikies(url)
issues_get = url_issues(url)

# 3 instances of the spider class to get each respective type. these staticly declared but the most efficient implamentation would dynamic
spidey_repos = spidey(repos_get, ip_generator.prox_out())
spidey_wikies = spidey(wikies_get, ip_generator.prox_out())
spidey_issues = spidey(issues_get, ip_generator.prox_out())

print(spidey_repos.crawl())

# print (spidey_wikies.crawl())
