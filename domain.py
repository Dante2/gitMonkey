from urllib.parse import urlparse

# Get sub domain name (name.example.com)
def get_sub_domain_name(url):
    try:
        parsed = urlparse(url).netloc
        return parsed
    except:
        return ''

def url_repos(parsed):
    try:
        repos = parsed + '/search?q=repositories'
        return repos
    except:
        return ''

def url_wikies(parsed):
    try:
        repos = parsed + '/search?q=wikies'
        return repos
    except:
        return ''

def url_issues(parsed):
        try:
            repos = parsed + '/search?q=issues'
            return repos
        except:
            return ''

print()
