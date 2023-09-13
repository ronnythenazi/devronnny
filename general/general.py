from django.contrib.sites.shortcuts import get_current_site
from django.urls import reverse
exposed_request = None

def safeExtend(lst, lst2):
    if lst2 != None:
        lst.extend(lst2)
    return lst



def get_curr_domain():
    domain  = get_current_site(exposed_request).domain
    return str(domain)

def get_homepage_path():
    path = get_curr_domain()
    path = path + get_homepage_rel_path()
    return path

# good for search result on my website for search engine
def is_url_startswith_article_path(url):
    article_path = get_article_path()

    if url.startswith('http://' + article_path):
        return True

    if url.startswith('https://' + article_path):
        return True

    return False

def get_article_path():
    homepage_url = get_homepage_path()
    path = homepage_url  + get_article_page_name() + '/'
    return path


def get_article_rel_path():
    homepage_url = get_homepage_rel_path()
    path = homepage_url  + get_article_page_name() + '/'
    return path

def get_article_page_name():
    return 'article'


def get_homepage_rel_path():
    rel_path = reverse('magazine:magazineNews')
    return str(rel_path)
